from io import StringIO
import psycopg2
import psycopg2.extras
import getpass

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

# Connection to my database
print('Logging to the databse...')
USERNAME="vvercasson"
PASS= getpass.getpass('Password for '+ USERNAME + ':')

try:
   conn = psycopg2.connect("host=pgsql dbname="+ USERNAME+" user="+ USERNAME+ " password="+PASS)
except Exception as e :
   exit("Connection failed to the database : " + str(e))

print('Successfull connection')

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Copyign all my CSV files into the right table
try:
    cur.copy_from(regionsFilename,regionTable,sep=',')
    cur.copy_from(departementFilename, deptTable, sep=',')
    cur.copy_from(communesFilename,communeTable,sep=',')
    cur.copy_from(clDeptFilename,clDeptTable, sep=',')
    cur.copy_from(clRegFilename, clRegTable, sep=',')
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