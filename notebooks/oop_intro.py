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
import random


# %%
class Creature:
    alive = True  # atrybut; attribute
    p_death = 0.2
    p_reproduce = 0.2

    def kill(self):  # metoda; method
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        if (random.random() < self.p_reproduce) and self.alive:
            return Creature()
    


# %%
gnom = Creature()

# %%
krasnal = Creature()

# %%
gnom is krasnal

# %%
gnom.kill()
gnom.alive

# %%
child = gnom.reproduce()

# %%
child is None

# %%
child.kill()
child.alive

# %%
