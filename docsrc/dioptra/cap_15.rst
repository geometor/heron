:order: 1
:type: section
:canonical_id: Dioptra 15
:folio: Schöne 238–240
:tracks: English: cap_15 | Greek: cap_15-el | Summary: summary | Notes: notes

.. _sec-dioptra-tunnel:

Dioptra Ch. 15: Tunneling a Mountain from Both Ends simultaneously
==================================================================

.. folio:: Schöne 238
   :page: 238

In his treatise *On the Dioptra* (*Περὶ διόπτρας*, :cite:`Schöne 1903, pp. 188–314 <schoene:1903>`), :person:`Hero <hero>` designs a precision geared sighting and leveling theodolite (:term:`dioptra <dioptra>`) and demonstrates in **Chapter 15 (pp. 238–240, Fig. 95)** how engineers can bore a straight underground tunnel or aqueduct (*ὑπόνομος*) through an opaque mountain **simultaneously from both portals**—providing the mathematical paradigm behind masterpieces like :person:`Eupalinus of Megara's <eupalinus>` Tunnel of Samos:

   **Problem 15**: *"To bore straight through a mountain when the mouths (:g:`B <g3:B>`, :g:`D <g3:D>`) of the tunnel upon the mountain are given."*

*(Diagram Mapping: Portals* :g:`B <g3:B>` :math:`= (0,0)` *and* :g:`D <g3:D>` :math:`= (12,5)` *have true tunnel length* :math:`13`; *orthogonal dioptra traverse stations* :g:`E <g3:E>`, :g:`Z <g3:Z>`, :g:`H <g3:H>`, :g:`G <g3:G>` *(Hero's* :math:`\Theta` *),* :g:`K <g3:K>`, :g:`M <g3:M>` *skirt the mountain foot; virtual vertex* :g:`N <g3:N>` :math:`= (12,0)` *completes the hidden right triangle* :g:`BND <g3:< B N D >>`; *and exterior similar triangles* :g:`BOX <g3:< B O X >>` *and* :g:`DPQ <g3:< D P Q >>` *align both digging crews along* :g:`XQ <g3:[ X Q ]>` *).*

.. picture:: /_static/figures/dioptra-mountain-tunnel.svg
   :alt: Hero Dioptra Ch. 15 — Orthogonal Traverse and Similar-Triangle Sighting for Two-Portal Mountain Tunneling (Schöne Fig. 95)

**Hero's Survey & Alignment Algorithm**:

1. **Orthogonal Traverse Around the Mountain**: Starting from portal :g:`B <g3:B>`, sight an arbitrary baseline :g:`BE <g3:/ B E />` with the :term:`dioptra <dioptra>`, turn successively through **exact right angles** around the base of the mountain along segments :g:`EZ <g3:/ E Z />`, :g:`ZH <g3:/ Z H />`, :g:`HG <g3:/ H G />`, :g:`GK <g3:/ G K />`, and slide the dioptra along the perpendicular line through :g:`K <g3:K>` until the second portal :g:`D <g3:D>` appears directly through the orthogonal sights at station :g:`M <g3:M>` (giving :g:`MD <g3:/ M D />` parallel to :g:`BE <g3:[ E B ]>` and :g:`ZH <g3:/ Z H />`).
2. **Signed Coordinate Summation**: Summing the signed East–West and North–South legs determines the invisible right-angled triangle :g:`BND <g3:< B N D >>` inside the rock:

   .. math::

      BN = \sum \Delta x = (-2) + 18 + (-2) + (-2) = 12, \qquad ND = \sum \Delta y = (-3) + 11 + (-3) = 5,

   whence by :just:`I.47` the exact underground tunnel distance :g:`BD <g3:/ B D />` is :math:`\sqrt{12^2 + 5^2} = 13`!
3. **Exterior Similar-Triangle Sighting**: Outside portal :g:`B <g3:B>`, produce :math:`NB` to :g:`O <g3:O>` and erect perpendicular :math:`OX` in the exact ratio :math:`BO : OX = BN : ND = 12 : 5`, constructing right triangle :g:`BOX <g3:< B O X >>`. Likewise outside portal :g:`D <g3:D>`, produce :math:`MD` to :g:`P <g3:P>` and erect :math:`PQ` with :math:`DP : PQ = 12 : 5`, constructing :g:`DPQ <g3:< D P Q >>`.
4. **Guaranteed Underground Rendezvous**: Because :g:`BOX <g3:< B O X >>` and :g:`DPQ <g3:< D P Q >>` are similar to :g:`BND <g3:< B N D >>` (:just:`VI.4`), their hypotenuses :math:`XB` and :math:`DQ` lie **on the exact same straight line** :g:`XQ <g3:[ X Q ]>` as the subterranean chord :g:`BD <g3:/ B D />` (:just:`I.14`). Sighting backward along straightedge rules aligned with :math:`XB` and :math:`QD` (*κανόνας παραβάλλοντες*), both excavation crews meet face-to-face in the heart of the mountain—and if vertical ventilation shafts (*φρέατα*) are needed from the ridge above, the same ratio locates every shaft directly over the tunnel axis!
