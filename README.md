# Compte Rendu du projet de base de données avancées
Réalisé par ITHURBIDE Martin et VERCASSON Victor

# 1. Scripts

## 1.1 Scripts de créations/manipulations de CSV
---
*Certaines manipulation ont étés faites sur Excel avant pour retirer les colonnes totalement inutiles dans les csv de departements, communes et regions pour ce projet*

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

### 1.2.1 - **copyToTables.py**

Ce scripts utiles nos les fichiers csv qui ont été crées au dessus par nos scripts de créations de CSV afin de pouvoir utiliser la fonction **copy_from(...)** de psycopg2.

### 1.2.2 - **copyStatsToDb.py**

Même principe que le copyToTable au dessus mais celui ci ne copie que les stats

# Fichiers SQL

## Vues
