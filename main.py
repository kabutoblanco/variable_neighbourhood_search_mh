from problem.knapsack import Knapsack
from metaheuristics.simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic
from metaheuristics.simplestate.hillclimbing.hillclimbing_maxslope import HillclimbingMaxslope
from metaheuristics.simplestate.vns.vns import VNS

import random

def main():
    k = Knapsack("./data/files/f3.txt")
    hcc = HillclimbingClassic()
    hcm = HillclimbingMaxslope()
    vns = VNS(random.randint(2, k.total_items))
    algorithms = {hcc, hcm, vns}
    hcc.max_efos = 500
    hcm.max_efos = 500
    for algorithm in algorithms:
        sum = 0
        for i in range(30):
            algorithm.execute(k, None)
            sum += algorithm.best_solution.fitness
            print(algorithm.best_solution.fitness)
        print("Promedio {}: {}".format(algorithm, sum / 30))

    
if __name__ == "__main__":
    main()
