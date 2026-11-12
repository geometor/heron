:order: 20
:type: chapter
:canonical_id: book-i-polygons-circles
:folio: Schöne 26–90
:book: Metrica Book I (Props. 10–39)

.. _unit-book-i-polygons-circles-en:

Metrica Book I (Props. 10–39): Quadrilaterals, Regular Polygons, Circles & Conics
=================================================================================

*Trapezia & Irregular Quadrilaterals, the Regular Polygon Series (3-gon to 12-gon) & Golden Section Pentagon Lemma, Archimedes' Plinthides & Circular Annulus, Circular & Parabolic Segments via the Method, Ellipse Area, and Curved Surfaces* — **Schöne (1903), pp. 26–90** · *Codex Constantinopolitanus Palatii Veteris 1, fols. 72r–87r*

.. note::

   **Edition Track (English)**: Original GEOMETOR scholarly translation and proposition-by-proposition synthesis directly from :person:`Hermann Schöne's <schoene>` :cite:`1903 Teubner editio princeps <schoene:1903>` (pp. 26–90), verified against 300 DPI archival page scans. Hover or click any highlighted geometric symbol (such as :g:`ABD <g1:< A B D >>`, :g:`AB <g1:/ A B />`, or :g:`AG <g1:/ A G />`) to illuminate the corresponding element in the interactive diagram. Switch tracks above for **Greek (Teubner)**, **Summary**, or **Notes**.

.. _sec-metrica-i-10-16:

Props. I.10–I.16: Trapezia, Rhombi & General Quadrilaterals
-----------------------------------------------------------

.. folio:: Schöne 26
   :page: 26

Having mastered every species of triangle in Propositions I.1–I.9, :person:`Hero <hero>` points out a foundational distinction between triangles and four-sided figures: whereas three given sides uniquely determine the angles and :term:`area <embadon>` of a triangle (:just:`I.8`), four given sides do *not* determine a quadrilateral unless either a right angle, a parallel relation, or a diagonal is also specified.

- **Proposition I.10 (Right-Angled Trapezium, Schöne pp. 26–28)**: Given a trapezium :math:`AB\Gamma\Delta` with parallel bases :math:`A\Delta = 6`, :math:`B\Gamma = 14`, and perpendicular side :math:`AB = 15` (so :math:`\Gamma\Delta = 17`), the area equals half the sum of the parallel bases multiplied by the perpendicular height:

  .. math::

     \text{Area} = \frac{A\Delta + B\Gamma}{2} \cdot AB = \frac{6 + 14}{2} \times 15 = 150.

- **Proposition I.11 (Isosceles Trapezium, Schöne pp. 28–30)**: Given parallel bases :math:`6` and :math:`20` and equal oblique legs :math:`13` and :math:`13`, dropping two :term:`perpendiculars <kathetos>` from the upper vertices cuts off equal projections :math:`\frac{20 - 6}{2} = 7`—or in Hero's crisp integer example (:math:`A\Delta = 10, B\Gamma = 20, AB = \Gamma\Delta = 13`), projections of :math:`5`, yielding height :math:`\sqrt{13^2 - 5^2} = 12` and area :math:`\frac{10 + 20}{2} \times 12 = 180`.

.. folio:: Schöne 32
   :page: 32

- **Propositions I.12–I.13 (Acute & Obtuse General Trapezia, Schöne pp. 30–36)**: Given unequal parallel bases :math:`a > c` and unequal oblique legs :math:`b, d`, drawing a line through an upper vertex parallel to one leg (:just:`I.31`) decomposes the trapezium into a parallelogram of base :math:`c` and a scalene differential triangle of sides :math:`(b, d, a - c)`. Applying Hero's Formula (Prop. I.8) or the Euclidean projection rule (Props. I.5–I.6) to that differential triangle determines the common altitude :math:`h`, whence :math:`\text{Area} = \frac{a + c}{2} h`.

- **Propositions I.14–I.16 (Rhombi, Rhomboids & Re-Entrant Quadrilaterals, Schöne pp. 36–46)**: For a rhombus, rhomboid, or arbitrary convex or non-convex (*κοιλογώνιον*, dart-shaped) quadrilateral, Hero requires one diagonal :math:`d` in addition to the four sides, partitioning the figure into two given triangles measured either via perpendiculars or directly via Proposition I.8.

.. _sec-metrica-i-17-25:

Props. I.17–I.25: Regular Polygons (3-gon to 12-gon) & the Golden Section Pentagon Lemma
----------------------------------------------------------------------------------------

.. folio:: Schöne 46
   :page: 46

In Propositions I.17–I.25, Hero systematically computes the area :math:`A_n` of every regular :math:`n`-gon of given side :math:`a` from the equilateral triangle (:math:`n = 3`) through the regular dodecagon (:math:`n = 12`), expressing each ratio :math:`A_n : a^2` both by an exact geometric construction and by a close rational multiplier suitable for architectural and surveying calculations.

- **Proposition I.17 (Equilateral Triangle, Schöne pp. 46–48)**: For side :math:`a = 10`, :math:`h^2 = a^2 - (\frac{a}{2})^2 = \frac{3}{4}a^2`, so :math:`A_3^2 = \frac{3}{16}a^4` (:term:`dynamodynamis`). Approximating :math:`\frac{\sqrt{3}}{4} \approx \frac{13}{30}`, Hero obtains :math:`A_3 \approx \frac{13}{30}a^2 = 43\frac{1}{3}` (exact :math:`25\sqrt{3} \approx 43.3013`).

.. folio:: Schöne 50
   :page: 50

**Proposition I.18 & Lemma — The Regular Pentagon via Extreme and Mean Ratio (Schöne pp. 48–54; fol. 77v)**:

To measure the regular pentagon of side :math:`a = 10`, Hero inscribes it in a circle of center :math:`Z` and considers the right triangle formed by the circumradius :math:`ZB`, the apothem :math:`Z\Gamma`, and the half-side :math:`B\Gamma = \frac{a}{2}`, whose acute central angle at :math:`Z` is one-tenth of four right angles, i.e., :math:`\frac{2}{5}` of a right angle (:math:`36^\circ`). He isolates its fundamental golden-section property in an explicit Euclidean lemma:

   **Lemma (Schöne p. 50; fol. 77v)**: *Let* :g:`ABC <g1:[ A C ]>` *be a right-angled triangle having a right angle at* :g:`C <g1:C>` *(Hero's* :math:`\Gamma` *), and at* :g:`A <g1:A>` *an angle of two-fifths of a right angle (* :math:`36^\circ` *). To prove that the square on the sum* :math:`(BA + A\Gamma)` *is five times the square on* :math:`A\Gamma`:

   .. math::

      (BA + A\Gamma)^2 = 5\,A\Gamma^2 \qquad \Longleftrightarrow \qquad \frac{BA + A\Gamma}{A\Gamma} = \sqrt{5}, \qquad \frac{BA}{A\Gamma} = \sqrt{5} - 1 = \frac{2}{\phi}.

*(Diagram Mapping:* :g:`A <g1:A>` = :math:`A`, :g:`B <g1:B>` = :math:`B`, :g:`C <g1:C>` = :math:`\Gamma`, :g:`D <g1:D>` = :math:`\Delta`, *and* :g:`G <g1:G>` *marks the golden cut on* :math:`A\Delta` *with* :eq:`AG = AB = BD <g1:/ A G /,/ A B /,/ B D />` *).*

.. picture:: /_static/figures/pentagon-golden-lemma.svg
   :alt: Hero Metrica I.18 — Pentagon Golden Section Lemma in Q(phi)

**Proof of the Lemma**:

1. Produce :g:`AC <g1:/ A C />` to :g:`D <g1:D>` so that :eq:`CD = AC <g1:/ C D /,/ A C />`, and join :g:`BD <g1:/ B D />`.
2. Because right triangles :math:`AB\Gamma` and :math:`\Delta B\Gamma` share leg :math:`B\Gamma` and have :eq:`AC = CD <g1:/ A C /,/ C D />`, we have :eq:`AB = BD <g1:/ A B /,/ B D />` and :math:`\angle AB\Gamma = \angle \Gamma B\Delta` (:just:`I.4`).
3. Since :math:`\angle BA\Gamma = \frac{2}{5}` of a right angle (:math:`36^\circ`), its complement :math:`\angle AB\Gamma` is :math:`\frac{3}{5}` of a right angle (:math:`54^\circ` by :just:`I.32`). Hence the whole apex angle :math:`\angle AB\Delta` of isosceles triangle :g:`ABD <g1:< A B D >>` is :math:`\frac{6}{5}` of a right angle (:math:`108^\circ`), which is the interior angle of a regular pentagon!
4. In a regular pentagon, the diagonal :math:`A\Delta` and sides :g:`AB <g1:/ A B />`, :g:`BD <g1:/ B D />` cut one another in **extreme and mean ratio** (:just:`XIII.8`), with :g:`AB <g1:/ A B />` (= :g:`AG <g1:/ A G />` via circle :g:`(AB) <g1:( A B )>`) equal to the greater segment of :math:`A\Delta`.
5. Since :g:`AC <g1:/ A C />` is half the greater segment's whole line :math:`A\Delta`—or directly by **Euclid's *Elements* XIII.1** ("If a straight line be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half")—it follows immediately that:

   .. math::

      (BA + A\Gamma)^2 = 5\,A\Gamma^2. \qquad \text{Q.E.D.}

Approximating :math:`\sqrt{5} \approx \frac{9}{4}` (since :math:`(\frac{9}{4})^2 = \frac{81}{16} = 5\frac{1}{16}`), Hero derives :math:`\frac{BA}{A\Gamma} \approx \frac{5}{4}`, whence :math:`\frac{B\Gamma}{A\Gamma} \approx \frac{3}{4}` (a :math:`3\text{-}4\text{-}5` triangle approximation to the :math:`36^\circ\text{-}54^\circ\text{-}90^\circ` triangle!) and obtains the rational pentagon formula :math:`A_5 \approx \frac{5}{3}a^2` (or more closely :math:`\frac{12}{7}a^2 = 171\frac{3}{7}` vs. exact :math:`\frac{\sqrt{25 + 10\sqrt{5}}}{4}a^2 \approx 172.0477`).

.. folio:: Schöne 56
   :page: 56

**Summary of Regular Polygons in Props. I.17–I.25 (Schöne pp. 46–66)**:

.. list-table:: Exact Algebraic Multipliers vs. Hero's Rational Polygon Ratios
   :widths: 12 22 34 18 14
   :header-rows: 1

   * - Prop.
     - Polygon (:math:`n`)
     - Exact Ratio :math:`A_n / a^2`
     - Hero's Ratio
     - Rel. Error
   * - **I.17**
     - Equilateral (:math:`3`)
     - :math:`\frac{\sqrt{3}}{4} \approx 0.43301`
     - :math:`\frac{13}{30} \approx 0.43333`
     - :math:`+0.074\%`
   * - **I.18**
     - Pentagon (:math:`5`)
     - :math:`\frac{\sqrt{25+10\sqrt{5}}}{4} \approx 1.72048`
     - :math:`\frac{12}{7} \approx 1.71429` (alt. :math:`\frac{5}{3}`)
     - :math:`-0.360\%`
   * - **I.19**
     - Hexagon (:math:`6`)
     - :math:`\frac{3\sqrt{3}}{2} \approx 2.59808`
     - :math:`\frac{13}{5} = 2.60000`
     - :math:`+0.074\%`
   * - **I.20**
     - Heptagon (:math:`7`)
     - :math:`\frac{7}{4}\cot\frac{\pi}{7} \approx 3.63391`
     - :math:`\frac{43}{12} \approx 3.58333` (via :math:`a \approx r_{\text{hex}}\frac{\sqrt{3}}{2}`)
     - :math:`-1.392\%`
   * - **I.21**
     - Octagon (:math:`8`)
     - :math:`2(1 + \sqrt{2}) \approx 4.82843`
     - :math:`\frac{29}{6} \approx 4.83333` (via :math:`\sqrt{2} \approx \frac{17}{12}`)
     - :math:`+0.102\%`
   * - **I.22**
     - Enneagon (:math:`9`)
     - :math:`\frac{9}{4}\cot\frac{\pi}{9} \approx 6.18182`
     - :math:`\frac{51}{8} = 6.375` (*chord table*)
     - :math:`+3.125\%`
   * - **I.23**
     - Decagon (:math:`10`)
     - :math:`\frac{5}{2}\sqrt{5+2\sqrt{5}} \approx 7.69421`
     - :math:`\frac{15}{2} = 7.500` (via :math:`\mathbb{Q}(\phi)`)
     - :math:`-2.524\%`
   * - **I.24**
     - Hendecagon (:math:`11`)
     - :math:`\frac{11}{4}\cot\frac{\pi}{11} \approx 9.36564`
     - :math:`\frac{66}{7} \approx 9.42857` (*chord table*)
     - :math:`+0.672\%`
   * - **I.25**
     - Dodecagon (:math:`12`)
     - :math:`3(2 + \sqrt{3}) \approx 11.19615`
     - :math:`\frac{45}{4} = 11.250` (via :math:`\sqrt{3} \approx \frac{7}{4}`)
     - :math:`+0.481\%`

Notably, for the non-constructible **regular enneagon (Prop. I.22, 9-gon)** and **regular hendecagon (Prop. I.24, 11-gon)**, Hero explicitly appeals to *"the treatises on chords in a circle"* (*ἐκ τῶν περὶ τῶν ἐν κύκλῳ εὐθειῶν*)—providing vital historical testimony to pre-Ptolemaic Hellenistic chord tables descending from :person:`Hipparchus <hipparchus>`.

.. _sec-metrica-i-26-33:

Props. I.26–I.33: Circles, Archimedes' Plinthides, Annuli & Circular Segments
-----------------------------------------------------------------------------

.. folio:: Schöne 66
   :page: 66

- **Proposition I.26 (Circle, Lost Archimedean Bounds & Concentric Annulus, Schöne pp. 66–70)**: Hero cites :person:`Archimedes' <archimedes>` :cite:`Measurement of a Circle <archimedes:circle>`: the circumference of a circle exceeds thrice its diameter by less than :math:`\frac{1}{7}` and more than :math:`\frac{10}{71}` (:math:`3\frac{10}{71} < \pi < 3\frac{1}{7}`), and the circle's area equals the right triangle of legs :math:`r` and :math:`C`, giving :math:`A_{\text{circle}} \approx \frac{11}{14} d^2`. Crucially, Hero adds a unique citation of Archimedes' otherwise lost treatise :cite:`On Plinthides and Cylinders <archimedes:plinthides>` (*Περὶ πλινθίδων καὶ κυλίνδρων*), recording finer bounds equivalent to:

  .. math::

     \frac{211875}{67441} < \pi < \frac{197888}{62351} \quad \text{(with } \frac{211875}{67441} \approx 3.141635\text{)}.

  Hero then measures the concentric circular ring (:term:`annulus <itys>`, *ἴτυς*) between outer diameter :math:`D_1` and inner diameter :math:`D_2` of breadth :math:`w = \frac{D_1 - D_2}{2}` by the difference-of-squares identity (:just:`II.5`):

  .. math::

     A_{\text{itys}} = \frac{11}{14}\left(D_1^2 - D_2^2\right) = \frac{11}{14} \cdot 4w(D_2 + w).

- **Proposition I.27 (Infinite Geometric Progression in Ratio 4 : 1, Schöne pp. 70–72)**: As preparation for Archimedes' quadrature of the parabola and exhaustion bounds on circular segments, Hero proves that if :math:`A, B, C, D` are in continuous ratio :math:`4 : 1`, then:

  .. math::

     \frac{4}{3} A = A + B + C + D + \frac{1}{3} D \qquad \Longleftrightarrow \qquad \frac{A}{3} = B + C + D + \frac{D}{3}.

.. folio:: Schöne 74
   :page: 74

- **Propositions I.28–I.33 (Circular Segments, Schöne pp. 72–80)**: For a circular segment of chord (*base*) :math:`b` and sagitta (*height*) :math:`h` less than a semicircle, Hero first records the two ancient approximations :math:`\frac{b + h}{2} \cdot h` and :math:`\frac{b + h}{2} \cdot h + \frac{1}{14}\left(\frac{b}{2}\right)^2`, explains why the first fails near a semicircle while the second works well when :math:`b \le 3h`, and then proves (**Prop. I.31**) that every circular segment strictly exceeds :math:`\frac{4}{3}` of the inscribed triangle of the same base and height—comparing the inscribed triangle stack with :person:`Archimedes' <archimedes>` :cite:`Quadrature of the Parabola <archimedes:parabola>` (:math:`A_{\text{seg}} > \frac{2}{3} b h`). In **Prop. I.30**, he reconstructs the full circle's diameter from chord and sagitta via Euclid's intersecting-chords theorem (:just:`III.35`): :math:`(d - h) h = \left(\frac{b}{2}\right)^2 \implies d = h + \frac{b^2}{4h}`.

.. _sec-metrica-i-34-39:

Props. I.34–I.39: Ellipse, Parabolic Segment & Curved Surfaces
--------------------------------------------------------------

.. folio:: Schöne 80
   :page: 80

- **Proposition I.34 (Area of an Ellipse, Schöne pp. 80–82)**: Given an ellipse cut obliquely from a cylinder or cone (:cite:`Apollonius, Conics I.13 <apollonius:conics>`) with major axis :math:`2a = 16` and minor axis :math:`2b = 12`, Hero invokes :person:`Archimedes' <archimedes>` :cite:`On Conoids and Spheroids <archimedes:conoids>` (Prop. 4): the ellipse has the same area as the circle whose diameter is the geometric mean :math:`\sqrt{(2a)(2b)}` of its axes:

  .. math::

     A_{\text{ellipse}} = \pi a b \approx \frac{11}{14} (2a)(2b) = \frac{11}{14} \times 16 \times 12 = 150\frac{6}{7}.

- **Proposition I.35 (Area of a Parabolic Segment, Schöne pp. 82–84)**: Hero explicitly cites :person:`Archimedes' <archimedes>` :term:`Method <ephodikon>` (*ἐν τῷ Ἐφοδικῷ*)—prior to the 1906 rediscovery of the Archimedes Palimpsest, *Metrica* I.35, II.14, and II.15 were our principal Greek witnesses to the *Method*'s very existence!—stating that every segment bounded by a right-angled cone's section (parabola) and a straight line is :math:`\frac{4}{3}` of the triangle having the same base and equal height: :math:`A_{\text{parabola}} = \frac{4}{3} \cdot \frac{1}{2} b h = \frac{2}{3} b h`.

.. folio:: Schöne 86
   :page: 86

- **Propositions I.36–I.39 (Cylindrical, Conical & Spherical Surfaces, Schöne pp. 84–90)**: Concluding Book I's doctrine of surfaces (*ἐπιφάνειαι*), Hero establishes via :person:`Archimedes' <archimedes>` :cite:`On the Sphere and Cylinder <archimedes:sphere-cylinder>`:

  - **Prop. I.36 (Right Cylinder Lateral Surface)**: Unrolling the cylindrical mantle yields a rectangle of width equal to the height :math:`h` and length equal to the base circumference :math:`\pi d`, so :math:`S_{\text{cyl}} = \pi d h`.
  - **Prop. I.37 (Right Isosceles Cone Lateral Surface)**: Equal to :math:`\frac{1}{2} (\pi d) \ell = \pi r \ell`, where :math:`\ell` is the slant side (*πλευρά*).
  - **Prop. I.38 (Sphere Surface)**: Exactly four times its greatest circle (:cite:`Sphere and Cylinder I.33 <archimedes:sphere-cylinder>`): :math:`S_{\text{sphere}} = 4\pi r^2 = \pi d^2`.
  - **Prop. I.39 (Spherical Segment / Cap Surface)**: Equal to the circle whose radius is the chord :math:`c = \sqrt{r_{\text{base}}^2 + h^2}` drawn from the vertex (*πόλος*) of the segment to its base circumference (:cite:`Sphere and Cylinder I.42–43 <archimedes:sphere-cylinder>`): :math:`S_{\text{cap}} = \pi \left(r_{\text{base}}^2 + h^2\right) = 2\pi R h`.
