from data.file import File
from problem.knapsack import Knapsack
from metaheuristics.solution import Solution
from metaheuristics.simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic

from metaheuristics.simplestate.vns.localserch.localsearch_basic import LocalsearchBasic
from metaheuristics.simplestate.vns.localserch.localsearch_decomp import LocalsearchDecomp

import random
from metaheuristics.simplestate.vns.neighborhood import Neighborhood
from metaheuristics.simplestate.algorithm import Algorithm

def main():
    #k = Knapsack("./data/datos.txt")
    #r = random
    #hc = HillclimbingClassic()
    #hc.execute(k, r)
    random.seed(33)
    k = Knapsack("./data/datos.txt")
    s = Solution(k)
    s.getSolution()
    n = Neighborhood(0.5,1,4)
    a = HillclimbingClassic()
    l = LocalsearchBasic(s,a)
    l.execute(n)
    
    
if __name__ == "__main__":
    main()
