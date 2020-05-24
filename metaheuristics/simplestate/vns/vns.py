from ..algorithm import Algorithm
from .neighborhood import Neighborhood
from ...solution import Solution

class VNS(Algorithm):
    def __init__(self, k_max):
        Algorithm.__init__(self)
        self.k_max = k_max
        self.neighborhoods = []

    def execute(self, obj_knapsack, random):
        self.efos = 0

        for i in range(self.k_max):
            self.neighborhoods.append(Neighborhood(random.uniform(0, 0.5), i + 1, 0))

        s = Solution(obj_knapsack)
        s.initial_random(random)

        while self.efos < self.max_efos:
            k = 0
            while k < self.k_max:
                ##launch ls class
                
                s.tweak(random, self.neighborhoods[k].pm, self.neighborhoods[k].dh, self.neighborhoods[k].change_attr)
