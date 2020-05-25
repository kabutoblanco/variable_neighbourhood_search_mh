from .localsearch import Localsearch
from ....solution import Solution
import random
import copy

class LocalsearchBasic(Localsearch):
    
    def execute(self, obj_neighborhood):
        s = copy.deepcopy(self.solution)

        #  Selección aleatoria (S’) del vecindario actual (Nk) de S
        obj_neighborhood.execute(s)
        rand_index = random.randint(0, obj_neighborhood.size - 1)
        s_prima = obj_neighborhood.neighborhood[rand_index]
        
        # Búsqueda local
        self.algorithm.execute(s.obj_knapsack, s_prima)
        s_prima2 = self.algorithm.best_solution

        return s_prima2
            

    