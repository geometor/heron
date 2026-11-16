"""Codex unit specifications, provenance manifest checks, and cross-corpus concordance."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

__all__ = [
    "CODEX_UNITS",
    "CODEX_UNITS_BY_SLUG",
    "CodexUnitSpec",
    "default_repo_root",
    "default_resources_dir",
    "load_concordance",
    "load_sources_manifest",
    "verify_manifest_checksums",
]


@dataclass(frozen=True)
class CodexUnitSpec:
    """Canonical unit in the 4-Track Book Codex (``docsrc/metrica/``).

    Attributes:
        slug: Directory and filename stem for the unit.
        order: Numeric navigation order in the Book Codex.
        number_label: Short display label (e.g., ``"Metrica I (1–9)"``).
        title: Full unit title.
        subtitle: Thematic summary of propositions covered.
        edition_pages: Teubner / Weidmann critical edition page span.
        manuscript_folios: Manuscript witness folio span.
    """

    slug: str
    order: int
    number_label: str
    title: str
    subtitle: str
    edition_pages: str
    manuscript_folios: str


CODEX_UNITS: tuple[CodexUnitSpec, ...] = (
    CodexUnitSpec(
        slug="metrica/book_01",
        order=10,
        number_label="Metrica I",
        title="Metrica Book I: Planar Mensuration, Heron's Formula & Surface Areas",
        subtitle=(
            "Origins of Geometry, Orthogonal Units, Triangles, Quadrilaterals, "
            "Regular Polygons via φ, Circles, Annulus, Parabola & Curved Surfaces"
        ),
        edition_pages="Schöne 1903, pp. 2–90",
        manuscript_folios="Cod. Cpolit. 1, fols. 67r–86v",
    ),
    CodexUnitSpec(
        slug="metrica/book_02",
        order=20,
        number_label="Metrica II",
        title="Metrica Book II: Stereometry, Torus, Vaults & Platonic Solids",
        subtitle=(
            "Eudoxus & Archimedes, Cones, Frusta, Spheres, Dionysodorus's Torus (Σπεῖρα), "
            "Cylindrical Ungula & Groin Vault (Method), Five Platonic Solids, and Bath Displacement"
        ),
        edition_pages="Schöne 1903, pp. 90–140",
        manuscript_folios="Cod. Cpolit. 1, fols. 87r–99r",
    ),
    CodexUnitSpec(
        slug="metrica/book_03",
        order=30,
        number_label="Metrica III",
        title="Metrica Book III: Proportional Division of Plane & Solid Figures",
        subtitle=(
            "Proportional Distributive Justice, Dividing Triangles, Trapezia, Quadrilaterals, "
            "Polygons, Concentric Circles, Pyramids, Cones, Frusta & Spheres in Given Ratios"
        ),
        edition_pages="Schöne 1903, pp. 140–184",
        manuscript_folios="Cod. Cpolit. 1, fols. 99v–107v",
    ),
    CodexUnitSpec(
        slug="definitiones",
        order=40,
        number_label="Definitiones",
        title="Definitiones (Geometric Definitions)",
        subtitle=(
            "Genetic Definitions, Rigid-Motion Symmetry, Three Postulates, "
            "Direct Proofs, and the Universal Gnomon (§58)"
        ),
        edition_pages="Hultsch pp. 7–23 · Heiberg IV, pp. 1–160",
        manuscript_folios="Cod. Par. gr. 2385 · Cod. Vat. gr. 215",
    ),
    CodexUnitSpec(
        slug="catoptrica",
        order=50,
        number_label="Catoptrica",
        title="Catoptrica (Variational Optics)",
        subtitle=(
            "Variational Shortest-Path Law of Reflection (Prop. 4), Olympiodorus "
            "Testimony, and Moerbeke Translation"
        ),
        edition_pages="Schmidt 1900, pp. 324–372",
        manuscript_folios="Cod. Ottobonianus lat. 1850 · Olympiodorus In Meteora III.2",
    ),
    CodexUnitSpec(
        slug="dioptra",
        order=60,
        number_label="Dioptra",
        title="Dioptra (Geodesy & Surveying)",
        subtitle=(
            "Precision Surveying Instruments, Orthogonal Coordinate Traverse, "
            "and Two-Portal Mountain Tunneling (Ch. 15)"
        ),
        edition_pages="Schöne 1903, pp. 188–314",
        manuscript_folios="Cod. Par. suppl. gr. 607, fols. 62r–82v",
    ),
)

CODEX_UNITS_BY_SLUG: dict[str, CodexUnitSpec] = {u.slug: u for u in CODEX_UNITS}


def default_repo_root() -> Path:
    """Return the root directory of ``geometor/heron``."""
    return Path(__file__).resolve().parents[3]


def default_resources_dir() -> Path:
    """Return ``<repo>/resources/metrica``."""
    return default_repo_root() / "resources" / "metrica"


def load_concordance(resources_dir: Path | None = None) -> dict[str, object]:
    """Load ``resources/metrica/concordance.json``.

    Args:
        resources_dir: Optional override directory.

    Returns:
        Parsed JSON dictionary.
    """
    res = resources_dir or default_resources_dir()
    return json.loads((res / "concordance.json").read_text(encoding="utf-8"))


def load_sources_manifest(resources_dir: Path | None = None) -> dict[str, object]:
    """Load ``resources/metrica/sources_manifest.json``.

    Args:
        resources_dir: Optional override directory.

    Returns:
        Parsed JSON dictionary.
    """
    res = resources_dir or default_resources_dir()
    return json.loads((res / "sources_manifest.json").read_text(encoding="utf-8"))


def verify_manifest_checksums(repo_root: Path | None = None) -> list[str]:
    """Verify SHA-256 checksums of local primary-source excerpts in ``sources_manifest.json``.

    Args:
        repo_root: Optional repository root path.

    Returns:
        List of error strings (empty when all files exist and match their SHA-256 digest).
    """
    root = repo_root or default_repo_root()
    manifest = load_sources_manifest(root / "resources" / "metrica")
    errors: list[str] = []

    excerpts = manifest.get("local_source_excerpts", [])
    if not isinstance(excerpts, list) or not excerpts:
        return ["No local_source_excerpts found in sources_manifest.json"]

    for item in excerpts:
        if not isinstance(item, dict):
            continue
        rel_path = str(item.get("path", ""))
        expected_sha = str(item.get("sha256", ""))
        fpath = root / rel_path
        if not fpath.is_file():
            errors.append(f"Missing primary source excerpt: {fpath}")
            continue
        actual_sha = hashlib.sha256(fpath.read_bytes()).hexdigest()
        if actual_sha != expected_sha:
            errors.append(
                f"SHA-256 mismatch for {rel_path}: expected {expected_sha}, got {actual_sha}"
            )
    return errors
