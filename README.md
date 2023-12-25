# hspcore
Hansen Solubility Parameters (HSP) core functions.

## Installation

Install **hspcore** easily with pip:

```
pip install hspcore
```

## Usage Example

```
import hspcore as hsp

#hsp grid is a list of solvents as [name,D,P,H,score]
hsp_grid = [
    ['Acetonitrile' 15.3 18.0 6.1 1],
    ['1-Bromonaphthalene' 20.6 3.1 4.1 6],
    ['n-Butyl Acetate' 15.8 3.7 6.3 3],
    ...
]

product_hsp = get_hsp()

#{'hsp': [16.94774954607497, 14.990227992029617, 11.009633578254737], 'radius': 12.446654676104526, 'error': 0.9979557635334755}
```

## Links

- [See on GitHub](https://github.com/Gnpd/hspcore)
- [See on PyPI](https://pypi.org/project/hspcore)
