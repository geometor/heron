# GEOMETOR • heron

Scholarly **4-Track Bilingual Book Codex** (`:layout: book`) and **100% Exact Symbolic Python Constructions** for **Hero (Heron) of Alexandria** (*fl.* c. 60 CE) — covering ***Metrica* Books I–III** (ed. Hermann Schöne, Teubner 1903), ***Definitiones*** (ed. Friedrich Hultsch 1864 / J. L. Heiberg 1912), ***Catoptrica*** (ed. Wilhelm Schmidt & Ludwig Nix, Teubner 1900), and ***Dioptra*** (ed. Schöne, Teubner 1903).

---

## 1. Purpose & Architectural Mandates

1. **Dual-Pillar Scholarly + Constructive Architecture**:
   - **`docsrc/metrica/` (`:layout: book`)**: Strictly preserves historical source texts, original GEOMETOR English translations, proposition summaries, scholarly notes, calibrated `.euclid-graphic` SVGs, and apparatus registries (`concordance.rst`, `bibliography.rst`, `persons.rst`, `glossary.rst`) with **zero embedded Python `code-block`s**.
   - **`src/geometor/heron/` & `demos/`**: Implements 100% exact symbolic SymPy + `geometor.model` compass-and-straightedge constructions (`Model(..., auto_intersect=False)` with zero `float`/`sp.Float` coordinates), Rational Trigonometry invariants (`quadrance`, `line_spread`, `archimedes_quadrea`), and interactive walkthroughs in `docsrc/demos/`.
2. **Multimodal Scan Provenance**:
   - All polytonic Greek texts in `resources/metrica/sources/` and `docsrc/metrica/*/*-el.rst` are verified directly against 300 DPI archival page scans of the public-domain Teubner and Weidmann critical editions, protected by SHA-256 checksums in `resources/metrica/sources_manifest.json`.

---

## 2. Key Modules (`src/geometor/heron/`)

- `mensuration.py`: Exact symbolic Heron's Formula, Wildberger's polynomial Quadrea identity ($\mathcal{A} = 16\Delta^2$), iterative rational square-root stream (`heron_sqrt_convergents(720)`), Pentagon Golden Section Lemma in $\mathbb{Q}(\phi)$, regular $n$-gon multipliers ($n = 3 \dots 12$), Dionysodorus's torus volume ($2\pi^2 R r^2 \implies 9956\frac{4}{7}$), frustum mean-plus-third-difference identity, and the Five Platonic Solids.
- `constructions.py`: Seven exact zero-float `geometor.model.Model` theorem builders (`construct_heron_proof`, `construct_pentagon_lemma`, `construct_dionysodorus_torus`, `construct_catoptrica_reflection`, `construct_area_division`, `construct_heronian_gnomon`, `construct_dioptra_tunnel`).
- `render.py`: Theme-adaptive `.euclid-graphic` SVG exporter with 3-vertex `<path>` circle arcs, `#geom-tick-1..3` markers, `#highlights` layer, and angular collision-free label placement.
- `concordance.py` & `compile_codex.py`: Deterministic compiler for `docsrc/metrica/{concordance,bibliography,persons,glossary}.rst` and 4-track Codex + SHA-256 manifest verifier.
- `sphinx_ext.py`: Local Sphinx hook verifying apparatus registries before `photon_platform.publish` compilation.
- `cli.py`: `heron` CLI (`summary`, `verify`, `compile-apparatus`, `export-figures`).

---

## 3. Verification Commands (Python 3.13 Offline Sandbox)

```bash
/home/phi/.local/bin/ruff check src demos tests
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v
/home/phi/PROJECTS/geometor/.venv/bin/python demos/heron_formula_proof.py
/home/phi/.local/bin/publish build
```
