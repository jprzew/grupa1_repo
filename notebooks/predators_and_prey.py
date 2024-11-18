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
    """Population simulation

    Attributes
    -----------
    specimens: set - set of instances of Creature class
    history: list - list of the previous population counts
    n: int - current population count
    
    """

    def __init__(self, n=100):
        self.specimens = {Creature() for _ in range(n)}
        self.history = []

    @property
    def specimens(self):
        return self._specimens

    @specimens.setter
    def specimens(self, creatures):
        self._specimens = creatures
        self.n = len(creatures)

    def natural_selection(self):
        """Starts natural selection process for the population. 
           First makes creatures to reproduce, then tries to kill mature creatures
        """
        newborns = {creature.reproduce() for creature in self.specimens} - {None}
        {creature.kill() for creature in self.specimens}
        self.history.append(self.n)
        # We update the population
        self.specimens = {creature for creature in self.specimens
                          if creature.alive} | newborns

    def plot_history(self):
        plt.plot(self.history)

    def plot_histogram(self, attr):
        plt.hist(list(map(lambda x: getattr(x, attr), self.specimens)))


class Probability:
    """Descriptor of probability. Makes sure that probability values are in [0, 1]"""

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, min(max(0, value), 1))


class Creature:
    """Represents a single creature.

    Attributes
    ----------
    p_death: float - probability of death
    p_reproduce: float - probability of reproduction
    sigma: float - standard deviation of the error term in creature reproduction model
    """

    sigma = 0.01
    p_death = Probability()
    p_reproduce = Probability()

    def __init__(self, p_death=0.2, p_reproduce=0.2):
        self.p_death = p_death
        self.p_reproduce = p_reproduce
        self.alive = True

    def kill(self):
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        """Creates a new creature with probability p_reproduce"""
        if (random.random() < self.p_reproduce) and self.alive:
            return type(self)()


class Predator(Creature):

    p_death_hungry = 0.9

    def __init__(self, p_death=0.2, p_reproduce=0.2):
        super().__init__(p_death, p_reproduce)
        self.hungry = True
        
    
    def hunt(self, prey):
        if (random.random() < prey.p_hunt) and self.alive:
            prey.alive = False
            self.hungry = False

    def kill(self):
        p_death = self.p_death_hungry if self.hungry else self.p_death
        
        if random.random() < p_death:
            self.alive = False
        

class Prey(Creature):
    p_hunt = Probability()

    def __init__(self, p_death=0.2, p_reproduce=0.2, p_hunt=0.2):
        super().__init__(p_death, p_reproduce)
        self.p_hunt = p_hunt
        


# %%
predator = Predator()

# %%
predator.hungry

# %%
prey = Prey()

# %%
predator.hunt(prey)
predator.hungry, prey.alive

# %%
from collections import namedtuple

# %%

# %%
