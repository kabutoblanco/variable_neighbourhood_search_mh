from .localsearch import Localsearch

class LocalsearchBasic(Localsearch):
    
    def execute(self, obj_neighborhood):
        #generate neighborhood
        ##initial solution
        s = self.solution.getSolution()
        print(s)
        for r in range (0,4):
            pass