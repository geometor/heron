:order: 9
:type: proposition
:canonical_id: I.8
:folio: Schöne 18
:tracks: English: prop_08 | Greek: prop_08-el | Summary: summary | Notes: notes

.. _sec-metrica-i-8-proof:

Prop. I.8: Synthetic Incircle Proof of Δ = √(s(s−a)(s−b)(s−c)) & Root Extraction
================================================================================

.. folio:: Schöne 18
   :page: 18

**Proposition I.8 — Enunciation & Rule on (7, 8, 9) (Schöne p. 18; fol. 70v)**:

   *"There is a universal method for finding the area (:term:`embadon`) of any triangle whatever when its three sides are given, without a perpendicular (:term:`kathetos`)."*

For example, let the sides of the triangle be :math:`7, 8, 9` units:

1. Add :math:`7` and :math:`8` and :math:`9`; the result is :math:`24` (:term:`perimeter <perimetros>`).
2. Take half of these; the result is :math:`12` (:math:`s = 12`).
3. Subtract the :math:`7` units: remainder :math:`5` (:math:`s - c = 5`). Again subtract :math:`8` from :math:`12`: remainder :math:`4` (:math:`s - a = 4`). And further subtract :math:`9`: remainder :math:`3` (:math:`s - b = 3`).
4. Multiply :math:`12` by :math:`5`: the result is :math:`60`. Multiply this by :math:`4`: the result is :math:`240`. Multiply this by :math:`3`: the result is :math:`720`.
5. Take the :term:`square root <pleura>` (*side*) of :math:`720`, and it will be the area of the triangle:

.. math::

   \Delta^2 = 12 \times 5 \times 4 \times 3 = 720, \qquad \Delta = \sqrt{720} = 12\sqrt{5}.

.. _sec-metrica-i-8-sqrt:

Hero's Iterative Square-Root Extraction (√720 → 161/6 → 51841/1932)
-------------------------------------------------------------------

**Rational Iteration on 720 (Schöne pp. 18–20; fol. 70v)**:

Since :math:`720` does not possess a :term:`rational square root <rhetos>` (*ῥητὴν πλευρὰν οὐκ ἔχουσιν*), we shall extract its side within a minimal difference (*μετὰ διαφόρου ἐλαχίστου*) as follows:

- Since the square nearest to :math:`720` is :math:`729` and has side :math:`x_0 = 27`, divide :math:`720` by :math:`27`: the result is :math:`26\frac{2}{3}` (:math:`\frac{80}{3}`).
- Add :math:`27`: the result is :math:`53\frac{2}{3}` (:math:`\frac{161}{3}`).
- Take half of these: the result is :math:`x_1 = 26 + \frac{1}{2} + \frac{1}{3} = 26\frac{5}{6} = \frac{161}{6}`.
- Therefore the side of :math:`720` will be very nearly :math:`26\frac{5}{6}`. For :math:`26\frac{5}{6}` multiplied by itself gives :math:`720\frac{1}{36}` (:math:`\frac{25921}{36}`), so that the difference (*διάφορον*) is the :math:`\frac{1}{36}` part of a unit!
- And if we wish the difference to become even smaller than :math:`\frac{1}{36}`, instead of :math:`729` we shall place the :math:`720\frac{1}{36}` just found, and doing the same things we shall find the resulting difference to be vastly less than :math:`\frac{1}{36}` (namely :math:`x_2 = \frac{51841}{1932}`, whose square exceeds :math:`720` by only :math:`\frac{1}{3{,}732{,}624}`).

.. folio:: Schöne 20
   :page: 20

**The Geometric Demonstration (*Γραμμικὴ Ἀπόδειξις*, Schöne pp. 20–24, Fig. 7; fols. 70v–71v)**:

*(Note on Diagram Labels: In the interactive figure below, Roman letters map Hero's Greek labels as follows:* :g:`A <g1:A>` = :math:`A`, :g:`B <g1:B>` = :math:`B`, :g:`C <g1:C>` = :math:`\Gamma`, :g:`D <g1:D>` = :math:`\Delta`, :g:`E <g1:E>` = :math:`E`, :g:`F <g1:F>` = :math:`Z`, :g:`G <g1:G>` = :math:`\Theta`, :g:`H <g1:H>` = :math:`H`, :g:`K <g1:K>` = :math:`K`, :g:`L <g1:L>` = :math:`\Lambda`, *with auxiliary circumcenter* :g:`M <g1:M>` *of the cyclic quadrilateral).*

.. picture:: /_static/figures/heron-i8-incircle.svg
   :alt: Hero Metrica I.8 — Synthetic Incircle and Cyclic Quadrilateral Proof on (13, 14, 15)

1. **Incircle & Semiperimeter Rectangle**:
   Let the given triangle be :g:`ABC <g1:< A B C >>`, with each of :g:`AB <g1:[ A B ]>`, :g:`BC <g1:[ B C ]>`, :g:`CA <g1:[ C A ]>` given; it is required to find the area. Inscribe in the triangle the circle :g:`DEF <g1:( H E )>` (:just:`IV.4`), whose center is :g:`H <g1:H>` (`X(1)` in :cite:`Kimberling's ETC <kimberling:etc>`), and join the angle bisectors :g:`AH <g1:[ A H ]>`, :g:`BH <g1:[ B E ]>`, :g:`CH <g1:[ C G ]>` and perpendicular radii :g:`HD <g1:/ H D />`, :g:`HE <g1:/ H E />`, :g:`HF <g1:/ H F />` (:just:`III.18`, :eq:`g1:/ H D /,/ H E /,/ H F /`).

   Then the rectangle :math:`BC \cdot HE` is double :math:`\triangle BHC`, the rectangle :math:`CA \cdot HF` is double :math:`\triangle AHC`, and :math:`AB \cdot HD` is double :math:`\triangle AHB` (:just:`I.41`). Therefore the rectangle contained by the perimeter of :g:`ABC <g1:< A B C >>` and the inradius :g:`HE <g1:/ H E />` is double :g:`ABC <g1:< A B C >>`.

   Produce :g:`CB <g1:[ B C ]>` past :g:`B <g1:B>` to :g:`G <g1:G>` (Hero's :math:`\Theta`) so that :eq:`BG = AD <g1:/ B G /,/ A D />` (:just:`I.3`). Because tangents from each vertex to the incircle are equal (:g:`AD <g1:/ A D />` = :g:`AF <g1:/ A F />`, :g:`BD <g1:/ B D />` = :g:`BE <g1:/ B E />`, and :g:`CE <g1:/ C E />` = :g:`CF <g1:/ C F />` by :just:`III.17`), the extended segment :g:`CG <g1:/ C G />` equals half the perimeter (:math:`s`):

   .. math::

      \Delta(\triangle ABC) = |CG| \cdot |HE| = s \cdot r, \qquad \Delta^2 = |CG|^2 \cdot |HE|^2.

   *(Forming the fourth-degree product of two squares—a* :term:`dynamodynamis` *—the rectangle* :math:`|CG| \cdot |HE|` *is the square root of* :math:`|CG|^2 \cdot |HE|^2` *).*

.. folio:: Schöne 22
   :page: 22

2. **Orthogonal Auxiliary Construction & Cyclic Quadrilateral**:
   Draw :g:`HL <g1:[ T U ]>` at right angles to :g:`CH <g1:[ C G ]>` at :g:`H <g1:H>`, and :g:`BL <g1:[ W X ]>` at right angles to :g:`BC <g1:[ B C ]>` at :g:`B <g1:B>` (:just:`I.11`), meeting :g:`BC <g1:[ B C ]>` at :g:`K <g1:K>` and each other at :g:`L <g1:L>` (Hero's :math:`\Lambda`); join :g:`CL <g1:[ C L ]>`.

   Since both :math:`\angle CHL` and :math:`\angle CBL` are right angles, the quadrilateral :g:`CHBL <g1:< C H B L >>` is inscribed in a circle :g:`(CHBL) <g1:( M C )>` (:just:`III.22` converse, diameter :g:`CL <g1:[ C L ]>` centered at :g:`M <g1:M>`). Consequently the opposite angles :math:`\angle CHB + \angle CLB` equal two right angles (:just:`III.22`).

3. **Angle-Sum Reduction Around the Incenter**:
   Around the incenter :g:`H <g1:H>`, the three angle bisectors :g:`AH <g1:[ A H ]>`, :g:`BH <g1:[ B E ]>`, :g:`CH <g1:[ C G ]>` together with the three perpendicular radii partition the full :math:`360^\circ` (:math:`4` right angles) around :g:`H <g1:H>` into three pairs of congruent right-triangle central angles, so :math:`\angle CHB + \angle AHD` equals two right angles. Equating the two supplementary pairs gives:

   .. math::

      \angle AHD = \angle CLB, \qquad \angle ADH = \angle CBL = 90^\circ \implies \triangle AHD \sim \triangle CBL \quad (\text{by } \text{VI.4}).

4. **Proportion Chain & Right-Triangle Altitude Climax**:
   From :math:`\triangle AHD \sim \triangle CBL` and the parallelism :g:`BL <g1:[ W X ]>` :math:`\parallel` :g:`HE <g1:[ H J ]>` (:just:`I.28`, yielding :math:`\triangle KBL \sim \triangle KEH`), we chain five Euclidean ratio steps:

   .. math::

      \frac{|BC|}{|BL|} = \frac{|AD|}{|HD|} = \frac{|BG|}{|HE|}
      \implies \frac{|CB|}{|BG|} = \frac{|BL|}{|HE|} = \frac{|BK|}{|KE|}.

   Componendo (:just:`V.18`), adding :math:`1` to each side yields:

   .. math::

      \frac{|CG|}{|BG|} = \frac{|CB| + |BG|}{|BG|} = \frac{|BK| + |KE|}{|KE|} = \frac{|BE|}{|KE|}.

   Multiplying numerator and denominator on the left by :math:`|CG|` and on the right by :math:`|EC|` (:just:`VI.1`), and applying the right-triangle altitude theorem :math:`|KE| \cdot |EC| = |HE|^2` in right triangle :math:`\triangle KHC` (:just:`VI.8`):

   .. math::

      \frac{|CG|^2}{|CG| \cdot |BG|} = \frac{|BE| \cdot |EC|}{|KE| \cdot |EC|} = \frac{|BE| \cdot |EC|}{|HE|^2}
      \implies |CG|^2 \cdot |HE|^2 = |CG| \cdot |BG| \cdot |BE| \cdot |EC|.

   Since :math:`|CG| = s`, :math:`|BG| = s - a`, :math:`|BE| = s - b`, and :math:`|EC| = s - c`, each factor is given directly from the three sides, and therefore the area :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}` is given!

.. folio:: Schöne 24
   :page: 24

5. **Numerical Synthesis on (13, 14, 15) (Schöne p. 24; fol. 71v)**:
   *"It shall be compounded thus"*: let :math:`AB = 13`, :math:`BC = 14`, :math:`CA = 15`. Add the three: :math:`42`, whose half is :math:`s = 21`. Subtract :math:`13 \to 8`; subtract :math:`14 \to 7`; subtract :math:`15 \to 6`. Multiply :math:`21 \times 8 \times 7 \times 6 = 7056`. Its exact rational square root is :math:`\Delta = 84`—matching Proposition I.5 without computing an altitude!
