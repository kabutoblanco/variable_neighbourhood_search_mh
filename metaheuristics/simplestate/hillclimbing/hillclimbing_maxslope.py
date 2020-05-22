from ..algorithm import Algorithm
from ...solution import Solution
import copy

class HillclimbingMaxslope(Algorithm):
    def __init__(self):
        self.pm = 0.5
        self.ratio = 10
        self.neighborhood = 5

    def execute(self, obj_knapsack, random):
        self.efos = 0
        s = Solution(obj_knapsack, self)
        s.initial_random(random)

        while (self.efos < self.max_efos)
            r = copy.copy(s)
            r.tweak_base(random, self.pm, self.ratio)

            for v in range(self.neighborhood - 1):
                w = copy.copy(s)
                w.tweak_base(random, self.pm, self.ratio)

                if (w.fitness < r.fitness)
                    r = w
                if (self.efos >= self.max_efos) break

            if (r.fitness > s.fitness)
                s = r

        self.best_solution = s