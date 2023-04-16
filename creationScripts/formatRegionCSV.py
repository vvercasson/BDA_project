# File that creates the csv that will be used to copy from for our REGIONS

import csv

originalFilename = "originalCSVFiles/v_region_2023.csv"
filename = "newCSVFiles/new_regions.csv"

def readRegionCsv():
    newFile = open(filename, "w")
    with open(originalFilename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            newFile.write(",".join(row[0:1]))
            newFile.write(',')
            newFile.write(",".join(row[2:]))
            newFile.write('\n')


readRegionCsv()