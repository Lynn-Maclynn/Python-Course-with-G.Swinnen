print('Hello, I am Cynthia and I am learnig Python programming language')
pi = 22/7       #Valeur de réelle de pi
print('--Exercice 1 :Conversion dégré,minutes et seconde/radian---')
angle_degree = 109
angle_min = 29
angle_sec = 54
angle_rad = pi*(angle_degree + angle_min/60 + angle_sec/3600)/180
print("La mesure l'angle {}°{}'{}'' en radians est de {} rad".format(angle_degree, angle_min, angle_sec, angle_rad))