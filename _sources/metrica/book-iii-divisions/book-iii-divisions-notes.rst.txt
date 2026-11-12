:order: 43
:type: notes
:canonical_id: book-iii-divisions
:folio: Schöne 140–184
:book: Metrica Book III (Pref. & Props. 1–23)

.. _unit-book-iii-divisions-notes:

Scholarly Notes — Metrica Book III (Preface & Props. 1–23)
==========================================================

*Commentary on Euclid's On Divisions of Figures, Rational Quadrance Linearity, and Hero's Cube-Root Formula*

1. *Metrica* Book III & Euclid's Lost *On Divisions of Figures*
---------------------------------------------------------------

:person:`Proclus <proclus>` (:cite:`In Euclidem <proclus:in-euclidem>`, Friedlein p. 69) records that :person:`Euclid <euclid>` composed a dedicated treatise *On Divisions* (*Περὶ διαιρέσεων βιβλίον*), lost in Greek but partially preserved in a 10th-century Arabic compendium by al-Sijzī (published by Woepcke in 1851; reconstructed by Archibald in 1915). Comparing Euclid's *On Divisions* with *Metrica* Book III illuminates Hero's genius:

- Where Euclid gives pure existence and construction theorems (*Data*-style) for planar figures (triangles, trapezia, quadrilaterals, circles), Hero supplies **both** the rigorous Euclidean *analysis/synthesis* **and** explicit rational numerical algorithms on concrete survey triangles such as :math:`(13, 14, 15)`.
- Furthermore, Euclid's *On Divisions* stops at two-dimensional figures; **Props. III.20–III.23** extend proportional division into **three-dimensional stereometry** (pyramids, cones, frusta, and spheres), where straightedge-and-compass mean proportionals no longer suffice because triplicate ratios demand cube roots and conic intersections!

2. Rational Trigonometry View of Proposition III.2
--------------------------------------------------

Notice how Hero phrases the conclusion of his *analysis* in **Proposition III.2** (:cite:`Schöne 1903 <schoene:1903>`, p. 142):

   *«δοθεῖσα ἄρα καὶ ἡ ΑΔ δυνάμει»* — *"Therefore :math:`A\Delta` is given in square (:term:`quadrance`)."*

In :person:`Norman Wildberger's <wildberger>` Rational Trigonometry (:cite:`2005 <wildberger:2005>`), area division by a parallel line is **purely rational and linear in quadrance**: for *any* rational division ratio :math:`m : n`, the cut quadrance :math:`Q(A, D) = \frac{m}{m+n} Q(A, B)` belongs strictly to :math:`\mathbb{Q}` (:math:`\frac{507}{4}` on :math:`(13, 14, 15)` for :math:`3 : 1`), and compass construction via the semicircle on :math:`AB` (:just:`VI.13`) constructs the exact Euclidean point :math:`D` without numerical approximation. See the companion demonstration in :doc:`/demos/area-division-book-iii`.

3. Mathematical Structure of Hero's Cube-Root Formula (Prop. III.20)
--------------------------------------------------------------------

Hero's cube-root extraction of :math:`\sqrt[3]{100}` in **Proposition III.20** (:cite:`Schöne 1903 <schoene:1903>`, p. 178) attracted intense scrutiny from Curtze, Wertheim, Eneström, :person:`Thomas Heath <heath>` (:cite:`1921 <heath:1921>`, Vol. II, pp. 341–343), and Dijksterhuis. Letting :math:`\ell^3 < N < u^3` with :math:`u = \ell + 1`, :math:`e_\ell = N - \ell^3`, and :math:`e_u = u^3 - N`, Hero's arithmetic steps evaluate:

.. math::

   \sqrt[3]{N} \;\approx\; \ell + \frac{u \cdot e_\ell}{u \cdot e_\ell + \ell \cdot e_u}.

Why is weighting :math:`e_\ell` by :math:`u` and :math:`e_u` by :math:`\ell` so vastly superior to naive linear interpolation :math:`\ell + \frac{e_\ell}{e_\ell + e_u}`?

- Naive linear interpolation between :math:`4^3 = 64` and :math:`5^3 = 125` gives :math:`4 + \frac{36}{61} \approx 4.5902` (error :math:`-0.0514`, nearly **forty times worse**!).
- Because :math:`f(x) = x^3` is convex (:math:`f''(x) = 6x > 0`), its slope :math:`3x^2` is steeper near :math:`u = 5` than near :math:`\ell = 4`. Weighting the lower deficit :math:`e_\ell` by :math:`u` and the upper excess :math:`e_u` by :math:`\ell` cancels the leading second-order curvature error of :math:`x^3` across unit intervals :math:`[\ell, \ell + 1]`—producing :math:`\frac{65}{14} \approx 4.64286` (error :math:`+0.00127`) in a single rational fraction!
