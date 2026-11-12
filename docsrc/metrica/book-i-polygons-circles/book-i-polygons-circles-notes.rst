:order: 23
:type: notes
:canonical_id: book-i-polygons-circles
:folio: Schöne 26–90
:book: Metrica Book I (Props. 10–39)

.. _unit-book-i-polygons-circles-notes:

Scholarly Notes — Metrica Book I (Props. 10–39)
===============================================

*Commentary on Golden-Section Polygon Algebra, Hipparchian Chord Tables, Archimedes' Lost Plinthides, and the Method*

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
