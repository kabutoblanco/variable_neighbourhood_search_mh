class Algorithm:
    def __init__(self):
        self.efos = 0
        self.max_efos = 5000
        self.best_solution = None

    def execute(self, obj_knapsack, random):
        raise NotImplementedError