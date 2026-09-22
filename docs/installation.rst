Installation
============

Editable installation
---------------------

The repository uses a standard `src/` package layout. From the repository
root:

.. code-block:: bash

   pip install -e .

This installs the distribution `trend-estimation` and exposes:

.. code-block:: python

   import trend_estimation

Conda environment
-----------------

.. code-block:: bash

   conda env create -f environment.yml
   conda activate trend-estimation
   pip install -e .

Development and documentation
-----------------------------

.. code-block:: bash

   pip install -e ".[dev,docs]"
   pytest
   sphinx-build -W -b html docs docs/_build/html

Optional finance dependencies
-----------------------------

.. code-block:: bash

   pip install -e ".[finance]"

Naming
------

* repository: `Trend-Estimation`;
* pip distribution: `trend-estimation`;
* Python package: `trend_estimation`;
* source directory: `src/trend_estimation/`.
