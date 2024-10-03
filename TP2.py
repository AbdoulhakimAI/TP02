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
liste = csv.DictReader(csvfile3)
liste_emprunt = {}
for column in liste:
	liste_emprunt[column['cote_rangement']] = column['date_emprunt']

for cote in bibliotheque.keys():
	if cote in liste_emprunt.keys():
		bibliotheque[cote]['emprunts'] = "emprunté"
		bibliotheque[cote]['date_emprunt'] = liste_emprunt[cote]
	else:
		bibliotheque[cote]['emprunts'] = "Disponible"
		   
print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')



########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

import datetime
from datetime import datetime

now = datetime.now()
livres_en_retard = []

for key, date in liste_emprunt.items():
  
	date_emprunt = datetime.strptime(date, '%Y-%m-%d')
	number_of_days = (now - date_emprunt).days

	if number_of_days > 365:
		bibliotheque[key]["livres_perdus"]= "livre est perdu"
	
	elif 30 < number_of_days < 365 :
	
		jours_de_retard = number_of_days - 30
		frais = min(jours_de_retard*2, 100)

		bibliotheque[key]["frais_retard"]= frais
		livres_en_retard.append(f' Livre: {bibliotheque[key]["titre"]} , frais de retard: {bibliotheque[key]["frais_retard"]} $')
		
print("La liste des livres en retard est:", (livres_en_retard))
print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')
