.. _demo-area-division-book-iii:

Proportional Area Divisions & ∛100 (Metrica Book III)
=====================================================

*Exact Mean-Proportional Compass Cuts Carrying Zero "Millet-Seed" Error* — Codex Reference: :doc:`/metrica/book-iii-divisions/book-iii-divisions-en`

Interactive Construction (`metrica-iii-area-division.svg`)
----------------------------------------------------------

Hover or click any element—given triangle :g:`ABC <g1:< A B C >>`, vertex cevian :g:`AV <g1:/ A V />` (:math:`5 : 3`), semicircle altitude :g:`PR <g1:/ P R />`, compass transfer circle :g:`(AR) <g1:( A R )>`, or parallel division :g:`ADE <g1:< A D E >>` vs. :g:`DECB <g1:< D B C E >>` (:math:`3 : 1`)—to inspect Hero's *Metrica* III.1–2 constructions:

.. picture:: /_static/constructions/metrica-iii-area-division.svg
   :alt: Hero Metrica III.1 and III.2 — Vertex and Parallel Area Divisions on (13, 14, 15)

Exact Symbolic Verification on ``(13, 14, 15)``
-----------------------------------------------

On Hero's canonical estate :g:`ABC <g1:< A B C >>` of total area :math:`84`:

- **Proposition III.1 (Vertex Cut in 5 : 3)**: Point :g:`V <g1:V>` :math:`= \left(\frac{35}{4}, 0\right)` partitions :math:`BC = 14` into :math:`BV = 8\frac{3}{4}` and :math:`VC = 5\frac{1}{4}`, giving exact sub-areas :math:`\frac{105}{2} = 52\frac{1}{2}` and :math:`\frac{63}{2} = 31\frac{1}{2}`.
- **Proposition III.2 (Parallel Cut in 3 : 1)**: Marking :g:`P <g1:P>` at :math:`\frac{3}{4}` along :g:`AB <g1:[ A B ]>` and erecting perpendicular :g:`PR <g1:/ P R />` to the semicircle on :g:`AB <g1:[ A B ]>` constructs :g:`R <g1:R>` with exact mean-proportional :term:`quadrance`:

  .. math::

     Q(A, D) = Q(A, R) = \frac{3}{4} \times 13^2 = \frac{507}{4} = 126\frac{3}{4}, \qquad |AD| = \frac{13\sqrt{3}}{2}.

  Drawing :g:`DE <g1:/ D E />` parallel to :g:`BC <g1:[ B C ]>` yields :math:`\text{Area}(\triangle ADE) = 63` and :math:`\text{Area}(DECB) = 21` (:math:`63 : 21 = 3 : 1` identically in :math:`\mathbb{Q}(\sqrt{3})`).

Executable Python API
---------------------

.. code-block:: python

   import sympy as sp
   from geometor.heron import construct_area_division

   model, inv = construct_area_division(m_ratio=3, n_ratio=1)
   assert inv["ad_quadrance"] == sp.Rational(507, 4)
   assert inv["area_ade"] == 63 and inv["area_decb"] == 21
