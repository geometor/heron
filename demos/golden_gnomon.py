"""Golden Gnomon (Def. 58), Pentagon Lemma (I.18), Torus (II.13) & Dioptra Tunnel (Ch. 15).

Demonstrates Hero's golden-section morphogenesis in Q(phi), Dionysodorus's torus
unrolling (9956 4/7), and two-portal mountain tunneling via orthogonal coordinate traverse.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.heron.constructions import (  # noqa: E402
    construct_dionysodorus_torus,
    construct_dioptra_tunnel,
    construct_heronian_gnomon,
    construct_pentagon_lemma,
)


def main() -> int:
    console = Console()
    console.rule(
        "[bold cyan]Hero of Alexandria — Golden Gnomon, Torus & Dioptra Tunnel[/bold cyan]"
    )

    _m_pent, pent_inv = construct_pentagon_lemma()
    _m_gnom, gnom_inv = construct_heronian_gnomon()
    _m_tor, tor_inv = construct_dionysodorus_torus()
    _m_diop, diop_inv = construct_dioptra_tunnel()

    table = Table(title="Exact Symbolic Invariants Across Metrica, Definitiones & Dioptra")
    table.add_column("Locus", style="bold yellow")
    table.add_column("Invariant", style="cyan")
    table.add_column("Exact Symbolic Value", style="bold green")

    table.add_row(
        "Metrica I.18 Lemma",
        "(|BA| + |AC|)^2 == 5 |AC|^2",
        (
            f"{pent_inv['sum_sq']} == {pent_inv['five_ac_sq']} "
            f"(|AB| = {pent_inv['ab']}, s_36° = {pent_inv['spread_36_deg']})"
        ),
    )
    table.add_row(
        "Definitiones §58",
        "Recursive Aspect Quadrance Q_long / Q_short",
        (
            f"Whole = {gnom_inv['whole_aspect_quadrance']}, "
            f"Seed = {gnom_inv['seed_aspect_quadrance']}, "
            f"Gen2 = {gnom_inv['gen2_aspect_quadrance']}"
        ),
    )
    table.add_row(
        "Definitiones §58",
        "Golden Carrier Cross-Ratio (E1, A; B, E)",
        str(gnom_inv["golden_cross_ratio"]),
    )
    table.add_row(
        "Metrica II.13 Torus",
        "Volume V = 2*pi^2*R*r^2 (R=14, r=6)",
        (
            f"Exact = {tor_inv['exact_volume']}, "
            f"Hero (pi=22/7) = {tor_inv['heron_rational_volume']} (9956 4/7)"
        ),
    )
    table.add_row(
        "Dioptra Ch. 15 Tunnel",
        "Subterranean Chord BD from Traverse",
        f"(Δx, Δy) = ({diop_inv['east_displacement']}, {diop_inv['north_displacement']}), "
        f"|BD| = {diop_inv['tunnel_length']}, Spread = {diop_inv['heading_spread']}",
    )
    console.print(table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
