"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  L25
Noms et matricules : Alexa Kassar(2350528), Abdoulhakim Abdillahi Ibrahim (2221997)

"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

import csv
#parcourir collection_bibliotheque.csv et le lire comme un dictionnaire

csvfile= open('collection_bibliotheque.csv', newline='')
collection_initiale = csv.DictReader(csvfile)
bibliotheque ={}

#créer la bibliotheque
for row in collection_initiale:
	bibliotheque[row['cote_rangement']] = {"titre":row['titre'], "auteur" : row['auteur'], "date_publication" : row['date_publication']}

print(f' \n Bibliotheque initiale: {bibliotheque} \n')

csvfile.close()

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

#parcourir la nouvelle collection, DictReader permet de la lire comme un dictionnaire

csvfile2= open('nouvelle_collection.csv', newline='')
nouvelle_collection = csv.DictReader(csvfile2)

#accéder aux cotes, titres et auteurs de la nouvelle collection

for new_row in nouvelle_collection:
	cote = new_row['cote_rangement'] 
	titre2 = new_row['titre'] 
	auteur2 = new_row['auteur'] 
	date_publication2 = new_row['date_publication']

	if cote in bibliotheque.keys():
		print(f'Le livre {cote} ---- {titre2} par {auteur2} ---- est déjà présent dans la bibliothèque')

# ajouter les livres qui n'ont pas de doublure dans la bibliothèque

	else:
		bibliotheque[cote] = {"titre": titre2 , "auteur" : auteur2 , "date_publication" : date_publication2}
		print(f'Le livre {cote} ---- {titre2} par {auteur2} ---- a été ajouté avec succès')

csvfile2.close()

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

copie_bibliotheque = bibliotheque.copy()

for key, value in copie_bibliotheque.items():
	if value['auteur'] == "William Shakespeare" and key[0] == "S":
		new_key = key.replace("S" , "WS") #remplacer la cote des livres
		bibliotheque[new_key] = bibliotheque.pop(key) #supprimer l'ancienne key
		
print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# parcourir emprunt.csv comme un dictionnaire 

csvfile3 = open('emprunts.csv', newline='')
liste = csv.DictReader(csvfile3)
liste_emprunt = {}

for column in liste: #création d'une liste de livres empruntés
	liste_emprunt[column['cote_rangement']] = column['date_emprunt']

for cote in bibliotheque.keys(): #vérifier lesquels des livres de la biblio sont empruntés
#ajout de nouvelles clés
	if cote in liste_emprunt.keys():
		bibliotheque[cote]['emprunts'] = "emprunté" 
		bibliotheque[cote]['date_emprunt'] = liste_emprunt[cote]
	else:
		bibliotheque[cote]['emprunts'] = "disponible"
		   
print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')

csvfile3.close()

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

import datetime
from datetime import datetime

now = datetime.now() #date actuelle
livres_en_retard = []
livres_perdus = []

for key, date in liste_emprunt.items():
	for key1 in bibliotheque.keys():
		if key1 == key:
  
			date_emprunt = datetime.strptime(date, '%Y-%m-%d') #convertir en date
			number_of_days = (now - date_emprunt).days  #retard en jours

			if number_of_days >= 365: #trouver les livres perdus
				bibliotheque[key1]["livres_perdus"]= "livre est perdu"
				bibliotheque[key1]["frais_retard"]= "100 $ "
				livres_perdus.append(bibliotheque[key1]["titre"])

			else: 
				bibliotheque[key1]["livres_perdus"]= " ce livre n'est pas perdu"
				

			if number_of_days >30: 
				jours_de_retard = number_of_days - 30 #frais appliquables sur les jours après le delai de retour

			#min compare le frais calculé à la valeur 100 et choisit la plus petite valeur càd : frais max = 100
				frais = min(jours_de_retard*2, 100)
				bibliotheque[key1]["frais_retard"]= str(frais) + " $" 

				#création d'une liste de livres en retard
				livres_en_retard.append(f' Livre: {bibliotheque[key1]["titre"]} , frais de retard: {bibliotheque[key1]["frais_retard"]} $')

			else: 
				bibliotheque[key1]["frais_retard"]= "0 $"

			
		else: 
			bibliotheque[key1]["livres_perdus"]= "livre n'est pas perdu"
			bibliotheque[key1]["frais_retard"]= "0 $"

print("la liste des livres perdus est:",  (livres_perdus))
print("La liste des livres en retard est:", (livres_en_retard))
print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')

