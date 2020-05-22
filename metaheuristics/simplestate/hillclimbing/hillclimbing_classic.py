from ..algorithm import Algorithm
from ...solution import Solution
import copy

class HillclimbingClassic(Algorithm):
    def __init__(self):
        self.pm = 0.5
        self.ratio = 10

    def execute(self, obj_knapsack, random):
        self.efos = 0

        s = Solution(obj_knapsack, self)
        s.initial_random(random)

        while (self.efos < self.max_efos):
            r = copy.copy(s)
            r.tweak_base(random, self.pm, self.ratio)

            if (r.fitness > s.fitness):
                s = r

        self.best_solution = s