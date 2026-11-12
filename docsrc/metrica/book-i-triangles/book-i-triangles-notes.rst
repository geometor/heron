:order: 13
:type: notes
:canonical_id: book-i-triangles
:folio: Schöne 2–26
:book: Metrica Book I (Pref. & Props. 1–9)

.. _unit-book-i-triangles-notes:

Metrica Book I (Preface & Props. 1–9) — GEOMETOR Commentary & Notes
===================================================================

GEOMETOR Mathematical & Historical Commentary
---------------------------------------------

1. **The 1896 Constantinople Rediscovery & Archimedian Attribution of I.8**:
   For over a millennium, :person:`Hero's <hero>` *Metrica* was known only through fragmentary citations in :person:`Eutocius <eutocius>` (*In Archimedis Dim. Circ.*), until :person:`Richard Schöne <schoene-richard>` and Paul Tannery identified the complete three-book treatise in 1896 in the 11th-century *Codex Constantinopolitanus Palatii Veteris* no. 1 (fols. 67r–107v), edited by :person:`Hermann Schöne <schoene>` in :cite:`1903 <schoene:1903>`. Medieval Arabic geometer :person:`al-Bīrūnī <al-biruni>` reports that the triangle area theorem :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}` originated with :person:`Archimedes <archimedes>`, while *Metrica* I.8 preserves its oldest extant Greek synthetic proof—duplicated verbatim in Hero's *Dioptra* Ch. 30.

2. **Fourth-Degree Magnitude (*Dynamodynamis*) Inside Greek Geometry**:
   Classical Euclidean geometry restricts magnitudes to three homogeneous spatial dimensions (line, square, solid). At *Schöne* p. 20, lines 22–25, Hero boldly writes: *"the rectangle* :math:`\Gamma\Theta \cdot EH` *is the square root of* :math:`\Gamma\Theta^2 \cdot EH^2` *"*—multiplying a square by a square (a fourth-degree :term:`dynamodynamis`, named explicitly at *Metrica* I.17, *Schöne* p. 48) inside a *synthetic* proof! This conceptual leap bridges classical geometric algebra (:just:`Elements Book II <II.13>`) and Diophantine symbolic algebra.

3. **Archimedes' Function / Wildberger's Quadrea (:math:`\mathcal{A} = 16\Delta^2`)**:
   In :person:`Norman J. Wildberger's <wildberger>` :cite:`Rational Trigonometry <wildberger:2005>` (formalized in ``geometor/wildberger`` W.07), expanding :math:`16 s(s-a)(s-b)(s-c)` in the side :term:`quadrances <quadrance>` :math:`Q_a = a^2, Q_b = b^2, Q_c = c^2` eliminates every square root:

   .. math::

      \mathcal{A}(Q_a, Q_b, Q_c) = (Q_a + Q_b + Q_c)^2 - 2(Q_a^2 + Q_b^2 + Q_c^2) = 16 s(s-a)(s-b)(s-c) = 16\Delta^2.

   On Hero's two benchmark triangles:

   - For :math:`(7, 8, 9)`, :math:`(Q_a, Q_b, Q_c) = (49, 64, 81) \implies \mathcal{A} = 194^2 - 2(12738) = 11520 = 16 \times 720`.
   - For :math:`(13, 14, 15)`, :math:`(Q_a, Q_b, Q_c) = (196, 225, 169) \implies \mathcal{A} = 590^2 - 2(117562) = 112896 = 16 \times 7056 = (4 \times 84)^2`.

4. **Quadratic Convergence of Hero's Root Algorithm**:
   Hero's rule :math:`x_{k+1} = \frac{1}{2}\!\left(x_k + \frac{N}{x_k}\right)` satisfies the exact algebraic error recurrence:

   .. math::

      x_{k+1}^2 - N = \left(\frac{x_k^2 - N}{2 x_k}\right)^2 > 0.

   Every iterate :math:`k \ge 1` is therefore a **strict rational upper bound** whose quadratic excess squares at every step: from :math:`x_0^2 - 720 = +9` (:math:`x_0 = 27`), step 1 gives :math:`\frac{9^2}{4 \cdot 729} = \frac{1}{36}` (:math:`x_1 = \frac{161}{6}`), and step 2 gives :math:`\frac{1}{4 \cdot 36 \cdot 25921} = \frac{1}{3{,}732{,}624}` (:math:`x_2 = \frac{51841}{1932}`), accurate to **8 significant decimal digits** in two hand divisions!

Interactive GEOMETOR Demonstrations & Sister Concordance
--------------------------------------------------------

- **Symbolic Proof Walkthrough**: :doc:`/demos/heron-formula-proof` — Executes ``construct_heron_proof()`` in ``geometor.model`` (`B = (0, 0)`, `C = (14, 0)`, `A = (5, 12)`, incenter `H = (6, 4)` = `X(1)`, cyclic circumcenter `M = (7, -4)` of squared radius `65`).
- **Exact Rational Stream**: :doc:`/demos/sqrt-720-iteration` — Evaluates ``heron_sqrt_convergents(720, steps=4)`` in exact ``sympy.Rational`` arithmetic up to a 154-digit fraction.
- **Concordance Loci in Unit I**:
  - :ref:`Metrica I, Prooemium <locus-metrica-i-pref>` (*Schöne* pp. 2–6) ↔ ``proclus`` *Friedlein* 64.16–65.7
  - :ref:`Metrica I, Props. 1–7 <locus-metrica-i-1-7>` (*Schöne* pp. 6–18) ↔ :just:`I.47`, :just:`II.12`, :just:`II.13`
  - :ref:`Metrica I, Prop. 8 Proof <locus-metrica-i-8>` (*Schöne* pp. 18–24) ↔ ``etc`` `X(1)` & ``wildberger`` `W.07`
  - :ref:`Metrica I, Prop. 8b √720 <locus-metrica-i-8-sqrt>` (*Schöne* pp. 18–20) ↔ :person:`Eutocius <eutocius>` testimony
