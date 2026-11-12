.. _demo-heron-formula-proof:

Heron's Formula Synthetic Proof & Quadrea (Metrica I.8)
=======================================================

*Exact Compass-and-Straightedge Model of Hero's Incircle & Cyclic Quadrilateral Proof* — Codex Reference: :doc:`/metrica/book-i-triangles/book-i-triangles-en`

Interactive Construction (`heron-i8-incircle.svg`)
--------------------------------------------------

Hover or click any geometric label below—such as :g:`ABC <g1:< A B C >>`, incenter :g:`H <g1:H>`, cyclic quadrilateral :g:`CHBL <g1:< C H B L >>`, or extended semiperimeter :g:`CG <g1:/ C G />`—to trace :person:`Hero's <hero>` synthetic proof step-by-step:

.. picture:: /_static/constructions/heron-i8-incircle.svg
   :alt: Exact geometor.model Construction of Hero Metrica I.8 on (13, 14, 15)

Exact Symbolic Coordinates & Deductive Chain
--------------------------------------------

On Hero's synthesis triangle :math:`(AB, BC, CA) = (13, 14, 15)` placed at :g:`B <g1:B>` :math:`= (0, 0)`, :g:`C <g1:C>` :math:`= (14, 0)`, and :g:`A <g1:A>` :math:`= (5, 12)`:

1. **Incenter & Inradius**: Internal angle bisectors meet at :g:`H <g1:H>` :math:`= (6, 4)` (`X(1)` in :cite:`Kimberling's ETC <kimberling:etc>`), with touchpoints :g:`E <g1:E>` :math:`= (6, 0)`, :g:`D <g1:D>` :math:`= \left(\frac{30}{13}, \frac{72}{13}\right)`, and :g:`F <g1:F>` :math:`= \left(\frac{46}{5}, \frac{32}{5}\right)` of radius :g:`HE <g1:/ H E />` :math:`r = 4`.
2. **Extended Semiperimeter**: Compass extension past :g:`B <g1:B>` locates :g:`G <g1:G>` :math:`= (-7, 0)` so that :eq:`BG = AD <g1:/ B G /,/ A D />` :math:`= s - a = 7` and :g:`CG <g1:/ C G />` :math:`= s = 21`, certifying :math:`\Delta = s \cdot r = 21 \times 4 = 84`.
3. **Cyclic Auxiliary Quadrilateral**: Erecting :math:`HL \perp CH` at :g:`H <g1:H>` (meeting :g:`BC <g1:[ B C ]>` at :g:`K <g1:K>` :math:`= (4, 0)`) and :math:`BL \perp BC` at :g:`B <g1:B>` meets at :g:`L <g1:L>` :math:`= (0, -8)`. Quadrilateral :g:`CHBL <g1:< C H B L >>` is inscribed in circle :g:`(MC) <g1:( M C )>` with center :g:`M <g1:M>` :math:`= (7, -4)` and squared radius :math:`Q(M, C) = 65`.
4. **Right-Triangle Altitude Identity (:just:`VI.8`)**: In right triangle :math:`KHC`, altitude :g:`HE <g1:/ H E />` satisfies :math:`|KE| \cdot |EC| = 2 \times 8 = 16 = 4^2 = r^2`, completing Hero's proportion:

   .. math::

      \Delta^2 = |CG|^2 \cdot |HE|^2 = |CG| \cdot |BG| \cdot |BE| \cdot |EC| = 21 \times 7 \times 6 \times 8 = 7056 = 84^2.

5. **Wildberger's Polynomial Quadrea**: Over :math:`\mathbb{Z}[Q_a, Q_b, Q_c]` with :math:`(Q_a, Q_b, Q_c) = (196, 225, 169)`:

   .. math::

      \mathcal{A} = (196 + 225 + 169)^2 - 2(196^2 + 225^2 + 169^2) = 112{,}896 = 16 \times 7056.

Executable Python API
---------------------

.. code-block:: python

   from geometor.heron import archimedes_quadrea, construct_heron_proof, verify_quadrea_identity

   model, inv = construct_heron_proof()
   assert inv["area"] == 84
   assert inv["quadrea"] == archimedes_quadrea(196, 225, 169) == 112896
   assert verify_quadrea_identity() == 0
