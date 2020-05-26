from problem.knapsack import Knapsack
from metaheuristics.simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic
from metaheuristics.simplestate.hillclimbing.hillclimbing_maxslope import HillclimbingMaxslope
from metaheuristics.simplestate.vns.vns import VNS
from utils.statistics import Statistics

import random

def main():
    ITER_MAX = 30
    list_statistics = []
    
    for i in range(1, 10):
        name_file = "./data/files/f{}.txt".format(i)
        statistics = Statistics(name_file, i, ITER_MAX)
        k = Knapsack(name_file)
        hcc = HillclimbingClassic()
        hcm = HillclimbingMaxslope()
        vns = VNS(random.randint(2, k.total_items))
        algorithms = {hcc, hcm, vns}
        hcc.max_efos = 100
        hcm.max_efos = 100
        information = [0] * 2
        print(name_file)
        for algorithm in algorithms:
            vector = []
            successfull_count = 0
            random.seed(i)
            for i in range(ITER_MAX):
                algorithm.execute(k, None)
                vector.append(algorithm.best_solution.fitness)
                successfull_count += 1 if algorithm.successfull else False
            information[0] = algorithm.__str__()
            information[1] = vector
            statistics.set_vector(information)
            statistics.successfull_count = successfull_count
            i += 1
            print(algorithm)
            print("Promedio: {}".format(statistics.average()))
            print("Desviación: {}".format(statistics.std()))
            print("Tasa de exito: {}".format(statistics.successfull_rate()))

    
if __name__ == "__main__":
    main()
