import copy

class Neighborhood:
    def __init__(self, pm, dh, size):
        self.pm = pm
        self.dh = dh
        self.size = size
        self.neighborhood = []

    def execute(self, s):
        for i in range(0, self.size):
            r = copy.deepcopy(s)
            r.tweak(self.pm, self.dh)
            self.neighborhood.append(r)

    def best_neighbors(self):
        best = self.neighborhood[0]

        for neighbor in self.neighborhood:
            if neighbor.fitness > best.fitness:
                best = copy.deepcopy(neighbor)
        
        return best