.. _heron-home:

===============================================================================
Hero of Alexandria — *Metrica*, *Definitiones*, *Catoptrica* & *Dioptra*
===============================================================================

*Mensuration, Variational Optics, Geodesy, and Constructive Exactness in the GEOMETOR Digital Scriptorium*

.. epigraph::

   «Ἡ πρώτη γεωμετρία, καθάπερ ὁ παλαιὸς ἡμᾶς διδάσκει λόγος, περὶ τὰς ἐν Αἰγύπτῳ τῆς χώρας μετρήσεις καὶ διανομὰς ἠσχολεῖτο· διὰ γὰρ τὰς τοῦ Νείλου ἀναβάσεις τὰ ὅρια τῶν ἰδιοκτησιῶν ἠφανίζετο…»

   *"Original geometry, just as the ancient account teaches us, was occupied with the measurements and distributions of land in Egypt; for owing to the risings of the Nile, the boundaries of private holdings were obliterated…"*

   — :person:`Hero of Alexandria <hero>`, *Metrica* I, Preface (:cite:`ed. Hermann Schöne, Leipzig: B. G. Teubner, 1903 <schoene:1903>`, p. 2)

**GEOMETOR • heron** unites two complementary pillars of the GEOMETOR canon in a single scholarly and computational edition of **Hero (Heron) of Alexandria** (*fl.* c. 60 CE):

1. **4-Track Bilingual Book Codex** (:doc:`/metrica/index`):
   A folio-indexed Digital Scriptorium edition of Hero's three-book masterwork ***Metrica*** (*Μετρικά*, rediscovered in 1896 by :person:`Richard Schöne <schoene-richard>` in the 11th-century *Codex Constantinopolitanus Palatii Veteris* no. 1 and edited by :person:`Hermann Schöne <schoene>`, :cite:`Teubner 1903 <schoene:1903>`), paired with foundational selections from ***Definitiones*** (:cite:`ed. Hultsch 1864 <hultsch:1864>` / :cite:`Heiberg 1912 <heiberg:1912>`), ***Catoptrica*** (:cite:`ed. Schmidt & Nix 1900 <schmidt:1900>`), and ***Dioptra*** (:cite:`ed. Schöne 1903 <schoene:1903>`). Every unit synchronizes four parallel tracks:

   - **English**: Original GEOMETOR scholarly translation directly from the scan-verified critical Greek editions, instrumented with interactive ``.euclid-graphic`` SVG diagrams and ``:g:`` / ``:eq:`` / ``:just:`` / ``:person:`` / ``:cite:`` / ``:term:`` markup.
   - **Greek (Teubner)**: Polytonic Greek text transcribed via multimodal vision from 300 DPI archival scans of Schöne (1903), Schmidt (1900), and Hultsch (1864).
   - **Summary**: Proposition-by-proposition structural, algorithmic, and mathematical synopses.
   - **Notes**: Deep philosophical, historical, and Rational Trigonometry commentary cross-linked to executable symbolic demonstrations and sister GEOMETOR repositories (`euclid`, `elements`, `proclus`, `pappus`, `wildberger`, `etc`, `divine`).

2. **100% Exact Symbolic Python Constructions & Demos** (:doc:`/demos/index`):
   Executable compass-and-straightedge proofs and mensuration engines in ``geometor.heron`` built on SymPy and ``geometor.model`` (`Model(..., auto_intersect=False)` with zero floating-point coordinates):

   - :doc:`/demos/heron-formula-proof` — Hero's synthetic incircle & cyclic-quadrilateral proof of :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}` (*Metrica* I.8) on :math:`(13, 14, 15) \implies 84` alongside :person:`Norman J. Wildberger's <wildberger>` polynomial :term:`quadrea` identity :math:`\mathcal{A} = 16\Delta^2`.
   - :doc:`/demos/sqrt-720-iteration` — Exact :math:`\mathbb{Q}` rational sequence of Hero's square-root extraction on :math:`(7, 8, 9) \implies \sqrt{720}` (:math:`x_0 = 27`, :math:`x_1 = \frac{161}{6}`, :math:`x_2 = \frac{51841}{1932}`, :math:`x_3, x_4`).
   - :doc:`/demos/catoptrica-reflection` — Hero's *Catoptrica* Prop. 4 variational shortest-path proof of the Law of Reflection (:math:`S_{\text{inc}} = S_{\text{refl}}` minimizes path length :math:`|\Gamma E| + |E\Delta|`).
   - :doc:`/demos/area-division-book-iii` — *Metrica* III.1–2 vertex (:math:`5:3`) and parallel mean-proportional (:math:`3:1`, :math:`Q(A,D) = \frac{507}{4}`) area divisions realizing geometric distributive justice.
   - :doc:`/demos/golden-gnomon-dioptra` — Hero's universal :term:`gnomon` (*Definitiones* §58) over :math:`\mathbb{Q}(\phi)` and two-portal mountain tunneling by orthogonal right-triangle traversal (*Dioptra* Ch. 15).

Architecture of the Codex
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 34 26 30

   * - Unit
     - Codex Chapter
     - Critical Source Pages
     - Interactive Constructions
   * - **I**
     - :doc:`/metrica/book-i-triangles/book-i-triangles-en`
     - Schöne (1903), pp. 2–26
     - ``heron-i8-incircle.svg`` (:doc:`Demo </demos/heron-formula-proof>`, :doc:`√720 </demos/sqrt-720-iteration>`)
   * - **II**
     - :doc:`/metrica/book-i-polygons-circles/book-i-polygons-circles-en`
     - Schöne (1903), pp. 26–90
     - ``pentagon-golden-lemma.svg`` (:math:`\mathbb{Q}(\phi)` Golden Lemma & Polygons 3–12)
   * - **III**
     - :doc:`/metrica/book-ii-solids/book-ii-solids-en`
     - Schöne (1903), pp. 90–140
     - ``dionysodorus-torus-section.svg`` (Torus :math:`V = 2\pi^2 R r^2`, Vaults, 5 Solids)
   * - **IV**
     - :doc:`/metrica/book-iii-divisions/book-iii-divisions-en`
     - Schöne (1903), pp. 140–184
     - ``metrica-iii-area-division.svg`` (:doc:`Demo </demos/area-division-book-iii>`)
   * - **V**
     - :doc:`/metrica/definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-en`
     - Hultsch pp. 7–23 · Schmidt pp. 324–372 · Schöne pp. 238–240
     - ``heronian-golden-gnomon.svg``, ``catoptrica-reflection.svg``, ``dioptra-mountain-tunnel.svg`` (:doc:`Optics </demos/catoptrica-reflection>`, :doc:`Gnomon & Dioptra </demos/golden-gnomon-dioptra>`)

.. toctree::
   :maxdepth: 2
   :hidden:

   mission/index
   metrica/index
   demos/index
   changelog
