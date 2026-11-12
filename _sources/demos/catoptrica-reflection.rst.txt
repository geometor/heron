.. _demo-catoptrica-reflection:

Shortest-Path Law of Reflection (Catoptrica Prop. 4)
====================================================

*Hero's Mirror-Unfolding Variational Proof Preserved in Greek by Olympiodorus* — Codex Reference: :doc:`/metrica/definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-en`

Interactive Construction (`catoptrica-reflection.svg`)
------------------------------------------------------

Hover or click any geometric label—plane mirror :g:`AB <g1:[ A B ]>`, visual source :g:`C <g1:C>`, object :g:`D <g1:D>`, reflected virtual image :g:`K <g1:K>`, optimal incidence point :g:`E <g1:E>`, or perturbed triangle :g:`CZK <g1:< C Z K >>`—to inspect Hero's shortest-path proof:

.. picture:: /_static/constructions/catoptrica-reflection.svg
   :alt: Hero Catoptrica Prop. 4 — Variational Shortest-Path Proof of Reflection

Exact Symbolic Unfolding in ``geometor.model``
----------------------------------------------

Setting mirror :g:`AB <g1:[ A B ]>` along :math:`y = 0`, eye :g:`C <g1:C>` :math:`= (1, 3)`, and target :g:`D <g1:D>` :math:`= (10, 6)`:

1. Dropping perpendicular :g:`DH <g1:/ D H />` onto :g:`AB <g1:[ A B ]>` gives foot :g:`H <g1:H>` :math:`= (10, 0)`, and compass reflection across :g:`H <g1:H>` gives virtual image :g:`K <g1:K>` :math:`= (10, -6)`.
2. Joining the straight line :g:`CK <g1:[ C K ]>` intersects mirror :g:`AB <g1:[ A B ]>` at the unique equal-angle point :g:`E <g1:E>` :math:`= (4, 0)`:

   - Incidence and reflection :term:`spreads <spread>` with the mirror are strictly equal: :math:`s(AB, CE) = s(AB, ED) = \frac{1}{2}` (:math:`45^\circ`).
   - Total unfolded ray length is :math:`|CE| + |ED| = 3\sqrt{2} + 6\sqrt{2} = 9\sqrt{2} = |CK|`, with exact squared length :math:`(9\sqrt{2})^2 = 162`.

3. For any perturbed mirror point such as :g:`Z <g1:Z>` :math:`= (7, 0)`, congruence :eq:`ZD = ZK <g1:/ Z D /,/ Z K />` and Euclid's triangle inequality (:just:`I.20`) on :g:`CZK <g1:< C Z K >>` yield:

   .. math::

      |CZ| + |ZD| = 3\sqrt{5} + 3\sqrt{5} = 6\sqrt{5}, \qquad (6\sqrt{5})^2 = 180 > 162 = (|CE| + |ED|)^2.

Executable Python API
---------------------

.. code-block:: python

   import sympy as sp
   from geometor.heron import construct_catoptrica_reflection

   model, inv = construct_catoptrica_reflection()
   assert inv["incidence_spread"] == inv["reflection_spread"] == sp.Rational(1, 2)
   assert inv["optimal_length_sq"] == 162
   assert inv["perturbed_length_sq"] == 180
