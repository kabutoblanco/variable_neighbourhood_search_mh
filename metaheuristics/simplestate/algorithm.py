class Algorithm:
    def __init__(self):
        self.efos = 0
        self.max_efos = 500
        self.best_solution = None

    def execute(self, obj_knapsack, random):
        raise NotImplementedError