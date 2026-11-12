:order: 33
:type: notes
:canonical_id: book-ii-solids
:folio: Schöne 90–140
:book: Metrica Book II (Pref. & Props. 1–20)

.. _unit-book-ii-solids-notes:

Scholarly Notes — Metrica Book II (Preface & Props. 1–20)
=========================================================

*Commentary on Dionysodorus of Caunus, Centroid Unrolling, the Archimedes Palimpsest, and the Bomiskos*

1. Dionysodorus's *On the Torus* & the Prehistory of Pappus's Centroid Theorem
------------------------------------------------------------------------------

**Proposition II.13** (:cite:`Schöne 1903 <schoene:1903>`, pp. 126–130; fols. 95v–96r) is one of the jewels recovered when :person:`Richard Schöne <schoene-richard>` and :person:`Hermann Schöne <schoene>` brought the *Codex Constantinopolitanus* to light in 1896–1903. Prior to 1896, :person:`Dionysodorus of Caunus <dionysodorus>` was known primarily through :person:`Eutocius's <eutocius>` commentary on :cite:`Archimedes' Sphere and Cylinder II.4 <archimedes:sphere-cylinder>` for cutting a sphere in a given ratio via the intersection of a parabola and a rectangular hyperbola.

Hero preserves both Dionysodorus's rigorous exhaustion proportion—comparing the torus to the cylinder of radius :math:`R` and height :math:`2r` in the ratio :math:`\pi r^2 : R r`—and his own intuitive centroid reformulation: *unrolling* (*ἁπλωθεῖσα*) the torus into a right circular cylinder whose length equals the circumference :math:`2\pi R` traced by the center of gravity :math:`Z` of the generating meridian circle! Two and a half centuries later, :person:`Pappus of Alexandria <pappus>` generalized this exact principle to arbitrary planar domains in :cite:`Synagoge Book VII <pappus:synagoge>` (the Pappus–Guldinus Centroid Theorem). Notice also that because :math:`\pi` enters *squared* in :math:`V = 2\pi^2 R r^2`, Hero evaluates :math:`\pi^2 \approx \left(\frac{22}{7}\right)^2 = \frac{484}{49}`, producing the rational signature :math:`\frac{69696}{7} = 9956\frac{4}{7}` (vs. exact :math:`1008\pi^2 \approx 9948.56`).

2. *Metrica* II.14–II.15 & the 1906 Discovery of Archimedes' *Method*
---------------------------------------------------------------------

History records a dramatic convergence between *Metrica* and the Archimedes Palimpsest. In 1903, :person:`Hermann Schöne <schoene>` published Hero's explicit citations in *Metrica* I.35, II.14, and II.15 to :person:`Archimedes' <archimedes>` hitherto unknown treatise *The Method* (*Ἐφοδικόν*), revealing that Archimedes had proved both the cylindrical ungula (:math:`V = \frac{1}{6}d^2 h`) and the bicylinder groin vault (:math:`V = \frac{2}{3}d^3`). Just **three years later**, in 1906, :person:`Johan Ludvig Heiberg <heiberg>` traveled to Constantinople (to the Metochion of the Holy Sepulchre, steps away from the Old Seraglio where the *Metrica* manuscript lay!) and deciphered the **Archimedes Palimpsest**, finding the *Method of Mechanical Theorems Addressed to Eratosthenes*! Crucially, because the final folios of the Archimedes Palimpsest containing the classical exhaustion proof of Proposition 15 (the bicylinder) were lost, Hero's *Metrica* II.15 remains an indispensable witness confirming that Archimedes completed and circulated the theorem for architectural vaults (*καμάραι*).

3. Why Hero Rewrote the Frustum Formula (Props. II.6–II.10)
-----------------------------------------------------------

Egyptian Moscow Mathematical Papyrus Problem 14 (c. 1850 BCE) already computed the square frustum via :math:`\frac{h}{3}(a^2 + ab + b^2)`. Why did Hero systematically rewrite this throughout Book II as :math:`h\left[\left(\frac{a+b}{2}\right)^2 + \frac{1}{3}\left(\frac{a-b}{2}\right)^2\right]`?

1. **Direct Error Correction of Surveyor Practice**: Everyday Roman and Egyptian masons frequently averaged top and bottom dimensions :math:`\bar{a} = \frac{a+b}{2}` and multiplied :math:`\bar{a}^2 h`. Hero's decomposition isolates :math:`\bar{a}^2 h` as the leading term and exhibits :math:`\frac{1}{3}\left(\frac{a-b}{2}\right)^2 h` as the exact positive convexity correction.
2. **Seamless Generalization to Dissimilar Rectangles (Prop. II.8)**: Whereas :math:`a^2 + ab + b^2` has no obvious symmetric extension when length and breadth taper at *different* rates (:math:`a_1 \ne a_2, b_1 \ne b_2`), Hero's mean-plus-third-difference form generalizes immediately by replacing squares with products: :math:`\bar{a}\bar{b} + \frac{1}{3}\Delta a\,\Delta b`, which is equivalent to Simpson's prismatoid rule :math:`\frac{h}{6}(A_{\text{top}} + 4 A_{\text{mid}} + A_{\text{bot}})`!
