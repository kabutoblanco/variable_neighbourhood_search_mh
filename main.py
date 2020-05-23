from data.file import File
from problem.knapsack import Knapsack
from metaheuristics.solution import Solution

import random

def main():
    k = Knapsack("./data/datos.txt")
    s = Solution(k, None)
    r = random
    s.initial_random(r)
    print(s.dimensions)


if __name__ == "__main__":
    main()
