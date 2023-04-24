import psycopg2
import psycopg2.extras
import getpass
import sys

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

attribute = None

def requestCommand(command, args):
   try:
      # Lancement de la requête
      if args is None:
         cur.execute(command)
      else:
         cur.execute(command,args)
   except Exception as e :
      #fermeture de la connexion
      cur.close()
      conn.close()
      exit("error when running: " + command + " : " + str(e))


# New Queries
# Liste des départements d'une région donnée
# Args : Région
def query1():
    print("*** Cette requête permet de listers les départements d'une région donnée ***\n")
    # Input
    inputReg = input("Donnez une région :")
    attribute = (inputReg, )
    
    # Query
    query = "SELECT D.NCC FROM DEPARTEMENT D, REGION R WHERE D.CREG = R.CREG AND R.NCC = %s"
    
    requestCommand(query,attribute)
    
    rows = cur.fetchall()
    output = "La région " + inputReg + " est composé de tous ces départements --> \n"
    for r in rows:
        output += r[0] + '\n'
    print(output)
    
# Liste des communes de plus de X habitants d'un département donné
# Args : Departement - Nombre d'habitants
def query2():
    print("*** Cette requête permet de lister les communes de plus de X habitants d'un département donné ***\n") 
    
    # Input
    inputDept = input("Donnez un département :")
    inputHabitants = input("Donnez un nombre d'habitants minimum :")
    attribute = (inputDept, inputHabitants, )
    
    # Query
    query = "SELECT C.NCC FROM COMMUNE C, DEPARTEMENT D, STATSCOMANNEE S, STATS T WHERE C.CDEPT = D.CDEPT AND S.IDCOM = C.CCOM AND S.IDSTAT = T.IDSTAT AND T.LABEL = 'Population en 2019' AND D.NCC = %s AND S.VALEUR > %s;"
    
    requestCommand(query,attribute)
    
    rows = cur.fetchall()
    output = "Le departement " + str(inputDept) + " possède " + str(len(rows)) + " communes avec plus de " + str(inputHabitants) + "\n Les voici :"
    for r in rows:
        output += r[0] + '\n'
    print(output)

# La region la plus peuplé
# No args
def query3():
   print("*** Cette requête renvoie la region la plus peuplée ***\n") 
   
   # Query
   query = "SELECT R.NCC, SUM(S.VALEUR) as habitants FROM REGION R, COMMUNE C, STATSCOMANNEE S, STATS T WHERE R.CREG = C.CREG AND T.LABEL = 'Population en 2019' AND C.CCOM = S.IDCOM AND S.IDSTAT = T.IDSTAT GROUP BY(R.NCC) ORDER BY habitants DESC LIMIT 1;"

   requestCommand(query, attribute)

   rows = cur.fetchall()
   
   output = "La région le plus peuplée est : " + str(rows[0][0]) + " avec ses " + str(rows[0][1]) + " habitants"
   
   print(output)
   
# La region la moins peuplé
# No args
def query4():
   print("*** Cette requête renvoie la region la moins peuplée ***\n") 
   
   # Query
   query = "SELECT R.NCC, SUM(S.VALEUR) as habitants FROM REGION R, COMMUNE C, STATSCOMANNEE S, STATS T WHERE R.CREG = C.CREG AND T.LABEL = 'Population en 2019' AND C.CCOM = S.IDCOM AND S.IDSTAT = T.IDSTAT GROUP BY(R.NCC) ORDER BY habitants ASC LIMIT 1;"

   requestCommand(query, attribute)

   rows = cur.fetchall()
   
   output = "La region la moins peuplée est : " + str(rows[0][0]) + " avec ses " + str(rows[0][1]) + " habitants"
   
   print(output)


# Invite
print("\n\n")
print("*** Pour les requêtes demandant un département ou une région, le nom doit être saisi en majuscule (exemple:ILE DE FRANCE) ***\n")
print("1 - Lister les départements d'une région donnée")
print("2 - Lister les communes de plus de X habitants d'un département donné")
print("3 - La region la plus peuplée")
print("4 - La region la moins peuplée")
requestedQuery = input("Quelles requête voulez vous executer ? [Taper le numéro]\n")

if requestedQuery == '1':
   query1()
elif requestedQuery == '2':
   query2()
elif requestedQuery == '3':
   query3()
elif requestedQuery == '4':
   query4()

#fermeture de la connexion
cur.close()
conn.close()