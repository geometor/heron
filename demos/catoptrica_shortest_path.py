"""Hero's Variational Shortest-Path Proof of the Law of Reflection (Catoptrica Prop. 4).

Constructs Hero's mirror-reflection unfolding proof (Schmidt 1900, pp. 368–372, Fig. 92)
and tabulates exact optical path lengths across mirror positions Z_x = (x, 0).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.heron.constructions import construct_catoptrica_reflection  # noqa: E402


def main() -> int:
    console = Console()
    console.rule(
        "[bold cyan]Hero of Alexandria — Catoptrica Prop. 4: Shortest-Path Reflection[/bold cyan]"
    )

    _model, inv = construct_catoptrica_reflection()

    cx, cy = sp.Integer(1), sp.Integer(3)
    dx, dy = sp.Integer(10), sp.Integer(6)

    table = Table(title="Optical Ray Path Length L(x) = |C Z_x| + |Z_x D| along Mirror y = 0")
    table.add_column("Mirror x", justify="right", style="bold yellow")
    table.add_column("Exact Path Length L(x)", style="green")
    table.add_column("Numeric L(x)", justify="right", style="cyan")
    table.add_column("Incidence Spread s_i", style="magenta")
    table.add_column("Reflection Spread s_r", style="magenta")
    table.add_column("Status")

    for x_val in (1, 2, 3, 4, 5, 7, 9, 10):
        x = sp.Integer(x_val)
        q1 = (x - cx) ** 2 + cy**2
        q2 = (dx - x) ** 2 + dy**2
        length_expr = sp.simplify(sp.sqrt(q1) + sp.sqrt(q2))
        s_inc = sp.Rational(cy**2, q1)
        s_ref = sp.Rational(dy**2, q2)
        status = (
            "[bold green]GLOBAL MINIMUM (Equal Angles / Collinear C-E-K)[/bold green]"
            if x_val == 4
            else ("Hero's Perturbed Z = (7,0)" if x_val == 7 else "Unequal angles (L > L_min)")
        )
        table.add_row(
            str(x_val),
            str(length_expr),
            f"{float(length_expr.evalf()):.6f}",
            str(s_inc),
            str(s_ref),
            status,
        )

    console.print(table)
    console.print(
        f"[bold green]Verified Unfolded Minimum:[/bold green] "
        f"|CE| + |ED| = {inv['optimal_length']} (Squared = {inv['optimal_length_sq']}) < "
        f"|CZ| + |ZD| = {inv['perturbed_length']} (Squared = {inv['perturbed_length_sq']}, "
        f"Excess Δ(L^2) = {inv['excess_sq']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
