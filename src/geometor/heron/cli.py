"""Command-line interface for ``geometor.heron``."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from rich.console import Console
from rich.table import Table

from geometor.heron.compile_codex import verify_codex_tracks, write_apparatus_pages
from geometor.heron.concordance import CODEX_UNITS, load_concordance
from geometor.heron.constructions import (
    construct_area_division,
    construct_catoptrica_reflection,
    construct_dioptra_tunnel,
    construct_heron_proof,
    construct_heronian_gnomon,
)
from geometor.heron.mensuration import heron_sqrt_convergents, verify_quadrea_identity
from geometor.heron.render import export_all_figures

__all__ = ["build_parser", "main"]


def build_parser() -> argparse.ArgumentParser:
    """Build the ``heron`` CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="heron",
        description=(
            "GEOMETOR Heron: 4-Track Bilingual Book Codex & Exact Symbolic "
            "Constructions for Hero of Alexandria."
        ),
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("summary", help="Display Codex units and exact symbolic model summary")
    sub.add_parser("verify", help="Verify symbolic models, SHA-256 manifest, and 4-track Codex")
    sub.add_parser("compile-apparatus", help="Compile apparatus RST pages from resources/metrica")
    sub.add_parser("export-figures", help="Render all interactive .euclid-graphic SVGs")
    return parser


def _cmd_summary(console: Console) -> int:
    conc = load_concordance()
    entries = conc.get("entries", [])
    n_loci = len(entries) if isinstance(entries, list) else 0

    tbl = Table(title="GEOMETOR • heron — 4-Track Book Codex Units")
    tbl.add_column("Order", justify="right", style="cyan")
    tbl.add_column("Slug", style="green")
    tbl.add_column("Edition Pages", style="yellow")
    tbl.add_column("Title")
    for unit in CODEX_UNITS:
        tbl.add_row(str(unit.order), unit.slug, unit.edition_pages, unit.title)
    console.print(tbl)

    _, inv_i8 = construct_heron_proof()
    convs = heron_sqrt_convergents(720, steps=2)
    console.print(
        f"[bold]Concordance Loci:[/bold] {n_loci} · "
        f"[bold]Metrica I.8 (13,14,15):[/bold] Δ = {inv_i8['area']} "
        f"(Q-area = {inv_i8['quadrea']}) · "
        f"[bold]√720 x₁:[/bold] {convs[1].approx} (x₂ = {convs[2].approx})"
    )
    return 0


def _cmd_verify(console: Console) -> int:
    verify_quadrea_identity()
    for builder in (
        construct_heron_proof,
        construct_catoptrica_reflection,
        construct_area_division,
        construct_heronian_gnomon,
        construct_dioptra_tunnel,
    ):
        builder()

    report = verify_codex_tracks()
    if not report["valid"]:
        errs = report.get("errors", [])
        if isinstance(errs, list):
            for err in errs:
                console.print(f"[red]ERROR:[/red] {err}")
        return 1

    console.print(
        f"[green]VERIFIED:[/green] 5 symbolic models + {report['units']} Codex units "
        f"({report['track_files']} track files) + SHA-256 manifest."
    )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Execute the ``heron`` CLI entry point.

    Args:
        argv: Optional command-line argument sequence.

    Returns:
        Process exit code (``0`` on success).
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    console = Console()

    cmd = args.command or "summary"
    if cmd == "summary":
        return _cmd_summary(console)
    if cmd == "verify":
        return _cmd_verify(console)
    if cmd == "compile-apparatus":
        written = write_apparatus_pages()
        console.print(f"[green]Compiled {len(written)} apparatus RST pages.[/green]")
        return 0
    if cmd == "export-figures":
        svgs = export_all_figures()
        console.print(f"[green]Exported {len(svgs)} interactive SVG files.[/green]")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
