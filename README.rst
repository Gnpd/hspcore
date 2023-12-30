hspcore
========

Hansen Solubility Parameters (HSP) core functions.

Installation
-------------

Install **hspcore** easily with pip:

.. code-block:: python

    pip install hspcore

Usage Example
--------------

.. code-block:: python

    from hspcore import get_hsp
    #hsp grid is a list of solvents as [[Solvent,D,P,H,Score],...]
    hsp_grid = [
        ['Acetonitrile' 15.3 18.0 6.1 1],
        ['1-Bromonaphthalene' 20.6 3.1 4.1 6],
        ['n-Butyl Acetate' 15.8 3.7 6.3 3],
        ...
    ]
    
    hsp,radius,error = get_hsp(hsp_grid)
   
Links
-------

- See on GitHub: https://github.com/Gnpd/hspcore
- See on PyPI: https://pypi.org/project/hspcore
