"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  Y25
Noms et matricules : Alexa Kassar(2350528), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

import csv

csvfile= open('collection_bibliotheque.csv', newline='')
collection_initiale = csv.DictReader(csvfile)
bibliotheque ={}
for row in collection_initiale:
    bibliotheque.update({row['cote_rangement']: row['titre'] + " , " + row['auteur']+ " , " + row['date_publication']})

print(f' \n Bibliotheque initiale: {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

csvfile2= open('nouvelle_collection.csv', newline='')
nouvelle_collection = csv.DictReader(csvfile2)
bibliotheque2 = {}

for new_row in nouvelle_collection:
    bibliotheque2.update({new_row['cote_rangement']: new_row['titre'] + " , " + new_row['auteur'] + " , " + new_row['date_publication']})


keys2 = list(bibliotheque2.keys())
keys1 =list(bibliotheque.keys())

for new_key in keys2:

    newlist=[]
    newlist.extend(bibliotheque2[new_key].split(","))

    if new_key in keys1:
        print(f'Le livre {new_key} ---- {newlist[0]} par {newlist[1]} ---- est déjà présent dans la bibliothèque')
    else: 
        bibliotheque[new_key] = bibliotheque2[new_key]  
        print(f'Le livre {new_key} ---- {newlist[0]} par {newlist[1]} ---- a été ajouté avec succès')

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

#1ere etape : acceder aux livres de william shaksperare
#2eme etape modifier le key







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici



