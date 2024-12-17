print('Hello, I am Cynthia and I am learnig Python programming language')
#******************************* EXERCICES *******************************#
pi = 22/7       #Valeur de réelle de pi
print('--Exercice 1 :Conversion dégré,minutes et seconde/radian---')
angle_degree = 109
angle_min = 29
angle_sec = 54
angle_rad = pi*(angle_degree + angle_min/60 + angle_sec/3600)/180
print("La mesure l'angle {}°{}'{}'' en radians est de {} rad".format(angle_degree, angle_min, angle_sec, angle_rad))

#angle_degre = 180*angle_rad/pi
#angle_minute = 60*(angle_degre - int(angle_degre))
#angle_seconde = 60*(angle_minute - int(angle_minute))
#print("La mesure de cet angle est de {}°{}'{}''".format(int(angle_degre), int(angle_minute), int(angle_seconde)))

print('--Exercice 2 :Conversion radian/dégré,minutes et seconde---')
#angle_radian = input("Entrer la valeur d'un angle en radian :")
#angle_radian = float(angle_radian)
angle_radian = 3*pi/5
angle_degre = 180*angle_radian/pi
angle_minute = 60*(angle_degre - int(angle_degre))
angle_seconde = 60*(angle_minute - int(angle_minute))
print("La mesure de cet angle est de {}°{}'{}''".format(int(angle_degre), int(angle_minute), int(angle_seconde)))

print('--Exercice 3 :Conversion dégré Celsius/dégré Fahrenheit---')
temp_fahrenheit = 40.5
temp_celsius = (temp_fahrenheit - 32)/1.8
print("{}°F = {}°C".format(temp_fahrenheit, temp_celsius))
temp_celsius = 40.5
temp_fahrenheit = temp_celsius*1.8 + 32
print("{}°C = {}°F".format(temp_celsius,temp_fahrenheit))

print('--Exercice 4 :Calcul intérêt bancaire---')
somme, interet, taux, annee = 1500000, 0, 0.0245,0
while annee<20 :
    interet, annee = somme*taux, annee+1
    somme +=interet
    print("Année {} -> {} FCFA".format(annee, somme))

print("--Exercice 5 :jeu d'échecs---")
print("Calcul du nombre de grains de riz en entier")
grain_riz, case = 1,1
print("Case {} -> {} grain de riz".format(case, grain_riz))
while case<64 :
    grain_riz, case = grain_riz*2, case + 1
    print("Case {} -> {} grains de riz".format(case, grain_riz))

print("Calcul du nombre de grains de riz en notation scientifique")
grain_riz, case = 1.,1              # Ici le nombre de grain de riz initial est en décimal 1./1.0
print("Case {} -> {} grain de riz".format(case, grain_riz))
while case<64 :
    grain_riz, case = grain_riz*2, case + 1
    print("Case {} -> {} grains de riz".format(case, grain_riz))

#******************************* LE TYPE STRING *******************************#
# l'antislash \ me permet d'inserer l'apostrostrophe dans le '__'
print('je n\'irai pas au campus aujourd\'hui')    

# l'antislash \ me permet d'écrire sur la même ligne une commande écrite sur plusieurs ligne
msg = 'LYNN: Bonjour comment vas-tu aujoud\'hui ? \
    BORIS: Je vais très bien? MERCI. \
    Et toi ? \
            LYNN: Moi aussi, je vais bien'      
print(msg)   

# la commande \n me permet d'aller à la ligne
msg = 'Mme LYNN: Bonjour comment-allez-vous aujoud\'hui ?\n M. BORIS: Je vais très bien? MERCI, et vous ?\n Mme LYNN: Moi aussi, je vais bien'
print(msg)   

# les triples quotes permettent d'écrire sur plusieurs ligne et d'insérer des caractères spéciaux
msg = """LYNN: Est ce que tu sais écrire & 
BORIS: Non non, mais je sais écrire ' et "
LYNN: Moi aussi, je sais écrire ces signe là"""
print(msg)

#Opérations sur les chaines de caractères
print("------Opérations sur les chaines de caractères----")
nom = "Cynthia"
print(nom[1], nom[5])   # On a accès à chaque lettre de la chaine
print("Ce nom a ", len(nom), "lettres")     # On peut avoir la taille d'une chaine de caractère
nom = "Magny Anoune"
prenom = " Cynthia Lynn"        # ATTENTION à ne pas oublier l'espace au debut
print(nom + prenom)             # L'opérateur + permet de faire la concatenation


#******************************* EXERCICES *******************************#
print('--Exercice 6 : Recherche voyelle dans un mot---')
mot = "chaise"
i = n = 0
while i<len(mot):
    if mot[i] == "e" :
        print("Ce mot contient la lettre 'e' ")
    i +=1

print('--Exercice 7 : Recherche voyelle dans un mot---')
mot = "ce message vous est destiné"
i = n = 0
while i<len(mot):
    if mot[i] == "e" :
        n +=1
    i +=1
print('Le nombre d\'occurences de \'e\' est de ', n)

print('--Exercice 8 : Insertion des astérix---')
mot = "amie"
i = 0
while i<len(mot):
    print("{}*".format(mot[i]), end="")
    i +=1
print()
print('--Exercice 9 : inversement de l\'ordre des lettres ---')
mot = "bulgroz"
i = 0
while i<len(mot) :
    print(mot[len(mot)-(i+1)], end="")
    i +=1
print()
print('--Exercice 10 : Recherche palindrome ---')       # NON REUSSI
mot = 'madar'
i = n = 0
while i<len(mot) :
    if mot[len(mot)-(i+1)] != mot[i] :
        print("Ce n'est pas un palindrome")
        break
    else:
        continue
print("Le mot {} est un palindrome".format(mot))

print('--Exercice 11 : Ajouter des valeurs dans des Listes ---')
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []
i = 0
while i<len(t2) :
    t3.append(t2[i])            # append(argument) permet d'ajouter l'élément "argument" dans une liste
    t3.append(t1[i])
    i +=1
print(t3)

print('--Exercice 12 : Afficher les valeur d\'une liste ---')
i = 0
while i<len(t2) :
    print(t2[i], end=" ")       # t2[i] permet d'afficher l'élément "i" de la liste
    i +=1
print()

print('--Exercice 13 : Rechercher le plus grand élément d\'une liste ---')
t4 = [32, 5, 12, 8, 3, 75, 2, 15]
print("Le plus grand élément de cette liste a la valeur", max(t4))

print('--Exercice 14 : Classer les valeur d\'une Liste ---')
i, t_pair, t_impair = 0, [], []
while i<len(t4) :
    if t4[i]%2 == 0 :
        t_pair.append(t4[i])
    else:
        t_impair.append(t4[i])
    i +=1
print("La liste des nombres impairs est :",t_impair)
print("La liste des nombres pairs est :", t_pair)

print('--Exercice 14 : Classer les valeur d\'une Liste ---')
t5 = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
i, t_pair, t_impair = 0, [], []
while i<len(t5) :
    if len(t5[i]) < 6 :
        t_pair.append(t5[i])
    else:
        t_impair.append(t5[i])
    i +=1
print("La liste des noms ayant moins de 6 caractères est :", t_pair)
print("La liste des noms ayant au moins 6 caractères est :", t_impair)

print('-------------------------------------FIN DE LA LECON---------------------------------------------')
# ***************************************** FIN DU CHAPITRE ************************************************#