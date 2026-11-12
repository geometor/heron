:order: 53
:type: notes
:canonical_id: definitiones-catoptrica-dioptra
:folio: Hultsch 7–23 · Schmidt 324–372 · Schöne 238–240
:book: Definitiones · Catoptrica · Dioptra

.. _unit-definitiones-catoptrica-dioptra-notes:

Scholarly Notes — Definitiones, Catoptrica & Dioptra
====================================================

*Commentary on Olympiodorus & William of Moerbeke, D'Arcy Thompson's Gnomon, and the Tunnel of Eupalinus*

1. Transmission of Hero's *Catoptrica*: Moerbeke & Olympiodorus
---------------------------------------------------------------

For centuries, the medieval Latin treatise *De speculis*—translated from Greek at Viterbo on December 31, 1269 by :person:`William of Moerbeke <moerbeke>`—circulated under the name of :person:`Claudius Ptolemy <ptolemy>` (*Ptolemaei De speculis*). In 1871–1900, Valentin Rose and :person:`Wilhelm Schmidt <schmidt>` (:cite:`Teubner 1900 <schmidt:1900>`, pp. 301–372) proved decisively that *De speculis* is in fact **Hero of Alexandria's *Catoptrica***!

The clinching philological proof came from the 6th-century Alexandrian Neoplatonist :person:`Olympiodorus <olympiodorus>`, who in his Greek commentary on :person:`Aristotle's <aristotle>` *Meteorology* III.2 (:cite:`Schmidt 1900, pp. 368–372 <schmidt:1900>`) quotes **Hero the Mechanician in his *Catoptrica*** (*δείκνυσιν Ἥρων ὁ μηχανικὸς ἐν τοῖς αὑτοῦ Κατοπτρικοῖς*) and reproduces word-for-word the Greek mirror-reflection proof that matches Moerbeke's Latin Proposition 4! Thus we possess Hero's variational shortest-path theorem in **authentic Greek prose**, directly linking Greek synthetic geometry (:just:`I.4`, :just:`I.14`, :just:`I.15`, :just:`I.20`) to Fermat's Principle of Least Time (1662), Maupertuis, Euler, and Hamilton's Principle of Stationary Action. See :doc:`/demos/catoptrica-reflection`.

2. Hero's Definition 58 & D'Arcy Wentworth Thompson's *On Growth and Form*
--------------------------------------------------------------------------

Hero's **Definition 58** (*«καθόλου δὲ γνώμων ἐστὶ πᾶν ὃ προσλαβὸν ὁτιοῦν, ἀριθμὸν ἢ σχῆμα, ποιεῖ τὸ ὅλον ὅμοιον ᾧ προσείληφεν»*) inspired one of the most celebrated chapters of modern mathematical biology: Chapter XI (*"The Equiangular Spiral"*) of D'Arcy Wentworth Thompson's *On Growth and Form* (1917 / 1942). Whereas Euclid restricted the :term:`gnomon <gnomon>` to L-shaped parallelogram increments (:just:`II.def.2`), Hero recognized that **self-similar accretion** unites:

- **Arithmetic Gnomons**: Adding the odd number :math:`2n + 1` to the square :math:`n^2` produces the next square :math:`(n + 1)^2`.
- **Planar Golden Gnomons**: Adding a square of side :math:`1` to a rectangle of aspect :math:`1 : (\phi - 1)` produces a similar rectangle of aspect :math:`\phi : 1` (and in isosceles golden triangles of :math:`36^\circ\text{-}72^\circ\text{-}72^\circ` and :math:`108^\circ\text{-}36^\circ\text{-}36^\circ`, adjoining one gnomon triangle produces the next larger similar triangle!).
- **Logarithmic Spirals & Nautilus Shells**: Continuous gnomonic accretion around a pole generates the equiangular spiral :math:`r = a e^{b\theta}` without ever altering the organism's shape. See :doc:`/demos/golden-gnomon-dioptra` and the ``geometor/divine`` and ``geometor/phyllotaxis`` repositories.

3. *Dioptra* Chapter 15, Cartesian Coordinates & the Tunnel of Samos
--------------------------------------------------------------------

In *History of Greek Mathematics* (:cite:`1921 <heath:1921>`, Vol. II, pp. 346–351), :person:`Thomas Heath <heath>` highlighted **Dioptra Chapter 15** alongside *Dioptra* Chapter 34 (which determines the great-circle terrestrial distance between Rome and Alexandria from observations of a single lunar eclipse!). Nearly six centuries before Hero, :person:`Eupalinus of Megara <eupalinus>` excavated the :math:`1{,}036`-meter **Tunnel of Samos** (c. 530 BCE) under Mount Castro from both ends simultaneously. Hero's *Dioptra* Ch. 15 demonstrates the exact Hellenistic perfection of two-portal tunneling: rather than climbing over a rugged mountain ridge (where slope errors accumulate rapidly), Hero wraps an **orthogonal horizontal Cartesian coordinate frame** (:math:`\sum \Delta x, \sum \Delta y`) around the level foot of the mountain, transforming physical obstacles into pure Euclidean similarity (:just:`VI.4`).
