"""Runtime Sphinx & ``photon-platform/publish`` integration for ``geometor.heron``.

Registers the ``el`` ("Greek (Teubner)") companion track in ``photon_platform.publish.book``
at build time (without modifying ``photon-platform/publish``) and configures offline-safe
local ``intersphinx`` inventories for sister GEOMETOR repositories.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

__all__ = [
    "configure_local_intersphinx",
    "register_greek_book_track",
    "setup",
]

GREEK_TRACK_LABEL = "Greek (Teubner)"


def register_greek_book_track() -> None:
    """Extend ``photon_platform.publish.book`` to recognize ``<stem>-el`` Greek tracks."""
    try:
        from photon_platform.publish import book
    except ImportError:
        return

    el_pattern = (r"^(.+)[._-]el$", "el", GREEK_TRACK_LABEL)
    if not any(key == "el" for _pat, key, _lbl in book._TRACK_SUFFIX_PATTERNS):
        book._TRACK_SUFFIX_PATTERNS.append(el_pattern)

    book._AUX_TRACK_BASENAMES.add("el")
    el_aux_re = re.compile(r"^.+[._-]el$")
    if not any(p.pattern == el_aux_re.pattern for p in book._AUX_TRACK_PATTERNS):
        book._AUX_TRACK_PATTERNS.append(el_aux_re)

    if getattr(book.detect_companion_tracks, "_heron_el_patched", False):
        return

    orig_detect = book.detect_companion_tracks

    def _detect_with_greek(env: object, pagename: str) -> list[dict[str, object]]:
        found_docs: set[str] = set(getattr(env, "found_docs", set()))
        if not found_docs:
            return []

        doc_dir = os.path.dirname(pagename)
        basename = os.path.basename(pagename)
        stem = book._extract_unit_stem(basename, doc_dir)
        if basename == "el" and doc_dir:
            stem = os.path.basename(doc_dir)

        def _qual(local_name: str) -> str:
            return f"{doc_dir}/{local_name}" if doc_dir else local_name

        probe_page = pagename
        el_candidates = [
            _qual(f"{stem}.el"),
            _qual(f"{stem}_el"),
            _qual(f"{stem}-el"),
            _qual("el"),
        ]
        el_doc = next((c for c in el_candidates if c in found_docs), None)
        if el_doc and pagename == el_doc:
            en_cand = next(
                (
                    c
                    for c in (
                        _qual(f"{stem}-en"),
                        _qual(f"{stem}_en"),
                        _qual(f"{stem}.en"),
                    )
                    if c in found_docs
                ),
                None,
            )
            if en_cand:
                probe_page = en_cand

        tracks = orig_detect(env, probe_page)
        if not el_doc:
            return tracks

        updated: list[dict[str, object]] = []
        inserted_el = False
        el_entry: dict[str, object] = {
            "key": "el",
            "label": GREEK_TRACK_LABEL,
            "docname": el_doc,
            "active": el_doc == pagename,
        }
        for tr in tracks:
            if tr.get("docname") == el_doc:
                continue
            item = dict(tr)
            item["active"] = item.get("docname") == pagename
            updated.append(item)
            if item.get("key") == "en" and not inserted_el:
                updated.append(el_entry)
                inserted_el = True

        if not inserted_el:
            updated.insert(0, el_entry)

        return updated if len(updated) >= 2 else []

    _detect_with_greek._heron_el_patched = True  # type: ignore[attr-defined]
    book.detect_companion_tracks = _detect_with_greek


def configure_local_intersphinx(
    intersphinx_mapping: dict[str, tuple[str, object]],
    project_root: Path,
) -> None:
    """Bind local ``objects.inv`` files for sister GEOMETOR repos and drop remote-only ones.

    Args:
        intersphinx_mapping: Mutable Sphinx ``intersphinx_mapping`` dictionary.
        project_root: Root directory of ``geometor/heron``.
    """
    geometor_dir = project_root.parent
    sisters = ("euclid", "elements", "proclus", "pappus", "wildberger", "etc")
    for sister in sisters:
        inv = geometor_dir / sister / "docs" / "objects.inv"
        if inv.is_file():
            intersphinx_mapping[sister] = (
                f"https://geometor.github.io/{sister}",
                str(inv.resolve()),
            )
    for key in list(intersphinx_mapping.keys()):
        _uri, inv_target = intersphinx_mapping[key]
        if inv_target is None:
            intersphinx_mapping.pop(key, None)


def setup(app: object) -> dict[str, object]:
    """Sphinx extension entry point.

    Args:
        app: Sphinx application instance.

    Returns:
        Extension metadata dictionary.
    """
    _ = app
    register_greek_book_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
