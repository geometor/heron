"""Hero's Synthetic Incircle & Cyclic Quadrilateral Proof of Heron's Formula (Metrica I.8).

Executes the exact SymPy / geometor.model construction of Hero's Metrica I.8 on
triangle (13, 14, 15) alongside his (7, 8, 9) -> sqrt(720) benchmark and
Wildberger's Rational Trigonometry Quadrea identity.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import sympy as sp  # noqa: E402
import sympy.geometry as spg  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.heron.constructions import construct_heron_proof  # noqa: E402
from geometor.heron.mensuration import (  # noqa: E402
    archimedes_quadrea,
    heron_area,
    heron_area_squared,
    verify_quadrea_identity,
)


def main() -> int:
    console = Console()
    console.rule("[bold cyan]Hero of Alexandria — Metrica I.8: Synthetic Proof of Δ[/bold cyan]")

    model, inv = construct_heron_proof()
    poly_zero = verify_quadrea_identity()

    pt_table = Table(title="Exact Constructive Points in Metrica I.8 on (13, 14, 15)")
    pt_table.add_column("ID", style="bold yellow")
    pt_table.add_column("Exact Coordinates (x, y)", style="green")
    pt_table.add_column("Role in Schöne (1903, pp. 20–24, Fig. 7)")

    roles = {
        "A": "Apex vertex (5, 12)",
        "B": "Left base vertex (0, 0)",
        "C": "Right base vertex Γ (14, 0)",
        "H": "Incenter H = X(1)",
        "D": "Touchpoint Δ on AB",
        "E": "Touchpoint E on BC",
        "F": "Touchpoint Z on CA",
        "G": "Extended point Θ on CB (|CG| = s = 21, |BG| = s - a = 7)",
        "K": "Intersection K of perpendicular HL with BC",
        "L": "Vertex Λ of cyclic quadrilateral CHBL",
        "M": "Circumcenter of cyclic quadrilateral CHBL",
    }
    for el, meta in model.items():
        if isinstance(el, spg.Point) and not meta.guide and meta.ID in roles:
            pt_table.add_row(meta.ID, f"({el.x}, {el.y})", roles[meta.ID])
    console.print(pt_table)

    inv_table = Table(title="Deductive Proof Invariants & Rational Trigonometry Quadrea")
    inv_table.add_column("Quantity", style="cyan")
    inv_table.add_column("Exact Value", style="bold magenta")
    inv_table.add_column("Verification")

    inv_table.add_row("Sides (a, b, c)", f"({inv['a']}, {inv['b']}, {inv['c']})", "Given ∈ Z")
    inv_table.add_row("Semiperimeter s = |CG|", str(inv["s"]), "a+b+c = 42 -> s = 21")
    inv_table.add_row("Inradius r = |HE|", str(inv["r"]), "Area = s*r = 21*4 = 84")
    inv_table.add_row(
        "Tangents (s-a, s-b, s-c)",
        f"({inv['s_minus_a']}, {inv['s_minus_b']}, {inv['s_minus_c']})",
        "|BG|=7, |BE|=6, |EC|=8",
    )
    inv_table.add_row(
        "Elements VI.8 Altitude |KE|*|EC|",
        str(inv["ke_times_ec"]),
        f"Equals r^2 = {inv['r']**2}",
    )
    inv_table.add_row(
        "Synthesis Area^2 (13, 14, 15)",
        str(inv["area_squared"]),
        f"21*7*6*8 = 7056 -> Δ = {inv['area']}",
    )
    inv_table.add_row(
        "Quadrea A(196, 225, 169)",
        str(inv["quadrea"]),
        f"16 * Δ^2 = 16 * 7056 (Polynomial diff = {poly_zero})",
    )
    area_789_sq = heron_area_squared(7, 8, 9)
    area_789 = heron_area(7, 8, 9)
    quadrea_789 = archimedes_quadrea(49, 64, 81)
    inv_table.add_row(
        "Analysis Exemplar (7, 8, 9)",
        f"Δ^2 = {area_789_sq}, Δ = {area_789}",
        f"Quadrea A = {quadrea_789} = 16*720 (≈ {float(sp.N(area_789, 8)):.6f})",
    )
    console.print(inv_table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
