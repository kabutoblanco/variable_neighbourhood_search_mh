from data.file import File
from problem.knapsack import Knapsack
from metaheuristics.simplestate.vns.vns import VNS
from metaheuristics.simplestate.vns.neighborhood import Neighborhood

import random

def main():
    k = Knapsack("./data/files/f2.txt")
    vns = VNS(4)
    vns.execute(k)
    print(vns.best_solution)
    print(vns.best_solution.fitness)
    
if __name__ == "__main__":
    main()
