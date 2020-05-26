import csv 
import os

class Export:

    def __init__(self,statistics):
        self.filename = "dataExport.csv"
        self.statistics = statistics
        
    def writeCSV(self):
        if(os.path.isfile(self.filename)):
            os.remove(self.filename)
        with open(self.filename,'w',newline='') as file:
            writer =csv.writer(file)
            tittle = "                   RS (BUSQUEDA ALEATORIA)         ASCENSO DE COLINA (HC)          ALGORITMO IMPLEMENTADO"
            infodata = "                MEDIA|DESVIACION|TASA EXITO     MEDIA|DESVIACION|TASA EXITO     MEDIA|DESVIACION|TASA EXITO "
            footer = "Total promedio"
            writer.writerow([tittle])
            writer.writerow([infodata])
            for r in self.statistics:
                writer.writerow([self._createRow(r)])
            writer.writerow([footer])
    
    def writeHTML(self):
        pass

    def _createRow(self, obj):

        name = obj[0].name_file
        data = []
        for r in obj:
            media = r.average()
            std = r.std()
            succ = r.successfull_rate()
            data.append([media,std,succ])
        st = '{}                {}                {}                {}'.format(name,data[0],data[1],data[2])
        return st
