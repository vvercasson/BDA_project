# File that copies our CSV files to our database for STATS

from io import StringIO
import psycopg2
import psycopg2.extras
import getpass

# FILENAMES
stats = open('newCSVFiles/required_stats_table.csv', 'r')
statsAnnee = open('newCSVFiles/commAnneeStat2.csv', 'r')
statsInter = open('newCSVFiles/commInterStat2.csv', 'r')

# TABLES NAME
statsTable = 'stats'
statsAnneeTable = 'statscomannee'
statsInterTable = 'statscominter'

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

# Copying all my CSV files into the right table
try:
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