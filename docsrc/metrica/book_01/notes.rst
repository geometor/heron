:order: 10
:type: notes
:canonical_id: Metrica I Notes
:folio: Schöne 2–90
:tracks: English: prooemium | Summary: summary | Notes: notes

.. _unit-book-i-triangles-notes:
.. _unit-book-i-polygons-circles-notes:

Metrica Book I — Scholarly Commentary, Historical Loci & Demonstrations
=======================================================================

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

1. Euclid *Elements* XIII.1 & the Pentagon Lemma in :math:`\mathbb{Q}(\phi)`
----------------------------------------------------------------------------

In **Proposition I.18** (:cite:`Schöne 1903 <schoene:1903>`, p. 50), :person:`Hero <hero>` compresses :person:`Euclid's <euclid>` Book XIII theory of the regular pentagon and decagon into a remarkably direct right-triangle lemma. By reflecting right triangle :math:`AB\Gamma` (:math:`\angle A = 36^\circ`) across :math:`B\Gamma` to form isosceles triangle :math:`AB\Delta` with apex angle :math:`108^\circ` (:math:`\frac{6}{5}` of a right angle), Hero identifies :math:`AB = B\Delta` as the side of a regular pentagon and :math:`A\Delta = 2 A\Gamma` as its diagonal.

By :just:`XIII.8`, :math:`A\Delta : AB = AB : (A\Delta - AB) = \phi : 1`. Invoking :just:`XIII.1`—if :math:`A\Delta` is cut in extreme and mean ratio with greater segment :math:`AB`, then adding half the whole (:math:`A\Gamma = \frac{1}{2} A\Delta`) yields :math:`(AB + A\Gamma)^2 = 5\,A\Gamma^2`—Hero avoids nested fourth-degree radicals until the very end of the numerical evaluation! In Rational Trigonometry (:cite:`Wildberger 2005 <wildberger:2005>`), the spread at :math:`A` (:math:`36^\circ`) lives purely in :math:`\mathbb{Q}(\sqrt{5})`:

.. math::

   s_{36^\circ} = \frac{B\Gamma^2}{AB^2} = \frac{AB^2 - A\Gamma^2}{AB^2} = 1 - \frac{\phi^2}{4} = \frac{5 - \sqrt{5}}{8}.

See the executable construction in :doc:`/demos/golden-gnomon-dioptra` and ``geometor.heron.constructions.construct_pentagon_lemma``.

2. Pre-Ptolemaic Chord Tables in Propositions I.22 & I.24
---------------------------------------------------------

Because the regular :math:`9`-gon (:math:`40^\circ` central angle, requiring angle trisection) and regular :math:`11`-gon (:math:`32\frac{8}{11}^\circ` central angle) cannot be constructed with unmarked straightedge and compass, Hero explicitly cites *"the books on chords in a circle"* (*τὰ περὶ τῶν ἐν κύκλῳ εὐθειῶν*). As :person:`Thomas Heath <heath>` (:cite:`1921 <heath:1921>`, Vol. II, pp. 259, 326) and :person:`Otto Neugebauer <neugebauer>` observed, Hero's ratios—specifically :math:`d / a_9 \approx \frac{17}{6}` (equivalent to a chord of :math:`40^\circ` near :math:`\frac{6}{17} d \approx 0.3529 d` vs. exact :math:`\sin 20^\circ = 0.3420 d`) and :math:`d / a_{11} \approx \frac{25}{7}` (:math:`\frac{7}{25} d = 0.2800 d` vs. exact :math:`\sin\frac{\pi}{11} \approx 0.28173 d`, accurate to :math:`0.6\%`!)—preserve precious pre-Ptolemaic trigonometric data prior to :person:`Claudius Ptolemy's <ptolemy>` *Almagest* I.10, pointing back to :person:`Hipparchus of Nicaea <hipparchus>`.

3. Archimedes' Lost *Plinthides and Cylinders* (Prop. I.26)
-----------------------------------------------------------

In **Proposition I.26** (:cite:`Schöne 1903 <schoene:1903>`, p. 66; fol. 81v), Hero preserves our *sole surviving ancient testimony* to :person:`Archimedes' <archimedes>` work :cite:`On Plinthides and Cylinders <archimedes:plinthides>` (*Περὶ πλινθίδων καὶ κυλίνδρων*). In the *Codex Constantinopolitanus*, the manuscript numerals read :math:`\frac{211875}{67441}` (:math:`\approx 3.141635`) and :math:`\frac{197888}{62351}` (:math:`\approx 3.17377`, slightly corrupted in a single Greek digit; Paul Tannery and :person:`Hermann Schöne <schoene>` showed that restoring a single numeral yields tight four-decimal bounds straddling :math:`\pi = 3.14159265\dots`). This proves that Archimedes' famous :math:`3\frac{10}{71} < \pi < 3\frac{1}{7}` in *Measurement of a Circle* was merely a simplified didactic bound, whereas Archimedes had computed :math:`\pi` far more tightly in *Plinthides and Cylinders*.

4. Surfaces in Book I vs. Volumes in Book II
--------------------------------------------

Why do the curved 3D surfaces of the cylinder, cone, sphere, and spherical cap appear at the end of **Book I (Props. I.36–I.39)** rather than in Book II? Hero adheres strictly to the **dimensional ontology** enunciated in his Book I Prooemium: Book I measures *two-dimensional surfaces* (*ἐπιφάνειαι*), whether planar or curved in three-dimensional space, because every surface—even a sphere's—is measured in homogeneous *unit squares* (:math:`S_{\text{sphere}} = 4\pi r^2`), whereas Book II is reserved exclusively for *three-dimensional solid capacities* measured in *unit cubes*.
