:navigation: header
:order: 5

.. _heron-mission:

==============================================================
Mission: Bridging Classical Deduction and Exact Mensuration
==============================================================

Within the twenty-seven repositories of the **GEOMETOR** ecosystem, **Hero of Alexandria** (*fl.* c. 60 CE; astronomical lunar eclipse benchmark fixed by :person:`Otto Neugebauer <neugebauer>` to 13 March 62 CE) occupies a singular architectural crossroads. Where :person:`Euclid <euclid>` establishes synthetic congruence and proportion without numerical magnitudes, and :person:`Archimedes <archimedes>` ascends to exhaustion proofs on curved surfaces and solids, Hero unifies **rigorous Euclidean–Archimedean synthetic proof** with **computable rational mensuration, variational physics, and field geodesy**.

Four Pillars of the Heronian Synthesis
--------------------------------------

1. **Orthogonal Measure & Algebraic Invariance (*Metrica* Books I–II)**:
   In the preface to *Metrica* Book I, Hero grounds all measurement in homogeneous orthogonal units—the unit square for plane surfaces and the unit cube for solids—reducing arbitrary oblique triangles, polygons, conic segments, tori, groin vaults, and Platonic polyhedra to invariant algebraic relations on linear chords and edges. His celebrated proof of :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}` (*Metrica* I.8) is pure synthetic geometry (:just:`Elements III.17 <III.17>`, :just:`III.22 <III.22>`, :just:`IV.4 <IV.4>`, :just:`VI.8 <VI.8>`), yet its computational realization anticipates :person:`Norman J. Wildberger's <wildberger>` polynomial :term:`quadrea` :math:`\mathcal{A} = (Q_a + Q_b + Q_c)^2 - 2(Q_a^2 + Q_b^2 + Q_c^2) = 16\Delta^2`.

2. **Convergent Rational Approximation Over Exact Symbolic Fields**:
   Whenever a geometric magnitude falls in a quadratic or cubic extension—such as :math:`\sqrt{720}` in *Metrica* I.8, the golden pentagon ratio :math:`\phi = \frac{1+\sqrt{5}}{2}` in *Metrica* I.18, or :math:`\sqrt[3]{100}` in *Metrica* III.20—Hero pairs an exact synthetic theorem with an explicit iterative rational algorithm over :math:`\mathbb{Q}`. In ``geometor.heron``, both layers are preserved side by side: exact algebraic coordinates in :math:`\mathbb{Q}(\sqrt{d})` and :math:`\mathbb{Q}(\phi)`, and exact ``sympy.Rational`` convergent streams.

3. **Proportional Distributive Justice (*Metrica* Book III)**:
   Echoing :person:`Plato <plato>` and :person:`Aristotle <aristotle>`, Hero opens *Metrica* Book III by declaring that **Nature herself distributes estates according to merit through geometric proportion** (*ἀναλογία*), leaving no share exceeding or falling short *"even by a single millet-seed."* Every division problem reduces area and volume ratios to Euclidean mean proportionals and projective cuts.

4. **Variational Principle & Geodetic Sightlines (*Catoptrica* & *Dioptra*)**:
   In *Catoptrica* Prop. 4 (preserved in Greek by :person:`Olympiodorus <olympiodorus>`), Hero formulates the **earliest variational extremum proof in mathematical physics**, deriving the equality of angles of incidence and reflection from the axiom that visual rays travel along the **shortest unbent path**—the ancestor of Fermat's Principle of Least Time and Euler–Lagrange mechanics. In *Dioptra* Ch. 15, he converts the opaque interior of a mountain into a computable right triangle via orthogonal perimeter traverses, guiding two tunneling crews from opposite hillsides to meet underground—the Hellenistic engineering heritage behind :person:`Eupalinus's <eupalinus>` Samian tunnel.

Strict Content / Code Separation
--------------------------------

In fidelity to the GEOMETOR Digital Scriptorium standard:

- ``docsrc/metrica/`` (`:layout: book`) contains **zero embedded Python scripts**, preserving clean bilingual historical editions, scan-verified Teubner/Hultsch Greek texts, interactive ``.euclid-graphic`` SVGs, and apparatus registries (:doc:`Concordance </metrica/concordance>`, :doc:`Bibliography </metrica/bibliography>`, :doc:`Persons </metrica/persons>`, :doc:`Glossary </metrica/glossary>`).
- ``src/geometor/heron/``, ``demos/``, and ``docsrc/demos/`` house **100% exact symbolic SymPy & ``geometor.model`` constructions**, verified by automated ``pytest`` suites and bidirectionally linked from every Codex commentary track.
