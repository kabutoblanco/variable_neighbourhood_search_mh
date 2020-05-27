from ..algorithm import Algorithm
from .neighborhood import Neighborhood
from ...solution import Solution
from ..hillclimbing.hillclimbing_classic import HillclimbingClassic
from .localserch.localsearch_basic import LocalsearchBasic
from .localserch.localsearch_desc import LocalsearchDesc
from .localserch.localsearch_redux import LocalsearchRedux

import random
from time import time

class VNS(Algorithm):
    def __init__(self, k_max):
        Algorithm.__init__(self)
        self.k_max = k_max
        self.neighborhoods = []

    def execute(self, obj_knapsack, obj_solution):
        start_time = time()
        self.efos = 0

        checks = []
        while len(checks) < self.k_max:
            rand_dh = random.randint(1, int(obj_knapsack.total_items / 3) + 1)
            if rand_dh not in checks:
                checks.append(rand_dh)
        
        checks = sorted(checks)
        for dh in checks:
            self.neighborhoods.append(Neighborhood(random.random(), dh, 4))

        
        hc = HillclimbingClassic()
        s = Solution(obj_knapsack, self)
        s.get_solution()
        k = 0
        while k < self.k_max and self.efos < self.max_efos and s.fitness != obj_knapsack.optimal_know and time() - start_time < 0.5:
            obj_searchlocal = LocalsearchRedux(s, hc)
            s_prima2 = obj_searchlocal.execute(self.neighborhoods[k])
            self.efos += obj_searchlocal.efos
            
            if s_prima2.fitness > s.fitness:
                s = s_prima2
                k = 0
            else:
                k += 1

            if s.fitness == obj_knapsack.optimal_know:
                self.successfull = True
            
        self.best_solution = s

    def __str__(self):
        return "VNS"
