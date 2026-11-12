==============
geometor-heron
==============

**Hero of Alexandria's Metrica, Definitiones, Catoptrica & Dioptra — 4-Track Bilingual Book Codex & Exact Symbolic Constructions**

``geometor-heron`` brings together a scholarly Digital Scriptorium **4-Track Bilingual Book Codex** (``English`` · ``Greek (Teubner)`` · ``Summary`` · ``Notes``) of **Hero (Heron) of Alexandria** (*fl.* c. 60 CE) with **100% exact symbolic Python constructions** built on `SymPy <https://www.sympy.org/>`__ and ``geometor.model``.

Highlights
==========

1. **4-Track Bilingual Book Codex** (``docsrc/metrica/``):

   - **Unit I — Metrica Book I (Preface & Props. 1–9)**: Egyptian origins of geometry, orthogonal unit measures, Hero's synthetic incircle & cyclic-quadrilateral proof of :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}`, and iterative rational square-root extraction on :math:`\sqrt{720} \to \frac{161}{6} \to \frac{51841}{1932}` (*ed.* H. Schöne, Teubner 1903, pp. 2–26).
   - **Unit II — Metrica Book I (Props. 10–39)**: Trapezia, regular polygons (:math:`3`-gon through :math:`12`-gon), the **Prop. I.18 Pentagon Golden Section Lemma** :math:`(BA + A\Gamma)^2 = 5 A\Gamma^2` over :math:`\mathbb{Q}(\phi)`, Archimedes' lost *Plinthides and Cylinders*, circular & parabolic segments citing Archimedes' *Method*, ellipse area :math:`\pi ab`, and curved surfaces (*Schöne* pp. 26–90).
   - **Unit III — Metrica Book II (Preface & Props. 1–20)**: Eudoxus & Archimedes in stereometry, frusta & hip-roof wedges (*bomiskoi*), **Dionysodorus's Torus Theorem** (:math:`V = 2\pi^2 R r^2` & Hero's unrolled centroid cylinder :math:`9956\frac{4}{7}`), Archimedes' *Method* cylindrical ungula & bicylinder groin vault, the **Five Platonic Solids**, and irregular solid hydrostatic displacement (*Schöne* pp. 90–140).
   - **Unit IV — Metrica Book III (Preface & Props. 1–23)**: Distributive justice & geometric proportion (*"not exceeding or falling short by a single millet-seed"*), Euclidean planar divisions, exterior-point cuts, solid divisions, and **Hero's cube-root extraction** :math:`\sqrt[3]{100} \approx 4\frac{9}{14}` (*Schöne* pp. 140–184).
   - **Unit V — Definitiones, Catoptrica & Dioptra**: Genetic definitions & **Definition 58 (Universal Gnomon)** (*ed.* Hultsch 1864 / Heiberg 1912), **Variational Shortest-Path Proof of the Law of Reflection** (*Catoptrica* Prop. 4, *ed.* Schmidt 1900, pp. 368–372), and **Two-Portal Mountain Tunneling** (*Dioptra* Ch. 15, *ed.* Schöne 1903, pp. 238–240).

2. **Exact Symbolic Python Package & Standalone Demos** (``src/geometor/heron/``, ``demos/``):

   - Zero-float ``geometor.model`` compass-and-straightedge theorem builders verified with Rational Trigonometry invariants (`quadrance`, `line_spread`, `cross_ratio`, `archimedes_quadrea`).
   - Interactive ``.euclid-graphic`` SVG figures instrumented for ``photon-platform/publish``.

Quick Start
===========

.. code-block:: bash

   # Run test suite & linter
   ruff check src demos tests
   pytest -v

   # Run standalone Rich CLI demonstrations
   python demos/heron_formula_proof.py
   python demos/sqrt_720_iteration.py
   python demos/catoptrica_shortest_path.py
   python demos/area_division_book_iii.py
   python demos/golden_gnomon.py

   # Build the Book Codex HTML documentation
   publish build

License
=======

MIT License — Copyright (c) 2026 phi ARCHITECT / GEOMETOR.
