import psycopg2
import psycopg2.extras
import getpass
import sys

# CSV Outputs
deptO = "SQL_Files/Procedures/dept.csv"
regO = "SQL_Files/Procedures/reg.csv"

# Tables
reg_pop = 'reg_pop'
dept_pop = 'dept_pop'

dFile = open(deptO,"r")
rFile = open(regO,"r")

print('Connexion à la base de données...')
USERNAME=input("Saisir le nom d'utilisateur de la base de données : ")
PASS= getpass.getpass('Mot de passe de '+ USERNAME + ':')

try:
    conn = psycopg2.connect("host=pgsql dbname="+ USERNAME+" user="+ USERNAME+ " password="+PASS)
except Exception as e :
    exit("Connexion impossible à la base de données: " + str(e))

print('Connecté à la base de données')

print('Successfull connection')

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Copying all my CSV files into the right table
try:
    cur.copy_from(rFile,reg_pop,sep=',')
    cur.copy_from(dFile, dept_pop, sep=',')
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