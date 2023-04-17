import psycopg2
import psycopg2.extras
import getpass

def connect():
    print('Connexion à la base de données...')
    USERNAME=input("Saisir le nom d'utilisateur de la base de données : ")
    PASS= getpass.getpass('Mot de passe de '+ USERNAME + ':')

    try:
        conn = psycopg2.connect("host=pgsql dbname="+ USERNAME+" user="+ USERNAME+ " password="+PASS)
    except Exception as e :
        exit("Connexion impossible à la base de données: " + str(e))

    print('Connecté à la base de données')
    
    return conn