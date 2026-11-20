:order: 41
:type: summary
:canonical_id: Metrica I Summary
:folio: Schöne 2–90
:tracks: English: prooemium | Summary: summary | Notes: notes

.. _unit-book-i-triangles-summary:
.. _unit-book-i-polygons-circles-summary:

Metrica Book I — Analytical Summary & Proposition Synopses
==========================================================

Architectural Progression
-------------------------

Unit I opens :person:`Hero of Alexandria's <hero>` *Metrica* by establishing the epistemological and metrological foundations of Greek mensuration and ascending in nine propositions from the unit square to the universal side-only area law for any triangle:

1. **Philosophical Prooemium (Schöne pp. 2–6)**:
   - Recounts the origin of geometry in annual Nile flood resurveying (matching the Eudemian history preserved in :person:`Proclus <proclus>`, *In Euclidem* 64.16–65.7).
   - Formulates the **Axiom of Homogeneous Orthogonal Comparison**: lines are measured by linear units (cubit, foot, palm, dactyl), surfaces (:term:`embadon`) by the orthogonal unit square, and solids by the orthogonal unit cube.
   - Announces the triadic design of the *Metrica*: Book I (plane & curved surfaces), Book II (solid bodies), Book III (proportional divisions).

2. **Altitude-Based Triangle Mensuration (Props. I.1–I.7, Schöne pp. 6–18)**:
   - **I.1–I.3**: Oblong rectangle (:math:`5 \times 3 = 15`), right triangle (:math:`3, 4, 5 \implies 6`), isosceles triangle (:math:`10, 10, 12 \implies 48`).
   - **I.4–I.6**: Uses :just:`II.13` (acute, :math:`(13, 14, 15) \implies B\Delta = 5, A\Delta = 12, \Delta = 84`) and :just:`II.12` (obtuse, :math:`(13, 11, 20) \implies B\Delta = 5, A\Delta = 12, \Delta = 66`) to locate the foot of the :term:`altitude <kathetos>` and compute area.
   - **I.7**: Eliminates the acute/obtuse branch test via a unified algebraic projection formula.

3. **Heron's Formula & Iterative Root Extraction (Props. I.8–I.9, Schöne pp. 18–26)**:
   - **I.8a (Algorithm & √720)**: Evaluates :math:`(7, 8, 9) \implies s = 12 \implies 12 \cdot 5 \cdot 4 \cdot 3 = 720`, and introduces the quadratic Newton–Heron iteration :math:`x_{k+1} = \frac{1}{2}(x_k + N/x_k)` from :math:`x_0 = 27` (:math:`27^2 = 729`) to :math:`x_1 = 26\frac{5}{6} = \frac{161}{6}` (error :math:`x_1^2 - 720 = \frac{1}{36}`) and :math:`x_2 = \frac{51841}{1932}`.
   - **I.8b (Synthetic Proof & (13, 14, 15))**: Proves :math:`\Delta^2 = s(s-a)(s-b)(s-c)` synthetically using only the incircle (:just:`IV.4`), equal tangents (:just:`III.17`), cyclic quadrilateral :math:`\Gamma HB\Lambda` (:just:`III.22`), similar right triangles (:just:`VI.4`), and the right-triangle altitude theorem (:just:`VI.8`), culminating in :math:`(13, 14, 15) \implies \sqrt{7056} = 84`.
   - **I.9**: Extends triangle mensuration to sides given only *in square* (irrational lengths).

Proposition Synopsis Table
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 20 34 30

   * - Locus
     - Schöne Pages
     - Canonical Paradigm
     - Key Euclidean / Algebraic Principle
   * - **Prooemium**
     - pp. 2–6
     - Nile resurveying; unit square & cube
     - :just:`I.def.22`; homogeneous orthogonal units
   * - **Props. I.1–I.3**
     - pp. 6–10
     - :math:`5\times 3`; :math:`(3,4,5)`; :math:`(10,10,12)`
     - :just:`I.34`, :just:`I.41`, :just:`I.47`
   * - **Props. I.4–I.7**
     - pp. 10–18
     - :math:`(13,14,15) \to 84`; :math:`(13,11,20) \to 66`
     - :just:`II.12`, :just:`II.13` projection laws
   * - **Prop. I.8**
     - pp. 18–24
     - :math:`(7,8,9) \to \sqrt{720}`; :math:`(13,14,15) \to 84`
     - :just:`IV.4`, :just:`III.22`, :just:`VI.8`; :math:`x_{k+1}=\frac{1}{2}(x_k + N/x_k)`
   * - **Prop. I.9**
     - pp. 24–26
     - Irrational side quadrances
     - Iterative rational root extraction

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
