:order: 2
:type: section
:canonical_id: Def. §58
:folio: Hultsch 21

.. _sec-definitiones-gnomon:

Definitiones §58: The Universal Gnomon & Golden Self-Similarity
===============================================================

.. folio:: Hultsch 21
   :page: 21

**Definition 58 — Universal Gnomon (*Καθόλου Γνώμων*, Heiberg §58 / Hultsch p. 21 §59)**:

   *"Primarily, in a parallelogrammic area, a :term:`gnomon <gnomon>` is any one of the parallelograms about the diameter together with the two complements (:just:`II.def.2`). **Universally, however, a gnomon is anything whatever which, when added to anything—whether number or figure—makes the whole similar to that to which it has been added** (*καθόλου δὲ γνώμων ἐστὶ πᾶν ὃ προσλαβὸν ὁτιοῦν, ἀριθμὸν ἢ σχῆμα, ποιεῖ τὸ ὅλον ὅμοιον ᾧ προσείληφεν*)."*

This single sentence generalizes Euclid's parallelogram gnomon into the universal law of **scale-invariant morphogenesis** across arithmetic (polygonal numbers), geometry, and botanical phyllotaxis. Its supreme planar realization is the **Golden Rectangle** over :math:`\mathbb{Q}(\phi)` (:math:`\phi = \frac{1 + \sqrt{5}}{2}`):

.. picture:: /_static/figures/heronian-golden-gnomon.svg
   :alt: Hero Definitiones 58 — Universal Golden Gnomon Recursive Similarity in Q(phi)

1. Construct the unit square **gnomon** :g:`ABCD <g1:< A B C D >>` (:math:`AB = BC = 1`), bisect :g:`AB <g1:[ A B ]>` at :g:`M <g1:M>`, and swing compass circle :g:`(MC) <g1:( M C )>` of radius :math:`MC = \frac{\sqrt{5}}{2}` onto :g:`AB <g1:[ A B ]>` extended to :g:`E <g1:E>` (:just:`II.11`), giving :g:`AE <g1:/ A E />` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2} = \phi` and :g:`BE <g1:/ B E />` :math:`= \phi - 1 = \frac{1}{\phi}`.
2. Erect the perpendicular at :g:`E <g1:E>` to complete the whole rectangle :g:`AEFD <g1:< A E F D >>`. Adjoining the unit square gnomon :g:`ABCD <g1:< A B C D >>` to the seed rectangle :g:`BEFC <g1:< B E F C >>` (sides :math:`1` and :math:`\phi - 1`) produces a whole rectangle :g:`AEFD <g1:< A E F D >>` (sides :math:`\phi` and :math:`1`) **strictly similar to the seed**:

   .. math::

      \frac{AE}{AD} = \frac{\phi}{1} = \frac{1}{\phi - 1} = \frac{BC}{BE}, \qquad \frac{Q(A, E)}{Q(A, D)} = \frac{Q(B, C)}{Q(B, E)} = \phi^2 = \frac{3 + \sqrt{5}}{2}.

3. Swinging circle :g:`(EB) <g1:( E B )>` inside :g:`BEFC <g1:< B E F C >>` cuts off a second square gnomon :math:`BEGH` (:g:`G <g1:G>`, :g:`H <g1:H>`), leaving residual rectangle :math:`HGFC` with the *exact same aspect quadrance* :math:`\phi^2` *ad infinitum*, while circle :g:`(MC) <g1:( M C )>` also meets :g:`AB <g1:[ A B ]>` at the conjugate point :g:`E1 <g1:E1>` (:math:`x = -\phi^{-1}`), forming a golden projective range :math:`(E_1, A; B, E)`!
