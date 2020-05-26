import csv 
import os
import time

class Export:

    def __init__(self,statistics):
        self.filename = "./exports/dataExport.csv"
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
        html = "<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='X-UA-Compatible' content='ie=edge'><link rel='stylesheet' href='./styles/style.css'><title>Algoritmos de Estado Simple</title></head><body>"
        html += "<div class='schedule-container'><div class='schedule-title'><span>Rendimiento</span></div><div class='table-responsive'><div class='schedule-table'><table>"
        html += "<thead><tr><th rowspan='2'>Dataset</th><th colspan='3'>Busqueda aleatoria</th><th colspan='3'>Ascenso a la colina</th><th colspan='3'>VNS</th></tr><tr>"
        for i in range(3):
            html += "<th>Media</th><th>Desviacion</th><th>Tasa de exito</th>"
        html += "</tr></thead><tbody>"
        for statistics in self.statistics:
            html += "<tr><td>" + statistics[0].name_file + "</td>"
            for i in range(3):
                html += "<td class='non-select'><span>" + str(statistics[0].average()) + "</span></td>"
                html += "<td class='non-select'><span>" + str(statistics[0].std()) + "</span></td>"
                html += "<td class='non-select'><span>" + str(statistics[0].successfull_rate()) + "</span></td>"
            html += "</tr>"
        html += "</tbody></table></div></div></div></body></html>"

        name = "schedules_{}_{}.html".format(time.strftime("%d_%m_%y"), time.strftime("%H_%M"))
        hs = open("./data/exports/" + name, 'w')
        hs.write(html)

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
