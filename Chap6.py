print('Hello, I am Cynthia and I am learnig Python programming language')
# from math import *
# number = 25
# angle = pi/2
# print('La racine carré de', number, 'est', sqrt(number))
# print('Le sinus de', angle, 'rad est', sin(angle))

# from turtle import *
# forward(120)
# left(90)
# color('red')
# forward(80);
# reset()
# a = 0
# while a <12:
#     a = a +1
#     forward(150)
#     left(150)

print("J'aime", "la", "vie", "comme", "elle", "est", "sans", "fantaisie", sep="--")
print("J'aime", "la", "vie", "comme", "elle", "est", "sans", "fantaisie", sep="**")     # "sep" permet de séparer les mots
print("J'aime", "la", "vie", "comme", "elle", "est", "sans", "fantaisie", sep="++")                     # par autres choses que l'espace

i = 0
while i<6:
    print('Merci', end='')          # "end='' " permet d'annuler le saut à la ligne
    i +=1
print()

#Utilisation de "input()"
# n = input("Entrer un nombre entre 1 et 2 : ")       #C'est possible d'afficher la valeur en argument dans le module input()
# n = int(n)
# while n < 3 :
#     print('Merci')
#     n +=1
# print("Entrez votre nom :", end=" ")
# nom = input()
# print("Bonjour", nom)

# d = input("Entrer la longueur du carré : " )
# d = float(d)
# print("La surface de ce carré est de", d**2)

#******************************* EXERCICES *******************************#
# print('--Exercice 1 : Conversion vitesse ---')

# vitesse = input("Entrer la valeur de votre vitesse : ")
# vitesse = int(vitesse)
# print("Votre vitesse est de :", 1.609*vitesse, "km/h et de", 1609/3600*vitesse, "m/s")

# print('--Exercice 2 : Périmètre et surface d\'un triangle ---')
# print("Entrer les valeurs des dimensions du triangle en cm")
# a = input("Longueur du premier coté = ")
# b = input("Longueur du 2e coté = ")
# c = input("Longueur du 3e coté = ")

# a, b, c = int(a), int(b), int(c)
# perimetre = (a+b+c)
# d = perimetre/2
# surface = sqrt(d*(d - a)*(d - b)*(d - c))
# print("Le périmètre de ce triangle est de", perimetre, "cm et sa surface est de", surface, "cm^2")

# print('--Exercice 3 : Période d\'un pendule ---')
# print("Entrer la longueur du pendule et l'accélération de la pesanteur ")
# l = int(input())
# g = int(input())
# print("La période de ce pendule est de", 2*pi*sqrt(l/g))

# print('--Exercice 4 : Entrer des valeurs ---')
# liste = []
# n = 0
# while n:
#     n = input('Entrer une valeur : ')
#     if n:
#         n = int(n)
#         liste.append(n)
#         n = str(n)          # J'ajoute cette expression pour pouvoir ajouter la valeur 0 dans la liste. Sans elle, la boucle while ne va pas s'executer pour la valeur 0
# print(liste)

# print('--Exercice 8 : Recherche des multiples ---')
# a = input('Entrer un nombre (0 pour terminer l\'exercice) : ')
# a = int(a)
# while a:
#     b = input('Entrer un autre nombre : ')
#     b = int(b)
#     n = m = 0
#     if a<b :
#         i = a
#         while i<=b :
#             if not(i%3) and not(i%5) :
#                 n = n+i
#             if not(i%3) or not(i%5) :
#                 m = m+i
#             i +=1
#         print("La somme des multiples de 3 et de 5 est ", n)
#         print("La somme des multiples de 3 ou de 5 est ", m)
#     elif b<a:
#         a,b = b,a
#         i = a
#         while i<=b :
#             if not(i%3) and not(i%5) :
#                 n = n+i
#             if not(i%3) or not(i%5) :
#                 m = m+i
#             i +=1
#         print("La somme des multiples de 3 et de 5 est ", n)
#         print("La somme des multiples de 3 ou de 5 est ", m)
#     else:
#         print("Entrer deux nombres différents svp")
#     a = input('Entrer un nombre : ')
#     a = int(a)
# print("Vous avez entré 0, l'exercice est donc terminé")

print('--Exercice 9 : Année Bissextile ---')
# print("Ce programme vous dira si l'année entrée au clavier est une année bissextile")
# print("Entrer une année de votre choix :", end=" ")
# annee = input()
# annee = int(annee)
# if not(annee%100):
#     if not(annee%400):
#         print("{} est une année bissextile".format(annee))
#     else:
#         print("{} n'est pas une année bissextile".format(annee))        
# elif not(annee%4):
#         print("{} est une année bissextile".format(annee))
# else:
#     print("{} n'est pas une année bissextile".format(annee))

# print('--Exercice 9 : Salutations ---')
# nom = input("Veuillez entrer votre nom : ")
# sexe = input("Veuillez entrer votre sexe (M pour masculin, F pour feminin) :")
# if sexe == "F" :
#     print("Chère Mademoiselle", nom)
# else:
#     print("Cher Monsieur", nom)

# print('--Exercice 11 : Nature d\'un triangle ---')
# print("Entrer 3 nombres et vous saurez si c'est possible de construire un triangle ainsi que sa nature")
# print("Veuillez entrer tois nombres séparés par des virgules :", end=" ")
# nombre = input()
# cote = list(eval(nombre))
# if cote[0]<cote[1]+cote[2] and cote[1]<cote[0]+cote[2] and cote[2]<cote[1]+cote[0]:
#     print("Il est possible de construire ce triangle")
#     if cote[0]==cote[1] and cote[1]==cote[2] :
#         print("Ce triangle est équilatéral")
#     elif cote[0]==cote[1] or cote[0]==cote[2] or cote[1]==cote[2]:
#         print("Ce triangle est isocèle")
#     elif cote[0]**2==cote[1]**2+cote[2]**2 or cote[1]**2==cote[0]**2+cote[2]**2 or cote[2]**2==cote[1]**2+cote[0]**2:
#         print("Ce triangle est rectangle ")
#     else:
#         print("Ce triangle est un triangle quelconque")
# else:
#     print("Il n'est pas possible de construire ce triangle")


print('--Exercice 12 : Racine carre ---')
import math
print('Entrer un nombre :', end=' ')
n = input()
n = int(n)
if n>=0:
    print("La racine de ce nombre est ", math.sqrt(n))
else:
    print("Il n'est pas possible de calculer la racine de ce nombre")

    print('--Exercice 13 : Racine carre ---') # -----------------A FAIRE**************************