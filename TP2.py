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
    bibliotheque[row['cote_rangement']] = {"titre":row['titre'], "auteur" : row['auteur'], "date_publication" : row['date_publication']}

    #bibliotheque.update({row['cote_rangement']: row['titre'] + " , " + row['auteur']+ " , " + row['date_publication']})

print(f' \n Bibliotheque initiale: {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

csvfile2= open('nouvelle_collection.csv', newline='')
nouvelle_collection = csv.DictReader(csvfile2)


for new_row in nouvelle_collection:
    cote = new_row['cote_rangement']
    titre2 = new_row['titre'] 
    auteur2 = new_row['auteur'] 
    date_publication2 = new_row['date_publication']

    if cote in bibliotheque.keys():
        print(f'Le livre {cote} ---- {titre2} par {auteur2} ---- est déjà présent dans la bibliothèque')
    else:
        bibliotheque[cote] = {"titre": titre2 , "auteur" : auteur2 , "date_publication" : date_publication2}
        print(f'Le livre {cote} ---- {titre2} par {auteur2} ---- a été ajouté avec succès')
    
########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

copie_bibliotheque = bibliotheque.copy()

for key, value in copie_bibliotheque.items():
    if value['auteur'] == "William Shakespeare" and key[0] == "S":
        new_key = key.replace("S" , "WS")
        bibliotheque[new_key] = bibliotheque.pop(key)
        

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

csvfile3 = open('emprunts.csv', newline='')
liste_emprunt = csv.DictReader(csvfile3)

emprunts= {}

    cote_rangement = row1['cote_rangement']
    date_emprunt = row1['date_emprunt']

    for key_emprunt in bibliotheque.keys():
        if key_emprunt in cote_rangement:
            bibliotheque[key_emprunt]['emprunts'] = "emprunté"
            bibliotheque[key_emprunt]['date_emprunt'] = date_emprunt
        else:
            bibliotheque[key_emprunt]['emprunts'] = "disponible"

print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici
