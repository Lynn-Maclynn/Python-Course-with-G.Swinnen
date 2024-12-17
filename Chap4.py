print('Hello, I am Cynthia and I am learnig Python programming language')

#****************** REAFFECTATION ****************************#
print('----------réaffectation des variables par affectation parallèle----------')
a,b,c,d = 3,4,0,6
print(a,c)
a,c = c,a   #affectation parallèle
print(a,c)  # les valeurs de a et c sont échangées

#******************* REPETITION EN BOUCLE *******************#
print('--------Utilisation de la boucle "while"------------')

print("J'affiche les carré et les cube des nombres inférieurs à 5")
while a<5 :
    a = a+1
    print(a, a**2, a**3)

print('Suite de Fibonacci')
a, b, c = 1, 1, 1
while c<11 :
    print(b, end =" ")
    a,b,c = b, a+b, c+1
print()
#******************* EXERCICES *******************#
print('--Exercice 1 : La table de multiplication par 7---')
a = 0
while a<20 :
    print(a*7, end = " ")
    a = a+1
print()

print('--Exercice 2 : Conversion euro/dollar ---')
a, b = 1, 1.65
while a<16384 :
    print('{} euro(s) = {} dollar(s)'.format(a,b))
    a, b = a*2, b*2

print('--Exercice 3 : suite de chiffres ---')
a, c = 2, 1
while c<13:
    print(a, end = ' ')
    a,c = a*3, c+1
print()

print("--Exercice 4 : volume d'un parallépipède---")
L = 7; l = 3; h = 5; V = L*l*h
print("Le volume de ce parallépipède est de ", L*l*h)
print("Le volume de ce parallépipède de longueur {}, de largeur {} et de hauteur {} est de {}".format(L,l,h,V))

print("--Exercice 5 :  ---")  #***********NON REUSSI
t = 18300; jour = t%3600; min = t%60
print("i y a {} jours {} minutes {} secondes".format(jour,min,t)) # inserer des valeurs dans un texte

print("--Exercice 6 : Afficher les multiples commus de 7 et 3 ---")
a = 1
while a<20 :
    if a*7 %3 ==0 :
        print(a*7,"*", end = " ")
    else:
        print(a*7, end = " ")
    a = a+1
print()

print("--Exercice 7 : Afficher les multiples commus de 7 et 13 ---")
a = 1
while a<50 :
    if a*13 %7 == 0 :
        print(a*13, end = " ")
    a = a+1
print()

print("--Exercice 8 : Afficher les caractères ---")
a = 1
while a<8 :
    star = "*"
    print(star*a)
    a = a+1

print('----------FIN DE LA LECON------------')
# ******************* FIN DU CHAPITRE ************************#