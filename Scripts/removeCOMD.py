import csv

filename = "../newCSVFiles/new_communes.csv"

def readCommuneCSV():
    newFile = open(filename, "x")
    with open('../CSV_Files/v_commune_2023.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[0] in {'COM','TYPECOM'}:
                newFile.write(",".join(row[1:-1]))
                newFile.write('\n')
readCommuneCSV()