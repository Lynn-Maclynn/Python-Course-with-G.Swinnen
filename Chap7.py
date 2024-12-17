print('Hello, I am Cynthia and I am learnig Python programming language')
from turtle import *
# def carre(taille, couleur):
#     "fonction qui dessine un carré de taille et de couleur déterminées"
#     color(couleur)
#     c =0
#     while c <4:
#         forward(taille)
#         right(90)
#         c = c +1
# up() # relever le crayon
# goto(-150, 50) # reculer en haut à gauche
# # dessiner dix carrés rouges, alignés :
# i = 0
# while i < 10:
#     down() # abaisser le crayon
#     carre(25, 'red') # tracer un carré
#     up() # relever le crayon
#     forward(30) # avancer + loin
#     i = i +1
# a = input() # attendre

# print('--Exercice 1 : Dessin d\'un triangle ---')

# def triangle(couleur) :
#     "fonction qui dessine un triangle de taille et de couleur déterminées"
#     color(couleur)
#     c = 0
#     while c<3:
#         forward(100)
#         left(120)
#         c = c+1

# liste_couleur = ['green', 'red', 'yellow', 'blue', 'orange', 'black','gold', 'violet', 'pink']
# up()
# goto(-500, 0)
# i = j = 0
# while i<len(liste_couleur):
#     down()
#     triangle(liste_couleur[i])
#     up()
#     forward(120)
#     i = i+1
# a = input()

print('--Exercice 6 : Dessin des triangles et des carres ---')
def carre(taille, couleur, angle):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    left(angle)
    c =0
    while c <4:
        forward(taille)
        right(90)
        c = c +1
def triangle(taille, couleur, angle) :
    "fonction qui dessine un triangle de taille et de couleur déterminées"
    color(couleur)
    left(angle)
    c = 0
    while c<3:
        forward(taille)
        right(120)
        c = c+1

up() # relever le crayon
goto(-500, 50) # reculer en haut à gauche
# dessiner huit carrés rouges et dix triangles bleus, alignés :
i = 0
taille = 25
while i < 8:
    down() # abaisser le crayon
    carre(taille, 'red',0) # tracer un carré
    up() # relever le crayon
    forward(30 +i*10) # avancer + loin
    down() # abaisser le crayon
    triangle(taille, 'blue',0) # tracer un triangle
    up()
    forward(30 + i*10) # avancer + loin
    i = i +1
    taille +=10
a = input() # attendre
