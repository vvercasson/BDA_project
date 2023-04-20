import csv
from io import StringIO
import psycopg2
import psycopg2.extras
import getpass


# Pop stats
stats = ['D99_POP','P08_POP','P13_POP','P19_POP']

# CSV Inputs
dept = "newCSVFiles/new_dept.csv"
reg = "newCSVFiles/new_regions.csv"

# CSV Outputs
deptO = "SQL_Files/Procedures/dept.csv"
regO = "SQL_Files/Procedures/reg.csv"

# Tables
reg_pop = 'reg_pop'
dept_pop = 'dept_pop'

dFile = open(deptO,"w+")
rFile = open(regO,"w+")

with open(dept, newline='') as deptCSV:
    deptReader = csv.reader(deptCSV, delimiter=',')
    for row in deptReader:
        for s in stats:
            dFile.write(str(row[0]) + ',' + s + ',' + str(0))
            dFile.write('\n')

with open(reg, newline='') as regCSV:
    regReader = csv.reader(regCSV, delimiter=',')
    for row in regReader:
        for s in stats:
            rFile.write(str(row[0]) + ',' + s + ',' + str(0))
            rFile.write('\n')