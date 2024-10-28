# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from functools import reduce


# %%
def factorial(n):
    """Calculates factorial.

    Keyword arguments:
    n -- nonnegative integer
    """

    if (not isinstance(n, int)) or (n < 0):
        raise ValueError('Value of n should a be nonnegative int.')
 
    outcome = reduce(lambda x, y: x*y, range(1, n+1), 1)
    
    return outcome
        


# %%
factorial(0)

# %%
factorial('coś głupiego')

# %%
