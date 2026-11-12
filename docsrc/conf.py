"""Sphinx configuration for ``geometor/heron``."""

from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _PROJECT_ROOT.parent
for _extra_src in (
    _PROJECT_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / "divine" / "src",
):
    if _extra_src.is_dir() and str(_extra_src) not in sys.path:
        sys.path.insert(0, str(_extra_src))

from photon_platform.publish.global_conf import *  # noqa: F403

import geometor.heron as module
from geometor.heron.sphinx_ext import (
    configure_local_intersphinx,
    register_greek_book_track,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "heron"
repo_name = "heron"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

project = "GEOMETOR • heron"
author = "Hero of Alexandria"
copyright = "2026, phi ARCHITECT (GEOMETOR Digital Scriptorium)"

register_greek_book_track()

if "extensions" in globals():
    if "geometor.heron.sphinx_ext" not in extensions:  # noqa: F405
        extensions.append("geometor.heron.sphinx_ext")  # noqa: F405

if "intersphinx_mapping" in globals():
    configure_local_intersphinx(intersphinx_mapping, _PROJECT_ROOT)  # noqa: F405
