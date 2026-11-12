"""Proportional Divisions of Figures & Solids in Hero's Metrica Book III (Props. 1, 2 & 20).

Demonstrates exact straightedge-and-compass parallel area cuts on triangle (13, 14, 15)
across arbitrary integer ratios m : n alongside Hero's cube-root extraction of cbrt(100).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.heron.constructions import construct_area_division  # noqa: E402


def heron_cbrt_interpolation(n_val: int, lower_int: int, upper_int: int) -> sp.Rational:
    """Evaluate Hero's Metrica III.20 weighted cube-root interpolation."""
    n_rat = sp.Rational(n_val)
    lo = sp.Rational(lower_int)
    hi = sp.Rational(upper_int)
    d_lo = n_rat - lo**3
    d_hi = hi**3 - n_rat
    return lo + (hi * d_lo) / (hi * d_lo + lo * d_hi)


def main() -> int:
    console = Console()
    console.rule(
        "[bold cyan]Hero of Alexandria — Metrica Book III: Proportional Divisions[/bold cyan]"
    )

    table = Table(
        title="Metrica III.2 Parallel Area Cuts DE || BC on Triangle (13, 14, 15), Area = 84"
    )
    table.add_column("Target Ratio m : n", style="bold yellow")
    table.add_column("Cut Quadrance Q(A, D)", style="green")
    table.add_column("Exact Cut Length |AD|", style="cyan")
    table.add_column("Upper Area(ADE)", style="magenta")
    table.add_column("Lower Area(DECB)", style="magenta")
    table.add_column("Verified Ratio")

    for m_r, n_r in ((3, 1), (1, 1), (5, 3), (4, 3)):
        _model, inv = construct_area_division(m_ratio=m_r, n_ratio=n_r)
        table.add_row(
            f"{m_r} : {n_r}",
            str(inv["ad_quadrance"]),
            str(inv["ad_length"]),
            str(inv["area_ade"]),
            str(inv["area_decb"]),
            str(inv["parallel_ratio"]),
        )
    console.print(table)

    cbrt_100_hero = heron_cbrt_interpolation(100, 4, 5)
    exact_100 = 100 ** (1 / 3)
    rel_err = abs(float(cbrt_100_hero) - exact_100) / exact_100 * 100
    console.print(
        f"[bold green]Metrica III.20 Cube-Root Extraction of ∛100:[/bold green] "
        f"Hero's rational value = {cbrt_100_hero} = 4 + 9/14 ≈ {float(cbrt_100_hero):.6f} "
        f"(Exact ∛100 ≈ {exact_100:.6f}, relative error = {rel_err:.4f}%)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
