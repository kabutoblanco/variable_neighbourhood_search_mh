import numpy as np
import math

class Statistics:
    def __init__(self, name_file, seed, max_rep):
        self.name_file = name_file
        self.seed = seed
        self.a = np.array([])
        self.max_rep = max_rep

        self.algorithm = ""
        self.successfull_count = 0

    def set_vector(self, vector):
        self.algorithm = vector[0]
        self.a = np.array(vector[1])

    def average(self):
        return np.average(self.a)

    def std(self):
        return np.std(self.a)

    def successfull_rate(self):
        return self.successfull_count / self.max_rep * 100