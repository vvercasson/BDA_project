# This file created the file "cl_dept.csv" which is the file required to use copy_from to insert in our CL8_DEPT table

import csv

originalFilename = "originalCSVFiles/v_departement_2023.csv"
filename = "newCSVFiles/cl_dept.csv"

def readDeptCsv():
    newFile = open(filename, "w")
    with open(originalFilename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            newFile.write(row[2])
            newFile.write(',')
            newFile.write(row[0])
            newFile.write('\n')
readDeptCsv()