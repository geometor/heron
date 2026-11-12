:order: 10
:type: chapter
:canonical_id: book-i-triangles
:folio: Schöne 2–26
:book: Metrica Book I (Pref. & Props. 1–9)

.. _unit-book-i-triangles-en:

Metrica Book I (Preface & Props. 1–9): Triangles, Heron's Formula & √720
========================================================================

*Origins of Geometry in Egypt, Homogeneous Orthogonal Units, Rectangles & Triangles, Synthetic Incircle Proof of Δ = √(s(s−a)(s−b)(s−c)), and Iterative Square-Root Extraction* — **Schöne (1903), pp. 2–26** · *Codex Constantinopolitanus Palatii Veteris 1, fols. 67r–72r*

.. note::

   **Edition Track (English)**: Original GEOMETOR scholarly translation directly from :person:`Hermann Schöne's <schoene>` :cite:`1903 Teubner editio princeps <schoene:1903>` (pp. 2–26), verified against 300 DPI archival page scans. Hover or click any highlighted geometric symbol (such as :g:`ABC <g1:< A B C >>`, :g:`H <g1:H>`, or :g:`CG <g1:/ C G />`) to illuminate the corresponding element in the interactive diagram. Switch tracks above for **Greek (Teubner)**, **Summary**, or **Notes**.

.. _sec-metrica-i-prooemium:

Prooemium: Egyptian Origins & Orthogonal Unit Measures
------------------------------------------------------

.. folio:: Schöne 2
   :page: 2

**Book I, Prooemium (Schöne pp. 2–6; fols. 67r–68r)**. Original geometry, just as the ancient account teaches us, was occupied with the measurements and distributions of land-parcels in Egypt—whence indeed it was called *geometry* (*land-measurement*). Necessity itself furnished human beings with the invention of the subject: for since the Nile inundated the plains of Egypt year by year, obliterating boundaries, sweeping away many plots, and augmenting others with alluvial deposits, it came to pass that the holdings of some proprietors were diminished while those of others were enlarged, so that each person could no longer recover an equal share without some exact method.

Once the mensuration of land-parcels had been devised, the theorem proved serviceable not in Egypt alone, but everywhere; and as the discipline advanced still further, geometers undertook to measure not merely planar regions, but solid bodies as well—for abundant need of these too was found in architectural constructions, the fabrication of instruments, and the capacities of vessels.

.. folio:: Schöne 4
   :page: 4

Since, therefore, every continuous magnitude is measured by some determinate unit homogeneous with that which is measured—for a line is measured by a line, called a *cubit* or *foot* or *palm* or *finger-breadth*; a surface (:term:`planar content <embadon>`) is measured by an equilateral and rectangular square surface (:just:`I.def.22`); and a solid body is measured by a solid cube whose faces are unit squares—we judged it necessary both to gather together the useful results written by our predecessors and to arrange whatever we ourselves have additionally discovered into three books:

1. In the **First Book**, the measurements of plane and curved surfaces, both rectilinear and curvilinear;
2. In the **Second Book**, the measurements of solid bodies;
3. In the **Third Book**, the divisions of planar regions and solid bodies into given ratios (:term:`proportions <analogia>`).

Because every planar region is referred to an orthogonal unit square and every solid to an orthogonal unit cube, oblique figures whose angles are not right cannot be superposed directly upon unit squares by simple multiplication of adjacent sides; rather, geometry reduces every oblique triangle, polygon, and curved boundary to equivalent right-angled rectangles via :term:`perpendiculars <kathetos>` and the theorems of :person:`Euclid <euclid>` and :person:`Archimedes <archimedes>`.

.. _sec-metrica-i-1-7:

Props. I.1–I.7: Rectangles, Right/Isosceles Triangles & General Altitude Projections
------------------------------------------------------------------------------------

.. folio:: Schöne 6
   :page: 6

- **Proposition I.1 (Oblong Rectangle, Schöne pp. 6–8)**: Given an oblong rectangular region :math:`AB\Gamma\Delta` with :math:`AB = 5` feet and :math:`B\Gamma = 3` feet, dividing each side into unit-foot segments partitions the rectangle into :math:`5 \times 3 = 15` orthogonal unit squares. Thus the :term:`area <embadon>` of every rectangle equals the product of two containing sides.

- **Proposition I.2 (Right-Angled Triangle, Schöne p. 8)**: Given a right-angled triangle with legs :math:`3` and :math:`4` (and hypotenuse :math:`5` by :just:`I.47`), completing the oblong rectangle of sides :math:`3` and :math:`4` shows by :just:`I.34` and :just:`I.41` that the triangle is half the rectangle, namely :math:`\frac{1}{2}(3 \times 4) = 6` unit squares.

- **Proposition I.3 (Isosceles Triangle, Schöne pp. 8–10)**: Given an isosceles triangle with equal sides :math:`AB = A\Gamma = 10` and base :math:`B\Gamma = 12`, dropping the :term:`altitude <kathetos>` :math:`A\Delta` bisects the base (:math:`B\Delta = 6`), whence by :just:`I.47` :math:`A\Delta^2 = 10^2 - 6^2 = 64`, so :math:`A\Delta = 8` and the area is :math:`6 \times 8 = 48`.

.. folio:: Schöne 10
   :page: 10

- **Proposition I.4 (Distinguishing Acute vs. Obtuse Scalene Triangles, Schöne pp. 10–12)**: Given the three sides :math:`a, b, c` of a scalene triangle, before dropping an altitude to side :math:`BC = a`, how do we know whether the angle at :math:`B` is acute, right, or obtuse—that is, whether the altitude falls *inside* or *outside* segment :math:`BC`? Hero invokes :just:`II.13` and :just:`II.12`: compare :math:`AC^2` against :math:`AB^2 + BC^2`. If :math:`AC^2 < AB^2 + BC^2`, :math:`\angle B` is acute; if equal, right (:just:`I.48`); if :math:`AC^2 > AB^2 + BC^2`, :math:`\angle B` is obtuse.

- **Proposition I.5 (Acute-Angled Scalene Triangle on (13, 14, 15), Schöne pp. 12–14)**: Let :math:`AB = 13`, :math:`B\Gamma = 14`, :math:`A\Gamma = 15`. Since :math:`15^2 = 225 < 13^2 + 14^2 = 365`, the altitude :math:`A\Delta` falls inside :math:`B\Gamma`. By :just:`II.13`, :math:`AB^2 + B\Gamma^2 - A\Gamma^2 = 2 \cdot B\Gamma \cdot B\Delta`, whence :math:`2 \cdot 14 \cdot B\Delta = 169 + 196 - 225 = 140`, so :math:`B\Delta = 5`, :math:`A\Delta = \sqrt{169 - 25} = 12`, and the area is :math:`\frac{1}{2}(14 \times 12) = 84`.

- **Proposition I.6 (Obtuse-Angled Scalene Triangle on (5, 6, 9) / (10, 9, 17) type, Schöne pp. 14–16)**: In Hero's numerical example :math:`AB = 13, B\Gamma = 11, A\Gamma = 20`, :math:`20^2 = 400 > 13^2 + 11^2 = 290`, so :math:`\angle B` is obtuse and the foot :math:`\Delta` falls *outside* :math:`B\Gamma` past :math:`B`. By :just:`II.12`, :math:`2 \cdot B\Gamma \cdot B\Delta = 400 - 290 = 110`, whence :math:`B\Delta = 5`, :math:`A\Delta = \sqrt{13^2 - 5^2} = 12`, and the area is :math:`\frac{1}{2}(11 \times 12) = 66`.

- **Proposition I.7 (Unified Projection Formula without Case-Splitting, Schöne pp. 16–18)**: Hero next shows that one can compute the area of *any* triangle—acute, right, or obtuse—by a single algebraic rule without testing :math:`AC^2 \lessgtr AB^2 + BC^2`, paving the way directly for his supreme achievement in Proposition I.8.

.. _sec-metrica-i-8-proof:

Prop. I.8: Synthetic Incircle Proof of Δ = √(s(s−a)(s−b)(s−c))
--------------------------------------------------------------

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

   *(Here Hero explicitly forms the fourth-degree product of two squares—a* :term:`dynamodynamis` *—writing that* :math:`|CG| \cdot |HE|` *is the square root of* :math:`|CG|^2 \cdot |HE|^2` *).*

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
   From :math:`\triangle AHD \sim \triangle CBL` and the parallelism :g:`BL <g1:[ W X ]>` :math:`\parallel` :g:`HE <g1:[ H J ]>` (:just:`I.28`, yielding :math:`\triangle KBL \sim \triangle KEH`), Hero chains five Euclidean ratio steps:

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

- **Proposition I.9 (Triangles with Irrational Sides, Schöne pp. 24–26)**: When one or more sides of a triangle are given only *in square* (:term:`quadrance`, e.g., :math:`AB^2 = 20, BC^2 = 12`), Hero extracts their approximate rational roots via the Proposition I.8 method and applies either the projection rule or Proposition I.8.
