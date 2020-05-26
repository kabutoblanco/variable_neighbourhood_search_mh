from ..algorithm import Algorithm
from ...solution import Solution
import copy
import random


class HillclimbingMaxslope(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.pm = 0.5
        self.ratio = 4
        self.neighborhood = 5

    def execute(self, obj_knapsack, obj_solution):
        self.efos = 0

        if not obj_solution:
            s = Solution(obj_knapsack)
            s.get_solution()
        else:
            s = copy.deepcopy(obj_solution)

        while self.efos < self.max_efos:
            r = copy.deepcopy(s)
            r.tweak(self.pm, self.ratio)

            for v in range(self.neighborhood - 1):
                w = copy.deepcopy(s)
                w.tweak(self.pm, self.ratio)

                if w.fitness > r.fitness:
                    r = w
                if self.efos >= self.max_efos:
                    break
                self.efos += 1

            if r.fitness > s.fitness:
                s = r

            self.efos += 1

        self.best_solution = s

    def __str__(self):
        return "MP MaxSlope"