GEOMETOR • heron
================

**Visit the Online Archive:** https://geometor.github.io/heron/

.. image:: docsrc/_static/constructions/catoptrica-reflection.svg
   :alt: GEOMETOR • heron featured geometric construction
   :target: https://geometor.github.io/heron/
   :align: center

**Heron of Alexandria • Metrica, Definitiones, Catoptrica, Dioptra • semantic digital archive**

Mission
-------

``geometor/heron`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It liberates Heron of Alexandria's foundational works—*Metrica*, *Definitiones*, *Catoptrica*, and *Dioptra*—from isolated print bounds into addressable semantic units, synchronized bilingual reading tracks, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and exact symbolic algebra across the GEOMETOR corpus.

Books in This Archive
---------------------

- `Metrica <https://geometor.github.io/heron/metrica/>`_ — Books I, II & III (ed. Hermann Schöne, 1903) establishing synthetic triangle area proofs, Archimedean volume quadratures, and exact division algorithms.
- `Definitions <https://geometor.github.io/heron/definitiones/>`_ — Ὅροι τῶν γεωμετρίας ὀνομάτων (ed. Friedrich Hultsch, 1864 / J. L. Heiberg, 1912) formulating 133 genetic definitions and the universal gnomon.
- `Catoptrics <https://geometor.github.io/heron/catoptrica/>`_ — Κατοπτρικά / De speculis (ed. Wilhelm Schmidt, 1900) presenting the foundational shortest-path variational proof for the law of reflection.
- `On the Dioptra <https://geometor.github.io/heron/dioptra/>`_ — Περὶ διόπτρας (ed. Hermann Schöne, 1903) describing optical instrumentation, stellar alignment, and two-portal mountain tunneling.

Python Package & Modules
------------------------

The ``geometor-heron`` Python package (``import geometor.heron``) provides the executable symbolic geometry, construction, and compilation modules powering this archive:

- ``compile_codex.py`` — Deterministic apparatus compiler and 4-Track Book Codex verifier for ``geometor.heron``.
- ``concordance.py`` — Codex unit specifications, provenance manifest checks, and cross-corpus concordance.
- ``constructions.py`` — Exact symbolic geometric constructions for Hero of Alexandria in ``geometor.model``.
- ``mensuration.py`` — Exact symbolic mensuration formulas and rational approximations from Hero's Metrica.
- ``render.py`` — Publication-grade interactive ``.euclid-graphic`` SVG renderer for ``geometor.heron``.
- ``cli.py`` — Command-line interface for ``geometor.heron``.
- ``sphinx_ext.py`` — Runtime Sphinx & ``photon-platform/publish`` integration for ``geometor.heron``.

See the `API Reference <https://geometor.github.io/heron/modules/>`_ for full module documentation.

Repository Contents
-------------------

- ``docsrc/`` — Four-track Book Codex, apparatus registries, and Sphinx docs compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Primary folio scans, structure maps, persons/citations registries, and review manifests.
- ``src/geometor/heron/`` — Exact symbolic geometry models, algebraic audits, and demonstration pipelines.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
