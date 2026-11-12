"""Exact symbolic geometric constructions for Hero of Alexandria in ``geometor.model``.

Every model in this module obeys the GEOMETOR Iron Law of 100% Exact Symbolic Algebra:

- Initialized with ``Model(..., auto_intersect=False, enable_logging=False)``.
- Zero ``float`` or :class:`sympy.Float` coordinates anywhere in the model.
- Clean alphanumeric point IDs without underscores for ``geometor_interactive.js``.
- Verified step-by-step via :class:`~geometor.model.Model` proof assertions and
  Rational Trigonometry invariants (``quadrance``, ``line_spread``, ``cross_ratio``).
"""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.algebra import zero_test
from geometor.model.invariants import cross_ratio, line_spread, polygon_area2, quadrance

from geometor.heron.mensuration import PHI, archimedes_quadrea, heron_area_squared

__all__ = [
    "construct_area_division",
    "construct_catoptrica_reflection",
    "construct_dionysodorus_torus",
    "construct_dioptra_tunnel",
    "construct_heron_proof",
    "construct_heronian_gnomon",
    "construct_pentagon_lemma",
]


def _perp_bisector_line(
    model: Model,
    p1: spg.Point,
    p2: spg.Point,
    *,
    scope_name: str,
    classes: list[str] | None = None,
) -> spg.Line:
    """Construct the exact perpendicular bisector of ``p1`` and ``p2`` via compass."""
    with model.subconstruction(scope_name) as scope:
        c1 = model.construct_circle(p1, p2, guide=True)
        c2 = model.construct_circle(p2, p1, guide=True)
        pole1 = model.intersect(c1, c2, index=0, guide=True)
        pole2 = model.intersect(c1, c2, index=1, guide=True)
        bis_line = model.construct_line(pole1, pole2, classes=classes)
        scope.keep(bis_line)
        return bis_line


def _perp_at_point_on_line(
    model: Model,
    line: spg.Line,
    pt_foot: spg.Point,
    pt_ref_on_line: spg.Point,
    *,
    scope_name: str,
    classes: list[str] | None = None,
) -> spg.Line:
    """Erect the exact perpendicular to ``line`` at ``pt_foot`` via compass."""
    with model.subconstruction(scope_name) as scope:
        c_sym = model.construct_circle(pt_foot, pt_ref_on_line, guide=True)
        pt_opp = model.intersect(c_sym, line, other_than=pt_ref_on_line, guide=True)
        c1 = model.construct_circle(pt_ref_on_line, pt_opp, guide=True)
        c2 = model.construct_circle(pt_opp, pt_ref_on_line, guide=True)
        pole1 = model.intersect(c1, c2, index=0, guide=True)
        pole2 = model.intersect(c1, c2, index=1, guide=True)
        perp = model.construct_line(pole1, pole2, classes=classes)
        scope.keep(perp)
        return perp


def _drop_perp_from_point(
    model: Model,
    line: spg.Line,
    pt_ext: spg.Point,
    pt_on_line: spg.Point,
    *,
    scope_name: str,
    foot_id: str,
    foot_classes: list[str] | None = None,
    line_classes: list[str] | None = None,
) -> tuple[spg.Line, spg.Point]:
    """Drop the exact perpendicular from external point ``pt_ext`` onto ``line``."""
    with model.subconstruction(scope_name) as scope:
        c_cut = model.construct_circle(pt_ext, pt_on_line, guide=True)
        pt_mirror_on_line = model.intersect(
            c_cut, line, other_than=pt_on_line, guide=True
        )
        c1 = model.construct_circle(pt_on_line, pt_mirror_on_line, guide=True)
        c2 = model.construct_circle(pt_mirror_on_line, pt_on_line, guide=True)
        pole = model.intersect(c1, c2, other_than=pt_ext, index=0, guide=True)
        perp = model.construct_line(pt_ext, pole, classes=line_classes)
        foot = model.intersect(perp, line, ID=foot_id, classes=foot_classes)
        scope.keep(perp, foot)
        return perp, foot


def _angle_bisector_line(
    model: Model,
    vertex: spg.Point,
    ray1_line: spg.Line,
    ray1_pt: spg.Point,
    ray2_line: spg.Line,
    ray2_pt: spg.Point,
    *,
    scope_name: str,
    classes: list[str] | None = None,
) -> spg.Line:
    """Construct the internal angle bisector at ``vertex`` by compass."""
    with model.subconstruction(scope_name) as scope:
        c_v = model.construct_circle(vertex, ray1_pt, guide=True)
        q2 = model.intersect(c_v, ray2_line, on_ray=(vertex, ray2_pt), guide=True)
        c1 = model.construct_circle(ray1_pt, vertex, guide=True)
        c2 = model.construct_circle(q2, vertex, guide=True)
        apex = model.intersect(c1, c2, other_than=vertex, guide=True)
        bis = model.construct_line(vertex, apex, classes=classes)
        scope.keep(bis)
        return bis


def construct_heron_proof(
    model: Model | None = None,
) -> tuple[Model, dict[str, sp.Expr]]:
    r"""Construct Hero's synthetic incircle proof of *Metrica* I.8 on ``(13, 14, 15)``.

    Matches Schöne (1903), pp. 20–24 (**Fig. 7**), setting ``B = (0, 0)``,
    ``C = (14, 0)`` (Hero's :math:`\Gamma`), and ``A = (5, 12)`` so :math:`|AB| = 13`,
    :math:`|BC| = 14`, :math:`|CA| = 15`, semiperimeter :math:`s = 21`, incenter
    ``H = (6, 4)`` (:math:`X(1)`), inradius :math:`r = 4`, extended semiperimeter point
    ``G = (-7, 0)`` (Hero's :math:`\Theta`), orthogonal meet ``K = (4, 0)`` on ``BC``,
    and cyclic-quadrilateral vertex ``L = (0, -8)`` (Hero's :math:`\Lambda`).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Tuple ``(model, invariants)`` containing the populated model and verified
        symbolic expressions.
    """
    m = (
        model
        if model is not None
        else Model("heron_metrica_i8", auto_intersect=False, enable_logging=False)
    )

    # 1. Given: scalene Heronian triangle ABC with AB=13, BC=14, CA=15
    pt_b = m.given_point(sp.Integer(0), sp.Integer(0), ID="B")
    pt_c = m.given_point(sp.Integer(14), sp.Integer(0), ID="C")
    pt_a = m.given_point(sp.Integer(5), sp.Integer(12), ID="A")

    l_bc = m.construct_line(pt_b, pt_c, classes=["given", "carrier"], by="Post.1")
    l_ab = m.construct_line(pt_a, pt_b, classes=["given", "carrier"], by="Post.1")
    l_ca = m.construct_line(pt_c, pt_a, classes=["given", "carrier"], by="Post.1")
    tri_abc = m.set_polygon([pt_a, pt_b, pt_c], classes=["given", "triangle"])

    # 2. Construct: Incenter H = X(1) via angle bisectors of <B and <C (Elements IV.4)
    l_bh = _angle_bisector_line(
        m, pt_b, l_ab, pt_a, l_bc, pt_c, scope_name="bisectB", classes=["bisector"]
    )
    l_ch = _angle_bisector_line(
        m, pt_c, l_bc, pt_b, l_ca, pt_a, scope_name="bisectC", classes=["bisector"]
    )
    pt_h = m.intersect(l_bh, l_ch, ID="H", classes=["incenter", "meet"], by="IV.4")
    m.construct_line(pt_a, pt_h, classes=["bisector"], by="Post.1")

    # Drop perpendicular radius HE onto BC and describe incircle (H, E)
    l_he, pt_e = _drop_perp_from_point(
        m,
        l_bc,
        pt_h,
        pt_b,
        scope_name="dropHE",
        foot_id="E",
        foot_classes=["touchpoint"],
        line_classes=["radius"],
    )
    incircle = m.construct_circle(pt_h, pt_e, classes=["incircle"], by="IV.4")
    pt_d = m.intersect(incircle, l_ab, ID="D", classes=["touchpoint"], by="III.18")
    pt_f = m.intersect(incircle, l_ca, ID="F", classes=["touchpoint"], by="III.18")

    seg_hd = m.set_segment(pt_h, pt_d, classes=["radius"], by="Post.1")
    seg_he = m.set_segment(pt_h, pt_e, classes=["radius"], by="Post.1")
    seg_hf = m.set_segment(pt_h, pt_f, classes=["radius"], by="Post.1")

    # Extend CB past B to G (Hero's Theta) so |BG| = |AD| = s - a:
    # For any triangle, midpoint of U1 (x = -c) and U2 (x = a - b) on BC is x = -(s - a).
    with m.subconstruction("extendBG") as scope:
        c_ba = m.construct_circle(pt_b, pt_a, guide=True)
        u1 = m.intersect(c_ba, l_bc, beyond=(pt_c, pt_b), guide=True)
        c_ca = m.construct_circle(pt_c, pt_a, guide=True)
        u2 = m.intersect(c_ca, l_bc, beyond=(pt_c, pt_b), guide=True)
        bis_u = _perp_bisector_line(m, u1, u2, scope_name="midU", classes=["guide"])
        pt_g = m.intersect(bis_u, l_bc, ID="G", classes=["semiperimeter"])
        scope.keep(pt_g)

    seg_bg = m.set_segment(pt_b, pt_g, classes=["golden", "tangent"], by="I.3")
    seg_ad = m.set_segment(pt_a, pt_d, classes=["golden", "tangent"])
    seg_af = m.set_segment(pt_a, pt_f, classes=["tangent"])
    seg_bd = m.set_segment(pt_b, pt_d, classes=["tangent"])
    seg_be = m.set_segment(pt_b, pt_e, classes=["tangent"])
    seg_ce = m.set_segment(pt_c, pt_e, classes=["tangent"])
    seg_cf = m.set_segment(pt_c, pt_f, classes=["tangent"])
    seg_cg = m.set_segment(pt_c, pt_g, classes=["semiperimeter"])

    # Erect HL perpendicular to CH at H, and BL perpendicular to BC at B
    l_hl = _perp_at_point_on_line(
        m, l_ch, pt_h, pt_c, scope_name="perpCH", classes=["auxiliary"]
    )
    l_bl = _perp_at_point_on_line(
        m, l_bc, pt_b, pt_e, scope_name="perpBC", classes=["auxiliary"]
    )
    pt_k = m.intersect(l_hl, l_bc, ID="K", classes=["meet"], by="Post.2")
    pt_l = m.intersect(l_hl, l_bl, ID="L", classes=["meet"], by="Post.2")
    l_cl = m.construct_line(pt_c, pt_l, classes=["quadrilateral"], by="Post.1")
    quad_chbl = m.set_polygon([pt_c, pt_h, pt_b, pt_l], classes=["cyclic"])

    # Circumcircle of cyclic quadrilateral CHBL (center M = midpoint of hypotenuse CL)
    with m.subconstruction("cyclicCircle") as scope:
        bis_cl = _perp_bisector_line(m, pt_c, pt_l, scope_name="midCL")
        pt_m = m.intersect(bis_cl, l_cl, ID="M", classes=["auxiliary"])
        cyc_circ = m.construct_circle(pt_m, pt_c, classes=["cyclic"], by="III.22")
        scope.keep(pt_m, cyc_circ)

    # 3. Demonstrate: Verify every deductive link in Hero's proof
    m.assert_equal(seg_hd, seg_he, seg_hf, by="I.def.15", label="Incircle radii equal")
    m.assert_equal(seg_ad, seg_af, seg_bg, by="III.17", label="AD = AF = BG = s - a")
    m.assert_equal(seg_bd, seg_be, by="III.17", label="BD = BE = s - b")
    m.assert_equal(seg_ce, seg_cf, by="III.17", label="CE = CF = s - c")
    m.assert_perpendicular(l_ch, l_hl, at=pt_h, by="I.11")
    m.assert_perpendicular(l_bc, l_bl, at=pt_b, by="I.11")
    m.assert_perpendicular(l_bc, l_he, at=pt_e, by="III.18")
    m.assert_parallel(l_bl, l_he, by="I.28")
    m.assert_concyclic(pt_c, pt_h, pt_b, pt_l, by="III.22")
    m.assert_spread_equal((pt_a, pt_h, pt_d), (pt_c, pt_l, pt_b), by="III.22")

    q_cg = quadrance(pt_c, pt_g)
    q_he = quadrance(pt_h, pt_e)
    q_bg = quadrance(pt_b, pt_g)
    q_be = quadrance(pt_b, pt_e)
    q_ec = quadrance(pt_e, pt_c)
    q_ke = quadrance(pt_k, pt_e)

    # Right triangle KHC altitude theorem (Elements VI.8): |KE|*|EC| = |HE|^2
    ke_times_ec = sp.sqrt(q_ke * q_ec)
    if not zero_test(ke_times_ec - q_he):
        msg = f"Right-triangle altitude check failed: {ke_times_ec} != {q_he}"
        raise AssertionError(msg)

    # Hero's climax: Area(ABC)^2 = |CG|^2 * |HE|^2 = |CG|*|BG|*|BE|*|EC|
    area_abc = polygon_area2([pt_a, pt_b, pt_c]) / 2
    lhs_area_sq = area_abc**2
    mid_area_sq = q_cg * q_he
    rhs_heron_prod = sp.sqrt(q_cg * q_bg * q_be * q_ec)
    quadrea_val = archimedes_quadrea(
        quadrance(pt_b, pt_c), quadrance(pt_c, pt_a), quadrance(pt_a, pt_b)
    )

    if not (
        zero_test(lhs_area_sq - mid_area_sq)
        and zero_test(lhs_area_sq - rhs_heron_prod)
        and zero_test(quadrea_val - 16 * lhs_area_sq)
        and zero_test(lhs_area_sq - heron_area_squared(14, 15, 13))
    ):
        msg = "Symbolic verification of Hero's Formula failed."
        raise AssertionError(msg)

    m.conclude(tri_abc, incircle, seg_cg, seg_he, quad_chbl, kind="qed", by="Metrica.I.8")

    invariants: dict[str, sp.Expr] = {
        "a": sp.sqrt(quadrance(pt_b, pt_c)),
        "b": sp.sqrt(quadrance(pt_c, pt_a)),
        "c": sp.sqrt(quadrance(pt_a, pt_b)),
        "s": sp.sqrt(q_cg),
        "r": sp.sqrt(q_he),
        "s_minus_a": sp.sqrt(q_bg),
        "s_minus_b": sp.sqrt(q_be),
        "s_minus_c": sp.sqrt(q_ec),
        "ke_times_ec": ke_times_ec,
        "area": area_abc,
        "area_squared": lhs_area_sq,
        "quadrea": quadrea_val,
        "cyclic_radius_sq": quadrance(pt_m, pt_c),
    }
    return m, invariants


def construct_pentagon_lemma(
    model: Model | None = None,
) -> tuple[Model, dict[str, sp.Expr]]:
    r"""Construct Hero's *Metrica* I.18 Pentagon Golden Section Lemma in :math:`\mathbb{Q}(\phi)`.

    Constructs ``A = (-1, 0)``, ``C = (0, 0)`` (Hero's :math:`\Gamma`), ``D = (1, 0)``
    (Hero's :math:`\Delta`), cuts ``AD`` in extreme and mean ratio via compass so
    ``|AG| = |AB| = |BD| = sqrt(5) - 1 = 2/phi``, and proves
    :math:`(|BA| + |AC|)^2 = 5 |AC|^2`.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Tuple ``(model, invariants)``.
    """
    m = (
        model
        if model is not None
        else Model("heron_pentagon_lemma", auto_intersect=False, enable_logging=False)
    )

    pt_a = m.given_point(sp.Integer(-1), sp.Integer(0), ID="A")
    pt_c = m.given_point(sp.Integer(0), sp.Integer(0), ID="C")
    l_ac = m.construct_line(pt_a, pt_c, classes=["given", "carrier"], by="Post.1")

    # Double AC to D so |CD| = |AC| = 1, |AD| = 2
    with m.subconstruction("doubleAC") as scope:
        c_ca = m.construct_circle(pt_c, pt_a, guide=True)
        pt_d = m.intersect(c_ca, l_ac, other_than=pt_a, ID="D", classes=["given"])
        scope.keep(pt_d)

    # Erect perpendicular bisector of AD at C, and cut AD in extreme & mean ratio (II.11)
    l_perp_c = _perp_bisector_line(
        m, pt_a, pt_d, scope_name="perpC", classes=["carrier"]
    )
    with m.subconstruction("goldenCutAD") as scope:
        l_perp_a = _perp_at_point_on_line(
            m, l_ac, pt_a, pt_c, scope_name="perpA", classes=["guide"]
        )
        c_at = m.construct_circle(pt_a, pt_c, guide=True)
        pt_t = m.intersect(
            c_at, l_perp_a, side_of=(pt_a, pt_d, 1), ID="T", guide=True
        )
        l_td = m.construct_line(pt_t, pt_d, guide=True)
        c_ta = m.construct_circle(pt_t, pt_a, guide=True)
        pt_w = m.intersect(c_ta, l_td, between=(pt_t, pt_d), guide=True)
        c_dw = m.construct_circle(pt_d, pt_w, classes=["golden"])
        pt_k = m.intersect(c_dw, l_ac, between=(pt_a, pt_d), guide=True)
        pt_b = m.intersect(
            c_dw, l_perp_c, side_of=(pt_a, pt_d, 1), ID="B", classes=["apex", "golden"]
        )
        # Mark Golden Section G on AD with |AG| = |AB| = sqrt(5) - 1
        c_ab = m.construct_circle(pt_a, pt_b, classes=["golden"])
        pt_g = m.intersect(
            c_ab, l_ac, between=(pt_a, pt_d), ID="G", classes=["golden"]
        )
        scope.keep(pt_b, pt_g, c_ab)
        _ = pt_k

    l_ab = m.construct_line(pt_a, pt_b, classes=["carrier"], by="Post.1")
    m.construct_line(pt_b, pt_d, classes=["carrier"], by="Post.1")
    tri_abd = m.set_polygon([pt_a, pt_b, pt_d], classes=["triangle"])
    seg_ag = m.set_segment(pt_a, pt_g, classes=["golden"])
    seg_ab = m.set_segment(pt_a, pt_b, classes=["golden"])
    seg_bd = m.set_segment(pt_b, pt_d, classes=["golden"])
    seg_ac = m.set_segment(pt_a, pt_c, classes=["given"])
    seg_cd = m.set_segment(pt_c, pt_d, classes=["given"])

    m.assert_perpendicular(l_ac, l_perp_c, at=pt_c, by="I.11")
    m.assert_equal(seg_ac, seg_cd, by="I.def.15")
    m.assert_equal(seg_ab, seg_bd, seg_ag, by="I.4")
    m.assert_spread_equal((pt_a, pt_b, pt_c), (pt_d, pt_b, pt_c), by="I.8")

    len_ab = sp.sqrt(quadrance(pt_a, pt_b))
    len_ac = sp.sqrt(quadrance(pt_a, pt_c))
    sum_sq = sp.simplify((len_ab + len_ac) ** 2)
    five_ac_sq = 5 * quadrance(pt_a, pt_c)
    if not zero_test(sum_sq - five_ac_sq):
        msg = f"Pentagon Golden Lemma failed: {sum_sq} != {five_ac_sq}"
        raise AssertionError(msg)

    m.conclude(tri_abd, seg_ab, seg_ag, kind="qed", by="Metrica.I.18")
    return m, {
        "ab": sp.simplify(len_ab),
        "ac": len_ac,
        "sum_sq": sum_sq,
        "five_ac_sq": five_ac_sq,
        "spread_36_deg": sp.simplify(line_spread(l_ac, l_ab)),
        "phi": PHI,
    }


def construct_dionysodorus_torus(
    model: Model | None = None,
) -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the meridian section of Dionysodorus's torus (*Metrica* II.13).

    Models Schöne (1903), pp. 126–130 on ``A = (0, 0)``, inner rim ``C = (8, 0)``,
    tube center ``Z = (14, 0)``, outer rim ``B = (20, 0)``, vertical tube diameter
    ``D = (14, 6)`` and ``E = (14, -6)``, and revolution-axis endpoints ``H1 = (0, 6)``,
    ``H2 = (0, -6)``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Tuple ``(model, invariants)``.
    """
    m = (
        model
        if model is not None
        else Model("heron_dionysodorus_torus", auto_intersect=False, enable_logging=False)
    )

    pt_a = m.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_c = m.given_point(sp.Integer(8), sp.Integer(0), ID="C")
    pt_b = m.given_point(sp.Integer(20), sp.Integer(0), ID="B")
    l_ab = m.construct_line(pt_a, pt_b, classes=["given", "carrier"], by="Post.1")

    # Bisect BC to obtain generating circle center Z = (14, 0) and vertical line DZE
    l_dze = _perp_bisector_line(
        m, pt_c, pt_b, scope_name="bisectBC", classes=["carrier"]
    )
    pt_z = m.intersect(l_dze, l_ab, ID="Z", classes=["incenter", "meet"], by="I.10")
    tube_circle = m.construct_circle(pt_z, pt_b, classes=["incircle"], by="Post.3")
    pt_d = m.intersect(
        tube_circle, l_dze, side_of=(pt_a, pt_b, 1), ID="D", classes=["touchpoint"]
    )
    pt_e = m.intersect(
        tube_circle, l_dze, side_of=(pt_a, pt_b, -1), ID="E", classes=["touchpoint"]
    )

    # Erect revolution axis H1 A H2 perpendicular to AB at A, and parallels DH1, EH2
    l_axis = _perp_at_point_on_line(
        m, l_ab, pt_a, pt_c, scope_name="axisA", classes=["carrier"]
    )
    l_dh = _perp_at_point_on_line(
        m, l_dze, pt_d, pt_z, scope_name="parD", classes=["auxiliary"]
    )
    l_eh = _perp_at_point_on_line(
        m, l_dze, pt_e, pt_z, scope_name="parE", classes=["auxiliary"]
    )
    pt_h1 = m.intersect(l_axis, l_dh, ID="H1", classes=["meet"])
    pt_h2 = m.intersect(l_axis, l_eh, ID="H2", classes=["meet"])
    rect_meridian = m.set_polygon(
        [pt_d, pt_e, pt_h2, pt_h1], classes=["cyclic", "quadrilateral"]
    )
    seg_az = m.set_segment(pt_a, pt_z, classes=["golden"])
    seg_zb = m.set_segment(pt_z, pt_b, classes=["radius"])

    m.assert_perpendicular(l_ab, l_axis, at=pt_a, by="I.11")
    m.assert_perpendicular(l_ab, l_dze, at=pt_z, by="I.10")
    m.assert_parallel(l_dh, l_ab, by="I.28")
    m.assert_parallel(l_eh, l_ab, by="I.28")
    m.assert_equal(seg_zb, (pt_z, pt_c), (pt_z, pt_d), (pt_z, pt_e), by="I.def.15")

    r_major = sp.sqrt(quadrance(pt_a, pt_z))
    r_minor = sp.sqrt(quadrance(pt_z, pt_b))
    rect_half = polygon_area2([pt_d, pt_e, pt_h2, pt_h1]) / 4
    heron_vol = sp.Rational(2) * sp.Rational(22, 7) ** 2 * r_major * r_minor**2

    m.conclude(tube_circle, rect_meridian, seg_az, kind="qed", by="Metrica.II.13")
    return m, {
        "major_radius": r_major,
        "minor_radius": r_minor,
        "meridian_half_rect": rect_half,
        "exact_volume": 2 * sp.pi**2 * r_major * r_minor**2,
        "heron_rational_volume": heron_vol,
    }


def construct_catoptrica_reflection(
    model: Model | None = None,
) -> tuple[Model, dict[str, sp.Expr]]:
    r"""Construct Hero's Variational Shortest-Path Reflection Proof (*Catoptrica* Prop. 4).

    Models Schmidt (1900), pp. 368–372 (**Fig. 92**): plane mirror ``A = (0, 0)``,
    ``B = (12, 0)``, eye ``C = (1, 3)`` (:math:`\Gamma`), object ``D = (10, 6)``
    (:math:`\Delta`), foot ``H = (10, 0)``, reflected virtual image ``K = (10, -6)``,
    equal-angle reflection point ``E = (4, 0)``, and unequal-angle point ``Z = (7, 0)``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Tuple ``(model, invariants)`` proving :math:`(|CE|+|ED|)^2 = 162 < 180 = (|CZ|+|ZD|)^2`.
    """
    m = (
        model
        if model is not None
        else Model("heron_catoptrica_4", auto_intersect=False, enable_logging=False)
    )

    pt_a = m.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = m.given_point(sp.Integer(12), sp.Integer(0), ID="B")
    pt_c = m.given_point(sp.Integer(1), sp.Integer(3), ID="C")
    pt_d = m.given_point(sp.Integer(10), sp.Integer(6), ID="D")
    pt_z = m.given_point(sp.Integer(7), sp.Integer(0), ID="Z")

    l_ab = m.construct_line(pt_a, pt_b, classes=["given", "carrier"], by="Post.1")

    # Drop perpendicular DH to mirror AB and reflect D across H to K
    l_dh, pt_h = _drop_perp_from_point(
        m,
        l_ab,
        pt_d,
        pt_b,
        scope_name="dropDH",
        foot_id="H",
        foot_classes=["touchpoint"],
        line_classes=["auxiliary"],
    )
    c_hd = m.construct_circle(pt_h, pt_d, classes=["guide"], guide=True, by="Post.3")
    pt_k = m.intersect(
        c_hd, l_dh, other_than=pt_d, ID="K", classes=["meet"], by="I.3"
    )

    # Unfolded straight segment CK meets mirror AB at optimal reflection point E
    l_ck = m.construct_line(pt_c, pt_k, classes=["bisector"], by="Post.1")
    pt_e = m.intersect(l_ck, l_ab, ID="E", classes=["incenter", "meet"], by="Post.1")

    l_ed = m.construct_line(pt_e, pt_d, classes=["bisector"], by="Post.1")
    seg_ce = m.set_segment(pt_c, pt_e, classes=["golden"])
    seg_ed = m.set_segment(pt_e, pt_d, classes=["golden"])
    seg_ek = m.set_segment(pt_e, pt_k, classes=["golden"])
    m.set_segment(pt_c, pt_z, classes=["tangent"])
    seg_zd = m.set_segment(pt_z, pt_d, classes=["tangent"])
    seg_zk = m.set_segment(pt_z, pt_k, classes=["tangent"])
    seg_dh = m.set_segment(pt_d, pt_h, classes=["radius"])
    seg_hk = m.set_segment(pt_h, pt_k, classes=["radius"])
    tri_czk = m.set_polygon([pt_c, pt_z, pt_k], classes=["triangle"])

    # Deductive assertions matching Hero/Olympiodorus word-for-word
    m.assert_perpendicular(l_ab, l_dh, at=pt_h, by="I.12")
    m.assert_equal(seg_dh, seg_hk, by="I.def.15")
    m.assert_equal(seg_ed, seg_ek, by="I.4")
    m.assert_equal(seg_zd, seg_zk, by="I.4")
    m.assert_collinear(pt_c, pt_e, pt_k, by="I.14")
    m.assert_spread_equal((l_ab, l_ck), (l_ab, l_ed), signed=False, by="I.15")

    len_opt = sp.simplify(sp.sqrt(quadrance(pt_c, pt_e)) + sp.sqrt(quadrance(pt_e, pt_d)))
    len_ck = sp.simplify(sp.sqrt(quadrance(pt_c, pt_k)))
    len_pert = sp.simplify(sp.sqrt(quadrance(pt_c, pt_z)) + sp.sqrt(quadrance(pt_z, pt_d)))
    opt_sq = sp.simplify(len_opt**2)
    pert_sq = sp.simplify(len_pert**2)

    if not zero_test(len_opt - len_ck) or sp.simplify(pert_sq - opt_sq) <= 0:
        msg = "Shortest-path reflection inequality failed."
        raise AssertionError(msg)

    m.conclude(seg_ce, seg_ed, tri_czk, kind="qed", by="Catoptrica.4")
    return m, {
        "incidence_spread": line_spread(l_ab, l_ck),
        "reflection_spread": line_spread(l_ab, l_ed),
        "optimal_length": len_opt,
        "optimal_length_sq": opt_sq,
        "perturbed_length": len_pert,
        "perturbed_length_sq": pert_sq,
        "excess_sq": sp.simplify(pert_sq - opt_sq),
    }


def construct_area_division(
    model: Model | None = None,
    m_ratio: int = 3,
    n_ratio: int = 1,
) -> tuple[Model, dict[str, sp.Expr]]:
    """Construct Hero's *Metrica* III.1 & III.2 area divisions on ``(13, 14, 15)``.

    Constructs both:

    - **Prop. III.1**: Vertex cevian ``AV`` dividing ``BC`` at ``V = (35/4, 0)`` in ``5 : 3``.
    - **Prop. III.2**: Line ``DE || BC`` dividing area in ratio ``m_ratio : n_ratio``
      (default ``3 : 1``) by constructing the mean proportional ``|AD|^2 = (m/(m+n))|AB|^2``
      via a semicircle on diameter ``AB`` (*Elements* VI.13 & VI.19).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.
        m_ratio: Upper triangle area share :math:`m > 0`.
        n_ratio: Lower trapezium area share :math:`n > 0`.

    Returns:
        Tuple ``(model, invariants)``.
    """
    if m_ratio <= 0 or n_ratio <= 0:
        msg = "Area ratio integers m_ratio and n_ratio must be positive."
        raise ValueError(msg)

    m = (
        model
        if model is not None
        else Model("heron_metrica_iii", auto_intersect=False, enable_logging=False)
    )

    pt_b = m.given_point(sp.Integer(0), sp.Integer(0), ID="B")
    pt_c = m.given_point(sp.Integer(14), sp.Integer(0), ID="C")
    pt_a = m.given_point(sp.Integer(5), sp.Integer(12), ID="A")

    l_bc = m.construct_line(pt_b, pt_c, classes=["given", "carrier"], by="Post.1")
    l_ab = m.construct_line(pt_a, pt_b, classes=["given", "carrier"], by="Post.1")
    l_ca = m.construct_line(pt_c, pt_a, classes=["given", "carrier"], by="Post.1")
    m.set_polygon([pt_a, pt_b, pt_c], classes=["given", "triangle"])

    # Prop. III.1: Vertex division in 5 : 3 along base BC -> V = (35/4, 0)
    pt_v = m.set_point(
        sp.Rational(5, 8) * pt_c.x,
        sp.Integer(0),
        classes=["touchpoint"],
        ID="V",
        by="VI.1",
    )
    m.set_segment(pt_a, pt_v, classes=["auxiliary"], by="Post.1")

    # Prop. III.2: Parallel cut DE || BC in ratio m : n via semicircle on AB
    frac = sp.Rational(m_ratio, m_ratio + n_ratio)
    pt_p = m.set_point(
        pt_a.x + frac * (pt_b.x - pt_a.x),
        pt_a.y + frac * (pt_b.y - pt_a.y),
        classes=["auxiliary"],
        ID="P",
        by="VI.9",
    )

    with m.subconstruction("meanProportionalAB") as scope:
        bis_ab = _perp_bisector_line(m, pt_a, pt_b, scope_name="midAB")
        pt_m1 = m.intersect(bis_ab, l_ab, ID="M1", guide=True)
        semi_ab = m.construct_circle(pt_m1, pt_a, classes=["incircle"], by="Post.3")
        l_perp_p = _perp_at_point_on_line(
            m, l_ab, pt_p, pt_a, scope_name="perpP", classes=["guide"]
        )
        pt_r = m.intersect(
            semi_ab, l_perp_p, side_of=(pt_a, pt_b, -1), ID="R", classes=["touchpoint"]
        )
        c_ar = m.construct_circle(pt_a, pt_r, classes=["golden"], by="Post.3")
        pt_d = m.intersect(
            c_ar, l_ab, between=(pt_a, pt_b), ID="D", classes=["incenter", "golden"]
        )
        scope.keep(semi_ab, c_ar, pt_r, pt_d)
    m.set_segment(pt_p, pt_r, classes=["radius"], by="VI.13")

    # Parallel through D to horizontal base BC (drop perpendicular to BC then perp at D)
    with m.subconstruction("parallelDE") as scope:
        l_perp_d, _foot = _drop_perp_from_point(
            m,
            l_bc,
            pt_d,
            pt_b,
            scope_name="dropD",
            foot_id="F1",
            line_classes=["guide"],
        )
        l_de = _perp_at_point_on_line(
            m, l_perp_d, pt_d, _foot, scope_name="parDE", classes=["bisector"]
        )
        pt_e = m.intersect(
            l_de, l_ca, between=(pt_a, pt_c), ID="E", classes=["incenter", "golden"]
        )
        scope.keep(l_de, pt_e)

    tri_ade = m.set_polygon([pt_a, pt_d, pt_e], classes=["cyclic"])
    trap_decb = m.set_polygon([pt_d, pt_b, pt_c, pt_e], classes=["quadrilateral"])
    seg_de = m.set_segment(pt_d, pt_e, classes=["golden"], by="VI.2")

    m.assert_parallel(l_de, l_bc, by="I.28")
    m.assert_incident(pt_v, l_bc, by="VI.1")

    area_total = polygon_area2([pt_a, pt_b, pt_c]) / 2
    area_ade = polygon_area2([pt_a, pt_d, pt_e]) / 2
    area_decb = polygon_area2([pt_d, pt_b, pt_c, pt_e]) / 2
    area_abv = polygon_area2([pt_a, pt_b, pt_v]) / 2
    area_avc = polygon_area2([pt_a, pt_v, pt_c]) / 2

    if not zero_test(area_ade * n_ratio - area_decb * m_ratio):
        msg = f"Parallel area division failed: {area_ade} : {area_decb}"
        raise AssertionError(msg)
    if not zero_test(area_abv * 3 - area_avc * 5):
        msg = f"Vertex area division failed: {area_abv} : {area_avc}"
        raise AssertionError(msg)

    m.conclude(tri_ade, trap_decb, seg_de, kind="qef", by="Metrica.III.2")
    return m, {
        "total_area": area_total,
        "ad_quadrance": quadrance(pt_a, pt_d),
        "ad_length": sp.simplify(sp.sqrt(quadrance(pt_a, pt_d))),
        "area_ade": area_ade,
        "area_decb": area_decb,
        "parallel_ratio": sp.simplify(area_ade / area_decb),
        "area_abv": area_abv,
        "area_avc": area_avc,
        "bv_length": sp.sqrt(quadrance(pt_b, pt_v)),
        "vc_length": sp.sqrt(quadrance(pt_v, pt_c)),
    }


def construct_heronian_gnomon(
    model: Model | None = None,
) -> tuple[Model, dict[str, sp.Expr]]:
    r"""Construct Hero's Universal Gnomon (*Definitiones* §58) in :math:`\mathbb{Q}(\phi)`.

    Starts from unit square ``< A B C D >``, bisects ``AB`` at ``M = (1/2, 0)``, swings
    compass arc ``(M, C)`` to ``E = (phi, 0)``, completes ``< A E F D >`` with
    ``F = (phi, 1)``, and subdivides ``< B E F C >`` by a second square gnomon
    ``< B E G H >``, proving recursive similarity ``< A E F D > ~ < C B E F > ~ < H G F C >``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Tuple ``(model, invariants)``.
    """
    m = (
        model
        if model is not None
        else Model("heron_universal_gnomon", auto_intersect=False, enable_logging=False)
    )

    pt_a = m.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = m.given_point(sp.Integer(1), sp.Integer(0), ID="B")
    l_ab = m.construct_line(pt_a, pt_b, classes=["given", "carrier"], by="Post.1")

    # Construct unit square ABCD by compass perpendiculars (Elements I.46)
    l_ad = _perp_at_point_on_line(
        m, l_ab, pt_a, pt_b, scope_name="perpAD", classes=["carrier"]
    )
    l_bc = _perp_at_point_on_line(
        m, l_ab, pt_b, pt_a, scope_name="perpBC", classes=["carrier"]
    )
    with m.subconstruction("unitSquare") as scope:
        c_ad = m.construct_circle(pt_a, pt_b, guide=True)
        pt_d = m.intersect(c_ad, l_ad, side_of=(pt_a, pt_b, 1), ID="D", classes=["given"])
        c_bc = m.construct_circle(pt_b, pt_a, guide=True)
        pt_c = m.intersect(c_bc, l_bc, side_of=(pt_a, pt_b, 1), ID="C", classes=["given"])
        scope.keep(pt_d, pt_c)

    l_dc = m.construct_line(pt_d, pt_c, classes=["carrier"], by="Post.1")
    sq_gnomon1 = m.set_polygon([pt_a, pt_b, pt_c, pt_d], classes=["given", "triangle"])

    # Bisect AB at M and swing arc (M, C) onto AB extended to E = (phi, 0)
    l_bis = _perp_bisector_line(m, pt_a, pt_b, scope_name="midAB", classes=["guide"])
    pt_m = m.intersect(l_bis, l_ab, ID="M", classes=["touchpoint"], by="I.10")
    c_mc = m.construct_circle(pt_m, pt_c, classes=["golden"], by="II.11")
    pt_e = m.intersect(
        c_mc, l_ab, beyond=(pt_a, pt_b), ID="E", classes=["incenter", "golden"], by="II.11"
    )
    l_ef = _perp_at_point_on_line(
        m, l_ab, pt_e, pt_b, scope_name="perpEF", classes=["carrier"]
    )
    pt_f = m.intersect(l_ef, l_dc, ID="F", classes=["golden"], by="Post.2")

    # Second-order Heronian gnomon inside BEFC: square BEGH leaves similar HGFC
    with m.subconstruction("secondGnomon") as scope:
        c_eb = m.construct_circle(pt_e, pt_b, classes=["incircle"], by="Post.3")
        pt_g = m.intersect(
            c_eb, l_ef, between=(pt_e, pt_f), ID="G", classes=["touchpoint"]
        )
        l_gh = _perp_at_point_on_line(
            m, l_ef, pt_g, pt_e, scope_name="perpGH", classes=["bisector"]
        )
        pt_h = m.intersect(l_gh, l_bc, ID="H", classes=["touchpoint"])
        scope.keep(c_eb, pt_g, l_gh, pt_h)

    rect_whole = m.set_polygon([pt_a, pt_e, pt_f, pt_d], classes=["cyclic"])
    rect_seed = m.set_polygon([pt_b, pt_e, pt_f, pt_c], classes=["quadrilateral"])
    seg_ae = m.set_segment(pt_a, pt_e, classes=["golden"])
    seg_be = m.set_segment(pt_b, pt_e, classes=["golden"])

    m.assert_equal((pt_a, pt_b), (pt_b, pt_c), (pt_c, pt_d), (pt_d, pt_a), by="I.46")
    m.assert_equal((pt_b, pt_e), (pt_e, pt_g), (pt_g, pt_h), (pt_h, pt_b), by="I.46")
    m.assert_parallel(l_ad, l_bc, by="I.28")
    m.assert_parallel(l_bc, l_ef, by="I.28")

    # Verify Hero's Definition 58 similarity ratio across 3 nested generations in Q(phi)
    ratio_whole = sp.simplify(quadrance(pt_a, pt_e) / quadrance(pt_a, pt_d))
    ratio_seed = sp.simplify(quadrance(pt_b, pt_c) / quadrance(pt_b, pt_e))
    ratio_gen2 = sp.simplify(quadrance(pt_h, pt_g) / quadrance(pt_h, pt_c))
    phi_sq = sp.simplify(PHI**2)

    if not (
        zero_test(ratio_whole - phi_sq)
        and zero_test(ratio_seed - phi_sq)
        and zero_test(ratio_gen2 - phi_sq)
    ):
        msg = "Heronian Golden Gnomon similarity check failed."
        raise AssertionError(msg)

    # Projective cross-ratio along the golden carrier line (-phi^-1, 0, 1, phi) -> Cr
    pt_e_conj = m.intersect(c_mc, l_ab, other_than=pt_e, ID="E1", classes=["auxiliary"])
    cr_val = sp.simplify(cross_ratio(pt_e_conj, pt_a, pt_b, pt_e))

    m.conclude(sq_gnomon1, rect_whole, rect_seed, seg_ae, seg_be, kind="qed", by="Def.58")
    return m, {
        "phi": PHI,
        "phi_squared": phi_sq,
        "whole_aspect_quadrance": ratio_whole,
        "seed_aspect_quadrance": ratio_seed,
        "gen2_aspect_quadrance": ratio_gen2,
        "golden_cross_ratio": cr_val,
    }


def construct_dioptra_tunnel(
    model: Model | None = None,
) -> tuple[Model, dict[str, sp.Expr]]:
    r"""Construct Hero's Two-Portal Mountain Tunneling survey (*Dioptra* Ch. 15).

    Models Schöne (1903), pp. 238–240 (**Fig. 95**): portals ``B = (0, 0)`` and
    ``D = (12, 5)`` (tunnel length ``13``), orthogonal dioptra stations ``E = (-2, 0)``,
    ``Z = (-2, -3)``, ``H = (16, -3)``, ``G = (16, 8)`` (:math:`\Theta`), ``K = (14, 8)``,
    ``M = (14, 5)``, virtual right-angle vertex ``N = (12, 0)``, and exterior sighting
    triangles ``B O X`` (``O = (-6, 0), X = (-6, -5/2)``) and ``D P Q``
    (``P = (18, 5), Q = (18, 15/2)``) collinear along ``5x - 12y = 0``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Tuple ``(model, invariants)``.
    """
    m = (
        model
        if model is not None
        else Model("heron_dioptra_15", auto_intersect=False, enable_logging=False)
    )

    pt_b = m.given_point(sp.Integer(0), sp.Integer(0), ID="B")
    pt_d = m.given_point(sp.Integer(12), sp.Integer(5), ID="D")

    # Orthogonal dioptra traverse stations around the mountain foot
    pt_e = m.set_point(sp.Integer(-2), sp.Integer(0), classes=["touchpoint"], ID="E")
    pt_z = m.set_point(sp.Integer(-2), sp.Integer(-3), classes=["touchpoint"], ID="Z")
    pt_h = m.set_point(sp.Integer(16), sp.Integer(-3), classes=["touchpoint"], ID="H")
    pt_g = m.set_point(sp.Integer(16), sp.Integer(8), classes=["touchpoint"], ID="G")
    pt_k = m.set_point(sp.Integer(14), sp.Integer(8), classes=["touchpoint"], ID="K")

    l_eb = m.construct_line(pt_e, pt_b, classes=["carrier"], by="Dioptra.15")
    l_ez = m.construct_line(pt_e, pt_z, classes=["auxiliary"], by="Dioptra.15")
    l_zh = m.construct_line(pt_z, pt_h, classes=["auxiliary"], by="Dioptra.15")
    l_hg = m.construct_line(pt_h, pt_g, classes=["auxiliary"], by="Dioptra.15")
    l_gk = m.construct_line(pt_g, pt_k, classes=["auxiliary"], by="Dioptra.15")

    # Slide dioptra along perpendicular KL until portal D is sighted orthogonally at M
    l_kl = _perp_at_point_on_line(
        m, l_gk, pt_k, pt_g, scope_name="sightKL", classes=["auxiliary"]
    )
    l_md, pt_m = _drop_perp_from_point(
        m,
        l_kl,
        pt_d,
        pt_k,
        scope_name="sightMD",
        foot_id="M",
        foot_classes=["touchpoint"],
        line_classes=["carrier"],
    )

    # Reconstruct hidden right-triangle vertex N on EB extended by dropping DN perp EB
    l_dn, pt_n = _drop_perp_from_point(
        m,
        l_eb,
        pt_d,
        pt_b,
        scope_name="dropDN",
        foot_id="N",
        foot_classes=["meet"],
        line_classes=["radius"],
    )

    # Exterior sighting triangles BOX at portal B and DPQ at portal D
    pt_o = m.set_point(sp.Integer(-6), sp.Integer(0), classes=["auxiliary"], ID="O")
    pt_x = m.set_point(
        sp.Integer(-6), sp.Rational(-5, 2), classes=["incenter", "golden"], ID="X"
    )
    pt_p = m.set_point(sp.Integer(18), sp.Integer(5), classes=["auxiliary"], ID="P")
    pt_q = m.set_point(
        sp.Integer(18), sp.Rational(15, 2), classes=["incenter", "golden"], ID="Q"
    )

    l_tunnel = m.construct_line(pt_x, pt_q, classes=["bisector"], by="VI.4")
    seg_bd = m.set_segment(pt_b, pt_d, classes=["golden"])
    tri_bdn = m.set_polygon([pt_b, pt_n, pt_d], classes=["cyclic"])
    tri_box = m.set_polygon([pt_b, pt_o, pt_x], classes=["triangle"])
    tri_dpq = m.set_polygon([pt_d, pt_p, pt_q], classes=["triangle"])

    for p_start, p_end in (
        (pt_b, pt_e),
        (pt_e, pt_z),
        (pt_z, pt_h),
        (pt_h, pt_g),
        (pt_g, pt_k),
        (pt_k, pt_m),
        (pt_m, pt_d),
    ):
        m.set_segment(p_start, p_end, classes=["tangent"])

    # Verify orthogonal traverse, parallelism MD || BE || ZH, and exact collinearity X-B-D-Q
    m.assert_perpendicular(l_eb, l_ez, at=pt_e, by="Dioptra.15")
    m.assert_perpendicular(l_ez, l_zh, at=pt_z, by="Dioptra.15")
    m.assert_perpendicular(l_zh, l_hg, at=pt_h, by="Dioptra.15")
    m.assert_perpendicular(l_hg, l_gk, at=pt_g, by="Dioptra.15")
    m.assert_perpendicular(l_gk, l_kl, at=pt_k, by="Dioptra.15")
    m.assert_perpendicular(l_kl, l_md, at=pt_m, by="Dioptra.15")
    m.assert_perpendicular(l_eb, l_dn, at=pt_n, by="I.12")
    m.assert_parallel(l_md, l_eb, by="I.28")
    m.assert_parallel(l_md, l_zh, by="I.28")
    m.assert_collinear(pt_x, pt_b, pt_d, pt_q, by="VI.4")

    dx_sum = (pt_e.x - pt_b.x) + (pt_h.x - pt_z.x) + (pt_k.x - pt_g.x) + (pt_d.x - pt_m.x)
    dy_sum = (pt_z.y - pt_e.y) + (pt_g.y - pt_h.y) + (pt_m.y - pt_k.y)
    tunnel_len = sp.sqrt(quadrance(pt_b, pt_d))

    m.conclude(seg_bd, tri_bdn, tri_box, tri_dpq, l_tunnel, kind="qef", by="Dioptra.15")
    return m, {
        "east_displacement": dx_sum,
        "north_displacement": dy_sum,
        "tunnel_quadrance": quadrance(pt_b, pt_d),
        "tunnel_length": tunnel_len,
        "heading_spread": line_spread(l_eb, l_tunnel),
        "sight_ratio": sp.Rational(dx_sum, dy_sum),
    }
