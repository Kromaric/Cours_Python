#Eexercice 1
'''nom = input("Veillez entrer votre nom: ")
prenom = input("Veillez entrer votre prénom: ")
age = input("veillez entrer votre âge: ")
ville = input("veillez entrer votre ville: ")
print("Bonjour ", nom,prenom, "vou avez", age, "ans et vous habitez ", ville) '''


#Eexercice 2
'''
i = 23
f = 4.5
c = '12'

i = str(i)
print(i)
print(type(i))


print("concatenation: ", i + c)

f = int(f)

print(f)
print(type(f))'''

##Eexercice 3
'''
nombre1 = 2*10e5
print(nombre1) 


nombre2 = 0.3*10e-4
print(nombre2)

print(nombre1+nombre2)'''

#Eexercice 4
'''
x,y = 14, 4

print("x + y = ", x+y)

print("x - y = ", x-y)

print("x * y = ", x*y)
print("x/y = ", x/y)
print("x//y = ", x//y)
print("x % y = ", x%y)
print("x**y = ", x**y)
'''
'''
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("le minimum est:",min(L))
print("le maximum est:", max(L))
'''

nombre  = int(input("veillez entrer un nombre"))

if nombre > 0:
    if nombre%3 == 0:
        print("le nombre  est positif et divisible par 3")
    else:
        print("le nombre n'est pas divisible par 3")
else:
    print("le nombre est negatif")


flotant1 = 1.50
flotant2 = 1.53
tolerance = 10e6
print(abs(flotant1-flotant2) == tolerance)
