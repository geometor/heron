:order: 90
:type: apparatus

.. _heron-concordance:

Schöne / Schmidt / Hultsch & GEOMETOR Concordance
=================================================

Bidirectional scholarly concordance mapping **Hero of Alexandria's** *Metrica* (*ed.* Hermann Schöne, 1903), *Catoptrica* (*ed.* Wilhelm Schmidt & Ludwig Nix, 1900), *Dioptra* (*ed.* Schöne, 1903), and *Definitiones* (*ed.* Friedrich Hultsch, 1864 / J. L. Heiberg, 1912) across the **GEOMETOR** canon (``euclid``, ``elements``, ``proclus``, ``pappus``, ``wildberger``, ``etc``) and exact ``geometor.heron`` symbolic constructions (**24 loci**).

Overview by Codex Unit
----------------------

.. list-table::
   :header-rows: 1
   :widths: 25 22 10 43

   * - Codex Unit
     - Critical Edition Pages
     - Loci
     - Scope
   * - :doc:`Metrica I (Pref. & 1–9) <book-i-triangles/book-i-triangles-en>`
     - Schöne 1903, pp. 2–26
     - 4
     - Origins of Geometry, Orthogonal Comparison Units, Right/Isosceles/Scalene Triangles, Synthetic Incircle Proof of Δ = √(s(s−a)(s−b)(s−c)), and √720 Iteration
   * - :doc:`Metrica I (10–39) <book-i-polygons-circles/book-i-polygons-circles-en>`
     - Schöne 1903, pp. 26–90
     - 5
     - Trapezia, Regular Polygons (3-gon to 12-gon via Golden Section φ), Archimedean Circle & Annulus (Ἴτυς), Parabolic/Elliptic Sections, and Curved Surfaces
   * - :doc:`Metrica II (Pref. & 1–20) <book-ii-solids/book-ii-solids-en>`
     - Schöne 1903, pp. 90–140
     - 6
     - Eudoxus & Archimedes, Cones, Frusta, Spheres, Dionysodorus's Torus (Σπεῖρα), Cylindrical Ungula & Groin Vault (Method), Five Platonic Solids, and Bath Displacement
   * - :doc:`Metrica III (Pref. & 1–23) <book-iii-divisions/book-iii-divisions-en>`
     - Schöne 1903, pp. 140–184
     - 4
     - Proportional Distributive Justice, Dividing Triangles, Trapezia, Quadrilaterals, Polygons, Concentric Circles, Pyramids, Cones, Frusta & Spheres in Given Ratios
   * - :doc:`Definitiones · Catoptrica · Dioptra <definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-en>`
     - Hultsch pp. 7–23 · Schmidt pp. 324–372 · Schöne pp. 238–240
     - 5
     - Genetic Circle & Universal Gnomon (Def. §58), Variational Shortest-Path Law of Reflection (Catoptrica Prop. 4), and Two-Portal Mountain Tunneling (Dioptra Ch. 15)

.. _concordance-book-i-triangles:

Metrica I (Pref. & 1–9) (Schöne 1903, pp. 2–26)
-----------------------------------------------

Codex tracks: :doc:`English <book-i-triangles/book-i-triangles-en>` · :doc:`Greek (Teubner) <book-i-triangles/book-i-triangles-el>` · :doc:`Summary <book-i-triangles/book-i-triangles-summary>` · :doc:`Notes <book-i-triangles/book-i-triangles-notes>`

.. _locus-metrica-i-pref:

**Metrica I, Prooemium (Schöne pp. 2–6; fols. 67r–68r)** — :ref:`Prooemium: Egyptian Origins & Orthogonal Unit Measures <sec-metrica-i-prooemium>` · Euclid :just:`I.def.1`, :just:`I.def.22`
  Origins of geometry in Nile land-redivision; homogeneous orthogonal comparison units (linear foot/cubit, unit square, unit cube); triadic plan of the three books.

  * proclus: Prologue II (Friedlein 64.16–65.7, Eudemian Summary on Egyptian Nile origins of geometry)
  * euclid: Vol. I Introductory Note on Greek mensuration

.. _locus-metrica-i-1-7:

**Metrica I, Props. 1–7 (Schöne pp. 6–18; fols. 68r–70v)** — :ref:`Props. I.1–I.7: Rectangles, Right/Isosceles Triangles & General Altitude Projections <sec-metrica-i-1-7>` · Euclid :just:`I.41`, :just:`I.47`, :just:`II.12`, :just:`II.13`
  Area of rectangles and right/isosceles triangles; distinguishing acute vs. obtuse triangles via inner/outer projection differences (Elements II.12–13); general altitude computation without case-splitting.

  * elements: G-Index Book I.47 & Book II.12–13
  * wildberger: Cosine/Pythagoras Law in quadrances
  * Exact symbolic model: ``geometor.heron.mensuration.archimedes_quadrea``

.. _locus-metrica-i-8:

**Metrica I, Prop. 8 (Schöne pp. 18–24, Fig. 7; fols. 70v–71v)** — :ref:`Prop. I.8: Synthetic Incircle Proof of Δ = √(s(s−a)(s−b)(s−c)) <sec-metrica-i-8-proof>` · Euclid :just:`III.22`, :just:`IV.4`, :just:`VI.4`, :just:`VI.8`
  Direct area of any triangle from its three sides without an altitude: illustrated on (7, 8, 9) → √720 and synthesized on (13, 14, 15) → √7056 = 84 via incircle center H = X(1), tangent segments s−a, s−b, s−c, orthogonal bisectors, and cyclic quadrilateral CHBL.

  * etc: X(1) Incenter (H = (6, 4) on (13, 14, 15))
  * wildberger: W.07 Archimedes' Function / Quadrea A = 16Δ² = 16s(s−a)(s−b)(s−c)
  * euclid: Book IV.4 & Book II.13 Heath historical excursus on Hero's Formula
  * Exact symbolic model: ``geometor.heron.constructions.construct_heron_proof``

.. _locus-metrica-i-8-sqrt:

**Metrica I, Prop. 8b & Prop. 9 (Schöne pp. 18–20, 24–26; fols. 70v, 71v–72r)** — :ref:`Hero's Iterative Square-Root Extraction (√720 → 161/6 → 51841/1932) <sec-metrica-i-8-sqrt>` · Euclid :just:`II.4`, :just:`X.1`
  Quadratic rational iteration x_{k+1} = (x_k + N/x_k)/2 applied to N = 720 from seed x_0 = 27 (27² = 729), yielding x_1 = 26 5/6 = 161/6 (residual 1/36) and x_2 = 51841/1932 (residual 1/3732624).

  * euclid: Heath commentary on Greek root extraction & Eutocius testimony
  * Exact symbolic model: ``geometor.heron.mensuration.heron_sqrt_convergents``

.. _concordance-book-i-polygons-circles:

Metrica I (10–39) (Schöne 1903, pp. 26–90)
------------------------------------------

Codex tracks: :doc:`English <book-i-polygons-circles/book-i-polygons-circles-en>` · :doc:`Greek (Teubner) <book-i-polygons-circles/book-i-polygons-circles-el>` · :doc:`Summary <book-i-polygons-circles/book-i-polygons-circles-summary>` · :doc:`Notes <book-i-polygons-circles/book-i-polygons-circles-notes>`

.. _locus-metrica-i-10-16:

**Metrica I, Props. 10–16 (Schöne pp. 26–46; fols. 72r–76v)** — :ref:`Props. I.10–I.16: Trapezia, Rhombi & General Quadrilaterals <sec-metrica-i-10-16>` · Euclid :just:`I.34`, :just:`I.41`, :just:`I.47`
  Right, isosceles, acute, and obtuse trapezia; rhombi and rhomboids; general cyclic/non-cyclic quadrilaterals requiring a known diagonal or right angle to become determinate in area.

  * euclid: Book I.Def.22 & Heath note on Posidonius/Hero classification of quadrilaterals

.. _locus-metrica-i-18-golden:

**Metrica I, Prop. 18 & Lemma (Schöne pp. 50–52; fols. 77v–78r)** — :ref:`Prop. I.18 Lemma: Pentagon Golden Section Identity (r + h)² = 5h² <sec-metrica-i-17-25>` · Euclid :just:`II.11`, :just:`IV.11`, :just:`XIII.1`, :just:`XIII.8`
  Right triangle with 36° acute angle doubled into a 108° pentagon vertex angle cuts the base in extreme and mean ratio (φ = (1+√5)/2), proving (BA + AΓ)² = 5·AΓ² exactly over Q(φ), approximated rationally via 81 : 16 ≈ 5.

  * divine: Golden Section Q(φ) invariants
  * elements: Book IV.10–11 & Book XIII.1, XIII.8
  * Exact symbolic model: ``geometor.heron.mensuration.pentagon_golden_lemma``

.. _locus-metrica-i-17-25:

**Metrica I, Props. 17–25 (Schöne pp. 46–66; fols. 77r–81r)** — :ref:`Props. I.17–I.25: Regular Polygons from 3-gon to 12-gon <sec-metrica-i-17-25>` · Euclid :just:`IV.11`, :just:`IV.15`, :just:`XIII.9`, :just:`XIII.10`
  Systematic area ratios A_n / s² for equilateral triangle (3/16 of s⁴), pentagon (5/3 or 12/7), hexagon (27/4 of s⁴), heptagon (43/12), octagon (29/6), enneagon (51/8 via Table of Chords), decagon (15/2), hendecagon (66/7 via Table of Chords), and dodecagon (45/4).

  * elements: Regular polygon constructions (Book IV)
  * euclid: Vol. II Book IV & Vol. III Book XIII commentary
  * Exact symbolic model: ``geometor.heron.mensuration.regular_polygon_ratios``

.. _locus-metrica-i-26-itys:

**Metrica I, Prop. 26 (Schöne pp. 66–70; fols. 81r–82r)** — :ref:`Prop. I.26: Archimedean Circle Bounds, Plinthides & Concentric Annulus (Ἴτυς) <sec-metrica-i-26-33>` · Euclid :just:`II.8`, :just:`XII.2`
  Cites Archimedes' Measurement of a Circle (11 : 14 area ratio, π ≈ 22/7) and lost Plinthides and Cylinders; derives single-pass annulus formula (11/14)·4w(D₂ + w).

  * euclid: Book XII.2 & II.8 fourfold gnomon identity

.. _locus-metrica-i-27-39:

**Metrica I, Props. 27–39 (Schöne pp. 70–90; fols. 82r–86v)** — :ref:`Props. I.27–I.39: Circular/Parabolic Segments, Ellipses & Curved Surfaces <sec-metrica-i-34-39>` · Euclid :just:`XII.2`
  Geometric series A/3 = B+C+D+D/3 (I.27); ancient vs. Archimedean circular-segment formulas and exact 4/3 parabolic quadrature citing the Method (I.28–35); ellipse area πab (I.34); conical, cylindrical, and spherical surfaces (I.36–39).

  * pappus: Conic sections & Archimedean surface mensuration

.. _concordance-book-ii-solids:

Metrica II (Pref. & 1–20) (Schöne 1903, pp. 90–140)
---------------------------------------------------

Codex tracks: :doc:`English <book-ii-solids/book-ii-solids-en>` · :doc:`Greek (Teubner) <book-ii-solids/book-ii-solids-el>` · :doc:`Summary <book-ii-solids/book-ii-solids-summary>` · :doc:`Notes <book-ii-solids/book-ii-solids-notes>`

.. _locus-metrica-ii-1-10:

**Metrica II, Prooemium & Props. 1–10 (Schöne pp. 90–120; fols. 87r–94r)** — :ref:`Preface & Props. II.1–II.10: Eudoxus, Cones, Oblique Cylinders, Prisms & Frusta <sec-metrica-ii-1-10>` · Euclid :just:`XII.7`, :just:`XII.10`
  Historical credit to Eudoxus and Archimedes; oblique cylinders and cones; obelisk/hip-roof wedge decomposition (II.8); pyramidal and conical frustum mean-plus-third-difference identity ((a+b)/2)² + (1/3)((a−b)/2)² = (a²+ab+b²)/3.

  * euclid: Vol. III Book XII.7 & XII.10 commentary on Eudoxus's exhaustion
  * Exact symbolic model: ``geometor.heron.mensuration.verify_frustum_mean_identity``

.. _locus-metrica-ii-11-12:

**Metrica II, Props. 11–12 (Schöne pp. 120–126; fols. 94r–95v)** — :ref:`Props. II.11–II.12: Spheres, Spherical Segments, Vaulted Basins & Apse Niches <sec-metrica-ii-11-15>` · Euclid :just:`XII.18`
  Sphere volume (11/21)d³ from Archimedes On the Sphere and Cylinder I.34; spherical segments, basins (λουτῆρες), shells (κόγχαι), and vaults (καμάραι).

  * euclid: Book XII.18 sphere-cubed proportionality

.. _locus-metrica-ii-13-torus:

**Metrica II, Prop. 13 (Schöne pp. 126–130; fols. 95v–96r)** — :ref:`Prop. II.13: Dionysodorus's Torus Theorem (Σπεῖρα) & Unrolled Centroid Cylinder <sec-metrica-ii-11-15>` · Euclid :just:`XI.def.14`, :just:`XII.14`
  Kinematic generation of the torus; Dionysodorus's theorem V = 2π²Rr² illustrated on outer diameter 40, tube diameter 12 (R=14, r=6 → 9956 4/7); second proof unrolling the torus along centroid circle circumference 2πR = 88 into a right cylinder, anticipating Pappus's Centroid Theorem.

  * pappus: Synagoge Book VII.42 Pappus–Guldin Centroid Theorem
  * Exact symbolic model: ``geometor.heron.mensuration.dionysodorus_torus_volume``

.. _locus-metrica-ii-14-15-method:

**Metrica II, Props. 14–15 (Schöne pp. 130–132; fols. 96v–97r)** — :ref:`Props. II.14–II.15: Cylindrical Ungula & Bicylinder Groin Vault (Archimedes' Method) <sec-metrica-ii-11-15>` · Euclid :just:`XII.10`
  Preserves Archimedes' Method Props. 12–15: cylindrical hoof V = (1/6)d²h and intersecting perpendicular cylinders V = (2/3)d³ applied to four-way vaulted fountains and Roman-Alexandrian baths.

  * euclid: Heath History II.332 on Hero & the 1906 Archimedes Palimpsest

.. _locus-metrica-ii-16-19-platonic:

**Metrica II, Props. 16–19 (Schöne pp. 132–138; fols. 97r–98v)** — :ref:`Props. II.16–II.19: Volumes of the Five Platonic Solids <sec-metrica-ii-16-20>` · Euclid :just:`XIII.13`, :just:`XIII.14`, :just:`XIII.15`, :just:`XIII.16`, :just:`XIII.17`, :just:`XIII.18`
  Cube (a³), regular tetrahedron (a³√2/12, edge 12), octahedron (a³√2/3, edge 7), icosahedron (5(3+√5)a³/12 via inradius ratio 93:127, edge 10), and dodecahedron ((15+7√5)a³/4 via inradius ratio 9:8, edge 10).

  * elements: Book XIII Platonic Solids
  * pacioli: De Divina Proportione polyhedral proportions in Q(φ)
  * Exact symbolic model: ``geometor.heron.mensuration.platonic_solid_volumes``

.. _locus-metrica-ii-20-displacement:

**Metrica II, Prop. 20 (Schöne pp. 138–140; fols. 98v–99r)** — :ref:`Prop. II.20: Irregular Solids by Hydrostatic Displacement & Wax/Clay Encasing <sec-metrica-ii-16-20>` · Euclid :just:`XI.31`
  Measuring gnarled roots, rough stones, or statues via Archimedean water displacement in a rectangular prism tank, or encasing immovable sculptures in a rectangular block of wax/clay.

  * aristotle: Physical vs. intelligible magnitude

.. _concordance-book-iii-divisions:

Metrica III (Pref. & 1–23) (Schöne 1903, pp. 140–184)
-----------------------------------------------------

Codex tracks: :doc:`English <book-iii-divisions/book-iii-divisions-en>` · :doc:`Greek (Teubner) <book-iii-divisions/book-iii-divisions-el>` · :doc:`Summary <book-iii-divisions/book-iii-divisions-summary>` · :doc:`Notes <book-iii-divisions/book-iii-divisions-notes>`

.. _locus-metrica-iii-pref:

**Metrica III, Prooemium (Schöne pp. 140–142; fols. 99v–100r)** — :ref:`Prooemium: Geometric Proportion & Distributive Justice <sec-metrica-iii-prooemium>` · Euclid :just:`V.def.6`
  Philosophical manifesto echoing Plato (Laws VI 757b) and Aristotle (Nicomachean Ethics V.3): geometry alone guarantees exact proportional division without exceeding or falling short by a single millet-seed (κέγχρον μίαν).

  * aristotle: Posterior Analytics & proportional equality
  * proclus: Prologue I on mathematical proportion in civic order

.. _locus-metrica-iii-1-3:

**Metrica III, Props. 1–3 (Schöne pp. 142–148, Fig. 61; fols. 100r–101v)** — :ref:`Props. III.1–III.3: Dividing Triangles in a Given Ratio (Vertex, Parallel, Boundary Point) <sec-metrica-iii-1-3>` · Euclid :just:`VI.1`, :just:`VI.2`, :just:`VI.13`, :just:`VI.19`
  Dividing the (13, 14, 15) triangle of area 84: (III.1) from vertex A in ratio 5 : 3 (CD = 5 1/4, BD = 8 3/4); (III.2) parallel to base BC in ratio 3 : 1 via AD² = (3/4)·169 = 126 3/4 (AD = 13√3/2); (III.3) from an arbitrary point on a side.

  * elements: Book VI.1, VI.13 (mean proportional), VI.19 (duplicate ratio of similar triangles)
  * Exact symbolic model: ``geometor.heron.constructions.construct_area_division``

.. _locus-metrica-iii-4-19:

**Metrica III, Props. 4–19 (Schöne pp. 148–174; fols. 101v–106r)** — :ref:`Props. III.4–III.19: Dividing Trapezia, Quadrilaterals, Polygons, Circles & Exterior-Point Cuts <sec-metrica-iii-4-19>` · Euclid :just:`I.37`, :just:`VI.19`, :just:`XII.2`
  Parallel, vertex, interior-point, and exterior-point area divisions of trapezia, arbitrary quadrilaterals (via auxiliary area-preserving triangles), concentric circles (III.9), circular segments, and general polygons.

  * euclid: Lost On Divisions of Figures reconstruction (Heath Vol. I)

.. _locus-metrica-iii-20-23:

**Metrica III, Props. 20–23 (Schöne pp. 174–184; fols. 106r–107v)** — :ref:`Props. III.20–III.23: Stereometric Division of Pyramids, Cones, Frusta, Spheres & Cube Root Iteration <sec-metrica-iii-20-23>` · Euclid :just:`XII.8`, :just:`XII.12`
  Cutting pyramids, cones, and frusta parallel to the base in a given volume ratio via cube-root extraction (III.20 yields Hero's famous cube-root algorithm on ∛100 ≈ 4 9/14); dividing a sphere in ratio m : n via Archimedes On the Sphere and Cylinder II.4 cubic.

  * euclid: Heath History II.341–343 on Hero's cube-root extraction of 100

.. _concordance-definitiones-catoptrica-dioptra:

Definitiones · Catoptrica · Dioptra (Hultsch pp. 7–23 · Schmidt pp. 324–372 · Schöne pp. 238–240)
-------------------------------------------------------------------------------------------------

Codex tracks: :doc:`English <definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-en>` · :doc:`Greek (Teubner) <definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-el>` · :doc:`Summary <definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-summary>` · :doc:`Notes <definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-notes>`

.. _locus-def-1-27:

**Definitiones §§1–4, §27 [Hultsch §§1–5, §29] (pp. 7–8, 15)** — :ref:`Definitiones §§1–4 & §27: Point, Flowing Line, Axial Straight Line & Genetic Circle <sec-definitiones>` · Euclid :just:`I.def.1`, :just:`I.def.2`, :just:`I.def.4`, :just:`I.def.15`, :just:`I.post.3`
  Supplements Euclid's static definitions with kinematic generation: line from the flux of a point; straight line as shortest path and invariant axis under rotation between fixed poles; genetic compass circle swept by a rotating finite segment.

  * proclus: Definitions Commentary (Friedlein 97–110, 184–187)
  * hilbert: Axioms of Incidence & Congruence

.. _locus-def-58-gnomon:

**Definitiones §58 & §67 [Hultsch §59 & §68] (pp. 21–22)** — :ref:`Definitiones §58: The Universal Heronian Gnomon (Καθόλου Γνώμων) <sec-definitiones-gnomon>` · Euclid :just:`II.def.2`, :just:`II.11`, :just:`VI.def.1`
  Hero's celebrated universal definition: 'A gnomon is anything which, when added to anything whatever, number or figure, makes the whole similar to that to which it was added' — realized continuously in Q(φ) by the Golden Rectangle and Golden Triangle.

  * divine: Golden gnomon & recursive self-similarity in Q(φ)
  * phyllotaxis: Gnomonic botanical growth
  * Exact symbolic model: ``geometor.heron.constructions.construct_heronian_gnomon``

.. _locus-proclus-hero-postulates:

**Proclus In Euclidem pp. 196, 305, 323–326, 340–346 Friedlein** — :ref:`Hero's Economy of Postulates & Direct Proofs without Reductio <sec-definitiones-gnomon>` · Euclid :just:`I.post.1`, :just:`I.post.2`, :just:`I.post.3`, :just:`I.19`, :just:`I.20`, :just:`I.25`
  Testimonies preserved in Proclus showing Hero's axiomatic program: reducing Euclid's five postulates to three constructive postulates, proving Prop. I.19–20 and I.25 directly without reductio ad absurdum.

  * proclus: Postulates & Axioms (Friedlein 196.15–21) and Props. I.16–32 (Friedlein 305, 323, 340)

.. _locus-catoptrica-4:

**Catoptrica Prop. 4 / Greek Fragment (Schmidt pp. 324–329, 368–372, Fig. 92)** — :ref:`Catoptrica Prop. 4: Variational Shortest-Path Proof of the Law of Reflection <sec-catoptrica-reflection>` · Euclid :just:`I.4`, :just:`I.14`, :just:`I.15`, :just:`I.20`
  First variational extremum principle in mathematical physics: reflecting target Δ across mirror AB to K unfolds equal-angle path ΓΕ + ΕΔ into straight segment ΓΕΚ, strictly shorter than any unequal-angle path ΓΖ + ΖΔ = ΓΖ + ΖΚ by the triangle inequality (Elements I.20).

  * elements: Book I.4, I.15, I.20
  * wildberger: Equal line spreads s(AB, CE) = s(AB, ED)
  * Exact symbolic model: ``geometor.heron.constructions.construct_catoptrica_reflection``

.. _locus-dioptra-15:

**Dioptra Ch. 15 (Schöne pp. 238–240, Fig. 95; fols. 69v–70r)** — :ref:`Dioptra Ch. 15: Tunneling a Mountain Straight Through from Both Portals <sec-dioptra-tunnel>` · Euclid :just:`I.29`, :just:`I.34`, :just:`I.47`, :just:`VI.4`
  Reconstructs Eupalinian two-portal tunneling by traversing orthogonal dioptra stations BE, EZ, ZH, HΘ, ΘM, MD around the mountain base, summing signed Cartesian displacements (BN, DN), and erecting similar exterior sighting triangles BXO and DQP.

  * elements: Book VI.4 similar right triangles
  * Exact symbolic model: ``geometor.heron.constructions.construct_dioptra_tunnel``
