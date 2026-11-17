:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-heron:
.. _heron-about:
.. _heron-mission:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

*GEOMETOR heron* establishes a comprehensive Digital Scriptorium Book Codex and exact constructive symbolic suite dedicated to **Hero (Heron) of Alexandria** (*fl.* c. 60 CE). Occupying a singular crossroads in classical mathematical history, Hero unites the rigorous axiomatic deduction of :person:`Euclid <euclid>` and the exhaustion methods of :person:`Archimedes <archimedes>` with computable rational mensuration, variational mathematical physics, and field geodesy. This edition centers on Hero's three-book masterwork, the ***Metrica*** (*Μετρικά*), rediscovered in 1896 by :person:`Richard Schöne <schoene-richard>` in the eleventh-century *Codex Constantinopolitanus Palatii Veteris* no. 1, integrated alongside foundational selections from the ***Definitiones***, ***Catoptrica***, and ***Dioptra***.

Every definition, proposition, geometric division, and mechanical sightline has been extracted into structured, addressable semantic elements. Rather than static scans or uncurated OCR, each Greek chapter has been transcribed and verified directly against 300 DPI scans of the standard Teubner critical editions (:person:`Hermann Schöne <schoene>` 1903, Wilhelm Schmidt & Ludwig Nix 1900, Friedrich Hultsch 1864, and J. L. Heiberg 1912). The treatise is organized into a synchronized four-track Book Codex (English translation, polytonic Greek, proposition summaries, and scholarly commentary) linked with calibrated, resolution-independent ``.euclid-graphic`` vector diagrams and primary-source folio anchors.

Within the GEOMETOR canon, *heron* operates as the crucial bridge between abstract geometry and physical, computable reality. It connects the foundational definitions and propositions of :cite:`Euclid's Elements <euclid_elements>` (:mod:`geometor.elements`) and Apollonian conics with Norman J. Wildberger's Rational Trigonometry (:mod:`geometor.wildberger`), demonstrating how Hero's triangular area formula :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}` anticipates the polynomial quadrea invariant :math:`\mathcal{A} = 16\Delta^2`. Through the companion Python engine of :mod:`geometor.heron`, every geometric theorem and rational convergent stream is verified to exact symbolic closure.

The GEOMETOR Mission
--------------------

Founded and directed by **phi ARCHITECT**, the GEOMETOR initiative is dedicated to the systematic digitization, symbolic formalization, and multi-medium re-articulation of classical geometric and axiomatic literature across 2,300+ years of mathematical history. GEOMETOR bridges historical philology and modern computational geometry through three structural pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and lossy optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of classical, Renaissance, and modern mathematical treatises. Enunciations, geometric constructions, proof steps, axiomatic justifications, marginal citations, primary-source folios (rendered dynamically through ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams are converted into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Eliminating floating-point approximation errors entirely, GEOMETOR anchors geometric constructions and center proofs in 100% exact symbolic algebra via :mod:`sympy` and Rational Trigonometry invariants (quadrance, spread, cross-ratio) evaluated over exact algebraic number fields. Every center, line concurrence, circle intersection, and tangency condition is verified to exact symbolic zero.

Repurposing Knowledge Across Mediums
    Extracted semantic and algebraic models are mobilized across synchronized multi-track Book Codices and EPUB 3 editions via ``photon-platform/publish``, computable deductive canons (:mod:`geometor.elements`, :mod:`geometor.etc`, :mod:`geometor.pappus`, :mod:`geometor.divine`), interactive SVG laboratories (:mod:`geometor.explorer`), high-definition visual broadcasts, and neuro-symbolic program synthesis engines (:mod:`geometor.seer`) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This edition synthesizes century-old philological scholarship with modern algebraic rigor:

Critical Primary Editions
    * **Hermann Schöne (ed., 1903)**: *Heronis Alexandrini opera quae supersunt omnia*, Vol. III: *Vermessungslehre und Dioptra* (*Metrica*, *Dioptra*), Leipzig: B. G. Teubner (:cite:`schoene:1903`).
    * **Wilhelm Schmidt & Ludwig Nix (eds., 1900)**: *Heronis Alexandrini opera quae supersunt omnia*, Vol. II, Fasc. 1: *Mechanik und Katoptrik*, Leipzig: B. G. Teubner (:cite:`schmidt:1900`).
    * **Friedrich Hultsch (ed., 1864) & J. L. Heiberg (ed., 1912)**: *Heronis Alexandrini Definitiones cum variis collectionibus* / *Heronis Alexandrini opera*, Vol. IV, Leipzig: B. G. Teubner (:cite:`hultsch:1864`, :cite:`heiberg:1912`).

Digital Scriptorium Architecture
    * **Strict Content / Code Separation**: The historical Book Codex (:doc:`/metrica/index`) preserves pure, scan-verified Greek texts and English translations without inline code blocks, while runnable symbolic demonstrations reside in :doc:`/demos/index` and :mod:`geometor.heron`.
    * **Exact Symbolic Demonstrations**: All constructions—from the synthetic incircle proof of Heron's formula to the variational reflection law in *Catoptrica* and mountain tunneling in *Dioptra*—are executed over exact rationals and quadratic fields in :mod:`sympy`.
    * **Scholarly Registries**: Full cross-references are maintained in the :doc:`/concordance`, :doc:`/bibliography`, :doc:`/people/index`, and :doc:`/glossary`.
