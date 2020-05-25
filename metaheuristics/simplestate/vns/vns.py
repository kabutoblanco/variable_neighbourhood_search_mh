from ..algorithm import Algorithm
from .neighborhood import Neighborhood
from ...solution import Solution
from ..hillclimbing.hillclimbing_classic import HillclimbingClassic
from .localserch.localsearch_basic import LocalsearchBasic

import random

class VNS(Algorithm):
    def __init__(self, k_max):
        Algorithm.__init__(self)
        self.k_max = k_max
        self.neighborhoods = []

    def execute(self, obj_knapsack):
        self.efos = 0

        for i in range(self.k_max):
            self.neighborhoods.append(Neighborhood(random.uniform(0, 0.5), i + 1, 4))

        s = Solution(obj_knapsack)
        s.get_solution()

        k = 0
        while k < self.k_max:
            obj_searchlocal = LocalsearchBasic(s, HillclimbingClassic())
            s_prima2 = obj_searchlocal.execute(self.neighborhoods[k])
            
            if s_prima2.fitness > s.fitness:
                s = s_prima2
                k = 0
            else:
                k += 1
        
        self.best_solution = s
