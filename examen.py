#KOUADIO KOUASSI ROMARIC 

inventaire = []
produit1 = ["Montre", 1, 24]
produit2 =  ["Téléphone", 3, 499.98]
produit3 = [ "Ordinateur", 2, 1499.98]

inventaire.append(produit1) 
inventaire.append( produit2)
inventaire.append( produit3)

def afficher_inventaire():
    print(f"Le produit {inventaire[0][0]} coûte {inventaire[0][2]} pour une quantité de {inventaire[0][1]}")
    print(f"Le produit {inventaire[1][0]} coûte {inventaire[1][2]} pour une quantité de {inventaire[1][1]}")
    print(f"Le produit {inventaire[2][0]} coûte {inventaire[2][2]} pour une quantité de {inventaire[2][1]}")

afficher_inventaire()


def ajouter_produit(nom, quantite, prix):
    produit = [nom, quantite, prix]
    inventaire.append(produit)

ajouter_produit("bonjour", 2, 3)
print(inventaire)

def supprimer_produit(nom, quantite, prix):
    produit = [nom, quantite, prix]
    for i in range(len(inventaire)):
        if produit == inventaire[i]:
            inventaire.remove(produit)


supprimer_produit("bonjour", 2, 3)
print(inventaire)


def modifier_quantite(nom, nouvelle_quantite):
    for i in range(len(inventaire)):
        if inventaire[i][0] == nom:
            inventaire[i][1] = nouvelle_quantite
        else:
            print("le nom de produit n'existe pas")

modifier_quantite("Montre", 5)
print(inventaire)

def valeur_totale_inventaire():
    nombre_type_produit = 0
    valeur_totale = 0
    for i in range(len(inventaire)):
        nombre_type_produit +=1
        valeur_totale += inventaire[i][2] 
    print(f"Il y à en stock {nombre_type_produit} type(s) de produit(s). \n Ce qui fait une valeur totale de {valeur_totale:.2f}l")

valeur_totale_inventaire()

def sauvegarder_inventaire(fichier):
    with open(f"{fichier}.txt", 'a+') as fichier_texte:
        for i in range(len(inventaire)):
            fichier_texte.write(f"{inventaire[i][0]} | {inventaire[i][1]} | {inventaire[i][2]} \n")

sauvegarder_inventaire('env')

def charger_inventaire(fichier):
    with open(f"{fichier}", 'r') as fichier_texte:
        contenu = fichier_texte.read()
        tableau = contenu.replace('|',',')
        
        
        print(inventaire)
        # for i in tableau:
        #     produit = 
        

        
def rechercher_produit(nom):
    for i in range(len(inventaire)):
        if nom == inventaire[i][0]:
            print(f"Produit : {nom}, quantité : {inventaire[i][1]} prix : {inventaire[i][2]} ")
            break

rechercher_produit("Montre")

def afficher_produits_faibles(quantite_min):
    
    for i in range(len(inventaire)):
        if inventaire[i][1] < quantite_min:
            print(inventaire[i])
    
afficher_produits_faibles(6)

def actualiser_prix(pourcentage):
    for i in range(len(inventaire)):
        prix = inventaire[i][2]
        nouveaux_prix = prix + (prix*pourcentage)/100
        inventaire[i][2] = nouveaux_prix


import random

def generer_nom_produit():
    liste1 =  ["Super", "Éco", "Ultra"]
    liste2 = ["Chocolat", "Savon", "Jus"]
    random.shuffle(liste2)
    random.shuffle(liste1)

    nom_generer = liste1[0] + liste2[1]
    print(nom_generer)

generer_nom_produit()

import sys

'''if sys.argv['--faible']:
    afficher_produits_faibles()
elif sys.argv['--total']:
    valeur_totale_inventaire()'''


chaine = "10 boîtes de ceréales à 4.5€"
def extraire_nombres(chaine):
    for i in chaine:
        if i.isdigit():
            print(i)

extraire_nombres(chaine)


def convertir_prix_en_entiers():
    for i in range(len(inventaire)):
        inventaire[i][2] = int(inventaire[i][2])