Installation Instructions
=========================

Installation
------------
``pip install --upgrade git+https://github.com/AlanPearl/diffmahnet.git``

Prerequisites
-------------
- Tested on Python versions: ``python=3.10-12``
- Latest version of ``diffmah``
- JAX (GPU install available - see https://jax.readthedocs.io/en/latest/installation.html)

Example installation with conda env:
++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    conda create -n py312 python=3.12
    conda activate py312
    conda install -c conda-forge mpi4py jax
    pip install --upgrade git+https://github.com/ArgonneCPAC/diffmah.git
    pip install --upgrade git+https://github.com/AlanPearl/diffmahnet.git