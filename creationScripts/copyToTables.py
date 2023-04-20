# File that copies our CSV files to our database for REG,DEPT,COM,CL_DEPT,CL_REG

from io import StringIO
import psycopg2
import psycopg2.extras
import getpass
from connexionScript import *

# FILENAMES
communesFilename = open('newCSVFiles/new_communes.csv', 'r')
departementFilename = open('newCSVFiles/new_dept.csv', 'r')
regionsFilename = open('newCSVFiles/new_regions.csv', 'r')
clDeptFilename = open('newCSVFiles/cl_dept.csv', 'r')
clRegFilename = open('newCSVFiles/cl_reg.csv', 'r')

# STATS FILENAMES
stats = open('newCSVFiles/required_stats_table.csv', 'r')
statsAnnee = open('newCSVFiles/commAnneeStat.csv', 'r')
statsInter = open('newCSVFiles/commInterStat.csv', 'r')

# TABLES NAME
regionTable = 'region'
deptTable = 'departement'
communeTable = 'commune'
clDeptTable = 'cldept'
clRegTable = 'clreg'

# STATS TABLES NAME
statsTable = 'stats'
statsAnneeTable = 'statscomannee'
statsInterTable = 'statscominter'

# Connection to my database
print('Connexion à la base de données...')
USERNAME=input("Saisir le nom d'utilisateur de la base de données : ")
PASS= getpass.getpass('Mot de passe de '+ USERNAME + ':')

try:
    conn = psycopg2.connect("host=pgsql dbname="+ USERNAME+" user="+ USERNAME+ " password="+PASS)
except Exception as e :
    exit("Connexion impossible à la base de données: " + str(e))

print('Connecté à la base de données')

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Copying all my CSV files into the right table
try:
    cur.copy_from(regionsFilename,regionTable,sep=',')
    cur.copy_from(departementFilename, deptTable, sep=',')
    cur.copy_from(communesFilename,communeTable,sep=',')
    cur.copy_from(clDeptFilename,clDeptTable, sep=',')
    cur.copy_from(clRegFilename, clRegTable, sep=',')
    cur.copy_from(stats,statsTable,sep=',')
    cur.copy_from(statsAnnee, statsAnneeTable, sep=',')
    cur.copy_from(statsInter,statsInterTable,sep=',')
except Exception as e:
   cur.close()
   conn.close()
   exit("FAILURE --> Copy From : " + str(e))

# Comitting the change
conn.commit()

print("The copies where done correctly.")

# Disconnecting
cur.close()
conn.close()