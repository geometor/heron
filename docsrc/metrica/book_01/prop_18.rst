:order: 19
:type: proposition
:canonical_id: I.18
:folio: Schöne 50
:tracks: English: prop_18 | Greek: prop_18-el | Summary: summary | Notes: notes

.. _sec-metrica-i-18:

Prop. I.18: Regular Pentagon via Extreme and Mean Ratio
=======================================================

.. folio:: Schöne 50
   :page: 50

**Proposition I.18 & Lemma — The Regular Pentagon via Extreme and Mean Ratio (Schöne pp. 48–54; fol. 77v)**:

To measure the regular pentagon of side :math:`a = 10`, Hero inscribes it in a circle of center :math:`Z` and considers the right triangle formed by the circumradius :math:`ZB`, the apothem :math:`Z\Gamma`, and the half-side :math:`B\Gamma = \frac{a}{2}`, whose acute central angle at :math:`Z` is one-tenth of four right angles, i.e., :math:`\frac{2}{5}` of a right angle (:math:`36^\circ`). He isolates its fundamental golden-section property in an explicit Euclidean lemma:

   **Lemma (Schöne p. 50; fol. 77v)**: *Let* :g:`ABC <g1:[ A C ]>` *be a right-angled triangle having a right angle at* :g:`C <g1:C>` *(Hero's* :math:`\Gamma` *), and at* :g:`A <g1:A>` *an angle of two-fifths of a right angle (* :math:`36^\circ` *). To prove that the square on the sum* :math:`(BA + A\Gamma)` *is five times the square on* :math:`A\Gamma`:

   .. math::

      (BA + A\Gamma)^2 = 5\,A\Gamma^2 \qquad \Longleftrightarrow \qquad \frac{BA + A\Gamma}{A\Gamma} = \sqrt{5}, \qquad \frac{BA}{A\Gamma} = \sqrt{5} - 1 = \frac{2}{\phi}.

*(Diagram Mapping:* :g:`A <g1:A>` = :math:`A`, :g:`B <g1:B>` = :math:`B`, :g:`C <g1:C>` = :math:`\Gamma`, :g:`D <g1:D>` = :math:`\Delta`, *and* :g:`G <g1:G>` *marks the golden cut on* :math:`A\Delta` *with* :eq:`AG = AB = BD <g1:/ A G /,/ A B /,/ B D />` *).*

.. picture:: /_static/figures/pentagon-golden-lemma.svg
   :alt: Hero Metrica I.18 — Pentagon Golden Section Lemma in Q(phi)

**Proof of the Lemma**:

1. Produce :g:`AC <g1:/ A C />` to :g:`D <g1:D>` so that :eq:`CD = AC <g1:/ C D /,/ A C />`, and join :g:`BD <g1:/ B D />`.
2. Because right triangles :math:`AB\Gamma` and :math:`\Delta B\Gamma` share leg :math:`B\Gamma` and have :eq:`AC = CD <g1:/ A C /,/ C D />`, we have :eq:`AB = BD <g1:/ A B /,/ B D />` and :math:`\angle AB\Gamma = \angle \Gamma B\Delta` (:just:`I.4`).
3. Since :math:`\angle BA\Gamma = \frac{2}{5}` of a right angle (:math:`36^\circ`), its complement :math:`\angle AB\Gamma` is :math:`\frac{3}{5}` of a right angle (:math:`54^\circ` by :just:`I.32`). Hence the whole apex angle :math:`\angle AB\Delta` of isosceles triangle :g:`ABD <g1:< A B D >>` is :math:`\frac{6}{5}` of a right angle (:math:`108^\circ`), which is the interior angle of a regular pentagon!
4. In a regular pentagon, the diagonal :math:`A\Delta` and sides :g:`AB <g1:/ A B />`, :g:`BD <g1:/ B D />` cut one another in **extreme and mean ratio** (:just:`XIII.8`), with :g:`AB <g1:/ A B />` (= :g:`AG <g1:/ A G />` via circle :g:`(AB) <g1:( A B )>`) equal to the greater segment of :math:`A\Delta`.
5. Since :g:`AC <g1:/ A C />` is half the greater segment's whole line :math:`A\Delta`—or directly by **Euclid's *Elements* XIII.1** ("If a straight line be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half")—it follows immediately that:

   .. math::

      (BA + A\Gamma)^2 = 5\,A\Gamma^2. \qquad \text{Q.E.D.}

Approximating :math:`\sqrt{5} \approx \frac{9}{4}` (since :math:`(\frac{9}{4})^2 = \frac{81}{16} = 5\frac{1}{16}`), Hero derives :math:`\frac{BA}{A\Gamma} \approx \frac{5}{4}`, whence :math:`\frac{B\Gamma}{A\Gamma} \approx \frac{3}{4}` (a :math:`3\text{-}4\text{-}5` triangle approximation to the :math:`36^\circ\text{-}54^\circ\text{-}90^\circ` triangle!) and obtains the rational pentagon formula :math:`A_5 \approx \frac{5}{3}a^2` (or more closely :math:`\frac{12}{7}a^2 = 171\frac{3}{7}` vs. exact :math:`\frac{\sqrt{25 + 10\sqrt{5}}}{4}a^2 \approx 172.0477`).
