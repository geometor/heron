=========
Changelog
=========

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
