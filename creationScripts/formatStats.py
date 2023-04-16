# Formats the statsRequired file in order to use copy from on the two csv files generated

import csv

# CSV Inputs
stats = "newCSVFiles/statsRequired.csv"
communes = "newCSVFiles/new_communes.csv"

# CSV Outputs
anneeStatsFilename = "newCSVFiles/commAnneeStat2.csv"
interStatsFilename = "newCSVFiles/commInterStat2.csv"

list = []

def readStatsCSVs():
    # FILES
    anneeStats = open(anneeStatsFilename, "w")
    interStats = open(interStatsFilename, "w")
        
    # STATS
    statsList = ["P19_POP","P13_POP","P08_POP","D99_POP","NAIS1319","NAIS0813","DECE0813","DECE9908","P08_LOG","D99_LOG"]
    
    statsAnnee = ["P19_POP","P13_POP","P08_POP","D99_POP","P08_LOG","D99_LOG"]
    statsAnneeValue = [2019,2013,2008,1999,2008,1999]
        
    statsInter = ["NAIS1319","NAIS0813","DECE0813","DECE9908"]
    statsInterValues = [[2013,2019], [2008,2013], [2008,2013], [1999,2008]]    

    with open(stats, newline='') as requiredStats:
        statsReader = csv.reader(requiredStats, delimiter=',')
        next(statsReader)
        with open(communes, newline='') as comms:
            comsReader = csv.reader(comms, delimiter=',')
            next(comsReader)
            for row in comsReader:
                list.append(row[0])
            for row in statsReader:
                if row[0] in list:
                    for stat in statsList:
                        idx = statsList.index(stat)
                        if stat in statsAnnee:
                            idxInSubList = statsAnnee.index(stat)
                            anneeStats.write(row[0])
                            anneeStats.write(',')
                            anneeStats.write(str(statsAnneeValue[idxInSubList]))
                            anneeStats.write(',')
                            anneeStats.write(stat)
                            anneeStats.write(',')
                            anneeStats.write(row[idx+1])
                            anneeStats.write('\n')
                        elif stat in statsInter:
                            idxInSubList = statsInter.index(stat)
                            interStats.write(row[0])
                            interStats.write(',')
                            interStats.write(str(statsInterValues[idxInSubList][0]))
                            interStats.write(',')
                            interStats.write(str(statsInterValues[idxInSubList][1]))
                            interStats.write(',')
                            interStats.write(stat)
                            interStats.write(',')
                            interStats.write(row[idx+1])
                            interStats.write('\n')
                        else:
                            print("Error : some stats are missing in the sub lists")
                            return
                

readStatsCSVs()