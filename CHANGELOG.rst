=========
Changelog
=========

0.1.5 (2026-11-15)
------------------

- Synchronized ``.. picture::`` geometric figures onto all 5 Greek source track units alongside the English translation tracks and rebuilt inline SVGs with explicit ``viewBox`` dimensions and scoped theme styles (``publish`` ``v0.4.6``).

0.1.4
-----
*2026-11-15*

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3
-----
*2026-11-14*

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2
-----
*2026-11-14*

- Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- Curated and verified track-aware primary-source folio links for *Metrica*, *Definitiones*, *Catoptrica*, and *Dioptra* (62/62 directives and 20/20 badges resolved).

0.1.0 (2026-11-12)
------------------

Initial scholarly and symbolic release of **geometor-heron**:

- **4-Track Bilingual Book Codex** (``docsrc/metrica/``, ``:layout: book``):
  - 5 synchronized Codex units (20 track files: ``-en``, ``-el``, ``-summary``, ``-notes``) covering *Metrica* Books I–III (*ed.* H. Schöne, Teubner 1903), *Definitiones* (*ed.* F. Hultsch 1864 / J. L. Heiberg 1912), *Catoptrica* Prop. 4 (*ed.* W. Schmidt & L. Nix 1900), and *Dioptra* Ch. 15 (*ed.* Schöne 1903).
  - Multimodal scan-verified Greek source archive (``resources/metrica/sources/``) with SHA-256 provenance manifest and 24-locus cross-corpus GEOMETOR concordance.
- **Exact Symbolic Engine** (``src/geometor/heron/``):
  - ``mensuration.py``: Exact Heron's Formula, Wildberger's polynomial Quadrea identity (:math:`\mathcal{A} = 16\Delta^2`), rational square-root stream on :math:`\sqrt{720}`, Pentagon Golden Section Lemma in :math:`\mathbb{Q}(\phi)`, regular 3-gon to 12-gon multipliers, Dionysodorus's torus volume (:math:`9956\frac{4}{7}`), frustum mean-plus-third-difference identity, and Platonic solid volumes.
  - ``constructions.py`` & ``render.py``: Seven zero-float ``geometor.model`` constructions and interactive ``.euclid-graphic`` SVG exporter.
- **Executable Demonstrations** (``demos/`` & ``docsrc/demos/``):
  - Five standalone Rich CLI demonstrations and five interactive walkthrough pages.
