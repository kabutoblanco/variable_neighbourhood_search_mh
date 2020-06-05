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
    
    def total_average(self, statistics):
        ba = [0] * 3
        hc = [0] * 3
        vns = [0] * 3 
        total = len(statistics)
        for tr in statistics:
            for st in tr:
                if(st.algorithm == "Busqueda aleatoria"):
                    ba[0] += st.average()
                    ba[1] += st.std()
                    ba[2] += st.successfull_rate()
                if(st.algorithm == "Ascenso a la colina"):
                    hc[0] += st.average()
                    hc[1] += st.std()
                    hc[2] += st.successfull_rate()
                if(st.algorithm == "VNS"):
                    vns[0] += st.average()
                    vns[1] += st.std()
                    vns[2] += st.successfull_rate()
        for l in range(0,3):
            ba[l] = ba[l]/total
            hc[l] = hc[l]/total
            vns[l] = vns[l]/total
        return [ba,hc,vns]
        
                
        
        
                
