:order: 1
:type: proposition
:canonical_id: Catoptrica 4
:folio: Schmidt 368–372
:tracks: English: prop_04 | Greek: prop_04-el | Summary: summary | Notes: notes

.. _sec-catoptrica-reflection:

Catoptrica Prop. 4: Variational Shortest-Path Proof of the Law of Reflection
============================================================================

.. folio:: Schmidt 368
   :page: 368

In his *Catoptrica*—preserved in medieval Latin translation by :person:`William of Moerbeke <moerbeke>` (:cite:`Schmidt 1900, pp. 324–329 <schmidt:1900>`) and **verbatim in the original Greek** by :person:`Olympiodorus <olympiodorus>` (*Commentary on Aristotle's Meteorology* III.2, :cite:`Schmidt 1900, pp. 368–372, Fig. 92 <schmidt:1900>`)—:person:`Hero <hero>` delivers the **first variational extremum principle in the history of physics**, sixteen centuries before Fermat's Principle of Least Time (1662):

   *"Straight visual rays proceeding from the eye to mirrors and the objects seen are bent (:term:`reflected <anaklasis>`) at equal angles to themselves. Why then are they not also bent at unequal angles? To this we shall reply that **Nature does nothing in vain nor labors pointlessly** (*ἡ φύσις οὐδὲν μάτην ἐργάζεται οὐδὲ ματαιοπονεῖ*); and if she refuses to labor pointlessly, it is manifest that she sees by the **shortest paths** (*διʼ ἐλαχίστων*) and not by long detours. And since straight lines bent at equal angles are shorter than straight lines bent at unequal angles, for this reason reflection takes place at equal angles, and not at unequal angles."*

*(Diagram Mapping:* :g:`AB <g2:[ A B ]>` *= plane mirror; eye* :g:`C <g2:C>` *(Hero's* :math:`\Gamma` *); seen object* :g:`D <g2:D>` *(Hero's* :math:`\Delta` *); perpendicular foot* :g:`H <g2:H>`; *virtual reflected point* :g:`K <g2:K>`; *equal-angle point* :g:`E <g2:E>`; *arbitrary unequal-angle point* :g:`Z <g2:Z>` *).*

.. picture:: /_static/figures/catoptrica-reflection.svg
   :alt: Hero Catoptrica Prop. 4 — Variational Shortest-Path Proof of Reflection (Schmidt Fig. 92)

**Geometric Proof (Schmidt pp. 370–372)**:

1. Let the plane mirror be :g:`AB <g2:[ A B ]>`, the eye :g:`C <g2:C>`, and the object seen :g:`D <g2:D>`. Let ray :g:`CE <g2:/ C E />` strike the mirror at :g:`E <g2:E>` and reflect as :g:`ED <g2:/ E D />` making equal grazing angles with the mirror (:math:`\angle \Gamma EA = \angle \Delta EB`); and let another ray :g:`CZ <g2:/ C Z />` strike any other point :g:`Z <g2:Z>` and reflect as :g:`ZD <g2:/ Z D />` at unequal angles. *I say that* :math:`\Gamma E + E\Delta < \Gamma Z + Z\Delta`.
2. Drop the perpendicular :g:`DH <g2:/ D H />` from :g:`D <g2:D>` onto mirror :g:`AB <g2:[ A B ]>` (:just:`I.12`), produce it straight through to :g:`K <g2:K>` so that :eq:`HK = DH <g2:/ H K /,/ D H />` (:just:`I.3`), and join :g:`EK <g2:/ E K />` and :g:`ZK <g2:/ Z K />`.
3. In right triangles :math:`\Delta HE` and :math:`KHE`, :eq:`DH = HK <g2:/ D H /,/ H K />`, :math:`HE` is common, and the angles at :g:`H <g2:H>` are right; therefore by :just:`I.4`, :eq:`ED = EK <g2:/ E D /,/ E K />` and :math:`\angle \Delta EH = \angle KEH`.
4. **Unfolding Collinearity**: By hypothesis :math:`\angle \Delta EH = \angle \Gamma EA`; hence :math:`\angle \Gamma EA = \angle KEH`—they are vertical angles, so **:g:`CEK <g2:[ C K ]>` is a single unbroken straight line** (:just:`I.14`–:just:`I.15`)!
5. Again, in right triangles :math:`\Delta HZ` and :math:`KHZ`, :eq:`DH = HK <g2:/ D H /,/ H K />` and :math:`ZH` is common, so :eq:`ZD = ZK <g2:/ Z D /,/ Z K />` (:just:`I.4`).
6. **Triangle Inequality Climax**: In triangle :g:`CZK <g2:< C Z K >>`, any two sides are strictly greater than the remaining side (:just:`I.20`):

   .. math::

      \Gamma Z + ZK > \Gamma K.

   Substituting :math:`ZK = Z\Delta` and :math:`\Gamma K = \Gamma E + EK = \Gamma E + E\Delta` yields immediately:

   .. math::

      \Gamma Z + Z\Delta \;>\; \Gamma E + E\Delta. \qquad \text{Q.E.D.}

*(In our exact coordinates* :math:`C=(1,3), D=(10,6), E=(4,0), Z=(7,0)`*, the unfolded path has squared length* :math:`(|CE|+|ED|)^2 = (9\sqrt{2})^2 = 162` *with equal spreads* :math:`s = \frac{1}{2}`*, whereas the perturbed path has squared length* :math:`(|CZ|+|ZD|)^2 = (6\sqrt{5})^2 = 180 > 162` *!)*
