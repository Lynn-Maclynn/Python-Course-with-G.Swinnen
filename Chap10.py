print('Hello, I am Cynthia and I am learnig Python programming language')

print('Je vais créer des objets dans ce module')

class Point(object) :
    "Définition d'un point géométrique"

p9 = Point()
print(p9)
print(p9.__doc__)

def distance(p,q):
    x = p.x - q.x
    y = p.y - q.y
    return x**2+y**2

p1, p2 = Point(), Point()

p1.x, p2.x = 5.0, 3.0
p1.y, p2.y = 1.0, 6.0

d = distance(p1, p2)
print("La distance entre les points {} et {} est de {}.".format('p1','p2', d))