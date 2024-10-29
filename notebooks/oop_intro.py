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
class Population:

    def __init__(self, n=100):
        self.speciemens = {Creature() for _ in range(n)}

    @property
    def speciemens(self):
        return self._speciemens

    @speciemens.setter
    def speciemens(self, creatures):
        self._speciemens = creatures
        self.n = len(creatures)

    def natural_selection(self):
        {creature.kill() for creature in self.speciemens}
        # We discard dead creatures
        self.speciemens = {creature for creature in self.speciemens
                           if creature.alive}

    


class Creature:
    alive = True
    p_death = 0.2
    p_reproduce = 0.2

    def kill(self):
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        if (random.random() < self.p_reproduce) and self.alive:
            return Creature()



# %%
population = Population()

# %%
population.n

# %%
for _ in range(20):
    population.natural_selection()
    print(population.n)

# %%

# %%

# %%

# %%
population1.speciemens = [Creature()]

# %%
population1.n

# %%
population2 = Population(n=1000)

# %%
population2.n

# %%
{3, 4, 4, 5, 9, 11111111, 11111111}

# %%
{3, 4, 5} | {3, 7}

# %%
{3, 4, 5} - {3, 7}

# %%
{3, 4, 5} & {3, 7}

# %%
my_set = {3, 4, 5, 7}

# %%
for element in my_set:
    print(element)

# %%
my_list = {3, 4}

# %%
my_list.add(7)

# %%
my_list

# %%
