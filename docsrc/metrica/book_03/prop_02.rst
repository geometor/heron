:order: 3
:type: proposition
:canonical_id: III.2
:folio: Schöne 144
:tracks: English: prop_02 | Greek: prop_02-el | Summary: summary | Notes: notes

.. _sec-metrica-iii-2:

Prop. III.2: Dividing a Triangle Parallel to Base in Ratio 3 : 1
================================================================

.. folio:: Schöne 144
   :page: 144

**Proposition III.2 (Division by a Line Parallel to the Base in Ratio 3 : 1, Schöne pp. 142–144; fol. 100v)**:

*To divide the given triangle* :g:`ABC <g1:< A B C >>` (:math:`AB = 13, B\Gamma = 14, A\Gamma = 15`) *into two regions—an upper triangle* :g:`ADE <g1:< A D E >>` *and a lower trapezium* :g:`DECB <g1:< D B C E >>` — *in the given ratio* :math:`m : n = 3 : 1` *by a straight line* :g:`DE <g1:/ D E />` *parallel to base* :g:`BC <g1:[ B C ]>`.

.. picture:: /_static/figures/metrica-iii-area-division.svg
   :alt: Hero Metrica III.1 and III.2 — Vertex Division (5:3) and Parallel Mean-Proportional Division (3:1) on (13, 14, 15)

1. *Analysis*: Since :g:`DE <g1:/ D E />` is parallel to :g:`BC <g1:[ B C ]>`, triangle :g:`ADE <g1:< A D E >>` is equiangular and similar to :g:`ABC <g1:< A B C >>` (:just:`I.29`, :just:`VI.4`). When the ratio of upper triangle to lower trapezium is :math:`3 : 1`, *componendo* the ratio of the whole triangle :g:`ABC <g1:< A B C >>` to :g:`ADE <g1:< A D E >>` is :math:`(3 + 1) : 3 = 4 : 3`.
2. By **Euclid's *Elements* VI.19**, similar triangles are to one another in the **duplicate ratio** of their homologous sides:

   .. math::

      \frac{\text{Area}(\triangle AB\Gamma)}{\text{Area}(\triangle A\Delta E)} = \frac{AB^2}{A\Delta^2} = \frac{4}{3}.

3. *Geometric Mean-Proportional Construction*: Mark :g:`P <g1:P>` on :g:`AB <g1:[ A B ]>` so that :math:`AP = \frac{3}{4} AB`, describe the semicircle on diameter :g:`AB <g1:[ A B ]>`, erect the perpendicular :g:`PR <g1:/ P R />` to meet the semicircle at :g:`R <g1:R>`, and transfer radius :math:`AR` via circle :g:`(AR) <g1:( A R )>` back onto :g:`AB <g1:[ A B ]>` at :g:`D <g1:D>` (:just:`VI.13`), drawing :g:`DE <g1:/ D E />` parallel to :g:`BC <g1:[ B C ]>`.
4. *Synthesis on (13, 14, 15)*: Since :math:`AB^2 = 13^2 = 169`, the :term:`quadrance` of :math:`A\Delta` is exact over :math:`\mathbb{Q}`:

   .. math::

      A\Delta^2 = \frac{3}{4} \times 169 = \frac{507}{4} = 126\frac{3}{4}, \qquad A\Delta = \frac{13\sqrt{3}}{2} \approx 11\frac{1}{4},

   partitioning the area :math:`84` into :math:`\text{Area}(\triangle ADE) = 63` and :math:`\text{Area}(DECB) = 21` (:math:`63 : 21 = 3 : 1` with zero error!).
