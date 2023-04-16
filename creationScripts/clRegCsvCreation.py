# This file created the file "cl_reg.csv" which is the file required to use copy_from to insert in our CL_REG table

import csv

originalFilename = "originalCSVFiles/v_region_2023.csv"
filename = "newCSVFiles/cl_reg.csv"

def readRegCsv():
    newFile = open(filename, "w")
    with open(originalFilename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            newFile.write(row[1])
            newFile.write(',')
            newFile.write(row[0])
            newFile.write('\n')
readRegCsv()