"""Comprehensive symbolic, SVG, and 4-Track Book Codex test suite for ``geometor.heron``."""

from __future__ import annotations

import pytest
import sympy as sp
import sympy.geometry as spg

from geometor.heron import (
    CODEX_UNITS,
    PHI,
    __version__,
    archimedes_quadrea,
    construct_area_division,
    construct_catoptrica_reflection,
    construct_dionysodorus_torus,
    construct_dioptra_tunnel,
    construct_heron_proof,
    construct_heronian_gnomon,
    construct_pentagon_lemma,
    dionysodorus_torus_volume,
    frustum_volume,
    heron_area,
    heron_area_squared,
    heron_sqrt_convergents,
    load_concordance,
    load_sources_manifest,
    pentagon_golden_lemma,
    platonic_solid_volumes,
    regular_polygon_ratios,
    render_svg_string,
    verify_frustum_mean_identity,
    verify_quadrea_identity,
)
from geometor.heron.cli import main as cli_main
from geometor.heron.compile_codex import default_docsrc_book_dir, verify_codex_tracks


def test_version_and_quadrea_polynomial_identity():
    assert __version__ == "0.1.1"
    assert verify_quadrea_identity() == sp.Integer(0)
    assert heron_area_squared(7, 8, 9) == sp.Integer(720)
    assert heron_area(7, 8, 9) == 12 * sp.sqrt(5)
    assert heron_area_squared(13, 14, 15) == sp.Integer(7056)
    assert heron_area(13, 14, 15) == sp.Integer(84)
    assert archimedes_quadrea(196, 225, 169) == sp.Integer(112896)
    assert archimedes_quadrea(49, 64, 81) == 16 * sp.Integer(720)


def test_heron_sqrt_720_convergents():
    convs = heron_sqrt_convergents(720, steps=3)
    assert convs[0].approx == sp.Rational(27, 1)
    assert convs[0].residual == sp.Rational(9, 1)
    assert convs[1].approx == sp.Rational(161, 6)
    assert convs[1].residual == sp.Rational(1, 36)
    assert convs[2].approx == sp.Rational(51841, 1932)
    assert convs[2].residual == sp.Rational(1, 3732624)
    assert convs[3].approx == sp.Rational(5374978561, 200313624)


def test_pentagon_polygons_torus_frustum_and_platonic_solids():
    pent = pentagon_golden_lemma()
    assert pent["identity_residual"] == 0
    assert pent["sum_sq_over_apothem_sq"] == 5
    assert pent["heron_sum_sq_ratio"] == sp.Rational(81, 16)

    ratios = regular_polygon_ratios()
    assert [r.sides for r in ratios] == list(range(3, 13))
    for entry in ratios:
        assert abs(entry.relative_error) < 0.04

    assert dionysodorus_torus_volume(14, 6, pi_approx=sp.Rational(22, 7)) == sp.Rational(
        69696, 7
    )
    assert dionysodorus_torus_volume(14, 6) == 1008 * sp.pi**2

    assert verify_frustum_mean_identity() == sp.Integer(0)
    assert frustum_volume(10, 2, 9) == sp.Integer(372)

    solids = platonic_solid_volumes(1)
    assert set(solids) == {
        "tetrahedron",
        "cube",
        "octahedron",
        "icosahedron",
        "dodecahedron",
    }
    assert sp.simplify(solids["octahedron"] / solids["tetrahedron"]) == 4


@pytest.mark.parametrize(
    "builder",
    [
        construct_heron_proof,
        construct_pentagon_lemma,
        construct_dionysodorus_torus,
        construct_catoptrica_reflection,
        construct_area_division,
        construct_heronian_gnomon,
        construct_dioptra_tunnel,
    ],
)
def test_all_symbolic_constructions_obey_exact_algebra_laws(builder):
    model, invariants = builder()
    assert model.auto_intersect is False
    assert isinstance(invariants, dict) and len(invariants) > 0

    for el, meta in model.items():
        if isinstance(el, spg.Point):
            assert not el.x.atoms(sp.Float), f"Float found in {meta.ID}.x"
            assert not el.y.atoms(sp.Float), f"Float found in {meta.ID}.y"
            if not meta.guide:
                assert "_" not in meta.ID, f"Underscore in visible point ID {meta.ID}"
                assert meta.ID.isalnum(), f"Non-alphanumeric visible ID {meta.ID}"


def test_theorem_specific_invariants():
    _, inv_i8 = construct_heron_proof()
    assert inv_i8["area"] == 84
    assert inv_i8["ke_times_ec"] == 16
    assert inv_i8["cyclic_radius_sq"] == 65

    _, inv_cat = construct_catoptrica_reflection()
    assert inv_cat["incidence_spread"] == sp.Rational(1, 2)
    assert inv_cat["reflection_spread"] == sp.Rational(1, 2)
    assert inv_cat["optimal_length_sq"] == 162
    assert inv_cat["perturbed_length_sq"] == 180

    _, inv_div = construct_area_division(m_ratio=3, n_ratio=1)
    assert inv_div["ad_quadrance"] == sp.Rational(507, 4)
    assert inv_div["area_ade"] == 63
    assert inv_div["area_decb"] == 21

    _, inv_gnom = construct_heronian_gnomon()
    assert sp.simplify(inv_gnom["whole_aspect_quadrance"] - PHI**2) == 0
    assert sp.simplify(inv_gnom["seed_aspect_quadrance"] - PHI**2) == 0
    assert sp.simplify(inv_gnom["gen2_aspect_quadrance"] - PHI**2) == 0

    _, inv_diop = construct_dioptra_tunnel()
    assert inv_diop["east_displacement"] == 12
    assert inv_diop["north_displacement"] == 5
    assert inv_diop["tunnel_length"] == 13


def test_euclid_graphic_svg_renderer_contract():
    model, _ = construct_heron_proof()
    svg = render_svg_string(model, graphic_id="g1", title="Test I.8")
    assert 'class="euclid-graphic"' in svg
    assert 'data-graphic-id="g1"' in svg
    assert 'id="geom-tick-1"' in svg
    assert 'id="geom-tick-2"' in svg
    assert 'id="geom-tick-3"' in svg
    assert 'id="highlights"' in svg
    assert 'data-ref="( H E )"' in svg
    assert 'data-ref="&lt; A B C &gt;"' in svg


def test_codex_tracks_manifest_concordance_and_cli():
    assert len(CODEX_UNITS) == 5
    manifest = load_sources_manifest()
    assert len(manifest["local_source_excerpts"]) == 4
    conc = load_concordance()
    assert len(conc["entries"]) == 24

    report = verify_codex_tracks()
    assert report["valid"] is True, f"Codex verification errors: {report['errors']}"
    assert report["units"] == 5
    assert report["track_files"] == 20

    # Ensure zero raw $ inline math delimiters in docsrc/metrica
    for rst_file in default_docsrc_book_dir().rglob("*.rst"):
        text = rst_file.read_text(encoding="utf-8")
        assert "$" not in text, f"Raw $ found in {rst_file}"

    assert cli_main(["summary"]) == 0
    assert cli_main(["verify"]) == 0
