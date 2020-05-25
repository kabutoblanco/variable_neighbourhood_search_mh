from .localsearch import Localsearch
import random
import copy

class LocalsearchBasic(Localsearch):
    
    def execute(self, obj_neighborhood):
        #generate neighborhood
        try: 
            while(True):
                print("Solution : "+str(self.solution.dimensions)+ " Fitnes: " + str(self.solution.fitness)+"\n")
                neighborhood = obj_neighborhood._getNeighborhood(self.solution)
                selected = neighborhood[random.randint(0,len(neighborhood)-1)]
                newSolution = copy.copy(self.solution)
                
                newSolution.set_values(selected)
                print("\nNew solution selected: "+ str(newSolution.dimensions)+ " Fitness: "+ str(newSolution.fitness))
                
                self.algorithm.execute(newSolution)  
                print("\nBest solution HC: "+str(self.algorithm.best_solution.dimensions)+" Fitness: "+str(self.algorithm.best_solution.fitness))      
                
                if self.algorithm.best_solution.fitness > self.solution.fitness:
                    self.solution.dimensions = self.algorithm.best_solution.dimensions
                    self.solution.fitness = self.algorithm.best_solution.fitness
                    obj_neighborhood.restart_neighborhood()
                else: 
                    obj_neighborhood.next_neighborhood()
                    
        except ValueError as e:
            print(e)
            print("\n\nBest found:")
            print("Best : "+str(self.solution.dimensions)+ " Fitnes: " + str(self.solution.fitness)+"\n")
            

    