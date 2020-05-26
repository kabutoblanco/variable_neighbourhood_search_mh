from problem.knapsack import Knapsack
from metaheuristics.simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic
from metaheuristics.simplestate.hillclimbing.random_search import RandomSearch
from metaheuristics.simplestate.vns.vns import VNS
from utils.statistics import Statistics
from data.export import Export

import copy
import random

def main():
    ITER_MAX = 10
    list_statistics = []
    e = Export(list_statistics)
    for i in range(1, 10):
        name_file = "./data/files/f{}.txt".format(i)
        statistics = Statistics(name_file, i, ITER_MAX)
        k = Knapsack(name_file)
        hcc = HillclimbingClassic()
        hcm = RandomSearch()
        vns = VNS(random.randint(2, int(k.total_items / 2 + 1)))
        algorithms = []
        algorithms.append(hcc)
        algorithms.append(hcm)
        algorithms.append(vns)
        hcc.max_efos = 50
        hcm.max_efos = 50
        information = [0] * 2
        sublist_statistics = [0] * len(algorithms)
        print(name_file)
        j = 0
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
            sublist_statistics[j] = statistics
            i += 1
            j += 1
            print(algorithm)
            print("Promedio: {}".format(statistics.average()))
            print("Desviación: {}".format(statistics.std()))
            print("Tasa de exito: {}".format(statistics.successfull_rate()))
        list_statistics.append(copy.deepcopy(sublist_statistics)) 
    e.writeCSV()
    
if __name__ == "__main__":
    main()
