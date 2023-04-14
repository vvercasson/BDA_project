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
                newFile.write(",".join(row[1:]))
                newFile.write('\n')
readCommuneCSV()