from problem.knapsack import Knapsack
from metaheuristics.simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic
from metaheuristics.simplestate.hillclimbing.hillclimbing_maxslope import HillclimbingMaxslope
from metaheuristics.simplestate.hillclimbing.random_search import RandomSearch
from metaheuristics.simplestate.vns.vns import VNS
from utils.statistics import Statistics
from data.export import Export

import copy
import math
import random

def main():
    ITER_MAX = 30
    list_statistics = []
    e = Export(list_statistics)
    for i in range(1, 17):
        random.seed(i)
        name_file = ""
        if i < 11:
            name_file = "./data/files/f{}.txt".format(i)
        else:
            name_file = "./data/files/Knapsack{}.txt".format(i - 10)
        statistics = Statistics(name_file, i, ITER_MAX)
        k = Knapsack(name_file)
        hcc = HillclimbingClassic()
        hcm = RandomSearch()
        vns = VNS(random.randint(2, int(math.log(k.total_items) + 1)))
        algorithms = []        
        algorithms.append(hcm)
        algorithms.append(hcc)   
        algorithms.append(vns)             
        hcm.max_efos = 1000    
        hcc.max_efos = 1000            
        vns.max_efos = 1000
        information = [0] * 2
        sublist_statistics = [0] * len(algorithms)
        print(name_file)
        j = 0
        for algorithm in algorithms:
            vector = []
            successfull_count = 0            
            for l in range(ITER_MAX):
                algorithm.execute(k, None)
                vector.append(algorithm.best_solution.fitness)
                successfull_count += 1 if algorithm.successfull else 0
            information[0] = algorithm.__str__()
            information[1] = vector
            statistics.set_vector(information)
            statistics.successfull_count = successfull_count
            sublist_statistics[j] = copy.deepcopy(statistics)
            print(algorithm)
            j += 1
        list_statistics.append(copy.deepcopy(sublist_statistics)) 
    e.writeCSV()
    e.writeHTML()
    
if __name__ == "__main__":
    main()
