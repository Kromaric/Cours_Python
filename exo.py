import csv
from pathlib import Path


'''
with open("test.csv", "r+") as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(["Bonjour je en 3ème anné de license", "Je m'entraine aujourd'hui sur les fichiers python", "Les fichier csv sont particulièrement adorable", "surtout quand on les manipule en python "])
    fichier_csv.seek(0)
    posk = fichier_csv.tell()
    #contenu = fichier_csv.read()
    contenu = csv.reader(fichier_csv, delimiter=',')

    for i in contenu:
        print("La position du curseur est ", posk)
        print(i)'''

with open("test1.txt", "r+") as fichier_texte:
    contenu = fichier_texte.read()
    print(contenu)
    fichier_texte.write("Bonjour je en 3ème anné de license \nJe m'entraine aujourd'hui sur les fichiers python\nLes fichier csv sont particulièrement adorable\nsurtout quand on les manipule en python ")


