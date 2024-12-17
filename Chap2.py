print('Hello, I am Cynthia and I am learnig Python programming language')
print('Today, I have learned how to write in the window command prompt (DOS) and make some calculations')

#*********************** EXAMPLES OF CALCULATIONS I LEARNED TODAY *******************#

#*********************** Variables declarations **********************#
print('-------How to use variable ?---------')
add = 5+3
times = (7+3)*3
subtract = 2-9
divide = 3/2
wholeDivision = 3//2 # == 1, it gives only the whole part of the result
decimal = 3.5        #  NOT 3,5 as in french
msg = "Hi, my name is Cynthia and I am learning Python"
message = 'Today I learn how to use differents variables'
Msg = 'The case is it actually respected in this programming language ?'
Ans = 'Yes it is !'
# NOTICE : As we can see, it isn't necessary to indicate the variable type

#********************* Display values on the screen *******************#
print('----------How do I display value on my sreen ?-------------')
print(add); print(times); print(subtract); print(divide); print(wholeDivision)
print(decimal); 
print(msg); 
print(message)
print(Msg); 
print(Ans)

#********************* Multiple Affectations *************************#
print('------------Learn how to use multiple affectations----------------')
x = y = z = 7           # we can assigne a value simultaneously to many variables
print(x,y,z)
a, b = 4, 3.14          # we can use one operator for many affectations
print(a,b)
c, mess = 8.5, 'it works'
print(c, mess)

#********************* Expressions and operations ****************#
print('---------------Learn about the differents operators----------------')
a, b, c = 3/2, 6, 9//2
y = -1/2*a + 3*b + c
print(y)
x , z, t = 10%3, 10%5, 2**2        # % is modulo operator and ** is exponentiation operator
print(x, z, t) 

#********************** EXERCICES *****************************#
print('------EXERCICE---------')
r, pi = 12, 3.14159
s = pi * r**2
print('The area of the circle is', s)
print(type(r), type(pi), type(s))   # the instruction "type()" gives the variable type
print('the instruction "type()" gives the variable type')

#********************** Operations priorities ********************#
print('-------Learn about the priorities orders in calculations-------')
x = 2*3//4      # // and * operators have the same priority
y = 2*(3//4)    # ( ) operator has a highest priority on the others
z = (2*3)//4
print(x,y,z)  # We can see that x = z, so when two operators have the same priority, the evaluation begin from the LEFT to the RIGHT
# NOTICE : The priority order respect the PEMDAS law (parenthèse-exponentiel-multiplication-division-addition-soustraction)

#********************** Composition ****************************#
print('-------------Learn about composition----------')
print(5+8)
a,b = 5,8
print(a+b)   # Dans un langage de haut niveau, il est possible de faire des opérations complexes par assemblage des fragments divers
h, m, s = 13, 27, 50
print('le nombre de seconde écoulé depuis minuit = ', h*3600 + m*60 + s)

print('----------END OF THE LESSON, thank you for watching------------')
# ******************* FIN DU CHAPITRE ************************#