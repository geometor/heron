:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Four-Track Codex & Exact Symbolic Constructions

The GEOMETOR edition of Hero of Alexandria's :cite:`*Metrica*, *Definitiones*, *Catoptrica* & *Dioptra* <schoene:1903>` unites critical Teubner and Weidmann Greek philology with four synchronized reading tracks and zero-float symbolic geometry.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Every unit across the five codex sections provides synchronized parallel tracks accessible directly from the reading header:
   
   * **English Translation:** Direct modern English translation preserving Heronian geometric nomenclature and Euclidean deductive structure.
   * **Greek Source:** Polytonic Greek critical text transcribed from the editions of :person:`Hermann Schöne <schoene>` (1903), :person:`Wilhelm Schmidt <schmidt>` (1900), and :person:`Friedrich Hultsch <hultsch>` (1864).
   * **Summary:** Chapter summaries, formal propositions, and structural overview.
   * **GEOMETOR Notes:** Detailed commentary on Hellenistic engineering, variational optics, and Rational Trigonometry invariants.

2. Primary-Source Folio Milestones
   Marginal page markers (such as ``[p. 2]``, ``[p. 26]``, ``[p. 90]``) link directly to high-resolution scans of the 1903 Teubner edition and manuscript records (such as the 11th-century *Codex Constantinopolitanus Palatii Veteris 1*). Clicking header **Folio** badges opens the corresponding scan.

3. Interactive Diagrams & Deductive Links
   All geometric figures are rendered as scalable, theme-adaptive ``.euclid-graphic`` SVGs:
   
   * Incircle tangencies, torus cross-sections, and mountain tunneling sightlines adapt dynamically to light and dark reader modes.
   * Geometric terms link into the technical glossary (:term:`quadrea`, :term:`dioptra`, :term:`catoptrica`).
   * Deductive citations connect directly to foundational sources including :cite:`Euclid's *Elements* <euclid_elements>` and :cite:`Archimedes <archimedes>`.

4. Full-Text Search with In-Page Highlighting
   Use the sidebar search bar to query the complete Greek transcriptions, English translations, and critical apparatus. Clicking any result automatically opens the section with the search term highlighted in context.

5. Faceted Navigation & Collection Views
   Browse mathematical units, topics, and historical figures via the sidebar taxonomy. Collection pages provide **Cards**, **Banners**, and **List** layout switches.

6. People, Bibliography & Glossary Tooltips
   Hovering over any historical person (:person:`Hero of Alexandria <hero>`, :person:`Hermann Schöne <schoene>`, :person:`Archimedes <archimedes>`), citation (:cite:`schoene:1903`), or term (:term:`quadrea`, :term:`catoptrica`) surfaces rich tooltip cards.

----

Command-Line & Python Verification API
--------------------------------------

All constructions, radical approximations, and area divisions are executable locally via Python.

Running Demonstrations
~~~~~~~~~~~~~~~~~~~~~~

Run the exact symbolic demonstration scripts directly from the repository root:

.. code-block:: bash

   # Verify Heron's triangle formula on (13, 14, 15) and (7, 8, 9)
   python3 demos/heron_formula_proof.py

   # Compute exact rational sqrt(720) convergents
   python3 demos/sqrt_720_iteration.py

   # Verify Metrica Book III area division parallel to base
   python3 demos/area_division_book_iii.py

   # Verify Catoptrica shortest-path reflection theorem
   python3 demos/catoptrica_shortest_path.py

Python API Usage
~~~~~~~~~~~~~~~~

Import the symbolic engine directly into interactive Python or Jupyter notebooks:

.. code-block:: python

   import sympy as sp
   from geometor.heron import (
       heron_area,
       heron_area_squared,
       heron_sqrt_convergents,
       construct_heron_proof,
   )

   # Exact area on (13, 14, 15) Heronian triangle
   assert heron_area(13, 14, 15) == sp.Integer(84)
   assert heron_area_squared(13, 14, 15) == sp.Integer(7056)

   # Rational convergents for sqrt(720)
   convs = heron_sqrt_convergents(720, steps=3)
   print("Step 1 approx:", convs[1].approx)  # 161/6
   print("Step 2 approx:", convs[2].approx)  # 51841/1932
