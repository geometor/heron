:order: 30
:type: chapter
:canonical_id: book-ii-solids
:folio: Schöne 90–140
:book: Metrica Book II (Pref. & Props. 1–20)

.. _unit-book-ii-solids-en:

Metrica Book II (Preface & Props. 1–20): Stereometry, Dionysodorus's Torus, the Method & Platonic Solids
========================================================================================================

*Eudoxus & Archimedes in Stereometry, Frusta & Hip-Roof Wedges, Spheres & Vaults, Dionysodorus's Torus Theorem (9956 4/7), Archimedes' Method Vaults, the Five Platonic Solids, and Hydrostatic Displacement* — **Schöne (1903), pp. 90–140** · *Codex Constantinopolitanus Palatii Veteris 1, fols. 87r–99v*

.. note::

   **Edition Track (English)**: Original GEOMETOR scholarly translation and stereometric synthesis directly from :person:`Hermann Schöne's <schoene>` :cite:`1903 Teubner editio princeps <schoene:1903>` (pp. 90–140), verified against 300 DPI archival page scans. Hover or click any highlighted geometric symbol (such as :g:`(ZB) <g1:( Z B )>`, :g:`DEH2H1 <g1:< D E H2 H1 >>`, or :g:`AZ <g1:/ A Z />`) to illuminate the corresponding element in the interactive meridian diagram. Switch tracks above for **Greek (Teubner)**, **Summary**, or **Notes**.

.. _sec-metrica-ii-1-10:

Prooemium & Props. II.1–II.10: Eudoxus, Cones, Oblique Prisms, Wedges & Frusta
------------------------------------------------------------------------------

.. folio:: Schöne 90
   :page: 90

**Book II, Prooemium (Schöne pp. 90–94; fols. 87r–88r)**. Having set forth in the First Book the mensuration of planar and curved surfaces, :person:`Hero <hero>` opens the Second Book on solid bodies (*στερεὰ σώματα*) with a classic historical tribute: before :person:`Eudoxus of Cnidus <eudoxus>`, geometers did not possess rigorous proofs that every cylinder is triple the cone on the same base and of equal height (:just:`XII.10`), nor that every prism is triple the pyramid; and after Eudoxus established those theorems by exhaustion, :person:`Archimedes <archimedes>` surpassed all predecessors by proving that every sphere is two-thirds of its circumscribing cylinder (:cite:`Sphere and Cylinder I.34 <archimedes:sphere-cylinder>`).

Just as every planar area is referred to a unit square, every solid body is referred to an orthogonal **unit cube** (*στερεὸς κύβος*). Consequently, even when a cylinder, cone, or prism is **oblique** (*κεκλιμένος*), its solid content equals the product of its base area by its **perpendicular altitude** (:term:`kathetos`) dropped orthogonally to the plane of the base—never by its inclined slant edge!

.. folio:: Schöne 96
   :page: 96

- **Propositions II.1–II.5 (Cones, Oblique Cylinders, Parallelepipeds, Prisms & Pyramids, Schöne pp. 94–108)**: Hero computes right and oblique cylinders (:math:`V = A_{\text{base}} \cdot h`), cones (:math:`V = \frac{1}{3} A_{\text{base}} \cdot h`), hexagonal and polygonal prisms, and pyramids on arbitrary triangular or polygonal bases, obtaining the perpendicular altitude :math:`h` from the slant edge and circumradius (or base projection) via :just:`I.47`.

.. folio:: Schöne 110
   :page: 110

- **Propositions II.6–II.7, II.9–II.10 (Pyramidal & Conical Frusta — Hero's Mean-Plus-Third-Difference Identity, Schöne pp. 108–120)**: Rather than computing a truncated pyramid or cone (:term:`frustum <kolouros>`, *κόλουρος*) by extending it to its apex and subtracting two large pyramids, Hero transforms the classical multiplier :math:`\frac{a^2 + ab + b^2}{3}` into his signature **mean-square plus one-third half-difference-square** identity:

  .. math::

     \frac{a^2 + ab + b^2}{3} = \left(\frac{a + b}{2}\right)^2 + \frac{1}{3}\left(\frac{a - b}{2}\right)^2,

  so that for a square frustum of lower side :math:`a = 10`, upper side :math:`b = 2`, and perpendicular height :math:`h = 9` (slant edge :math:`9` or :math:`\sqrt{81 + 32}`):

  .. math::

     V_{\text{frustum}} = h \left[\left(\frac{a + b}{2}\right)^2 + \frac{1}{3}\left(\frac{a - b}{2}\right)^2\right],

  and similarly for a circular conical frustum of diameters :math:`D_1, D_2`:

  .. math::

     V_{\text{cone-frustum}} = \frac{\pi}{4} h \left[\left(\frac{D_1 + D_2}{2}\right)^2 + \frac{1}{3}\left(\frac{D_1 - D_2}{2}\right)^2\right].

  Notice the engineering insight: the naive "average cross-section" rule :math:`h\left(\frac{a+b}{2}\right)^2` underestimates the true volume by *precisely* :math:`\frac{1}{3} h \left(\frac{a-b}{2}\right)^2`!

- **Proposition II.8 (The *Βωμίσκος* / Hip-Roof Wedge / Prismatoid, Schöne pp. 114–116)**: Generalizing to a solid bounded by two parallel dissimilar rectangles :math:`(a_1 \times b_1)` and :math:`(a_2 \times b_2)` at distance :math:`h`—essential for temple altars (*βωμίσκοι*), stone lintels, and hipped roofs—Hero decomposes the solid into a central parallelepiped, two triangular prisms, and four corner pyramids, proving the exact universal prismatoid law:

  .. math::

     V_{\text{bomiskos}} = h \left[\left(\frac{a_1 + a_2}{2}\right)\left(\frac{b_1 + b_2}{2}\right) + \frac{1}{3}\left(\frac{a_1 - a_2}{2}\right)\left(\frac{b_1 - b_2}{2}\right)\right].

.. _sec-metrica-ii-11-15:

Props. II.11–II.15: Spheres, Dionysodorus's Torus (9956 4/7) & Archimedes' Method Vaults
----------------------------------------------------------------------------------------

.. folio:: Schöne 120
   :page: 120

- **Propositions II.11–II.12 (Spheres, Spherical Segments & Vaulted Basins, Schöne pp. 120–126)**: By :person:`Archimedes' <archimedes>` :cite:`Sphere and Cylinder I.34 <archimedes:sphere-cylinder>`, the sphere is :math:`\frac{2}{3}` of the circumscribing cylinder (:math:`\frac{\pi}{4} d^2 \cdot d`), giving :math:`V_{\text{sphere}} = \frac{\pi}{6} d^3 \approx \frac{11}{21} d^3`. For a spherical segment of base radius :math:`r_b` and sagitta (*height*) :math:`h` (**Prop. II.12**), Hero applies :cite:`Sphere and Cylinder II.2 <archimedes:sphere-cylinder>` to derive the intrinsic formula requiring no separate lookup of the full sphere's radius:

  .. math::

     V_{\text{seg}} = \frac{1}{2}\pi r_b^2 h + \frac{1}{6}\pi h^3 = \frac{\pi}{6} h \left(3 r_b^2 + h^2\right).

.. folio:: Schöne 126
   :page: 126

**Proposition II.13 — Dionysodorus's Torus Theorem (*Περὶ τῆς σπείρας*, Schöne pp. 126–130; fols. 95v–96r)**:

Hero next preserves our **sole surviving Greek witness** to the lost treatise :cite:`On the Torus <dionysodorus:speira>` (*Περὶ τῆς σπείρας*) by :person:`Dionysodorus of Caunus <dionysodorus>` (fl. c. 200 BCE):

   *"Let it be required to measure a torus (:term:`speira`), having first set out its generation. Let there be in a plane a straight line* :g:`AB <g1:[ A B ]>` *and two points* :g:`B <g1:B>`, :g:`C <g1:C>` *(Hero's* :math:`\Gamma` *) upon it. Let the circle* :g:`BCDE <g1:( Z B )>` *be perpendicular to the underlying plane in which* :g:`AB <g1:[ A B ]>` *lies; and while point* :g:`A <g1:A>` *remains fixed, let* :g:`AB <g1:[ A B ]>` *be carried round in the plane until it is restored to the same position, carrying round with it the circle* :g:`BCDE <g1:( Z B )>` *remaining always perpendicular to the underlying plane. Then the circumference* :g:`BCDE <g1:( Z B )>` *will generate a certain surface which they call spiric (toroidal)..."*

*(Diagram Mapping:* :g:`A <g1:A>` *= fixed center of revolution* :math:`(0,0)`; :g:`C <g1:C>` *= inner rim* :math:`\Gamma = (8,0)`; :g:`Z <g1:Z>` *= generating circle center* :math:`(14,0)`; :g:`B <g1:B>` *= outer rim* :math:`(20,0)`; :g:`D <g1:D>`, :g:`E <g1:E>` *= vertical diameter endpoints* :math:`(14, \pm 6)`; :g:`H1 <g1:H1>`, :g:`H2 <g1:H2>` *= endpoints* :math:`H, \Theta` *on the vertical axis of revolution).*

.. picture:: /_static/figures/dionysodorus-torus-section.svg
   :alt: Hero Metrica II.13 — Meridian Section of Dionysodorus's Torus (R = 14, r = 6)

1. **Dionysodorus's Proportion**: It was proved by :person:`Dionysodorus <dionysodorus>` in *On the Torus* that as the generating circle :g:`(ZB) <g1:( Z B )>` is to **half** the meridian parallelogram :g:`DEH2H1 <g1:< D E H2 H1 >>` (which has height :math:`\Delta E = 2r` and width :g:`AZ <g1:/ A Z />` :math:`= R`, so half its area is :math:`R r`), so is the torus generated by :g:`(ZB) <g1:( Z B )>` to the cylinder whose axis is :math:`H\Theta = 2r` and whose base radius is :g:`AZ <g1:/ A Z />` :math:`= R` (volume :math:`\pi R^2 \cdot 2r = 2\pi R^2 r`):

   .. math::

      \frac{V_{\text{torus}}}{2\pi R^2 r} = \frac{\pi r^2}{R r} \qquad \Longrightarrow \qquad V_{\text{torus}} = 2\pi^2 R r^2.

2. **Hero's Unrolled-Cylinder Centroid Demonstration**: Hero immediately adds a breathtaking physical-geometric alternative (*«δυνατὸν δέ ἐστι καὶ ἄλλως μετρῆσαι»*) that directly anticipates **Pappus's Centroid Theorem** (:cite:`Synagoge VII <pappus:synagoge>`):
   For :math:`AC = 8` and :math:`BC = 12` (so minor radius :g:`ZB <g1:/ Z B />` :math:`r = 6` and major radius :g:`AZ <g1:/ A Z />` :math:`R = 14`), the circle swept by center :g:`Z <g1:Z>` has diameter :math:`2R = 28` and circumference :math:`2\pi R \approx \frac{22}{7} \times 28 = 88`. *"When therefore the torus is unrolled and becomes like a cylinder"* (*ἁπλωθεῖσα ἄρα ἡ σπεῖρα καὶ γενομένη ὡς κύλινδρος*), it has length :math:`L = 88` and circular cross-section of diameter :math:`BC = 12` (area :math:`\frac{11}{14} \times 144 = \frac{792}{7}`), yielding the exact rational volume:

   .. math::

      V_{\text{torus}} = 88 \times \frac{792}{7} = \frac{69{,}696}{7} = 9956\frac{4}{7}.

.. folio:: Schöne 130
   :page: 130

- **Propositions II.14–II.15 (Archimedes' *Method* Solids: Cylindrical Ungula & Bicylinder Groin Vault, Schöne pp. 130–132; fols. 96v–97r)**: Immediately after Dionysodorus's torus, Hero cites the two celebrated final propositions of :person:`Archimedes' <archimedes>` :term:`Method <ephodikon>` (*Ἐφοδικόν*)—the very theorems whose Greek leaves were torn from or barely legible at the end of the Archimedes Palimpsest!

  - **Prop. II.14 (Cylindrical Hoof / Ungula)**: When a plane cuts a right cylinder through a diameter of its base and meets the opposite generator at height :math:`h`—useful for fluted niches and half-vaults—the cut-off wedge is exactly **one-sixth** of the circumscribing square prism (:math:`d \times d \times h`):

    .. math::

       V_{\text{ungula}} = \frac{1}{6} d^2 h = \frac{2}{3} r^2 h.

  - **Prop. II.15 (Intersection of Two Perpendicular Equal Cylinders — Groin Vault / Steinmetz Solid)**: When two equal right circular cylinders of diameter :math:`d` intersect at right angles inside a cube of edge :math:`d`—the monumental Roman cross-vault (*καμάρα*)—their common solid is **two-thirds of the cube**:

    .. math::

       V_{\text{bicylinder}} = \frac{2}{3} d^3 = \frac{16}{3} r^3.

.. _sec-metrica-ii-16-20:

Props. II.16–II.20: The Five Platonic Solids & Irregular Hydrostatic Displacement
---------------------------------------------------------------------------------

.. folio:: Schöne 132
   :page: 132

**Propositions II.16–II.19 — Volumes of the Five Regular Solids (Schöne pp. 132–138; fols. 97r–99r)**:

Turning to the five cosmic regular polyhedra of :person:`Plato <plato>`, :person:`Theaetetus <theaetetus>`, and :person:`Euclid <euclid>` (:just:`XIII.13`–:just:`XIII.17`), Hero decomposes the octahedron into two square pyramids and the icosahedron and dodecahedron into :math:`20` triangular and :math:`12` pentagonal pyramids meeting at the center of the circumscribed/inscribed sphere:

.. list-table:: Exact Symbolic Volumes of the Five Platonic Solids (Edge :math:`a`)
   :widths: 12 22 24 42
   :header-rows: 1

   * - Prop.
     - Regular Polyhedron
     - Faces
     - Exact Volume :math:`V(a)` in :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}, \phi)`
   * - *Unit*
     - **Cube** (*Κύβος*)
     - :math:`6` squares
     - :math:`a^3` *(foundational stereometric unit)*
   * - **II.16**
     - **Regular Tetrahedron** (*Πυραμίς*)
     - :math:`4` equilateral :math:`\triangle`
     - :math:`\frac{\sqrt{2}}{12} a^3` *(altitude* :math:`h = \sqrt{\frac{2}{3}} a` *)*
   * - **II.17**
     - **Regular Octahedron** (*Ὀκτάεδρον*)
     - :math:`8` equilateral :math:`\triangle`
     - :math:`\frac{\sqrt{2}}{3} a^3` *(two square pyramids of height* :math:`\frac{a}{\sqrt{2}}` *)*
   * - **II.18**
     - **Regular Icosahedron** (*Εἰκοσάεδρον*)
     - :math:`20` equilateral :math:`\triangle`
     - :math:`\frac{5(3 + \sqrt{5})}{12} a^3 = \frac{5\phi^2}{6} a^3` *(inradius via* :math:`\mathbb{Q}(\phi)` *)*
   * - **II.19**
     - **Regular Dodecahedron** (*Δωδεκάεδρον*)
     - :math:`12` regular pentagons
     - :math:`\frac{15 + 7\sqrt{5}}{4} a^3 = \frac{5\phi^3}{2(2-\phi)} a^3` *(12 pentagonal pyramids)*

Notice the exact golden-ratio duality between **II.18** and **II.19**: both depend directly upon the extreme-and-mean-ratio geometry established in Proposition I.18!

.. folio:: Schöne 138
   :page: 138

- **Proposition II.20 (Measuring Any Irregular Solid Body, Schöne pp. 138–140; fols. 99r–99v)**: Book II closes with an unforgettable synthesis of physics and geometry. How can one measure an irregular sculpted statue, rough boulder, or vessel (*ἀκανόνιστον σῶμα*) bounded by no geometric formula? Hero gives **two exact operational methods**:

  1. **Hydrostatic Immersion (*Archimedes' Bath*)**: Place a watertight rectangular parallelepiped tank horizontally, fill it with water, submerge the irregular solid completely, and measure the vertical rise (or displaced overflow) of the rectangular prism of water; its length :math:`\times` breadth :math:`\times` depth gives the irregular solid's exact volume in cubic units!
  2. **Plastic Clay/Wax Encasement**: If the body is too monumental or immovable to immerse, pack wax or potter's clay (*κηρὸς ἢ πηλός*) around it and plane the exterior flat with straightedges into a right-angled rectangular parallelepiped; measure that parallelepiped, strip off the clay and mold the clay alone into a smaller rectangular brick, and subtract the brick's volume from the whole!
