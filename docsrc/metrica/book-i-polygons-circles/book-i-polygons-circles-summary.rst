:order: 22
:type: summary
:canonical_id: book-i-polygons-circles
:folio: Schöne 26–90
:book: Metrica Book I (Props. 10–39)

.. _unit-book-i-polygons-circles-summary:

Summary — Metrica Book I (Props. 10–39)
=======================================

*Structural Overview of Quadrilaterals, Regular Polygons, Curvilinear Regions & Curved Surfaces*

1. Deductive Architecture of *Metrica* I.10–I.39
------------------------------------------------

Having solved the general triangle in Propositions I.1–I.9, :person:`Hero <hero>` extends planar and surface mensuration across four progressively richer geometric domains:

1. **Quadrilaterals & Trapezia (Props. I.10–I.16)**: Establishes why four side-lengths alone leave a quadrilateral underdetermined, reduces every trapezium (right, isosceles, acute, obtuse) to a parallelogram plus a differential scalene triangle of base :math:`|a - c|` (solved by Prop. I.8), and decomposes general convex or dart-shaped (*κοιλογώνιον*) quadrilaterals along a given diagonal.
2. **Regular Polygons from :math:`n = 3` to :math:`n = 12` (Props. I.17–I.25)**: Unifies Euclidean constructible polygons (:math:`3, 4, 5, 6, 8, 10, 12`) with chord-table polygons (:math:`7, 9, 11`), proving the **Prop. I.18 Golden Section Lemma** :math:`(BA + A\Gamma)^2 = 5 A\Gamma^2` over :math:`\mathbb{Q}(\phi)` and supplying high-precision rational multipliers :math:`A_n / a^2`.
3. **Circles, Annuli & Segments (Props. I.26–I.33)**: Combines :person:`Archimedes' <archimedes>` :cite:`Measurement of a Circle <archimedes:circle>` (:math:`\pi \approx \frac{22}{7}`), lost :cite:`Plinthides and Cylinders <archimedes:plinthides>` bounds, the concentric :term:`annulus <itys>` formula, the :math:`4:1` geometric series (**Prop. I.27**), intersecting-chords diameter recovery (**Prop. I.30**), and lower bounds on circular segments via inscribed parabolic exhaustion (**Props. I.31–I.33**).
4. **Conic Regions & Curved Surfaces in 3D (Props. I.34–I.39)**: Measures the ellipse (:math:`\pi a b`, **Prop. I.34**), the parabolic segment (:math:`\frac{4}{3} \Delta_{\text{inscr}}` citing Archimedes' :term:`Method <ephodikon>`, **Prop. I.35**), and the curved surface areas of the right cylinder, right cone, sphere (:math:`4\pi r^2`), and spherical cap (:math:`\pi c^2 = 2\pi R h`, **Props. I.36–I.39**).

2. Key Algebraic & Constructive Identities
------------------------------------------

- **Differential Triangle of a Trapezium (I.12–I.13)**: For parallel bases :math:`a > c` and legs :math:`b, d`, the altitude :math:`h` equals the altitude onto base :math:`(a - c)` of the triangle :math:`(b, d, a - c)`:

  .. math::

     A_{\text{trap}} = \frac{a + c}{a - c}\,\Delta(b, d, a - c).

- **Pentagon Golden Section Lemma (I.18)**: In a :math:`36^\circ\text{-}54^\circ\text{-}90^\circ` right triangle :math:`AB\Gamma` (:math:`\angle \Gamma = 90^\circ, \angle A = 36^\circ`):

  .. math::

     (BA + A\Gamma)^2 = 5\,A\Gamma^2, \qquad \frac{BA}{A\Gamma} = \sqrt{5} - 1 = \frac{2}{\phi}, \qquad s(\angle A) = \sin^2(36^\circ) = \frac{5 - \sqrt{5}}{8}.

- **Annulus (*Ἴτυς*, I.26)**: :math:`A_{\text{itys}} = \pi(R^2 - r^2) = \pi w (2r + w) \approx \frac{22}{7} w(D_2 + w)`.
- **Ellipse & Parabola (I.34–I.35)**: :math:`A_{\text{ellipse}} = \pi a b` and :math:`A_{\text{parabola}} = \frac{4}{3} A_{\triangle}`.
