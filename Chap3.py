print('Hello, I am Cynthia and I am learnig Python programming language')

#********************** SEQUENCE D'INSTRUCTIONS ***************************#
a, b = 3, 7
print(a,b)
a = b
b = a
print(a,b)     #le resultat est 7

#******************** INSTRUCTION DE TESTS *********************************#
print('----Utilisation des instructions de test "if", "elif" et "else"---- ')

print('a =',a)
if (a<0) :              
    print('a est négatif')
elif a==0 :                 # Les parenthèses sont optionnelles
    print('a est nul')
else:
    print('a est positif')

#********************* OPERATEURS DE COMPARAISON ******************************#
print('----Utilisations des opérateurs de comparaison----')

print('a =',a)
if a%2 == 0 :
    print('a est pair')
    print('Parce que le reste de sa division par 2 est nul')
else:
    print('a est impair')

#********************* INSTRUCTIONS IMBRIQUEES **************************#
print('----Utilisations des instructions imbriquées----')
print('Quel est cet animal ?')
embranchement, classe, ordre, famille = 'vertébrés', 'bipède','sauvage', 'homme'
#embranchement, classe, ordre, famille = 'vertébrés', 'oiseaux','sauvage', 'homme'
#embranchement, classe, ordre, famille = 'vers', 'bipède','sauvage', 'homme'
if embranchement == 'vertébrés':
    if classe == 'mammifère' :
        if ordre == 'félins' :
            if famille == 'félins' :
                print("C'est peut-être un chat")
        print("C'est un mammifère en tout cas")
    elif classe == 'oiseaux' :
        print("C'est peut-être un canari")
    else:
        print("C'est un homme")
else:
    print("C'est un invertébré")

print('----------FIN DE LA LECON------------')
# ******************* FIN DU CHAPITRE ************************#