from ..algorithm import Algorithm
from ...solution import Solution
import copy
import random


class HillclimbingClassic(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.pm = 0.5
        self.ratio = 4

    def execute(self, obj_knapsack, obj_solution):
        self.efos = 0

        if not obj_solution:
            s = Solution(obj_knapsack)
            s.get_solution()
        else:
            s = copy.deepcopy(obj_solution)

        while self.efos < self.max_efos and s.fitness != obj_knapsack.optimal_know:
            r = copy.deepcopy(s)
            r.tweak(self.pm, self.ratio)
        
            if r.fitness > s.fitness:
                s = r
            self.efos += 1

            if s.fitness == obj_knapsack.optimal_know:
                self.successfull = True
        
        self.best_solution = s

    def __str__(self):
        return "MP Clasico"