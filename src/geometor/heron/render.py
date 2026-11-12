"""Publication-grade interactive ``.euclid-graphic`` SVG renderer for ``geometor.heron``.

Serializes exact :class:`~geometor.model.Model` constructions into crisp pixel-space
SVGs conforming simultaneously to:

1. Standalone GitHub / browser dark- and light-mode viewing via CSS custom properties, and
2. ``photon-platform/publish`` interactive figures (``svg.euclid-graphic``, ``<defs>``
   midpoint equality markers ``#geom-tick-1..3``, 3-vertex ``<path>`` segments and lines,
   ``#elements``, ``#graphics``, ``#highlights``, ``#points``, ``#labels``, ``data-ref``,
   and ``data-aliases`` consumed by ``geometor_interactive.js``).
"""

from __future__ import annotations

import html
import math
import re
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.sections import Section

from geometor.heron.constructions import (
    construct_area_division,
    construct_catoptrica_reflection,
    construct_dionysodorus_torus,
    construct_dioptra_tunnel,
    construct_heron_proof,
    construct_heronian_gnomon,
    construct_pentagon_lemma,
)

__all__ = [
    "EMBEDDED_SVG_DEFS",
    "EMBEDDED_SVG_STYLE",
    "export_all_figures",
    "export_svg",
    "render_svg_string",
]

EMBEDDED_SVG_DEFS: str = """  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-assert, #059669)"
            stroke-width="2" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-2" y1="-4.5" x2="-2" y2="4.5" stroke="var(--geom-assert, #059669)"
            stroke-width="2" stroke-linecap="round" />
      <line x1="2" y1="-4.5" x2="2" y2="4.5" stroke="var(--geom-assert, #059669)"
            stroke-width="2" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-3.5" y1="-4.5" x2="-3.5" y2="4.5" stroke="var(--geom-assert, #059669)"
            stroke-width="1.8" stroke-linecap="round" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-assert, #059669)"
            stroke-width="1.8" stroke-linecap="round" />
      <line x1="3.5" y1="-4.5" x2="3.5" y2="4.5" stroke="var(--geom-assert, #059669)"
            stroke-width="1.8" stroke-linecap="round" />
    </marker>
  </defs>"""

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    --svg-bg: #fafaf9;
    --geom-bg: #fafaf9;
    --ink: #1c1917;
    --geom-fg: #1c1917;
    --geom-accent: #d97706;
    --geom-assert: #059669;
    --label-halo: rgba(250, 250, 249, 0.92);
    --carrier: #334155;
    --conic: #0284c7;
    --cyclic: #7c3aed;
    --bisector: #0f766e;
    --aux: #64748b;
    --golden: #b45309;
    --tangent: #0369a1;
    --radius-col: #059669;
    --pt-given: #0f172a;
    --pt-incenter: #d97706;
    --pt-touch: #0284c7;
    --pt-meet: #7c3aed;
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic {
      --svg-bg: #141417;
      --geom-bg: #141417;
      --ink: #f4f4f5;
      --geom-fg: #f4f4f5;
      --geom-accent: #fbbf24;
      --geom-assert: #34d399;
      --label-halo: rgba(20, 20, 23, 0.92);
      --carrier: #cbd5e1;
      --conic: #38bdf8;
      --cyclic: #c084fc;
      --bisector: #2dd4bf;
      --aux: #94a3b8;
      --golden: #facc15;
      --tangent: #38bdf8;
      --radius-col: #34d399;
      --pt-given: #f1f5f9;
      --pt-incenter: #fbbf24;
      --pt-touch: #38bdf8;
      --pt-meet: #c084fc;
    }
  }
  .euclid-graphic .svg-bg { fill: var(--svg-bg); }
  .euclid-graphic .geom-circle.incircle-curve {
    fill: none; stroke: var(--conic); stroke-width: 2.25; opacity: 0.92;
  }
  .euclid-graphic .geom-circle.cyclic-curve {
    fill: none; stroke: var(--cyclic); stroke-width: 1.75;
    stroke-dasharray: 6 4; opacity: 0.78;
  }
  .euclid-graphic .geom-circle.golden-curve {
    fill: none; stroke: var(--golden); stroke-width: 1.9;
    stroke-dasharray: 5 3.5; opacity: 0.85;
  }
  .euclid-graphic .geom-line {
    fill: none; stroke: var(--aux); stroke-width: 1.35;
    stroke-linecap: round; opacity: 0.72;
  }
  .euclid-graphic .carrier-line { stroke: var(--carrier); stroke-width: 2.05; opacity: 0.92; }
  .euclid-graphic .bisector-line { stroke: var(--bisector); stroke-width: 1.85; opacity: 0.88; }
  .euclid-graphic .aux-line {
    stroke: var(--aux); stroke-width: 1.35; stroke-dasharray: 5 3.5; opacity: 0.75;
  }
  .euclid-graphic .quad-line { stroke: var(--cyclic); stroke-width: 1.75; opacity: 0.85; }
  .euclid-graphic .geom-segment {
    fill: none; stroke: var(--tangent); stroke-width: 2.5;
    stroke-linecap: round; opacity: 0.85;
  }
  .euclid-graphic .geom-segment.golden-segment {
    stroke: var(--golden); stroke-width: 3.3; opacity: 0.92;
  }
  .euclid-graphic .geom-segment.radius-segment {
    stroke: var(--radius-col); stroke-width: 2.3; opacity: 0.9;
  }
  .euclid-graphic .geom-segment.semi-segment {
    stroke: var(--carrier); stroke-width: 2.4; opacity: 0.82;
  }
  .euclid-graphic .geom-polygon.tri-poly {
    fill: var(--conic); fill-opacity: 0.06;
    stroke: var(--carrier); stroke-width: 1.9; stroke-linejoin: round;
  }
  .euclid-graphic .geom-polygon.cyclic-poly {
    fill: var(--cyclic); fill-opacity: 0.07;
    stroke: var(--cyclic); stroke-width: 1.6; stroke-linejoin: round;
  }
  .euclid-graphic .geom-polygon.quad-poly {
    fill: var(--golden); fill-opacity: 0.07;
    stroke: var(--golden); stroke-width: 1.6; stroke-linejoin: round;
  }
  .euclid-graphic .geom-point { fill: var(--pt-given); stroke: var(--svg-bg); stroke-width: 1.5; }
  .euclid-graphic .incenter-point { fill: var(--pt-incenter); stroke-width: 1.8; }
  .euclid-graphic .touch-point { fill: var(--pt-touch); }
  .euclid-graphic .meet-point { fill: var(--pt-meet); }
  .euclid-graphic .golden-point { fill: var(--golden); stroke-width: 1.8; }
  .euclid-graphic .geom-label {
    fill: var(--ink);
    font-size: 13.5px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: var(--label-halo);
    stroke-width: 3.6px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .geom-label-sub { font-size: 10px; font-weight: 600; }""".strip()


def _fmt(val: float) -> str:
    """Format a pixel coordinate compactly to 2 decimal places."""
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _clip_line_to_rect(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    """Clip an algebraic line :math:`a x + b y + c = 0` to a math viewport box."""
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))

    if len(unique_hits) < 2:
        return None
    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(
                unique_hits[j][0] - unique_hits[i][0],
                unique_hits[j][1] - unique_hits[i][1],
            )
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _split_point_label(
    pt_id: str,
    overrides: dict[str, tuple[str, str]] | None = None,
) -> tuple[str, str]:
    """Split an alphanumeric point ID into ``(base, subscript)`` for ``<tspan>``."""
    if overrides and pt_id in overrides:
        return overrides[pt_id]
    m = re.match(r"^([A-Za-z]+)(\d+)$", pt_id)
    if m:
        return (m.group(1), m.group(2))
    return (pt_id, "")


def _circle_css_classes(classes: set[str]) -> str:
    """Map model circle classes to semantic CSS classes."""
    if "cyclic" in classes:
        return "geom-circle cyclic-curve"
    if "golden" in classes:
        return "geom-circle golden-curve"
    return "geom-circle incircle-curve"


def _line_css_classes(classes: set[str]) -> str:
    """Map model line classes to semantic CSS classes."""
    out = ["geom-line"]
    if "carrier" in classes:
        out.append("carrier-line")
    if "bisector" in classes:
        out.append("bisector-line")
    if "auxiliary" in classes or "radius" in classes:
        out.append("aux-line")
    if "quadrilateral" in classes:
        out.append("quad-line")
    return " ".join(out)


def _segment_css_classes(classes: set[str]) -> str:
    """Map model segment classes to semantic CSS classes."""
    out = ["geom-segment"]
    if "golden" in classes:
        out.append("golden-segment")
    elif "radius" in classes:
        out.append("radius-segment")
    elif "semiperimeter" in classes:
        out.append("semi-segment")
    return " ".join(out)


def _polygon_css_classes(classes: set[str]) -> str:
    """Map model polygon classes to semantic CSS classes."""
    if "cyclic" in classes:
        return "geom-polygon cyclic-poly"
    if "quadrilateral" in classes:
        return "geom-polygon quad-poly"
    return "geom-polygon tri-poly"


def _point_css_and_radius(classes: set[str]) -> tuple[str, float]:
    """Map model point classes to ``(css_class_string, pixel_radius)``."""
    out = ["geom-point"]
    radius = 3.9
    if "given" in classes:
        radius = 4.3
    if "incenter" in classes:
        out.append("incenter-point")
        radius = 5.0
    elif "golden" in classes:
        out.append("golden-point")
        radius = 4.6
    elif "touchpoint" in classes:
        out.append("touch-point")
        radius = 3.9
    elif "meet" in classes:
        out.append("meet-point")
        radius = 4.2
    return (" ".join(out), radius)


def _point_to_segment_dist(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    """Compute pixel distance from ``(px, py)`` to segment ``(x1, y1)-(x2, y2)``."""
    dx = x2 - x1
    dy = y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / len_sq))
    return math.hypot(px - (x1 + t * dx), py - (y1 + t * dy))


def render_svg_string(
    model: Model,
    *,
    graphic_id: str = "g1",
    title: str = "Hero Geometric Construction",
    width: int = 700,
    height: int = 480,
    margin: float = 42.0,
    bbox: tuple[float, float, float, float] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
) -> str:
    """Render a :class:`~geometor.model.Model` into a complete ``.euclid-graphic`` SVG string.

    Args:
        model: Populated :class:`~geometor.model.Model`.
        graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
        title: Accessible SVG title string.
        width: Pixel width of the SVG ``viewBox``.
        height: Pixel height of the SVG ``viewBox``.
        margin: Outer pixel margin around the framed geometry.
        bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
        include_guides: If ``True``, also render elements marked ``guide=True``.
        show_labels: Master toggle for point text labels.
        label_overrides: Optional mapping ``pt_id -> (base, subscript)``.

    Returns:
        UTF-8 XML/SVG string.
    """
    visible_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]
    visible_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    visible_circles = [
        circ
        for circ in model
        if isinstance(circ, spg.Circle) and (include_guides or not model[circ].guide)
    ]
    visible_polygons = [
        poly
        for poly in model
        if isinstance(poly, spg.Polygon) and (include_guides or not model[poly].guide)
    ]
    visible_segments = [
        seg
        for seg in model
        if isinstance(seg, spg.Segment) and (include_guides or not model[seg].guide)
    ]
    visible_sections = [
        sec
        for sec in model
        if isinstance(sec, Section) and (include_guides or not model[sec].guide)
    ]

    if bbox is not None:
        xmin_m, xmax_m, ymin_m, ymax_m = bbox
    elif visible_points or visible_circles:
        xs = [float(p.x.evalf()) for p in visible_points]
        ys = [float(p.y.evalf()) for p in visible_points]
        for circ in visible_circles:
            ccx = float(circ.center.x.evalf())
            ccy = float(circ.center.y.evalf())
            rad = float(circ.radius.evalf())
            xs.extend((ccx - rad, ccx + rad))
            ys.extend((ccy - rad, ccy + rad))
        xmin_m, xmax_m = min(xs), max(xs)
        ymin_m, ymax_m = min(ys), max(ys)
        span_x = max(xmax_m - xmin_m, 1.0)
        span_y = max(ymax_m - ymin_m, 1.0)
        xmin_m -= 0.10 * span_x
        xmax_m += 0.10 * span_x
        ymin_m -= 0.12 * span_y
        ymax_m += 0.12 * span_y
    else:
        xmin_m, xmax_m, ymin_m, ymax_m = -1.0, 5.0, -1.0, 3.0

    span_x = max(xmax_m - xmin_m, 1e-6)
    span_y = max(ymax_m - ymin_m, 1e-6)
    scale = min(
        max(width - 2.0 * margin, 100.0) / span_x,
        max(height - 2.0 * margin, 100.0) / span_y,
    )

    cx_m = 0.5 * (xmin_m + xmax_m)
    cy_m = 0.5 * (ymin_m + ymax_m)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    inset_px = 14.0
    clip_xmin = cx_m - (cx_s - inset_px) / scale
    clip_xmax = cx_m + (width - inset_px - cx_s) / scale
    clip_ymin = cy_m - (height - inset_px - cy_s) / scale
    clip_ymax = cy_m + (cy_s - inset_px) / scale

    pt_svg_coords: dict[spg.Point, tuple[float, float]] = {
        pt: to_svg(float(pt.x.evalf()), float(pt.y.evalf())) for pt in visible_points
    }

    # 1. Polygons
    polygon_elems: list[str] = []
    for poly in visible_polygons:
        el = model[poly]
        pts_attr = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},"
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        vert_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        poly_ref = f"< {' '.join(vert_ids)} >" if vert_ids else el.ID
        css_cls = _polygon_css_classes(set(el.classes.keys()))
        polygon_elems.append(
            f'      <polygon class="{css_cls}" points="{pts_attr}" '
            f'data-ref="{html.escape(poly_ref)}" />'
        )

    # 2. Circles
    circle_elems: list[str] = []
    for circ in visible_circles:
        el = model[circ]
        ccx_s, ccy_s = to_svg(float(circ.center.x.evalf()), float(circ.center.y.evalf()))
        r_px = float(circ.radius.evalf()) * scale
        on_ids = [
            model[pt].ID
            for pt in visible_points
            if model[pt].ID and circ.contains(pt)
        ]
        primary_c_ref = el.ID
        c_aliases: list[str] = []
        if circ.center in model and model[circ.center].ID:
            cid = model[circ.center].ID
            for pid in on_ids:
                cand2 = f"( {cid} {pid} )"
                if cand2 != primary_c_ref:
                    c_aliases.append(cand2)
        if len(on_ids) >= 3:
            cand3 = f"( {on_ids[0]} {on_ids[1]} {on_ids[2]} )"
            if cand3 != primary_c_ref:
                c_aliases.append(cand3)
        c_alias_attr = (
            f' data-aliases="{html.escape(" | ".join(c_aliases))}"' if c_aliases else ""
        )
        c_ref_attr = (
            f' data-ref="{html.escape(primary_c_ref)}"' if primary_c_ref else ""
        )
        c_cls = _circle_css_classes(set(el.classes.keys()))
        eq_c_str = str(circ.equation())
        circle_elems.append(
            f'      <circle class="{c_cls}" cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" '
            f'r="{_fmt(r_px)}"{c_ref_attr}{c_alias_attr} fill="none">'
            f"<title>{html.escape(primary_c_ref)}: {html.escape(eq_c_str)} = 0</title>"
            f"</circle>"
        )

    # 3. Clipped lines (3-vertex midpoint paths)
    line_elems: list[str] = []
    drawn_segments_px: list[tuple[float, float, float, float]] = []
    for ln in visible_lines:
        clipped = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped is None:
            continue
        (mx1, my1), (mx2, my2) = clipped
        sx1, sy1 = to_svg(mx1, my1)
        sx2, sy2 = to_svg(mx2, my2)
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        css_cls = _line_css_classes(set(el.classes.keys()))
        incident_ids: list[str] = []
        for pt in visible_points:
            pid = model[pt].ID
            if not pid:
                continue
            px, py = pt_svg_coords[pt]
            if _point_to_segment_dist(px, py, sx1, sy1, sx2, sy2) < 0.75 and ln.contains(pt):
                incident_ids.append(pid)

        primary_ref = el.ID
        aliases: list[str] = []
        for i in range(len(incident_ids)):
            for j in range(i + 1, len(incident_ids)):
                for cand in (
                    f"[ {incident_ids[i]} {incident_ids[j]} ]",
                    f"[ {incident_ids[j]} {incident_ids[i]} ]",
                ):
                    if cand != primary_ref and cand not in aliases:
                        aliases.append(cand)
        alias_attr = (
            f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        )
        ref_attr = f' data-ref="{html.escape(primary_ref)}"' if primary_ref else ""
        eq_str = str(ln.equation())
        line_elems.append(
            f'      <path class="{css_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{ref_attr}{alias_attr} fill="none">'
            f"<title>{html.escape(primary_ref)}: {html.escape(eq_str)} = 0</title></path>"
        )

    # 4. Explicit segments (3-vertex midpoint paths supporting #geom-tick-1..3)
    segment_elems: list[str] = []
    for seg in visible_segments:
        el = model[seg]
        sx1, sy1 = to_svg(float(seg.p1.x.evalf()), float(seg.p1.y.evalf()))
        sx2, sy2 = to_svg(float(seg.p2.x.evalf()), float(seg.p2.y.evalf()))
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        id1 = model[seg.p1].ID if seg.p1 in model else ""
        id2 = model[seg.p2].ID if seg.p2 in model else ""
        primary_s_ref = el.ID or (f"/ {id1} {id2} /" if id1 and id2 else "")
        rev_alias = f"/ {id2} {id1} /" if id1 and id2 else ""
        s_alias_attr = (
            f' data-aliases="{html.escape(rev_alias)}"'
            if rev_alias and rev_alias != primary_s_ref
            else ""
        )
        s_cls = _segment_css_classes(set(el.classes.keys()))
        seg_len = str(sp.simplify(seg.length))
        segment_elems.append(
            f'      <path class="{s_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
            f'data-ref="{html.escape(primary_s_ref)}"{s_alias_attr} fill="none">'
            f"<title>{html.escape(primary_s_ref)}: |seg| = {html.escape(seg_len)}</title></path>"
        )

    for sec in visible_sections:
        if len(sec.points) >= 3:
            el = model[sec]
            p_start, p_end = sec.points[0], sec.points[-1]
            sx1, sy1 = to_svg(float(p_start.x.evalf()), float(p_start.y.evalf()))
            sx2, sy2 = to_svg(float(p_end.x.evalf()), float(p_end.y.evalf()))
            smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
            sec_ids = [model[p].ID for p in sec.points if p in model and model[p].ID]
            sec_ref = f"/ {' '.join(sec_ids)} /" if sec_ids else el.ID
            d_sec = f"M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"
            segment_elems.append(
                f'      <path class="geom-segment golden-segment" '
                f'd="{d_sec}" data-ref="{html.escape(sec_ref)}" fill="none" />'
            )

    # 5. Points & collision-free labels
    point_elems: list[str] = []
    label_elems: list[str] = []
    placed_label_boxes: list[tuple[float, float, float, float]] = []
    all_pt_px = [pt_svg_coords[p] for p in visible_points]
    candidate_angles = [
        -0.5 * math.pi,
        0.5 * math.pi,
        -0.28 * math.pi,
        -0.72 * math.pi,
        0.28 * math.pi,
        0.72 * math.pi,
        0.0,
        math.pi,
    ]

    for pt in visible_points:
        sx, sy = pt_svg_coords[pt]
        if sx < -8 or sx > width + 8 or sy < -8 or sy > height + 8:
            continue

        el = model[pt]
        pid = el.ID
        css_cls, radius = _point_css_and_radius(set(el.classes.keys()))
        x_latex = sp.latex(pt.x)
        y_latex = sp.latex(pt.y)
        tooltip = f"{pid} = ({pt.x}, {pt.y})"
        ref_attr = f' data-ref="{html.escape(pid)}"' if pid else ""
        point_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" '
            f'r="{_fmt(radius)}"{ref_attr} '
            f'data-latex-x="{html.escape(x_latex)}" data-latex-y="{html.escape(y_latex)}">'
            f"<title>{html.escape(tooltip)}</title></circle>"
        )

        if not show_labels or not pid:
            continue

        base_txt, sub_txt = _split_point_label(pid, label_overrides)
        est_w = 9.2 * len(base_txt) + 6.2 * len(sub_txt) + 4.0
        est_h = 14.0
        dist_r = radius + 11.5

        best_pos = (sx + 6.0, sy - 9.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12
        for ang in candidate_angles:
            cand_cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
            cand_cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
            box = (
                cand_cx - 0.5 * est_w,
                cand_cy - 0.5 * est_h,
                cand_cx + 0.5 * est_w,
                cand_cy + 0.5 * est_h,
            )
            score = 0.0
            if box[0] < 6 or box[2] > width - 6 or box[1] < 6 or box[3] > height - 6:
                score -= 500.0
            for lx1, ly1, lx2, ly2 in drawn_segments_px:
                d_line = _point_to_segment_dist(cand_cx, cand_cy, lx1, ly1, lx2, ly2)
                if d_line < 12.0:
                    score -= (12.0 - d_line) * 16.0
            for opx, opy in all_pt_px:
                d_pt = math.hypot(cand_cx - opx, cand_cy - opy)
                if d_pt < 15.0:
                    score -= (15.0 - d_pt) * 20.0
            for bx1, by1, bx2, by2 in placed_label_boxes:
                ox = max(0.0, min(box[2], bx2) - max(box[0], bx1))
                oy = max(0.0, min(box[3], by2) - max(box[1], by1))
                if ox > 0 and oy > 0:
                    score -= ox * oy * 6.0
            if score > best_score:
                best_score = score
                best_pos = (cand_cx - 0.45 * est_w, cand_cy + 0.34 * est_h)
                best_box = box

        placed_label_boxes.append(best_box)
        lx, ly = best_pos
        if sub_txt:
            inner_txt = (
                f"{html.escape(base_txt)}"
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner_txt = html.escape(base_txt)

        label_elems.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}"'
            f"{ref_attr}>{inner_txt}</text>"
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'data-graphic-id="{html.escape(graphic_id)}" '
        f'role="img" aria-label="{html.escape(title)}">',
        f"  <title>{html.escape(title)}</title>",
        EMBEDDED_SVG_DEFS,
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *polygon_elems,
        *circle_elems,
        *line_elems,
        *segment_elems,
        "    </g>",
        '    <g id="highlights" style="pointer-events: none;"></g>',
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_svg(
    model: Model,
    output_path: str | Path,
    *,
    graphic_id: str = "g1",
    title: str = "Hero Geometric Construction",
    width: int = 700,
    height: int = 480,
    margin: float = 42.0,
    bbox: tuple[float, float, float, float] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
) -> Path:
    """Write an interactive ``.euclid-graphic`` SVG rendering of ``model`` to disk.

    Args:
        model: Populated :class:`~geometor.model.Model`.
        output_path: Destination ``.svg`` path.
        graphic_id: ``data-graphic-id`` attribute value.
        title: Accessible SVG title string.
        width: Pixel width of the SVG ``viewBox``.
        height: Pixel height of the SVG ``viewBox``.
        margin: Outer pixel margin.
        bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
        include_guides: Whether to render guide elements.
        show_labels: Whether to place text labels.
        label_overrides: Optional mapping ``pt_id -> (base, subscript)``.

    Returns:
        Resolved :class:`~pathlib.Path` of the written SVG file.
    """
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_svg_string(
        model,
        graphic_id=graphic_id,
        title=title,
        width=width,
        height=height,
        margin=margin,
        bbox=bbox,
        include_guides=include_guides,
        show_labels=show_labels,
        label_overrides=label_overrides,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()


def export_all_figures(docsrc_root: Path | None = None) -> list[Path]:
    """Generate all interactive SVGs for both ``docsrc/_static/figures`` and ``constructions``.

    Args:
        docsrc_root: Optional ``docsrc`` path (defaults to ``<repo>/docsrc``).

    Returns:
        List of all written SVG file paths.
    """
    root = docsrc_root or (Path(__file__).resolve().parents[3] / "docsrc")
    fig_dir = root / "_static" / "figures"
    con_dir = root / "_static" / "constructions"

    m_i8, _ = construct_heron_proof()
    m_pent, _ = construct_pentagon_lemma()
    m_torus, _ = construct_dionysodorus_torus()
    m_div, _ = construct_area_division()
    m_gnomon, _ = construct_heronian_gnomon()
    m_cat, _ = construct_catoptrica_reflection()
    m_diop, _ = construct_dioptra_tunnel()

    jobs: list[tuple[Model, str, str, str, int, int]] = [
        (
            m_i8,
            "heron-i8-incircle.svg",
            "g1",
            "Hero Metrica I.8 — Synthetic Incircle & Cyclic Quadrilateral Proof on (13, 14, 15)",
            720,
            520,
        ),
        (
            m_pent,
            "pentagon-golden-lemma.svg",
            "g1",
            "Hero Metrica I.18 Lemma — Pentagon Golden Section Identity (BA + AC)^2 = 5 AC^2",
            680,
            460,
        ),
        (
            m_torus,
            "dionysodorus-torus-section.svg",
            "g1",
            "Hero Metrica II.13 — Dionysodorus Torus Meridian Section (R = 14, r = 6)",
            700,
            440,
        ),
        (
            m_div,
            "metrica-iii-area-division.svg",
            "g1",
            "Hero Metrica III.1–2 — Vertex (5:3) & Parallel Mean-Proportional (3:1) Area Division",
            700,
            500,
        ),
        (
            m_gnomon,
            "heronian-golden-gnomon.svg",
            "g1",
            "Hero Definitiones §58 — Universal Gnomon Realized on the Golden Rectangle in Q(phi)",
            680,
            440,
        ),
        (
            m_cat,
            "catoptrica-reflection.svg",
            "g2",
            "Hero Catoptrica Prop. 4 — Variational Shortest-Path Proof of the Law of Reflection",
            700,
            500,
        ),
        (
            m_diop,
            "dioptra-mountain-tunnel.svg",
            "g3",
            "Hero Dioptra Ch. 15 — Two-Portal Mountain Tunneling by Orthogonal Traverse",
            720,
            480,
        ),
    ]

    written: list[Path] = []
    for mdl, fname, gid, title, w_px, h_px in jobs:
        written.append(
            export_svg(
                mdl, fig_dir / fname, graphic_id=gid, title=title, width=w_px, height=h_px
            )
        )
        # In standalone demo pages each diagram is the primary g1 figure on its page
        written.append(
            export_svg(
                mdl, con_dir / fname, graphic_id="g1", title=title, width=w_px, height=h_px
            )
        )
    return written
