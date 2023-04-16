# Creates metadonne csv file

import csv

statsMetaDonne = "originalCSVFiles/stats/metadonne_mayotte.CSV"

filename = "newCSVFiles/stats_table.csv"

def readRegionCsv():
    newFile = open(filename, "w")
    with open(statsMetaDonne, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader)
        for row in spamreader:
            if(row[0] != "CODGEO"):
                newFile.write(row[0])
                newFile.write(',')
                newFile.write(row[2])
                newFile.write('\n')


readRegionCsv()