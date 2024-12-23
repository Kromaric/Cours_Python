# Exerce 1.1
'''
print("Exerce 1.1".center(50, "-"))
nom = input("Veillez entrer votre nom: ")
age = input("veillez entrer votre age: ")
ville = input("veillez entrer votre ville: ")
print("Bonjour ", nom, "vou avez", age, "ans et vous habitez ", ville)
'''
# Exerce 1.2
'''
print("Exerce 1.2".center(50, "-"))
note = input("veillez entrer votre note sur 20: ")
connexion_status = True
distance_killometre  = input("veillez entrer la distance en killomèttre")
print("Votre note est de :",note,"/20")
print("Statut de la connexion: ", connexion_status)
print("Distance parcourue: ", distance_killometre,"Km")
'''
# Exerce 1.3
'''
print("Exerce 1.3".center(50, "-"))
entier = 12
flotant = 3.5
chaine = "bien"
booleen = False
print(type(entier))
print(type(flotant))
print(type(chaine))
print(type(booleen))
'''

# Exerce 1.4
"""
print("Exerce 1.4".center(50, "-"))
print("2nom : correction(nom2)")
print("age\_utilisateur : correction(age_utilisateur)")
print("total-prix: correction(total_prix")
print("if : correction(si)")
"""

# Exerce 1.5
'''
print("Exerce 1.5".center(50, "-"))
nom = input("Veillez entrer votre nom: ")
age = int(input("Veillez entrer votre âge: "))
annee_etude = int(input("Veillez entrer votre nombre d'années d'étude: "))
annee_etude = age - annee_etude
annee_debut = 2024 - age + annee_etude
print("Résumé !".center(20, "_"))
print("Vous êtes M.", nom+',', "vous avez ", age, "ans et vous avez commencé vos études à ", annee_etude, "ans c'est-à-dire en ", annee_debut )

'''

# Exerce 1.6
'''
print("Exerce 1.6".center(50, "-"))
entier = int(input("veillez entrer un entier: "))
flotant = float(input("veillez entrer un flotant: "))
chaine = input("veillez entrer une chaine de caractère: ")
booleen = bool(input("veillez entrer un booleen: "))

print(f"{entier}: {type(entier)}")
print(f"{flotant}: {type(flotant)}")
print(f"{chaine}: {type(chaine)}")
print(f"{booleen}: {type(booleen)}")

# if entier + flotant :
#     print("entier + flotant possible")
# else:
#     print("entier + flotant impossible")

# if chaine + booleen :
#     print("chaine + booleen possible")
# else:
#     print("chaine + booleen impossible")

# if flotant + booleen :
#     print("flotant + booleen possible")
# else:
#     print("flotant + booleen impossible")

# if chaine + entier :
#     print("chaine + entier possible")
# else:
#     print("chaine + entier impossible")

# if chaine + flotant :
#     print("chaine + flotant possible")
# else:
#     print("chaine + flotant impossible")

# if entier + booleen :
#     print("entier + booleen possible")
# else:
#     print("entier + booleen impossible")

'''
   
# Exerce 1.7  
'''  
print("Exerce 1.7".center(50, "-"))
print("user: correcte")
print("IF : incorrecte parce que c'est une mot réservé. Correction(si)")
print("Total : pas d'erreur mais pas conseillé à cause de la majuscule en debut. Correction(total)")
print("résultat: pas d'erreur mais pas conseillé à cause de l'accentuation. Correction(resultat)")
print("RETOUR : pas d'erreur mais pas conseillé parce que c'est en majuscule. Correction(retour)")
print("ma valeur: erreur. pas d'espace dans le nom d'une variable. Correction(ma_valeur)")
print("ma_variaBLE : pas d'erreur mais pas conseillé. Correction(ma_variable)")
'''
# Exerce 1.8
'''
print("Exerce 1.8".center(50, "-"))
prix_unitaire = float(input("veillez entrer le prix unitaire: "))
quantité = float(input("veillez entrer la quantité: "))
taxe = float(input("veillez entrer la taxe: "))
total = prix_unitaire * quantité + taxe
print(f"Total = {prix_unitaire} * {quantité} + {taxe}")
print(f"Total = {total}")
'''
# Exerce 2.1
'''
print("Exerce 2.1".center(50, "-"))
fonds_investis = float(input("veillez entrer le fonds investis: "))
fonds_epargne =  float(input("veillez entrer le fonds epargne: "))
if fonds_investis > fonds_epargne:
    print("le fonds investis est plus grand que le fonds epargne")
else:
    print("le fonds investis est plus petit que le fonds epargne")
'''
# Exerce 2.2
'''
print("Exerce 2.2".center(50, "-"))
longueur = float(input("veillez entrer la longueur du rectangle en mètres: "))
largeur = float(input("veillez entrer la largeur du rectangle en mètres: "))
print(f"Le perimetre du rectangle est : Longueur * 2 + Largeur * 2 = {longueur} * 2 + {largeur} * 2")
print(f"Le perimetre du rectangle est : {(longueur * 2) + (largeur * 2)} m")
print()
print(f"L'aire du rectangle est : Longueur * Largeur = {longueur}*{largeur}")
print(f"L'aire du rectangle est : {longueur * largeur} m2")
'''
# Exerce 3.1
'''
print("Exerce 3.1".center(50, "-"))
entier = int(input("veillez entrer un entier: "))
chaine = input("veillez entrer une chaine de caractère: ")
flotant = float(input("veillez entrer un flotant: "))
if type(entier) == int:
    print(f"{entier} est un entier")

if type(chaine) == str:
    print(f"{chaine} est une chaine de caractère")

if type(flotant) == float:
    print(f"{flotant} est un flotant")

# Exerce 3.2
print("Exerce 3.2".center(50, "-"))
annee_naissance  = int(input("veillez entrer votre année de naissance: "))
age = 2024 - annee_naissance
if age >= 18:
    print(f"vous avez {age} ans")
    print("vous vous êtes majeur")
else:
    print(f"vous avez {age} ans")
    print("vous êtes mineur")
'''

# Exerce 3.3
'''
print("Exerce 3.3".center(50, "-"))
nombre1 = int(input("veillez entrer un premier nombre: "))
nombre2 = int(input("veillez entrer un deuxieme nombre: "))
print("1. addition (+)")
print("2. soustraction (-)")
print("3. multiplication (*)")
print("4. division (/)")
choix = int(input("veillez choisir une opération: "))

if choix == 1:
    print(f"{nombre1} + {nombre2} = {nombre1 + nombre2}")
elif choix == 2:
    print(f"{nombre1} - {nombre2} = {nombre1 - nombre2}")
elif choix == 3:    
    print(f"{nombre1} * {nombre2} = {nombre1 * nombre2}")
elif choix == 4:
    if nombre2 == 0:
        print("vous ne pouvez pas diviser par 0")
    else:
        print(f"{nombre1} / {nombre2} = {nombre1 / nombre2}")
else:
    print("choix incorrect")
'''

# Exerce 3.4
'''
print("Exerce 3.4".center(50, "-"))
temperature = float(input("Veillez entrer la température: "))
print("1. Celsius(C)")
print("2. Fahrenheit(F)")
unite_temperature = input("veillez choisir l'unité de la temperature: ")
if unite_temperature == 1:
    # conversion en Fahrenheit
    temperature = (temperature * 9/5) + 32
    print("la température que vous avez entrer correspond à : {temperature}")
elif unite_temperature == 2:
    temperature = (temperature * 5/9) - 32
    print("la température que vous avez entrer correspond à : {temperature}")
else: 
    print("Choix invalide")
'''

# Exerce 6.2
'''
print("Exerce 3.5".center(50, "-"))
liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10]
liste3 = [11, 12, 13, 14, 15]
total_liste = liste1 + liste2 + liste3
print(f"Total: {total_liste}")
print(f"Longueur: {len(total_liste)}")
print(f"Minimum: {min(total_liste)}")
print(f"Maximum: {max(total_liste)}")
print(f"Moyenne: {sum(total_liste) / len(total_liste)}")
'''

# Exerce 6.3
'''
print("Exerce 3.6".center(50, "-"))
liste4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

liste5 = list(input("veillez entrer une sous-liste de chiffre: "))
print(liste4[int(liste5[0]):int(liste5[-1])])
if liste4[int(liste5[0]):int(liste5[-1])]:
    print("la sous-liste existe dans la lste principale")
else:
    print("la sous-liste n'existe pas dans la liste principale")

'''
# Exerce 6.4
'''
print("Exerce 3.7".center(50, "-"))
liste6 = [1, 2, 3, 4, 5]
'''
# Exerce de cours
'''
for i in range(21):
    if i % 2 == 0:
        print(i)

password = "azerty"
while True:
    user_password = input("veillez entrer un mot de passe: ")
    if user_password == password:
        print("mot de passe correct")
        break
    else:
        print("mot de passe incorrect ! Veillez réessayer")


while True:
    nombre = float(input("veillez entrer un nombre : "))
    if nombre > 0:
        print("Le nombre est positif")
    elif nombre < 0:
        print("Le nombre est negatif")
    elif nombre == 0:
        print("le nombre est nul")
    else:
        print("entree incorrecte")
'''
# Exerce 7.1
'''
print("Exerce 7.1".center(50, "-"))
for i in range(1, 11):
    print(i)
'''
# Exerce 7.2
'''
print("Exerce 7.2".center(50, "-"))
total = 0
N = int(input("veillez entrer un nombre: "))
for i in range(N + 1):
    total += i
print(total)
'''

# Exercice 7.3
'''
print("Exerce 7.3".center(50, "-"))
liste  = list(range(10))
compteur = 0
liste2 = []
print(type(liste2))
for i in range(10):
    if liste[i] > 5:
        print(liste[i]) 
        liste2.append(liste[i])

print("le nombre d'element supérieur à 5 est {}".format(len(liste2)))
print(f"la liste d'element supérieur à 5 est {liste2}")
'''

# Exercice 7.4
'''
print("Exerce 7.4".center(50, "-"))
liste = list(range(10))
i = 0
max = liste[0]
while i < len(liste):
    if liste[i] > max:
        max = liste[i]
    i += 1
print(f"le maximum est: {max}")
'''
# Exercice 7.5
'''
print("Exercice 7.5".center(50, "-"))
liste = ['A', 'B', 'C', 'D', 'E']
for i in range(1, len(liste)+1):
    print(liste[-i])
'''
#Exercice 7.6
'''
print("Exercice 7.6".center(50, "-"))
liste = list(range(5, 10))
print(liste)
for i in range(len(liste)):
    liste[i] = (liste[i])*2
print(liste)
'''

#Exercice 7.7
'''
print("Exercice 7.7".center(50, "-"))
import random
liste = list(range(1,11))
chance = 0
while chance < 3:
    liste2 = random.shuffle(liste)
    nombre_secret = liste[1]
    choix = int(input("veillez entrer un nombre entre 1 et 10: "))

    if choix == nombre_secret:
        print("vous avez gagner")
        break    
    elif chance == 2:
        print("vous avez perdu")
    else:
        print("Réessayez encore")
        
    chance +=1
'''

#Exercice 7.8
'''
print("Exercice 7.8".center(50, "-"))
nombre  = int(input("veillez entrer un nombre positif: ")) 
'''

#exercice de cours
'''
from pathlib import Path
mon_fichier = Path("texte.txt")

mon_fichier.write_text("Bienvenue à l'écolte-IT") 

contenu = mon_fichier.read_text() 
print(contenu)
print(mon_fichier.exists())
 '''

    
'''with open("texte.txt", "a+") as mon_fichier:
    mon_fichier.write("Bienvenue à l'écolte-IT\n je suis un programmeur\n niveau debutant")
    contenu = mon_fichier.read()
    print(contenu)

phrase =input("veillez saisir votre phrase à imprimer: ")
with open("phrase.txt", "a") as ma_phrase:
    ma_phrase.write(phrase)
'''
