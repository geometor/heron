:order: 40
:type: chapter
:canonical_id: book-iii-divisions
:folio: Schöne 140–184
:book: Metrica Book III (Pref. & Props. 1–23)

.. _unit-book-iii-divisions-en:

Metrica Book III (Preface & Props. 1–23): Proportional Divisions of Figures, Justice & ∛100
===========================================================================================

*Geometric Proportion & Distributive Justice ("Not By a Single Millet-Seed"), Dividing Triangles & Quadrilaterals, Euclid's On Divisions, Exterior-Point Cuts, Solid Divisions, and Hero's Cube-Root Algorithm* — **Schöne (1903), pp. 140–184** · *Codex Constantinopolitanus Palatii Veteris 1, fols. 99v–107v*

.. note::

   **Edition Track (English)**: Original GEOMETOR scholarly translation and synthesis directly from :person:`Hermann Schöne's <schoene>` :cite:`1903 Teubner editio princeps <schoene:1903>` (pp. 140–184), verified against 300 DPI archival page scans. Hover or click any highlighted geometric symbol (such as :g:`ABC <g1:< A B C >>`, :g:`ADE <g1:< A D E >>`, :g:`DECB <g1:< D B C E >>`, or :g:`AV <g1:/ A V />`) to illuminate the corresponding element in the interactive diagram. Switch tracks above for **Greek (Teubner)**, **Summary**, or **Notes**.

.. _sec-metrica-iii-prooemium:

Prooemium: Geometric Proportion, Distributive Justice & the Millet-Seed
-----------------------------------------------------------------------

.. folio:: Schöne 140
   :page: 140

**Book III, Prooemium (Schöne pp. 140–142; fol. 99v)**:

   *"We consider the divisions of land-parcels not far removed from the measurements performed upon them. For indeed to apportion an equal region to equals, and a greater share to the worthy according to :term:`proportion <analogia>`, is judged altogether serviceable and necessary. The whole habitable earth itself has been divided by Nature herself according to merit...*

   *And if anyone should wish to divide regions according to a given ratio, so that—so to speak—not even a single millet-seed (*κέγχρον μίαν*) exceeds or falls short of the proportion of the given ratio, he will have need of geometry alone: wherein superposition (*ἐφαρμογή*) yields equality, proportion (*ἀναλογία*) yields justice (*δικαιοσύνη*), and the demonstration concerning these things is indisputable—something that none of the other arts or sciences promises."*

Echoing :person:`Plato <plato>` (*Gorgias* 508a, *Laws* VI.757b) and :person:`Aristotle <aristotle>` (*Nicomachean Ethics* V.3, 1131a–b), :person:`Hero <hero>` elevates land-division from cadastral craft to philosophical exemplar: arithmetic equality superposes congruent magnitudes, geometric proportion distributes shares in exact ratio, and apodictic demonstration silences dispute.

.. _sec-metrica-iii-1-3:

Props. III.1–III.3: Dividing Triangles from a Vertex, Parallel to a Base & From a Side Point
--------------------------------------------------------------------------------------------

.. folio:: Schöne 142
   :page: 142

*(Diagram Mapping: Both **Proposition III.1** and **Proposition III.2** act upon Hero's canonical `(13, 14, 15)` triangle* :g:`ABC <g1:< A B C >>` *of area* :math:`84` *with* :g:`A <g1:A>` = :math:`(5, 12)`, :g:`B <g1:B>` = :math:`(0, 0)`, :g:`C <g1:C>` = :math:`(14, 0)` *).*

.. picture:: /_static/figures/metrica-iii-area-division.svg
   :alt: Hero Metrica III.1 and III.2 — Vertex Division (5:3) and Parallel Mean-Proportional Division (3:1) on (13, 14, 15)

- **Proposition III.1 (Division from a Vertex in Ratio 5 : 3, Schöne p. 142; fol. 100r)**:
  *To divide a given triangular region* :g:`ABC <g1:< A B C >>` *(:math:`AB = 13, B\Gamma = 14, A\Gamma = 15`) into two triangles in a given ratio (:math:`5 : 3`) having the same vertex* :g:`A <g1:A>`.

  Let the dividing cevian be :g:`AV <g1:/ A V />` (Hero's :math:`A\Delta`). Because triangles :math:`ABV` and :math:`AV\Gamma` share the same altitude from :g:`A <g1:A>`, their areas have the same ratio as their bases (:just:`VI.1`):

  .. math::

     \frac{\text{Area}(\triangle ABV)}{\text{Area}(\triangle AV\Gamma)} = \frac{BV}{V\Gamma} = \frac{5}{3}.

  *Componendo* (:just:`V.18`), :math:`B\Gamma : V\Gamma = (5 + 3) : 3 = 8 : 3`. Since :math:`B\Gamma = 14` is given, :math:`V\Gamma = \frac{3}{8} \times 14 = \frac{21}{4} = 5\frac{1}{4}` and :math:`BV = \frac{5}{8} \times 14 = \frac{35}{4} = 8\frac{3}{4}`, partitioning the total area :math:`84` into exact rational shares :math:`52\frac{1}{2}` and :math:`31\frac{1}{2}`.

.. folio:: Schöne 144
   :page: 144

- **Proposition III.2 (Division by a Line Parallel to the Base in Ratio 3 : 1, Schöne pp. 142–144; fol. 100v)**:
  *To divide the given triangle* :g:`ABC <g1:< A B C >>` *into two regions—an upper triangle* :g:`ADE <g1:< A D E >>` *and a lower trapezium* :g:`DECB <g1:< D B C E >>` *—in the given ratio :math:`m : n = 3 : 1` by a straight line* :g:`DE <g1:/ D E />` *parallel to base* :g:`BC <g1:[ B C ]>`.

  1. *Analysis*: Since :g:`DE <g1:/ D E />` is parallel to :g:`BC <g1:[ B C ]>`, triangle :g:`ADE <g1:< A D E >>` is equiangular and similar to :g:`ABC <g1:< A B C >>` (:just:`I.29`, :just:`VI.4`). When the ratio of upper triangle to lower trapezium is :math:`3 : 1`, *componendo* the ratio of the whole triangle :g:`ABC <g1:< A B C >>` to :g:`ADE <g1:< A D E >>` is :math:`(3 + 1) : 3 = 4 : 3`.
  2. By **Euclid's *Elements* VI.19**, similar triangles are to one another in the **duplicate ratio** of their homologous sides:

     .. math::

        \frac{\text{Area}(\triangle AB\Gamma)}{\text{Area}(\triangle A\Delta E)} = \frac{AB^2}{A\Delta^2} = \frac{4}{3}.

  3. *Geometric Mean-Proportional Construction*: Mark :g:`P <g1:P>` on :g:`AB <g1:[ A B ]>` so that :math:`AP = \frac{3}{4} AB`, describe the semicircle on diameter :g:`AB <g1:[ A B ]>`, erect the perpendicular :g:`PR <g1:/ P R />` to meet the semicircle at :g:`R <g1:R>`, and transfer radius :math:`AR` via circle :g:`(AR) <g1:( A R )>` back onto :g:`AB <g1:[ A B ]>` at :g:`D <g1:D>` (:just:`VI.13`), drawing :g:`DE <g1:/ D E />` parallel to :g:`BC <g1:[ B C ]>`.
  4. *Synthesis on (13, 14, 15)*: Since :math:`AB^2 = 13^2 = 169`, the :term:`quadrance` of :math:`A\Delta` is exact over :math:`\mathbb{Q}`:

     .. math::

        A\Delta^2 = \frac{3}{4} \times 169 = \frac{507}{4} = 126\frac{3}{4}, \qquad A\Delta = \frac{13\sqrt{3}}{2} \approx 11\frac{1}{4},

     partitioning the area :math:`84` into :math:`\text{Area}(\triangle ADE) = 63` and :math:`\text{Area}(DECB) = 21` (:math:`63 : 21 = 3 : 1` with zero error!).

- **Proposition III.3 (Division from an Arbitrary Point on a Side, Schöne pp. 144–146)**: Given a point :math:`\Delta` anywhere on side :math:`AB`, to cut off a fraction :math:`\frac{m}{m+n}` of :math:`\triangle AB\Gamma` by a line :math:`\Delta E`, Hero constructs :math:`AE` from the reciprocal proportion :math:`\Delta A \cdot AE = \frac{m}{m+n} BA \cdot A\Gamma` (:just:`VI.15`), solving every boundary-point triangle cut in two compass strokes.

.. _sec-metrica-iii-4-19:

Props. III.4–III.19: Trapezia, Quadrilaterals, Annuli & Exterior-Point Cuts
---------------------------------------------------------------------------

.. folio:: Schöne 148
   :page: 148

Extending :person:`Euclid's <euclid>` treatise :cite:`On Divisions of Figures <euclid:divisions>` (*Περὶ διαιρέσεων*) to survey engineering, Hero solves sixteen increasingly intricate planar division problems:

- **Propositions III.4–III.8 (Dividing Trapezia & General Quadrilaterals, Schöne pp. 146–160)**:

  - **Prop. III.4**: Dividing a trapezium in ratio :math:`m : n` by a line through a vertex or given point on a parallel base.
  - **Prop. III.5 (Parallel Cut of a Trapezium)**: Given parallel bases :math:`a < b`, a cut :math:`x` parallel to the bases divides the trapezium in ratio :math:`m : n` when :math:`x` satisfies the weighted root-mean-square law:

    .. math::

       \frac{x^2 - a^2}{b^2 - x^2} = \frac{m}{n} \qquad \Longrightarrow \qquad x^2 = \frac{n a^2 + m b^2}{m + n}.

    Hero proves this by extending the non-parallel legs to meet at an auxiliary apex pyramid-style, reducing the trapezium to nested similar triangles (:just:`VI.19`)!

  - **Props. III.6–III.8**: Dividing arbitrary quadrilaterals from a vertex, parallel to a side, or from a given point on any side by reducing the quadrilateral to an equivalent triangle (:just:`I.37`).

.. folio:: Schöne 162
   :page: 162

- **Proposition III.9 (Dividing a Circle & Concentric Ring, Schöne pp. 160–162)**: To divide a circle of diameter :math:`d` into an inner disk and an outer :term:`annulus <itys>` in ratio :math:`m : n`, Hero applies :just:`XII.2` (circles are to one another as the squares on their diameters): :math:`d_{\text{inner}}^2 = \frac{m}{m+n} d^2`.

- **Propositions III.10–III.19 (Divisions by Lines Through Exterior Points & Polygons, Schöne pp. 162–172)**: Suppose a well, boundary stone, or road junction :math:`\Delta` lies *outside* a triangular or polygonal estate, and the surveyor must draw a straight boundary line passing through :math:`\Delta` that cuts off a prescribed fraction of the estate! In **Props. III.10–III.13**, Hero reduces this problem to **application of areas with hyperbolic/elliptic excess** (:just:`VI.28`–:just:`VI.29`, equivalent to solving a quadratic equation geometrically) and extends the method to arbitrary polygons in **Props. III.14–III.19**.

.. _sec-metrica-iii-20-23:

Props. III.20–III.23: Stereometric Divisions & Hero's Cube-Root Algorithm (∛100 ≈ 4 9/14)
-----------------------------------------------------------------------------------------

.. folio:: Schöne 174
   :page: 174

In the final four propositions of the *Metrica*, Hero ascends from two-dimensional area divisions (governed by duplicate ratios and square roots) to **three-dimensional solid divisions** (governed by triplicate ratios :just:`XII.12` and **cube roots**):

- **Proposition III.20 — Dividing a Pyramid or Cone Parallel to Its Base & Extracting :math:`\sqrt[3]{100}` (Schöne pp. 172–178; fols. 105v–106v)**:
  To cut a pyramid (or cone) of slant edge :math:`5` into ratio :math:`4 : 1` from the apex (:math:`\frac{4}{5}` upper pyramid to :math:`\frac{1}{5}` lower frustum), similar pyramids stand in the **triplicate ratio** of their homologous edges:

  .. math::

     \frac{x^3}{5^3} = \frac{4}{5} \qquad \Longrightarrow \qquad x^3 = \frac{4}{5} \times 125 = 100.

  How can one extract the **cube root of 100** (:math:`\sqrt[3]{100}`), the sole surviving cube-root algorithm in all of Greek mathematical literature? Hero gives his celebrated **weighted secant/error-interpolation rule** (Schöne p. 178):

  1. Take the nearest integer cubes **above** and **below** :math:`N = 100`: :math:`5^3 = 125` (root :math:`u = 5`) and :math:`4^3 = 64` (root :math:`\ell = 4`).
  2. Compute the upper excess :math:`e_u = 125 - 100 = 25` and the lower deficit :math:`e_\ell = 100 - 64 = 36`.
  3. Multiply the upper root by the lower deficit (:math:`u \cdot e_\ell = 5 \times 36 = 180`), and the lower root by the upper excess (or in Schöne's text :math:`\sqrt{100 \dots}` / :math:`4 \times 25`—specifically :math:`90 + \dots` or :math:`180 / (180 + 100)`): adding :math:`180` and :math:`100` (:math:`= 280`) and dividing :math:`180` by :math:`280` gives :math:`\frac{9}{14}`!
  4. Add :math:`\frac{9}{14}` to the lower root :math:`4`:

     .. math::

        x \approx 4 + \frac{9}{14} = \frac{65}{14} \approx 4.642857\dots \qquad \text{(exact } \sqrt[3]{100} \approx 4.6415888\dots\text{)},

     achieving **relative accuracy of :math:`0.027\%`** (:math:`(\frac{65}{14})^3 = \frac{274{,}625}{2744} \approx 100.082`) in a single rational step!

- **Propositions III.21–III.22 (Dividing a Conical or Pyramidal Frustum Parallel to Its Bases, Schöne pp. 178–182)**: Extending the frustum to its virtual apex reduces the frustum cut to :math:`x^3 = \frac{n a^3 + m b^3}{m + n}`, solved immediately via the cube-root method of Prop. III.20.

- **Proposition III.23 (Dividing a Sphere in a Given Ratio by a Plane, Schöne pp. 182–184; fol. 107v)**: Concluding the entire three-book treatise, Hero poses the famous cubic problem of :person:`Archimedes' <archimedes>` :cite:`Sphere and Cylinder II.4 <archimedes:sphere-cylinder>`—to cut a sphere by a plane so that its segments have a given ratio :math:`m : n`—and cites :person:`Dionysodorus's <dionysodorus>` conic-section solution via the intersection of a parabola and a rectangular hyperbola!
