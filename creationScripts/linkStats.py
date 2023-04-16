# Links non-mayotte and mayotte stats

import csv

mayotteFilename = "originalCSVFiles/stats/stats_avec_mayotte.CSV"
notMayotteFilename = "originalCSVFiles/stats/stats_sans_mayotte.CSV"

filename = "newCSVFiles/stats.csv"
def readStatCsv():
    newFile = open(filename, "w")
    with open(mayotteFilename, newline='') as csvfileMayotte:
        with open(notMayotteFilename, newline='') as csvfileNotMayotte:

        # NOT MAYOTTE
            spamreader = csv.reader(csvfileNotMayotte, delimiter=';')
            for row in spamreader:
                newFile.write(';'.join(row))
                newFile.write('\n')

        # MAYOTTE
            spamreader = csv.reader(csvfileMayotte, delimiter=';')
            next(spamreader)
            for row in spamreader:
                newFile.write(';'.join(row))
                newFile.write('\n')

readStatCsv()