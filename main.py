from data.file import File
from problem.knapsack import Knapsack
from metaheuristics.solution import Solution
from metaheuristics.simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic

import random

def main():
    k = Knapsack("./data/datos.txt")
    r = random
    hc = HillclimbingClassic()
    hc.execute(k, r)


if __name__ == "__main__":
    main()
