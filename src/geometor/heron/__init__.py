"""Exact symbolic mensuration, proofs, and 4-Track Book Codex for Hero of Alexandria."""

from __future__ import annotations

from geometor.heron.concordance import (
    CODEX_UNITS,
    CODEX_UNITS_BY_SLUG,
    CodexUnitSpec,
    load_concordance,
    load_sources_manifest,
)
from geometor.heron.constructions import (
    construct_area_division,
    construct_catoptrica_reflection,
    construct_dionysodorus_torus,
    construct_dioptra_tunnel,
    construct_heron_proof,
    construct_heronian_gnomon,
    construct_pentagon_lemma,
)
from geometor.heron.mensuration import (
    PHI,
    PolygonRatioEntry,
    SqrtConvergent,
    archimedes_quadrea,
    dionysodorus_torus_volume,
    frustum_volume,
    heron_area,
    heron_area_squared,
    heron_sqrt_convergents,
    pentagon_golden_lemma,
    platonic_solid_volumes,
    regular_polygon_ratios,
    verify_frustum_mean_identity,
    verify_quadrea_identity,
)
from geometor.heron.render import export_all_figures, export_svg, render_svg_string

__version__ = "0.1.1"

__all__ = [
    "CODEX_UNITS",
    "CODEX_UNITS_BY_SLUG",
    "CodexUnitSpec",
    "PHI",
    "PolygonRatioEntry",
    "SqrtConvergent",
    "__version__",
    "archimedes_quadrea",
    "construct_area_division",
    "construct_catoptrica_reflection",
    "construct_dionysodorus_torus",
    "construct_dioptra_tunnel",
    "construct_heron_proof",
    "construct_heronian_gnomon",
    "construct_pentagon_lemma",
    "dionysodorus_torus_volume",
    "export_all_figures",
    "export_svg",
    "frustum_volume",
    "heron_area",
    "heron_area_squared",
    "heron_sqrt_convergents",
    "load_concordance",
    "load_sources_manifest",
    "pentagon_golden_lemma",
    "platonic_solid_volumes",
    "regular_polygon_ratios",
    "render_svg_string",
    "verify_frustum_mean_identity",
    "verify_quadrea_identity",
]
