import numpy as np
import math

class Statistics:
    def __init__(self, vector):
        self.a = np.array(vector)

    def average(self, vector):
        return np.average(self.a)

    def std(self, vector):
        return np.std(self.a)