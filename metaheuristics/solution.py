import random
import copy

class Solution:
    
    def __init__(self, obj_knapsack):
        self.fitness = 0
        self.obj_knapsack = obj_knapsack
        self.dimensions = [0] * obj_knapsack.total_items

    def getSolution(self):
        solution = self._getEmptySolution()
        while(True):
            randIndex = random.randint(0, self.obj_knapsack.total_items -1)
            if(self._validateSolution(solution,randIndex)):
                solution[randIndex]=0
                break
            else:
                solution[randIndex]=1
        self.dimensions = solution
        self.fitness = self.evaluate(self.dimensions)

    def tweak(self, pm, dh):
        shift = []
        solution = copy.copy(self.dimensions)
        while len(shift) < dh:
            index = random.randint(0, len(solution)-1)
            if index not in shift:
                if (random.random() > pm):
                    if(not self._validateSolution(solution,index)):
                        if(solution[index]==0): solution[index] = 1
                        else: solution[index] = 0
                        shift.append(index)
        #shift.sort()                    
        #print(str(shift))
        return solution

    def evaluate(self,dimensions):
        return self.obj_knapsack.evaluate(dimensions)
    
    def _validateSolution(self, s, index):
        count = 0
        ret = False
        solution = copy.copy(s)
        if solution[index] == 1:
            solution[index] = 0
        else:
            solution[index] = 1
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

    def set_values(self,values):
        self.dimensions = values[0]
        self.fitness = values[1]
