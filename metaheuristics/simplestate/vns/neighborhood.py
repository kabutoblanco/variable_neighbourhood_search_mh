class Neighborhood:
    def __init__(self, pm, dh, size):
        self.pm = pm
        self.dh = dh
        self.size = size
        self.neighborhood_number = 1
        self.start_values = [pm,dh,size]

    def next_neighborhood(self):
        self.pm-=0.05
        self.dh+=1
        self.neighborhood_number+=1
        if(self.pm < 0.1): raise ValueError("Error, maximum number of neighborhood generated")

    def _getNeighborhood(self,s):
        neighborhood = []
        print("Neighborhood #"+str(self.neighborhood_number)+ ": pm = "+str(self.pm)+ "  dh = "+str(self.dh))
        for i in range(0,self.size):
            newNeihborhood = s.tweak(self.pm, self.dh)
            fitness = s.evaluate(newNeihborhood)
            neighborhood.append([newNeihborhood,fitness])
            print("Tweak #"+str(i+1)+" : "+ str(newNeihborhood) + " Fitnes: "+ str(fitness))
        return neighborhood

    def restart_neighborhood(self):
        self.pm = self.start_values[0]
        self.dh = self.start_values[1]
        self.size = self.start_values[2]