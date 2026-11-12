:order: 12
:type: summary
:canonical_id: book-i-triangles
:folio: Schöne 2–26
:book: Metrica Book I (Pref. & Props. 1–9)

.. _unit-book-i-triangles-summary:

Metrica Book I (Preface & Props. 1–9) — Analytical Summary
==========================================================

*Scope*: **Schöne (1903), pp. 2–26** · *Cod. Constantinopolitanus 1, fols. 67r–72r*

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
