# File that creates the csv that will be used to copy from for our DEPARTEMENT

import csv

originalFilename = "originalCSVFiles/v_departement_2023.csv"
filename = "newCSVFiles/new_dept.csv"

def readDeptCsv():
    newFile = open(filename, "w")
    with open(originalFilename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            newFile.write(",".join(row[0:2]))
            newFile.write(',')
            newFile.write(",".join(row[3:]))
            newFile.write('\n')


readDeptCsv()