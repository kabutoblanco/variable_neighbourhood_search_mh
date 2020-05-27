from ..algorithm import Algorithm
from ...solution import Solution

import random
from time import time

class HillclimbingMaxslope(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.pm = 0.5
        self.ratio = 4
        self.neighborhood = 5

    def execute(self, obj_knapsack, obj_solution):
        start_time = time()
        self.efos = 0

        if not obj_solution:
            s = Solution(obj_knapsack, self)
            s.get_solution()
        else:
            s = obj_solution.copy()

        while self.efos < self.max_efos and s.fitness != obj_knapsack.optimal_know and time() - start_time < 0.5:
            r = s.copy()
            r.tweak(self.pm, self.ratio)

            for v in range(self.neighborhood - 1):
                w = s.copy()
                w.tweak(self.pm, self.ratio)

                if w.fitness > r.fitness:
                    r = w
                if self.efos >= self.max_efos and s.fitness != obj_knapsack.optimal_know:
                    break

            if r.fitness > s.fitness:
                s = r

            if s.fitness == obj_knapsack.optimal_know:
                self.successfull = True

        self.best_solution = s

    def __str__(self):
        return "MP MaxSlope"