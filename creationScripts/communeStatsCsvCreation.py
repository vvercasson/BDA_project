# This file creates a CSV file with only the few stats we only want to work with

import csv

# CSV Inputs
statsTableCsv = "newCSVFiles/stats.csv"

# CSV Outputs
selectStats = "newCSVFiles/statsRequired.csv"

def readStatsCSVs():
    file = open(selectStats,"w")
    
    with open(statsTableCsv, newline='') as statsCSV:
        statsReader = csv.reader(statsCSV, delimiter=';')
        for row in statsReader:
            file.write(",".join(row[:5]))
            file.write(',')
            file.write(",".join(row[10:12]))
            file.write(',')
            file.write(",".join(row[18:20]))
            file.write(",")
            file.write(",".join(row[26:28]))
            file.write('\n')

readStatsCSVs()