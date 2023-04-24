# Compte Rendu du projet de base de données avancées
Réalisé par ITHURBIDE Martin et VERCASSON Victor

*Voici la suite de commande à executer pour initialiser le projet (se positionner à la source du projet):*

1 - éxecuter **\i SQL_Files/CREATE.sql** dans pgsql pour créer les tables (Il existe **DROP.sql** pour les supprimer)

2 - éxecuter le script python de copy : **python3 creationScripts/copyToTables.py**

3 - tester les requêtes : **python3 tpScripts/queries/SQLqueries.py**  (les indications sont précisés à l'éxecution)

4 - pour créer les vues il faut faire **\i SQL_Files/Vues/[nom_vue]** pour chaque fichier se situant dans le dossier des Vues (Il y en a 4)

5 - Pour stocker les populations de departement / region nous avons créer deux nouvelles tables, il faut donc les executer avec **\i SQL_Files/Procedures/ALTER.sql**

6 - Une fois les tables crées il faut les initialiser avec **python3 SQL_Files/Procedures/initPopTables.py**

7 - Maintenant les nouvelles tables remplies, on peut créer les procédures avec : **\i SQL_Files/Procedures/DEPT_POP_PROC.sql** et **\i SQL_Files/Procedures/REG_POP_PROC.sql**

Lors de l'appel de ces fichier SQL, la procédure est appelée une première fois.

8 - Maintenant la partie trigger, pour créer le premier trigger qui bloque les modifications il faut faire : **\i SQL_Files/Triggers/BLOCK_REG_DEPT.sql**

9 - Pour finir la création de la table il manque le trigger qui met à jour la population lors de la modificaton et de l'ajout : **\i SQL_Files/Triggers/UPDATE_POP_TRIGGER.sql**

La partie pratique est finie pour ce qui est de la partie d'explication de requêtes et d'index, rien n'est a éxecuter tous les résultats obtenus on étaient stockées dans les fichier respectif.
Pour le détail des EXPLAIN voir **SQL_Files/EXPLAIN/explain.sql**.
Et pour les index **SQL_Files/INDEX/index.sql**.
L'analyse des résultats se trouve en bas de ce Markdown dans les parties respectives

# 1. Scripts

## 1.1 Scripts de créations/manipulations de CSV

---
*Certaines manipulation ont étés faites sur Excel avant pour retirer les colonnes totalement inutiles dans les csv de departements, communes et regions pour ce projet.*

Les scripts ci-dessous servent à créer les fichier csv adaptés à nos tables afin que l'on puisse utiliser la commande **copy_from(...)** sur les csv crées par ces scripts.

### 1.1.1 - **formatCommuneCSV.py**

Ce scrpit enleve toutes les communes qui ont un code différent de "COM", il s'occupe également de mettre formatter le numero de département et de commune pour que si le département est le "1" alors il se transformera en "01", le principe est le même pour le numéro de commune.

### 1.1.2 - **formatDepartementCSV.py**

Ce script ignore simplement les colonnes qui nous sont inutiles pour notre la création de la table département (c'est à dire qu'on ignore pour le moment le chef lieu)

### 1.1.3 - **formatRegionCSV.py**

Exactement, le même principe que le formatDepatement au dessus.

### 1.1.4 - **clDeptCsvCreation.py**

Ce script sert à récuperer le numéro de commune qui est le chef lieu d'un département afin d'en faire un CSV avec seulement ces deux informations.

### 1.1.5 - **clRegCsvCreation.py**

Même principe que le script au dessus mais pour le chef lieu d'une région.


### 1.1.6 - **statsCsvCreation.py**

Ce script est utilisé pour créer la table STATS, en effet le fichier csv des statistiques comporte beaucoup de colonnes hors pour notre table on ne gardera que la colonne COD_VAR et LIB_VAR_LONG

### 1.1.7 - **linkStats.py**

Ce script sert à fusionner les statistiques de la France hors DOM et les statistiques avec Mayotte (Cela aurait pu être facilement fait sur Excel)

### 1.1.8 - **communeStatsCsvCreation.py**

Ce script prend le csv crée par le script précedent et vas venir enlever toutes les statistiques qui ne nous interessent pas (On ne gardera que les dix suivantes : P19_POP,P13_POP,P08_POP,D99_POP,NAIS1319,NAIS0813,DECE0813,DECE9908,P08_LOG,D99_LOG)

### 1.1.9 - **formatStats.py**

Ce script sert à créer les fichiers CSV suivants : **commAnneeStat.csv** et **commInterStat.csv**. Ce script de séparer nos stats entre celles qui utilisent une année et celles qui utilisent une intervalle afin de pouvour créer nos tables : **STATSCOMANNEE** et **STATSCOMINTER**

## 1.2 Scripts d'alimentation de base de données

---
### 1.2.1 - **copyToTables.py**

Ce scripts utiles nos les fichiers csv qui ont été crées au dessus par nos scripts de créations de CSV afin de pouvoir utiliser la fonction **copy_from(...)** de psycopg2.

## 1.3 Scripts de requêtage

---

### 1.3.1 - **SQLqueries.py**

Ce fichier répond à la partie 1 du TP sur les divers requête a faire.
Les requêtes sont expliqués lors de l'éxecution après s'être connecté.

# 2. Fichiers SQL

## 2.1 Vues

---

### 2.1.1 - **POPDEPT.sql**

Création d'une vue qui renvoie toutes les stats concernant la population pour les départements.

### 2.1.2 - **POPREG.sql**

Même chose que le fichier **POPDEPT.sql** au dessus mais pour les régions.

### 2.1.3 - **STATDEPT.sql**

Dans ce fichier on crée une Vue qui renvoie toutes les stats pour chaque departement que ca soit une stat sur une intervalle ou sur une année précise.

### 2.1.4 - **STATREG.sql**

Même principe que **STATDEPT.sql**, on renvoie toutes les stats mais pour les regions cette fois-ci.

## 2.2 Prodécures

---

### 2.2.1 **ALTER.sql**

Ce fichier sert à créer les deux tables utilisés pour stocker les population pour les régions ainsi que pour les départements.

### 2.2.2 **DEPT_POP_PROC.sql** et **REG_POP_PROC.sql**

Ces deux fichiers servent a créer les procédures qui vont ajouter à nos tables DEPARTEMENTS et REGION la population qu'ils avaient en 2019.

## 2.3 Triggers

---

### 2.3.1 **BLOCK_REG_DEPT.sql**

Ce fichier SQL créer une fonction qui retourne une erreur lors ce qu'elle est appelé.

Et on crée 2 trigger (un pour les regions un pour les départements) pour que lorsque l'on va insert, update ou delete on va venir appeler notre fonction qui renvoie une erreur et l'action ne sera pas réalisée.

### 2.3.2 **UPDATE_POP_TRIGGER.sql**

Ce fichier comprend un trigger et une fonction.

Le trigger "update_population_on_statsAnnee_update", execute la fonction "refresh_pop_on_both_tables" après un UPDATE ou un INSERT dans la table STATSCOMANNEE. Il l'execute que dans le cas où on traite d'une population.

La fonction "refresh_pop_on_both_tables" est la fonction qui est executée et elle permet de mettre des conditions pour l'ajout ou la modification d'une commune.
Si pour un département, il n'y a pas toutes les populations des communes, alors l'update des départements et régions n'est pas fait.
Dans l'autre cas, l'update est fait avec succès. 

## 2.4 Explain

---

**Pour voir les résultats des requêtes avec le explain, il faut consulter le fichier SQL_Files/EXPLAIN/explain.sql**.

Lors de nos tests, nous avons remarquer que lorsqu'on fait une jointure entre deux tables relativement petites, le système va préferer un système de boucle imbriquée.

Alors que dans tous les autres cas il préfere utiliser une jointure par hachage.

Cependant nous n'avons pas réussi à forcer l'utilisation d'autres algorithmes tels que le tri fusion malgré le fait que nous avons créer des requêtes qui seraient a priori avantager par un tri fusion. Nous expliquons ça par le coût fort qu'un tri fusion peut representer sur de grandes tables.

## 2.5 Index

---

**Pour voir les résultats des requêtes avec explain et les index, il faut consulter le fichier SQL_Files/INDEX/index.sql**.

On sait qu'une clé primaire est un Index car lorsqu'on regarde les index d'une table sur phpPgAdmin, un index est créer pour chaque table et il prends tous les attributs qui compose la clé primaire.

En ajoutant des index sur les attributs habitants de DEPT_POP et REG_POP, on remarque une augmentation du temps de planning de la requête mais cependant le temps d'éxecution est plus cours. Dans notre exemple la différence n'est pas très importante mais cependant si on fait grossir la taille des tables le temps d'éxecution sera largement plus intéressant avec un index que sans.

Pour ce qui est de l'exemple qui liste les communes avec moins de 5000 habitants, on observe le même comportement que l'exemple précedent. Le système prend plus de temps à planifier la requête mais gagne en temps sur l'éxecution.
