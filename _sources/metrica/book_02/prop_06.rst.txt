:order: 7
:type: proposition
:canonical_id: II.6
:folio: Schöne 110
:tracks: English: prop_06 | Summary: summary | Notes: notes

.. _sec-metrica-ii-6:

Prop. II.6: Square Pyramidal Frustum via Mean-Plus-Third-Difference
===================================================================

.. folio:: Schöne 110
   :page: 108

**Proposition II.6 (Square Pyramidal Frustum, Schöne pp. 108–112)**:

Rather than computing a truncated pyramid (:term:`frustum <kolouros>`, *κόλουρος*) by extending it to its apex and subtracting two large pyramids, Hero transforms the classical multiplier :math:`\frac{a^2 + ab + b^2}{3}` into his signature **mean-square plus one-third half-difference-square** identity:

.. math::

   \frac{a^2 + ab + b^2}{3} = \left(\frac{a + b}{2}\right)^2 + \frac{1}{3}\left(\frac{a - b}{2}\right)^2,

so that for a square frustum of lower side :math:`a = 10`, upper side :math:`b = 2`, and perpendicular height :math:`h = 9` (slant edge :math:`\sqrt{81 + 32}`):

.. math::

   V_{\text{frustum}} = h \left[\left(\frac{a + b}{2}\right)^2 + \frac{1}{3}\left(\frac{a - b}{2}\right)^2\right] = 9 \left(36 + \frac{16}{3}\right) = 372.

Notice the engineering insight: the naive "average cross-section" rule :math:`h\left(\frac{a+b}{2}\right)^2` underestimates the true volume by *precisely* :math:`\frac{1}{3} h \left(\frac{a-b}{2}\right)^2`!
