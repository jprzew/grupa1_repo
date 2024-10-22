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
def factorial(n):
    """Calculates factorial.

    Keyword arguments:
    n -- nonnegative integer
    """

    if (not isinstance(n, int)) or (n < 0):
        raise ValueError('Value of n should a be nonnegative int.')
    
    outcome = 1
    for factor in range(1, n+1):
        outcome *= factor
    
    return outcome
        


# %%
factorial(0)

# %%
factorial(4)

# %%
factorial('coś głupiego')

# %%
