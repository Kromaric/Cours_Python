"""with open("fichier1.txt", 'w+') as fichier1, open("fichier2.txt", 'w+') as fichier2:
    fichier1.write("bonjour je suis de retour e ville \n passe me voir si tu as un bout de temps")
    fichier2.write("bonjour je suis de retour  ville \n passe me voir si tu as un bout de temps")
    fichier1.seek(0)
    fichier2.seek(0)
    contenu1 = fichier1.read()
    contenu2 = fichier2.read()
    test1 = contenu1.split('\n')
    test2 = contenu2.split('\n')


    #print(contenu1[8])
    print(len(contenu1.split('\n')))
    print(len(contenu2.split('\n')))
    for i in range(1,len(test1)):
        for j in range(1,len(test2)):
            if test1[i] == test2[j]:
                print(f" contenu1 : {test1[i]}")
                print(f" contenu2 : {test2[j]}")
                print(f" index contenu1 : {i} & index conten2 : {j} Oui")
            else :
                continue   
"""


with open("fichier1.txt", "r+") as f1, open("fichier2.txt", "r+") as f2:
    f1.write("Bonjour contenu 1 !\nComment ça va ?")
    f2.write("Bonsoir contenu 2 !\nComment ça va ?")
    f1.seek(0)
    f2.seek(0)
    if f1.readline() != f2.readline():
        print("La ligne 1 est différente !")
    else:
        print("La ligne 1 est identique")

    if f1.readline() != f2.readline():
        print("La ligne 2 est  différente !")
    else:
        print("La ligne 2 est identique !")


with open("fichier1.txt", 'w+') as fichier1, open("fichier2.txt", 'w+') as fichier2:
    fichier1.write("bonjour je suis de retour e ville \n passe me voir si tu as un bout de temps")
    fichier2.write("bonjour je suis de retour  ville \n passe me voir si tu as un bout de temps")
    fichier1.seek(0)
    fichier2.seek(0)
    if fichier1.readline() == fichier2.readline():
        print("ok")
    else:
        print("none")


