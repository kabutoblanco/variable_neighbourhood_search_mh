

class Solution:
    def __init__(self, obj_knapsack):
        self.weight = 0
        self.fitness = 0
        self.obj_knapsack = obj_knapsack
        self.dimensions = [0] * obj_knapsack.total_items

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
