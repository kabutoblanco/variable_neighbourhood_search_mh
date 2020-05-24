import random

class Solution:
    def __init__(self, obj_knapsack):
        self.weight = 0
        self.fitness = 0
        self.obj_knapsack = obj_knapsack
        self.dimensions = [0] * obj_knapsack.total_items
        random.seed(30)

    def initial_random(self, random):
        self.weight = 0
        while True:
            index = random.randint(0, self.dimensions.__len__() - 1)
            if random.random() < 0.5:
                self.dimensions[index] = int(not self.dimensions[index])
                if self.dimensions[index] == 1:
                    self.weight += self.obj_knapsack.get_weight(index)
                    if self.weight > self.obj_knapsack.capacity:
                        self.dimensions[index] = 0
                        self.weight -= self.obj_knapsack.get_weight(index)
                        break
                else:
                    self.weight -= self.obj_knapsack.get_weight(index)
        self.evaluate()

    def tweak(self, random, pm, dh, change_attr):
        checks = []

        while checks.__len__() <= dh:
            if random.random() < pm:
                index = random.randint(0, self.dimensions.__len__() - 1)
                if index not in checks:
                    checks.append(index)
                    self.dimensions[index] = int(not self.dimensions[index])
                    if self.dimensions[index] == 1:
                        self.weight += self.obj_knapsack.get_weight(index)
                        if self.weight > self.obj_knapsack.capacity:
                            self.dimensions[index] = 0
                            self.weight -= self.obj_knapsack.get_weight(index)
                            checks.remove(index)
                    else:
                        self.weight -= self.obj_knapsack.get_weight(index)
        self.evaluate()

    def evaluate(self):
        self.fitness = self.obj_knapsack.evaluate(self.dimensions)

    def getSolution(self):
        solution = self._getEmptySolution()
        while(True):
            randIndex = random.randint(0, self.obj_knapsack.total_items -1)
            solution[randIndex] = random.randint(0, 1)
            if(self._validateSolution(solution)):
                solution[randIndex]=0
                break
        return solution
    
    def _validateSolution(self, solution):
        count = 0
        ret = False
        for x in range(0, self.obj_knapsack.total_items):
            if solution[x] == 1:
                count+= self.obj_knapsack.variables[x].weight
            if count > self.obj_knapsack.capacity:
                ret = True
        return ret      

    def _getEmptySolution(self):
        ret = []
        for x in range(0, self.obj_knapsack.total_items):
            ret.append(0)
        return ret
