from ..algorithm import Algorithm
from ...solution import Solution
import copy


class HillclimbingClassic(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.pm = 0.5
        self.ratio = 4

    def execute(self, obj_knapsack, random):
        self.efos = 0

        s = Solution(obj_knapsack)
        s.initial_random(random)

        while self.efos < self.max_efos:
            r = copy.deepcopy(s)
            r.tweak(random, self.pm, self.ratio, 0)

            if (r.fitness > s.fitness):
                s = r
            self.efos += 1

        self.best_solution = s
        print(self.best_solution.dimensions)
        print(self.best_solution.fitness)
        print(self.best_solution.weight)
