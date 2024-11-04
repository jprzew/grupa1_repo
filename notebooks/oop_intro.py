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
import matplotlib.pyplot as plt


# %%
class Population:

    def __init__(self, n=100):
        self.speciemens = {Creature() for _ in range(n)}
        self.history = []

    @property
    def speciemens(self):
        return self._speciemens

    @speciemens.setter
    def speciemens(self, creatures):
        self._speciemens = creatures
        self.n = len(creatures)

    def natural_selection(self):
        newborns = {creature.reproduce() for creature in self.speciemens} - {None}
        {creature.kill() for creature in self.speciemens}
        self.history.append(self.n)
        # We update the population
        self.speciemens = {creature for creature in self.speciemens
                           if creature.alive} | newborns

    def plot_history(self):
        plt.plot(self.history)

    def plot_histogram(self, attr):  # attr-str, np. attr='p_death'
        plt.hist(list(map(lambda x: getattr(x, attr), self.speciemens)))

    


class Creature:

    sigma = 0.01

    def __init__(self, p_death=0.2, p_reproduce=0.2):
        self.p_death = p_death
        self.p_reproduce = p_reproduce
        self.alive = True

    def kill(self):
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        if (random.random() < self.p_reproduce) and self.alive:
            return Creature(p_death=self.p_death + random.normalvariate(sigma=Creature.sigma),
                            p_reproduce=self.p_reproduce + random.normalvariate(sigma=Creature.sigma))



# %%
population = Population()

# %%
population.n

# %%
population.plot_histogram('p_death')

# %%
population.plot_histogram('p_reproduce')

# %%
for _ in range(50):
    population.natural_selection()

# %%
population.n

# %%
population.plot_history()

# %%
population.plot_histogram('p_death')

# %%
population.plot_histogram('p_reproduce')

# %%
# getattr?

# %%
