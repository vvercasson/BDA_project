# 1. Scripts

## 1.1 Scripts de créations/manipulations de CSV

*Certaines manipulation ont étés faites sur Excel avant pour retirer les colonnes totalement inutiles pour ce projet*

Les scripts ci-dessous servent à créer les fichier csv adaptés à nos tables afin que l'on puisse utiliser la commande **copy_from(...)** sur les csv crées par ces scripts.

### 1.1.1 **formatCommuneCSV.py**

Ce scrpit enleve toutes les communes qui ont un code différent de "COM", il s'occupe également de mettre formatter le numero de département et de commune pour que si le département est le "1" alors il se transformera en "01", le principe est le même pour le numéro de commune.

### 1.1.2 **formatDepartementCSV.py**
Ce script ignore simplement les colonnes qui nous sont inutiles pour notre la création de la table département (c'est à dire qu'on ignore pour le moment le chef lieu)

### 1.1.3 **formatRegionCSV.py**

Exactement, le même principe que le formatDepatement au dessus.

### 1.1.4 **clDeptCsvCreation.py**

Ce script sert à récuperer le numéro de commune qui est le chef lieu d'un département afin d'en faire un CSV avec seulement ces deux informations.

### 1.1.5 **clRegCsvCreation.py**

Même principe que le script au dessus mais pour le chef lieu d'une région.

## 1.2 Scripts d'alimentation de base de données

### 1.2.1 **copyToTables.py**

Ce scripts utiles nos les fichiers csv qui ont été crées au dessus par nos scripts de créations de CSV afin de pouvoir utiliser la fonction **copy_from(...)** de psycopg2.