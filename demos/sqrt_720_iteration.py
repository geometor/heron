"""Hero's Iterative Square-Root Extraction on sqrt(720) & Exact (7, 8, 9) Model (Metrica I.8).

Demonstrates quadratic error squaring x_{k+1}^2 - N = (x_k^2 - N)^2 / (4 x_k^2) in
pure SymPy Rational arithmetic alongside the exact geometor.model construction of
Hero's (7, 8, 9) triangle of area sqrt(720) = 12*sqrt(5).
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import sympy as sp  # noqa: E402
from geometor.model import Model  # noqa: E402
from geometor.model.invariants import polygon_area2, quadrance  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.heron.mensuration import heron_area, heron_sqrt_convergents  # noqa: E402


def build_789_model() -> tuple[Model, sp.Expr]:
    """Construct Hero's (7, 8, 9) exemplar triangle by compass intersection in Q(sqrt(5))."""
    m = Model("heron_789_triangle", auto_intersect=False, enable_logging=False)
    pt_b = m.given_point(sp.Integer(0), sp.Integer(0), ID="B")
    pt_c = m.given_point(sp.Integer(8), sp.Integer(0), ID="C")
    m.construct_line(pt_b, pt_c, classes=["given", "carrier"])

    # Circle (B, 7) via point (7, 0) and Circle (C, 9) via point (-1, 0)
    with m.subconstruction("sideCircles") as scope:
        p_r7 = m.set_point(sp.Integer(7), sp.Integer(0), guide=True)
        p_r9 = m.set_point(sp.Integer(-1), sp.Integer(0), guide=True)
        c_b7 = m.construct_circle(pt_b, p_r7, guide=True)
        c_c9 = m.construct_circle(pt_c, p_r9, guide=True)
        pt_a = m.intersect(c_b7, c_c9, side_of=(pt_b, pt_c, 1), ID="A", classes=["apex"])
        scope.keep(pt_a)

    m.set_polygon([pt_a, pt_b, pt_c], classes=["triangle"])
    area_exact = sp.simplify(polygon_area2([pt_a, pt_b, pt_c]) / 2)
    assert sp.simplify(quadrance(pt_a, pt_b) - 49) == 0
    assert sp.simplify(quadrance(pt_b, pt_c) - 64) == 0
    assert sp.simplify(quadrance(pt_c, pt_a) - 81) == 0
    assert sp.simplify(area_exact - heron_area(7, 8, 9)) == 0
    return m, area_exact


def main() -> int:
    console = Console()
    console.rule("[bold cyan]Hero of Alexandria — Metrica I.8: √720 Rational Iteration[/bold cyan]")

    convergents = heron_sqrt_convergents(720, steps=4, x0=27)
    model_789, area_exact = build_789_model()
    pt_a = next(pt for pt in model_789.points if model_789[pt].ID == "A")

    table = Table(title="Exact Rational Convergents x_{k+1} = (x_k + 720 / x_k) / 2")
    table.add_column("Step k", justify="right", style="bold yellow")
    table.add_column("Rational x_k", style="green")
    table.add_column("Decimal Value", style="cyan")
    table.add_column("Quadratic Residual (x_k^2 - 720)", style="magenta")
    table.add_column("Accurate Digits", justify="right")

    exact_hp = sp.sqrt(720).evalf(60)
    for row in convergents:
        approx_f = float(row.approx)
        abs_err = float(abs(row.approx.evalf(60) - exact_hp))
        digits = "∞" if abs_err == 0 else f"{max(0.0, -math.log10(abs_err)):.1f}"
        res_str = (
            str(row.residual)
            if len(str(row.residual)) <= 36
            else f"≈ {float(row.residual):.3e}"
        )
        approx_str = (
            str(row.approx)
            if len(str(row.approx)) <= 32
            else f"{str(row.approx.p)[:12]}…/{str(row.approx.q)[:10]}…"
        )
        table.add_row(
            str(row.step),
            approx_str,
            f"{approx_f:.15f}",
            res_str,
            digits,
        )
    console.print(table)

    console.print(
        f"[bold green]Exact (7, 8, 9) Compass Construction in Q(√5):[/bold green] "
        f"Apex A = ({pt_a.x}, {pt_a.y}), Exact Area Δ = {area_exact} "
        f"(Δ^2 = {sp.simplify(area_exact**2)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
