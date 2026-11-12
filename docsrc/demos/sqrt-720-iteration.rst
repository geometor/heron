.. _demo-sqrt-720-iteration:

Iterative Square-Root Extraction on √720 (Metrica I.8)
======================================================

*Exact Rational Convergents & Quadratic Error Squaring on Hero's (7, 8, 9) Triangle* — Codex Reference: :doc:`/metrica/book-i-triangles/book-i-triangles-en`

Mathematical Derivation
-----------------------

On his opening scalene benchmark :math:`(a, b, c) = (7, 8, 9)` (:cite:`Schöne 1903, pp. 18–20 <schoene:1903>`), :person:`Hero <hero>` obtains :math:`s = 12` and :math:`\Delta^2 = 12 \times 5 \times 4 \times 3 = 720`. Because :math:`720 = 144 \times 5` is non-square (:math:`\sqrt{720} = 12\sqrt{5}`), Hero introduces the iterative averaging recurrence:

.. math::

   x_0 = 27 \quad (27^2 = 729), \qquad x_{k+1} = \frac{1}{2}\!\left(x_k + \frac{N}{x_k}\right).

Subtracting :math:`\sqrt{N}` and squaring reveals why convergence doubles the number of exact digits at *every* step:

.. math::

   x_{k+1}^2 - N = \frac{(x_k^2 - N)^2}{4 x_k^2}.

Exact ``sympy.Rational`` Convergent Table
-----------------------------------------

.. list-table:: Exact Rational Stream ``heron_sqrt_convergents(720, steps=4, x0=27)``
   :widths: 10 34 36 20
   :header-rows: 1

   * - :math:`k`
     - Exact Rational :math:`x_k \in \mathbb{Q}`
     - Exact Quadratic Excess :math:`x_k^2 - 720`
     - Accurate Digits
   * - :math:`0`
     - :math:`27`
     - :math:`+9`
     - :math:`2.8`
   * - :math:`1`
     - :math:`\frac{161}{6} = 26\frac{5}{6}` *(Hero's first value)*
     - :math:`\frac{1}{36}` *(Hero's* :math:`\lambda\varsigma'` *)*
     - :math:`4.3`
   * - :math:`2`
     - :math:`\frac{51{,}841}{1932}` *(Hero's second step)*
     - :math:`\frac{1}{3{,}732{,}624} \approx 2.68 \times 10^{-7}`
     - :math:`8.3`
   * - :math:`3`
     - :math:`\frac{5{,}374{,}978{,}561}{200{,}313{,}624}`
     - :math:`\frac{1}{40{,}125{,}547{,}959{,}889{,}976} \approx 2.49 \times 10^{-17}`
     - :math:`18.3`
   * - :math:`4`
     - :math:`79\text{-digit} / 77\text{-digit}` fraction
     - :math:`\approx 2.16 \times 10^{-37}`
     - :math:`38.4`

Executable Python API
---------------------

.. code-block:: python

   import sympy as sp
   from geometor.heron import heron_area, heron_sqrt_convergents

   conv = heron_sqrt_convergents(720, steps=3, x0=27)
   assert conv[1].approx == sp.Rational(161, 6)
   assert conv[1].residual == sp.Rational(1, 36)
   assert conv[2].approx == sp.Rational(51841, 1932)
   assert heron_area(7, 8, 9) == 12 * sp.sqrt(5)
