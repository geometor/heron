.. _demo-golden-gnomon-dioptra:

Universal Golden Gnomon & Dioptra Mountain Tunnel
=================================================

*Self-Similar Accretion in Q(φ) (Definitiones §58) & Subterranean Geodesy (Dioptra Ch. 15)* — Codex Reference: :doc:`/metrica/definitiones-catoptrica-dioptra/definitiones-catoptrica-dioptra-en`

1. Universal Golden Gnomon (`heronian-golden-gnomon.svg`)
---------------------------------------------------------

Realizing :person:`Hero's <hero>` **Definition 58** (*"a gnomon is anything which, added to any number or figure, makes the whole similar to that to which it was added"*), adjoining the unit square gnomon :g:`ABCD <g1:< A B C D >>` to the golden seed :g:`BEFC <g1:< B E F C >>` via compass swing :g:`(MC) <g1:( M C )>` creates the whole rectangle :g:`AEFD <g1:< A E F D >>` with identical aspect quadrance :math:`\phi^2 = \frac{3 + \sqrt{5}}{2}`:

.. picture:: /_static/constructions/heronian-golden-gnomon.svg
   :alt: Hero Definitiones 58 — Universal Golden Gnomon in Q(phi)

2. Two-Portal Mountain Tunneling (`dioptra-mountain-tunnel.svg`)
----------------------------------------------------------------

Realizing **Dioptra Chapter 15** (:cite:`Schöne 1903, pp. 238–240 <schoene:1903>`), orthogonal dioptra stations :g:`E <g3:E>`, :g:`Z <g3:Z>`, :g:`H <g3:H>`, :g:`G <g3:G>`, :g:`K <g3:K>`, :g:`M <g3:M>` determine the subterranean displacement :math:`(\Delta x, \Delta y) = (12, 5)` of :g:`BND <g3:< B N D >>`, aligning exterior sighting triangles :g:`BOX <g3:< B O X >>` and :g:`DPQ <g3:< D P Q >>` collinearly along :g:`XQ <g3:[ X Q ]>`:

.. picture:: /_static/figures/dioptra-mountain-tunnel.svg
   :alt: Hero Dioptra Ch. 15 — Two-Portal Mountain Tunneling by Orthogonal Traverse

Executable Python API
---------------------

.. code-block:: python

   import sympy as sp
   from geometor.heron import PHI, construct_dioptra_tunnel, construct_heronian_gnomon

   _, gnom = construct_heronian_gnomon()
   assert sp.simplify(gnom["whole_aspect_quadrance"] - PHI**2) == 0
   assert sp.simplify(gnom["seed_aspect_quadrance"] - PHI**2) == 0

   _, diop = construct_dioptra_tunnel()
   assert diop["east_displacement"] == 12 and diop["north_displacement"] == 5
   assert diop["tunnel_length"] == 13
