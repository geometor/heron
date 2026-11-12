:navigation: header
:order: 20

.. _demos-index:

Symbolic Constructions & Demos
==============================

*100% Exact SymPy & ``geometor.model`` Demonstrations Bringing Hero of Alexandria's Geometry Alive*

While the **4-Track Book Codex** (:doc:`/metrica/index`) preserves strict separation of historical text and scholarly commentary (zero embedded Python scripts), this **Constructive Laboratory** pairs every major theorem of :person:`Hero of Alexandria <hero>` with executable, zero-float ``geometor.model`` DAG constructions, Rational Trigonometry invariants, and standalone Rich CLI demonstrations in ``demos/``.

.. list-table:: Executable Demonstrations in ``geometor.heron``
   :widths: 30 34 36
   :header-rows: 1

   * - Walkthrough Page
     - CLI Script & Core Builder
     - Exact Algebraic Domain & Theorem
   * - :doc:`heron-formula-proof`
     - ``demos/heron_formula_proof.py`` · ``construct_heron_proof``
     - :math:`\mathbb{Q}` on :math:`(13, 14, 15) \implies \Delta = 84`, cyclic quad :math:`CHBL`, Quadrea :math:`\mathcal{A} = 16\Delta^2`
   * - :doc:`sqrt-720-iteration`
     - ``demos/sqrt_720_iteration.py`` · ``heron_sqrt_convergents``
     - :math:`\mathbb{Q}` & :math:`\mathbb{Q}(\sqrt{5})` on :math:`(7, 8, 9) \implies \sqrt{720} = 12\sqrt{5}`, :math:`x_1 = \frac{161}{6}, x_2 = \frac{51841}{1932}`
   * - :doc:`catoptrica-reflection`
     - ``demos/catoptrica_shortest_path.py`` · ``construct_catoptrica_reflection``
     - :math:`\mathbb{Q}(\sqrt{2}, \sqrt{5})` Shortest-Path Unfolding :math:`(|\Gamma E|+|E\Delta|)^2 = 162 < 180`
   * - :doc:`area-division-book-iii`
     - ``demos/area_division_book_iii.py`` · ``construct_area_division``
     - :math:`\mathbb{Q}(\sqrt{3})` Mean-Proportional Cut :math:`Q(A, D) = \frac{507}{4}` & :math:`\sqrt[3]{100} \approx 4\frac{9}{14}`
   * - :doc:`golden-gnomon-dioptra`
     - ``demos/golden_gnomon.py`` · ``construct_heronian_gnomon`` & ``construct_dioptra_tunnel``
     - :math:`\mathbb{Q}(\phi)` Universal Gnomon (:math:`\phi^2 = \frac{3+\sqrt{5}}{2}`) & Geodetic Tunnel :math:`(12, 5) \to 13`

Running All Demonstrations Locally
----------------------------------

Inside the GEOMETOR Python 3.13 environment:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/heron_formula_proof.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/sqrt_720_iteration.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/catoptrica_shortest_path.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/area_division_book_iii.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/golden_gnomon.py

.. toctree::
   :maxdepth: 1
   :caption: Walkthroughs

   heron-formula-proof
   sqrt-720-iteration
   catoptrica-reflection
   area-division-book-iii
   golden-gnomon-dioptra
