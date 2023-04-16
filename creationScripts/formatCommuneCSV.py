# File that creates the csv that will be used to copy from for our COMMUNES

import csv

originalFilename = "originalCSVFiles/v_commune_2023.csv"
filename = "newCSVFiles/new_communes.csv"

def readCommuneCSV():
    newFile = open(filename, "w")
    with open(originalFilename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            if row[0] in {'COM','TYPECOM'}:
                if len(row[3]) == 1:
                    row[3] = "0" + row[3]
                if len(row[1]) < 5:
                    row[1] = "0" + row[1]
                newFile.write(",".join(row[1:]))
                newFile.write('\n')
readCommuneCSV()