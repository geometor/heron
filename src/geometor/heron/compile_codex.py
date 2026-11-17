"""Deterministic apparatus compiler and 4-Track Book Codex verifier for ``geometor.heron``."""

from __future__ import annotations

import json
import re
from pathlib import Path

from geometor.heron.concordance import (
    CODEX_UNITS,
    CODEX_UNITS_BY_SLUG,
    default_repo_root,
    default_resources_dir,
    verify_manifest_checksums,
)

__all__ = [
    "default_docsrc_book_dir",
    "render_bibliography_rst",
    "render_concordance_rst",
    "render_glossary_rst",
    "render_persons_rst",
    "slugify_key",
    "verify_codex_tracks",
    "write_apparatus_pages",
]


def slugify_key(key: str) -> str:
    """Slugify an apparatus key identically to ``photon_platform.publish.roles.geometry``."""
    return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")


def default_docsrc_book_dir() -> Path:
    """Return ``<repo>/docsrc``."""
    return default_repo_root() / "docsrc"


def render_concordance_rst(concordance: dict[str, object]) -> str:
    """Render ``docsrc/metrica/concordance.rst`` from ``concordance.json``."""
    raw_entries = concordance.get("entries", [])
    entries = (
        [e for e in raw_entries if isinstance(e, dict)]
        if isinstance(raw_entries, list)
        else []
    )

    lines: list[str] = [
        ":navigation: footer",
        ":nav_title: Concordance",
        ":order: 90",
        ":type: apparatus",
        "",
        ".. _heron-concordance:",
        ".. _concordance:",
        "",
        "Concordance",
        "===========",
        "",
        (
            "Bidirectional scholarly concordance mapping **Hero of Alexandria's** "
            "*Metrica* (*ed.* Hermann Schöne, 1903), *Catoptrica* (*ed.* Wilhelm Schmidt & "
            "Ludwig Nix, 1900), *Dioptra* (*ed.* Schöne, 1903), and *Definitiones* "
            "(*ed.* Friedrich Hultsch, 1864 / J. L. Heiberg, 1912) across the **GEOMETOR** "
            "canon (``euclid``, ``elements``, ``proclus``, ``pappus``, ``wildberger``, ``etc``) "
            f"and exact ``geometor.heron`` symbolic constructions (**{len(entries)} loci**)."
        ),
        "",
        "Overview by Codex Unit",
        "----------------------",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 25 22 10 43",
        "",
        "   * - Codex Unit",
        "     - Critical Edition Pages",
        "     - Loci",
        "     - Scope",
    ]

    by_unit: dict[str, list[dict[str, object]]] = {u.slug: [] for u in CODEX_UNITS}
    for entry in entries:
        u_slug = str(entry.get("codex_unit", ""))
        if u_slug in by_unit:
            by_unit[u_slug].append(entry)

    for unit in CODEX_UNITS:
        u_entries = by_unit[unit.slug]
        lines.extend(
            [
                f"   * - :doc:`{unit.number_label} </{unit.slug}/index>`",
                f"     - {unit.edition_pages}",
                f"     - {len(u_entries)}",
                f"     - {unit.subtitle}",
            ]
        )
    lines.append("")

    for unit in CODEX_UNITS:
        u_entries = by_unit[unit.slug]
        heading = f"{unit.number_label} ({unit.edition_pages})"
        lines.extend(
            [
                f".. _concordance-{slugify_key(unit.slug)}:",
                "",
                heading,
                "-" * len(heading),
                "",
                (
                    f"Codex tracks: :doc:`Book Overview </{unit.slug}/index>` · "
                    f":doc:`Summary </{unit.slug}/summary>` · "
                    f":doc:`Notes </{unit.slug}/notes>`"
                ),
                "",
            ]
        )
        for entry in u_entries:
            anchor = str(entry.get("id", ""))
            canon = str(entry.get("canonical_locus", ""))
            sec_id = str(entry.get("codex_section_id", ""))
            sec_title = str(entry.get("codex_section_title", ""))
            topic = str(entry.get("topic", ""))
            euc_raw = entry.get("euclid_elements", [])
            euc_list = [str(x) for x in euc_raw] if isinstance(euc_raw, list) else []
            just_str = (
                " · Euclid " + ", ".join(f":just:`{el}`" for el in euc_list)
                if euc_list
                else ""
            )

            lines.extend(
                [
                    f".. _{anchor}:",
                    "",
                    f"**{canon}** — :ref:`{sec_title} <{sec_id}>`{just_str}",
                    f"  {topic}",
                ]
            )

            sisters_raw = entry.get("sister_links", [])
            sisters = [str(x) for x in sisters_raw] if isinstance(sisters_raw, list) else []
            code_sym = str(entry.get("code_symbol", ""))
            if sisters or code_sym:
                lines.append("")
                for sl in sisters:
                    lines.append(f"  * {sl}")
                if code_sym:
                    lines.append(f"  * Exact symbolic model: ``{code_sym}``")
            lines.append("")

    return "\n".join(lines)


def render_bibliography_rst(citations: dict[str, dict[str, object]]) -> str:
    """Render ``docsrc/metrica/bibliography.rst`` from ``citations.json``."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 6",
        ":nav_title: Bibliography",
        "",
        ".. _codex-bibliography:",
        ".. _bibliography:",
        "",
        "Bibliography",
        "============",
        "",
        (
            "Critical register of public-domain Greek/Latin editions of Hero of Alexandria, "
            "ancient mathematical treatises cited in the *Metrica*, *Catoptrica*, and *Dioptra*, "
            "and companion GEOMETOR works. Every ``:cite:`` reference resolves directly below."
        ),
        "",
    ]

    groups = [
        ("Critical Editions of Hero of Alexandria", "edition"),
        ("Ancient Mathematical & Philosophical Authorities", "ancient"),
        ("Companion GEOMETOR & Modern Critical Scholarship", "modern"),
    ]

    for group_title, category in groups:
        items = [
            (k, v)
            for k, v in citations.items()
            if str(v.get("category", "ancient")) == category
        ]
        if not items:
            continue
        lines.extend([group_title, "-" * len(group_title), ""])
        for key, entry in sorted(
            items, key=lambda kv: (str(kv[1].get("author", "")), kv[0])
        ):
            slug = slugify_key(key)
            author = str(entry.get("author", ""))
            work = str(entry.get("work", ""))
            locus = str(entry.get("locus", ""))
            year = str(entry.get("year", ""))
            note = str(entry.get("note", ""))
            url = str(entry.get("url", ""))
            header = f"**{author}** — *{work}*"
            if locus:
                header += f" ({locus})"
            if year:
                header += f" [{year}]"
            lines.extend(
                [
                    f".. _cite-{slug}:",
                    "",
                    header,
                    f"  Key: ``{key}``",
                ]
            )
            if note:
                lines.append(f"  {note}")
            if url:
                lines.append(f"  Provenance: `{url} <{url}>`__")
            lines.append("")

    return "\n".join(lines)


def render_persons_rst(persons: dict[str, dict[str, object]]) -> str:
    """Render ``docsrc/metrica/persons.rst`` from ``persons.json``."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 5",
        ":nav_title: People",
        "",
        ".. _codex-persons:",
        ".. _persons:",
        "",
        "People",
        "======",
        "",
        (
            "Prosopographical register of geometers, astronomers, philosophers, "
            "commentators, medieval translators, and critical editors connected with "
            "Hero of Alexandria's mathematical corpus."
        ),
        "",
        "----",
        "",
        "Authors, Translators & Editors",
        "------------------------------",
        "",
    ]

    featured = ["hero", "schoene"]
    for f_key in featured:
        if f_key in persons:
            entry = persons[f_key]
            slug = slugify_key(f_key)
            name = str(entry.get("name", f_key))
            greek = str(entry.get("greek", ""))
            dates = str(entry.get("dates", ""))
            summary = str(entry.get("summary", ""))
            loci = str(entry.get("hero_loci", ""))
            head = f"**{name}**"
            if greek:
                head += f" (*{greek}*)"
            if dates:
                head += f" — {dates}"
            lines.extend(
                [
                    f".. _person-{slug}:",
                    "",
                    head,
                    f"  {summary}",
                ]
            )
            if loci:
                lines.append(f"  *Loci*: {loci}.")
            lines.append("")

    eras = [
        ("Classical Geometers & Philosophers", "classical"),
        ("Hellenistic Mathematicians & Astronomers", "hellenistic"),
        ("Roman Imperial Geometers & Physicists", "roman_imperial"),
        ("Late Antique & Medieval Commentators and Translators", "late_antique"),
        ("Modern Philologists, Historians & Mathematicians", "modern"),
    ]

    for era_title, era_key in eras:
        items = [
            (k, v)
            for k, v in persons.items()
            if str(v.get("era", "hellenistic")) == era_key and k not in featured
        ]
        if not items:
            continue
        lines.extend([era_title, "-" * len(era_title), ""])
        for key, entry in sorted(
            items, key=lambda kv: int(str(kv[1].get("sort_year", 0)))
        ):
            slug = slugify_key(key)
            name = str(entry.get("name", key))
            greek = str(entry.get("greek", ""))
            dates = str(entry.get("dates", ""))
            summary = str(entry.get("summary", ""))
            loci = str(entry.get("hero_loci", ""))
            title_line = f"**{name}**"
            if greek:
                title_line += f" (*{greek}*)"
            if dates:
                title_line += f" — {dates}"
            lines.extend(
                [
                    f".. _person-{slug}:",
                    "",
                    title_line,
                    f"  {summary}",
                ]
            )
            if loci:
                lines.append(f"  *Loci*: {loci}.")
            lines.append("")

    return "\n".join(lines)


def render_glossary_rst(glossary: dict[str, dict[str, object]]) -> str:
    """Render ``docsrc/metrica/glossary.rst`` from ``glossary.json``."""
    lines: list[str] = [
        ":navigation: footer",
        ":nav_title: Glossary",
        ":order: 93",
        ":type: apparatus",
        "",
        ".. _codex-glossary:",
        ".. _glossary:",
        "",
        "Glossary",
        "========",
        "",
        (
            "Lexicon of Greek mensurational, optical, geodetic, and geometric terminology "
            "in Hero of Alexandria's *Metrica*, *Definitiones*, *Catoptrica*, and *Dioptra*, "
            "paired with modern Rational Trigonometry invariants."
        ),
        "",
    ]

    for key, entry in sorted(glossary.items(), key=lambda kv: kv[0]):
        slug = slugify_key(key)
        term = str(entry.get("term", key))
        greek = str(entry.get("greek", ""))
        latin = str(entry.get("latin", ""))
        english = str(entry.get("english", ""))
        definition = str(entry.get("definition", ""))
        loci = str(entry.get("hero_loci", ""))
        head = f"**{term}**"
        if greek:
            head += f" (*{greek}*)"
        if latin:
            head += f" · Lat. *{latin}*"
        if english:
            head += f" — {english}"
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                head,
                f"  {definition}",
            ]
        )
        if loci:
            lines.append(f"  *Loci*: {loci}.")
        lines.append("")

    return "\n".join(lines)


def write_apparatus_pages(
    resources_dir: Path | None = None,
    book_dir: Path | None = None,
) -> list[Path]:
    """Compile ``concordance.rst``, ``bibliography.rst``, ``persons.rst``, and ``glossary.rst``.

    Args:
        resources_dir: Optional override for ``resources/metrica``.
        book_dir: Optional override for ``docsrc/metrica``.

    Returns:
        List of written RST file paths.
    """
    res = resources_dir or default_resources_dir()
    bdir = book_dir or default_docsrc_book_dir()
    bdir.mkdir(parents=True, exist_ok=True)

    concordance = json.loads((res / "concordance.json").read_text(encoding="utf-8"))
    citations = json.loads((res / "citations.json").read_text(encoding="utf-8"))
    persons = json.loads((res / "persons.json").read_text(encoding="utf-8"))
    glossary = json.loads((res / "glossary.json").read_text(encoding="utf-8"))

    outputs = [
        (bdir / "concordance.rst", render_concordance_rst(concordance)),
        (bdir / "bibliography.rst", render_bibliography_rst(citations)),
        (bdir / "persons.rst", render_persons_rst(persons)),
        (bdir / "glossary.rst", render_glossary_rst(glossary)),
    ]
    written: list[Path] = []
    for path, content in outputs:
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def verify_codex_tracks(book_dir: Path | None = None) -> dict[str, object]:
    """Verify all 6 Codex units have valid structure, zero Python blocks, and valid SHA-256s.

    Args:
        book_dir: Optional override for ``docsrc``.

    Returns:
        Dictionary with ``valid``, ``units``, ``track_files``, and ``errors``.
    """
    bdir = book_dir or default_docsrc_book_dir()
    errors: list[str] = list(verify_manifest_checksums())
    track_counts = 0

    for rf in ("index.rst", "concordance.rst", "bibliography.rst", "people/index.rst", "glossary.rst"):
        if not (bdir / rf).is_file():
            errors.append(f"Missing book apparatus/index file: {bdir / rf}")

    code_block_re = re.compile(r"^\.\.\s+code-block::\s*(?:python|py)\b", re.MULTILINE)

    for unit in CODEX_UNITS:
        udir = bdir / unit.slug
        if not udir.is_dir():
            errors.append(f"Missing unit directory: {udir}")
            continue
        for req in ("index.rst", "summary.rst", "notes.rst"):
            req_path = udir / req
            if not req_path.is_file():
                errors.append(f"Missing {req} in unit {unit.slug}")

        for f_path in udir.glob("*.rst"):
            track_counts += 1
            txt = f_path.read_text(encoding="utf-8")
            if code_block_re.search(txt):
                errors.append(
                    f"Forbidden embedded Python code-block in historical treatise: {f_path}"
                )
            if f_path.name not in ("index.rst", "summary.rst", "notes.rst") and not f_path.name.startswith("title-"):
                if ".. folio::" not in txt:
                    errors.append(f"Expected `.. folio::` milestone marker in {f_path}")

    idx_path = bdir / "index.rst"
    if idx_path.is_file():
        idx_txt = idx_path.read_text(encoding="utf-8")
        if ":type: book" not in idx_txt and ":layout: book" not in idx_txt:
            errors.append("Missing `:type: book` or `:layout: book` metadata in docsrc/index.rst")

    return {
        "valid": len(errors) == 0,
        "units": len(CODEX_UNITS_BY_SLUG),
        "track_files": track_counts,
        "errors": errors,
    }
