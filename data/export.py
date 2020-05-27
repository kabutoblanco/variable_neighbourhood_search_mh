import csv 
import time

class Export:

    def __init__(self, statistics):
        self.root = "./data/exports/"
        self.name = "record_{}_{}".format(time.strftime("%d_%m_%y"), time.strftime("%H_%M"))
        self.HTML = ".html"
        self.CSV = ".csv"
        self.statistics = statistics
        
    def writeCSV(self):
        section = [["", "Busqueda aleatoria", "\t", "\t", "Ascenso a la colina", "\t", "\t", "Vecindad var"]]     
        vector = ["Dataset"]   
        for i in range(3):            
            vector.append("Media")
            vector.append("Desviación")
            vector.append("Tasa de exito")
        section.append(vector)        
        for statistics in self.statistics:
            vector = []
            vector.append(statistics[0].name_file)
            for i in range(3):
                vector.append(str(round(statistics[i].average(), 3)))
                vector.append(str(round(statistics[i].std(), 3)))
                vector.append(str(round(statistics[i].successfull_rate(), 3)))
            section.append(vector)
        
        with open(self.root + self.name + self.CSV, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
            writer.writerows(section)

        
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
                html += "<td class='non-select'><span>" + str(round(statistics[i].average(), 3)) + "</span></td>"
                html += "<td class='non-select'><span>" + str(round(statistics[i].std(), 3)) + "</span></td>"
                html += "<td class='non-select'><span>" + str(round(statistics[i].successfull_rate(), 3)) + "</span></td>"
            html += "</tr>"
        html += "</tbody></table></div></div></div></body></html>"

        hs = open(self.root + self.name + self.HTML, 'w')
        hs.write(html)
