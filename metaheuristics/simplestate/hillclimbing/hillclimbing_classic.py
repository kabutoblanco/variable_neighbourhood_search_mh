from ..algorithm import Algorithm
from ...solution import Solution
import copy


class HillclimbingClassic(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.pm = 0.5
        self.ratio = 4

    def execute(self, solution):
        self.efos = 0
        s = copy.copy(solution)

        while self.efos < self.max_efos:
            r = copy.deepcopy(s)
            temp = r.tweak(self.pm, self.ratio)
            r.set_values([temp,r.evaluate(temp)])
            if (r.fitness > s.fitness):
                s = r
            self.efos += 1
        self.best_solution = s
