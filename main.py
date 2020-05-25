from data.file import File
from problem.knapsack import Knapsack
from metaheuristics.simplestate.vns.vns import VNS
from metaheuristics.simplestate.vns.neighborhood import Neighborhood

import random

def main():
    k = Knapsack("./data/datos.txt")
    random.seed(4)
    vns = VNS(5)
    vns.execute(k)
    print(vns.best_solution)
    print(vns.best_solution.fitness)
    
if __name__ == "__main__":
    main()
