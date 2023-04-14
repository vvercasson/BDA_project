from io import StringIO
import psycopg2
import psycopg2.extras
import getpass
import sys

# FILENAMES
communesFilename = open('newCSVFiles/new_communes.csv', 'r')
departementFilename = open('newCSVFiles/new_dept.csv', 'r')
regionsFilename = open('newCSVFiles/new_regions.csv', 'r')
clDeptFilename = open('newCSVFiles/cl_dept.csv', 'r')
clRegFilename = open('newCSVFiles/cl_reg.csv', 'r')

# TABLES NAME
regionTable = 'region'
deptTable = 'departement'
communeTable = 'commune'
clDeptTable = 'cldept'
clRegTable = 'clreg'

# Try to connect to an existing database
print('Connexion à la base de données...')
USERNAME="vvercasson"
PASS= getpass.getpass('Password for '+ USERNAME + ':')

try:
   conn = psycopg2.connect("host=pgsql dbname="+ USERNAME+" user="+ USERNAME+ " password="+PASS)
except Exception as e :
   exit("Connexion impossible à la base de données: " + str(e))

print('Connecté à la base de données')

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# ------------------------ #

try:
    cur.copy_from(regionsFilename,regionTable,sep=',')
    cur.copy_from(departementFilename, deptTable, sep=',')
    cur.copy_from(communesFilename,communeTable,sep=',')
    cur.copy_from(clDeptFilename,clDeptTable, sep=',')
    cur.copy_from(clRegFilename, clRegTable, sep=',')
except Exception as e:
   cur.close()
   conn.close()
   exit("Copy from echec : " + str(e))

conn.commit()

print("Copy From was succesfull for Region table")

# ------------------------ #

# Disconnecting

cur.close()
conn.close()