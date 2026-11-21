:order: 21
:type: proposition
:canonical_id: III.20
:folio: Schöne 174
:tracks: English: prop_20 | Greek: prop_20-el | Summary: summary | Notes: notes

.. _sec-metrica-iii-20-23:
.. _sec-metrica-iii-20:

Prop. III.20: Dividing a Pyramid or Cone & Hero's Cube-Root Algorithm
=====================================================================

.. folio:: Schöne 174
   :page: 174

Ascending from two-dimensional area divisions (governed by duplicate ratios and square roots) to **three-dimensional solid divisions** (governed by triplicate ratios :just:`XII.12` and **cube roots**):

**Proposition III.20 — Dividing a Pyramid or Cone Parallel to Its Base & Extracting :math:`\sqrt[3]{100}` (Schöne pp. 172–178; fols. 105v–106v)**:

To cut a pyramid (or cone) of slant edge :math:`5` into ratio :math:`4 : 1` from the apex (:math:`\frac{4}{5}` upper pyramid to :math:`\frac{1}{5}` lower frustum), similar pyramids stand in the **triplicate ratio** of their homologous edges:

.. math::

   \frac{x^3}{5^3} = \frac{4}{5} \qquad \Longrightarrow \qquad x^3 = \frac{4}{5} \times 125 = 100.

.. folio:: Schöne 178
   :page: 178

To take the **cubic side of 100** (:math:`\sqrt[3]{100}`, Schöne p. 178), proceed by the following weighted interpolation between the two bracketing cubes:

1. Take the nearest integer cubes **above** and **below** :math:`N = 100`: :math:`5^3 = 125` (root :math:`u = 5`) and :math:`4^3 = 64` (root :math:`\ell = 4`).
2. Compute the upper excess :math:`e_u = 125 - 100 = 25` and the lower deficit :math:`e_\ell = 100 - 64 = 36`.
3. Multiply the upper root by the lower deficit (:math:`u \cdot e_\ell = 5 \times 36 = 180`), and the lower root by the upper excess (:math:`\ell \cdot e_u = 4 \times 25 = 100`): adding :math:`180` and :math:`100` (:math:`= 280`) and dividing :math:`180` by :math:`280` gives :math:`\frac{9}{14}`!
4. Add :math:`\frac{9}{14}` to the lower root :math:`4`:

   .. math::

      x \approx 4 + \frac{9}{14} = \frac{65}{14} \approx 4.642857\dots \qquad \text{(exact } \sqrt[3]{100} \approx 4.6415888\dots\text{)},

   achieving **relative accuracy of :math:`0.027\%`** (:math:`(\frac{65}{14})^3 = \frac{274{,}625}{2744} \approx 100.082`) in a single rational step!
