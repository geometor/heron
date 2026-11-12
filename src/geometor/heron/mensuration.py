r"""Exact symbolic mensuration formulas and rational approximations from Hero's Metrica.

Implements Hero of Alexandria's plane and solid mensuration algorithms in 100% exact
SymPy algebra alongside Norman J. Wildberger's Rational Trigonometry quadrea identity:

- **Heron's Formula & Archimedes' Quadrea** (*Metrica* I.8; *Wildberger* W.07).
- **Hero's Iterative Square-Root Extraction** (*Metrica* I.8: :math:`\sqrt{720}`).
- **Pentagon Golden Section Lemma** (*Metrica* I.18 Lemma over :math:`\mathbb{Q}(\phi)`).
- **Regular Polygon Area Ratios** (*Metrica* I.17–I.25, :math:`n = 3 \dots 12`).
- **Dionysodorus's Torus Theorem** (*Metrica* II.13: :math:`V = 2\pi^2 R r^2`).
- **Truncated Pyramid/Cone Mean-Plus-Third-Difference Identity** (*Metrica* II.6–10).
- **Exact Volumes of the Five Platonic Solids** (*Metrica* II.16–19).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import sympy as sp

__all__ = [
    "PHI",
    "PolygonRatioEntry",
    "SqrtConvergent",
    "archimedes_quadrea",
    "dionysodorus_torus_volume",
    "frustum_volume",
    "heron_area",
    "heron_area_squared",
    "heron_sqrt_convergents",
    "pentagon_golden_lemma",
    "platonic_solid_volumes",
    "regular_polygon_ratios",
    "verify_frustum_mean_identity",
    "verify_quadrea_identity",
]

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / 2


@dataclass(frozen=True)
class SqrtConvergent:
    r"""Single step of Hero's iteration :math:`x_{k+1} = \frac{1}{2}(x_k + N/x_k)`.

    Attributes:
        step: Zero-based iteration index (:math:`k = 0` is the initial rational seed).
        approx: Exact rational convergent :math:`x_k \in \mathbb{Q}`.
        square: Exact square :math:`x_k^2 \in \mathbb{Q}`.
        residual: Exact quadratic error :math:`x_k^2 - N \ge 0` (for :math:`k \ge 1`).
    """

    step: int
    approx: sp.Rational
    square: sp.Rational
    residual: sp.Rational


@dataclass(frozen=True)
class PolygonRatioEntry:
    r"""Exact vs. Heronian area-to-side-squared ratio :math:`A_n / s^2` for a regular :math:`n`-gon.

    Attributes:
        sides: Number of polygon sides :math:`n \in \{3, \dots, 12\}`.
        name: Classical polygon name.
        metrica_prop: Proposition locus in Schöne's *Metrica* Book I.
        exact_area_over_s2: Exact closed-form or cyclotomic SymPy expression for :math:`A_n / s^2`.
        heron_rational_over_s2: Hero's practical rational multiplier :math:`p / q` in *Metrica*.
        relative_error: Signed relative error :math:`(p/q - A_n/s^2) / (A_n/s^2)` as a float.
    """

    sides: int
    name: str
    metrica_prop: str
    exact_area_over_s2: sp.Expr
    heron_rational_over_s2: sp.Rational
    relative_error: float


def heron_area_squared(
    a: int | sp.Expr,
    b: int | sp.Expr,
    c: int | sp.Expr,
) -> sp.Expr:
    r"""Compute exact squared area :math:`\Delta^2 = s(s-a)(s-b)(s-c)` from side lengths.

    Args:
        a: Length of side :math:`a = BC`.
        b: Length of side :math:`b = CA`.
        c: Length of side :math:`c = AB`.

    Returns:
        Exact simplified SymPy expression for :math:`\Delta^2`.
    """
    sa, sb, sc = sp.sympify(a), sp.sympify(b), sp.sympify(c)
    s = (sa + sb + sc) / 2
    return sp.simplify(s * (s - sa) * (s - sb) * (s - sc))


def heron_area(
    a: int | sp.Expr,
    b: int | sp.Expr,
    c: int | sp.Expr,
) -> sp.Expr:
    r"""Compute exact triangle area :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}` (*Metrica* I.8).

    Args:
        a: Length of side :math:`a = BC`.
        b: Length of side :math:`b = CA`.
        c: Length of side :math:`c = AB`.

    Returns:
        Exact SymPy expression for :math:`\Delta`.
    """
    return sp.simplify(sp.sqrt(heron_area_squared(a, b, c)))


def archimedes_quadrea(
    q_a: int | sp.Expr,
    q_b: int | sp.Expr,
    q_c: int | sp.Expr,
) -> sp.Expr:
    r"""Compute Wildberger's quadrea :math:`\mathcal{A} = (Q_a+Q_b+Q_c)^2 - 2(Q_a^2+Q_b^2+Q_c^2)`.

    Requires only the three side quadrances :math:`Q_a = a^2, Q_b = b^2, Q_c = c^2`
    with zero square roots, satisfying :math:`\mathcal{A} = 16\Delta^2`.

    Args:
        q_a: Side quadrance :math:`Q_a`.
        q_b: Side quadrance :math:`Q_b`.
        q_c: Side quadrance :math:`Q_c`.

    Returns:
        Exact polynomial SymPy expression for :math:`\mathcal{A} = 16\Delta^2`.
    """
    qa, qb, qc = sp.sympify(q_a), sp.sympify(q_b), sp.sympify(q_c)
    return sp.simplify((qa + qb + qc) ** 2 - 2 * (qa**2 + qb**2 + qc**2))


def verify_quadrea_identity() -> sp.Expr:
    r"""Prove polynomially that :math:`\mathcal{A}(a^2, b^2, c^2) - 16 s(s-a)(s-b)(s-c) \equiv 0`.

    Returns:
        Exact :class:`sympy.Integer` ``0`` certifying the identity in :math:`\mathbb{Z}[a, b, c]`.
    """
    a_sym, b_sym, c_sym = sp.symbols("a b c", positive=True)
    diff = sp.expand(
        archimedes_quadrea(a_sym**2, b_sym**2, c_sym**2)
        - 16 * heron_area_squared(a_sym, b_sym, c_sym)
    )
    if diff != 0:
        msg = f"Quadrea identity failed: {diff}"
        raise AssertionError(msg)
    return sp.Integer(0)


def heron_sqrt_convergents(
    n_val: int | sp.Rational,
    steps: int = 4,
    x0: int | sp.Rational | None = None,
) -> list[SqrtConvergent]:
    r"""Generate exact rational convergents to :math:`\sqrt{N}` via Hero's *Metrica* I.8 method.

    If ``x0`` is omitted, selects the integer whose square is nearest to ``n_val``
    (matching Hero's choice :math:`x_0 = 27` with :math:`27^2 = 729` for :math:`N = 720`).

    Args:
        n_val: Positive integer or rational radicand :math:`N`.
        steps: Number of Newton–Heron averaging steps after :math:`x_0`.
        x0: Optional positive rational starting seed.

    Returns:
        List of ``steps + 1`` :class:`SqrtConvergent` records from :math:`k = 0` to ``steps``.
    """
    radicand = sp.Rational(n_val)
    if radicand <= 0:
        msg = "Radicand n_val must be strictly positive."
        raise ValueError(msg)

    if x0 is None:
        lo = (
            math.isqrt(int(radicand))
            if radicand.q == 1
            else max(1, int(math.sqrt(float(radicand))))
        )
        hi = lo + 1
        lo_r, hi_r = sp.Rational(lo), sp.Rational(hi)
        seed = lo_r if abs(lo_r**2 - radicand) <= abs(hi_r**2 - radicand) else hi_r
    else:
        seed = sp.Rational(x0)

    if seed <= 0:
        msg = "Initial seed x0 must be strictly positive."
        raise ValueError(msg)

    history: list[SqrtConvergent] = []
    xk = seed
    for k in range(steps + 1):
        sq = xk**2
        history.append(
            SqrtConvergent(
                step=k,
                approx=xk,
                square=sq,
                residual=sq - radicand,
            )
        )
        if k < steps:
            xk = sp.Rational(1, 2) * (xk + radicand / xk)
    return history


def pentagon_golden_lemma() -> dict[str, sp.Expr]:
    r"""Verify Hero's *Metrica* I.18 Golden Section Lemma in :math:`\mathbb{Q}(\phi)`.

    In right triangle :math:`AB\Gamma` with :math:`\angle\Gamma = 90^\circ` and
    :math:`\angle A = 36^\circ = \frac{2}{5}\cdot 90^\circ`, doubling :math:`A\Gamma`
    to :math:`A\Delta = 2\cdot A\Gamma` yields :math:`\angle AB\Delta = 108^\circ`,
    so :math:`A\Delta` is cut in extreme and mean ratio with greater segment :math:`AB`:
    :math:`AB = A\Delta / \phi = (2/\phi)\cdot A\Gamma = (\sqrt{5} - 1) A\Gamma`,
    hence :math:`(AB + A\Gamma)^2 = 5 \cdot A\Gamma^2`.

    Returns:
        Dictionary of exact symbolic invariants and Hero's :math:`81 : 16` rational proxy.
    """
    h = sp.Symbol("h", positive=True)
    a_delta = 2 * h
    a_b = sp.simplify(a_delta / PHI)
    lhs = sp.expand((a_b + h) ** 2)
    rhs = 5 * h**2
    residual = sp.simplify(lhs - rhs)
    if residual != 0:
        msg = f"Pentagon golden lemma identity failed: {residual}"
        raise AssertionError(msg)

    return {
        "phi": PHI,
        "radius_over_apothem": sp.simplify(a_b / h),
        "sum_over_apothem": sp.simplify((a_b + h) / h),
        "sum_sq_over_apothem_sq": sp.Integer(5),
        "heron_sum_sq_ratio": sp.Rational(81, 16),
        "heron_area_over_s2": sp.Rational(5, 3),
        "heron_refined_area_over_s2": sp.Rational(12, 7),
        "exact_area_over_s2": sp.sqrt(25 + 10 * sp.sqrt(5)) / 4,
        "identity_residual": residual,
    }


def regular_polygon_ratios() -> list[PolygonRatioEntry]:
    r"""Return exact vs. Heronian area multipliers :math:`A_n / s^2` (*Metrica* I.17–25).

    Returns:
        List of 10 :class:`PolygonRatioEntry` records for :math:`n = 3, \dots, 12`.
    """
    specs: list[tuple[int, str, str, sp.Expr, sp.Rational]] = [
        (3, "Equilateral triangle", "I.17", sp.sqrt(3) / 4, sp.Rational(13, 30)),
        (4, "Square", "I.1", sp.Integer(1), sp.Rational(1, 1)),
        (5, "Regular pentagon", "I.18", sp.sqrt(25 + 10 * sp.sqrt(5)) / 4, sp.Rational(5, 3)),
        (6, "Regular hexagon", "I.19", 3 * sp.sqrt(3) / 2, sp.Rational(13, 5)),
        (
            7,
            "Regular heptagon",
            "I.20",
            sp.Rational(7, 4) * sp.cot(sp.pi / 7),
            sp.Rational(43, 12),
        ),
        (8, "Regular octagon", "I.21", 2 * (1 + sp.sqrt(2)), sp.Rational(29, 6)),
        (
            9,
            "Regular enneagon",
            "I.22",
            sp.Rational(9, 4) * sp.cot(sp.pi / 9),
            sp.Rational(51, 8),
        ),
        (
            10,
            "Regular decagon",
            "I.23",
            sp.Rational(5, 2) * sp.sqrt(5 + 2 * sp.sqrt(5)),
            sp.Rational(15, 2),
        ),
        (
            11,
            "Regular hendecagon",
            "I.24",
            sp.Rational(11, 4) * sp.cot(sp.pi / 11),
            sp.Rational(66, 7),
        ),
        (12, "Regular dodecagon", "I.25", 3 * (2 + sp.sqrt(3)), sp.Rational(45, 4)),
    ]
    out: list[PolygonRatioEntry] = []
    for n_sides, name, prop, exact_expr, heron_rat in specs:
        ex_f = float(exact_expr.evalf())
        hr_f = float(heron_rat)
        rel_err = (hr_f - ex_f) / ex_f
        out.append(
            PolygonRatioEntry(
                sides=n_sides,
                name=name,
                metrica_prop=prop,
                exact_area_over_s2=exact_expr,
                heron_rational_over_s2=heron_rat,
                relative_error=rel_err,
            )
        )
    return out


def dionysodorus_torus_volume(
    major_radius: int | sp.Expr,
    minor_radius: int | sp.Expr,
    *,
    pi_approx: sp.Rational | None = None,
) -> sp.Expr:
    r"""Compute the volume :math:`V = 2\pi^2 R r^2` of a torus (*σπεῖρα*, *Metrica* II.13).

    On Hero's *Metrica* II.13 dimensions (:math:`R = 14, r = 6`) with Archimedean
    :math:`\pi \approx 22/7`, returns the exact fraction :math:`69696/7 = 9956\frac{4}{7}`.

    Args:
        major_radius: Distance :math:`R` from torus center to generating circle center.
        minor_radius: Radius :math:`r` of the generating meridian circle.
        pi_approx: Optional rational proxy for :math:`\pi` (e.g., ``sp.Rational(22, 7)``).

    Returns:
        Exact SymPy expression (or :class:`sympy.Rational` if ``pi_approx`` is rational).
    """
    r_maj = sp.sympify(major_radius)
    r_min = sp.sympify(minor_radius)
    pi_val: sp.Expr = sp.pi if pi_approx is None else sp.Rational(pi_approx)
    return sp.simplify(2 * pi_val**2 * r_maj * r_min**2)


def frustum_volume(
    b1: int | sp.Expr,
    b2: int | sp.Expr,
    height: int | sp.Expr,
) -> sp.Expr:
    r"""Compute square pyramidal frustum volume via Hero's *Metrica* II.6/II.9 decomposition.

    Evaluates :math:`V = h \left[ ((b_1 + b_2)/2)^2 + \frac{1}{3}((b_1 - b_2)/2)^2 \right]`.

    Args:
        b1: Lower square base edge :math:`b_1`.
        b2: Upper parallel square edge :math:`b_2`.
        height: Perpendicular altitude :math:`h`.

    Returns:
        Exact simplified SymPy expression equal to :math:`\frac{h}{3}(b_1^2 + b_1 b_2 + b_2^2)`.
    """
    u, v, h = sp.sympify(b1), sp.sympify(b2), sp.sympify(height)
    mean_sq = ((u + v) / 2) ** 2
    diff_sq_third = (((u - v) / 2) ** 2) / 3
    return sp.simplify(h * (mean_sq + diff_sq_third))


def verify_frustum_mean_identity() -> sp.Expr:
    """Prove that Hero's mean-plus-third-half-difference equals :math:`(u^2 + u v + v^2)/3`.

    Returns:
        Exact :class:`sympy.Integer` ``0``.
    """
    u_sym, v_sym, h_sym = sp.symbols("u v h")
    classical = h_sym * (u_sym**2 + u_sym * v_sym + v_sym**2) / 3
    residual = sp.expand(frustum_volume(u_sym, v_sym, h_sym) - classical)
    if residual != 0:
        msg = f"Frustum identity failed: {residual}"
        raise AssertionError(msg)
    return sp.Integer(0)


def platonic_solid_volumes(edge: int | sp.Expr = 1) -> dict[str, sp.Expr]:
    r"""Compute exact closed-form volumes of the Five Platonic Solids (*Metrica* II.15–19).

    Args:
        edge: Common edge length :math:`a` (defaults to ``1``).

    Returns:
        Mapping from solid name to exact volume over :math:`\mathbb{Q}(\sqrt{2}, \sqrt{5})`.
    """
    a = sp.sympify(edge)
    a3 = a**3
    return {
        "tetrahedron": sp.simplify(sp.sqrt(2) * a3 / 12),
        "cube": sp.simplify(a3),
        "octahedron": sp.simplify(sp.sqrt(2) * a3 / 3),
        "icosahedron": sp.simplify(5 * (3 + sp.sqrt(5)) * a3 / 12),
        "dodecahedron": sp.simplify((15 + 7 * sp.sqrt(5)) * a3 / 4),
    }
