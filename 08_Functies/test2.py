def welkom(naam):
    print("welkom terug " + naam)

#welkom("arthur")
#welkom(str(1))
#welkom(str(True))
#--------------------------

#test = welkom("arthur")
#print(test)
#-------------------------------------

from math import sqrt


def pythagoras(a, b):
    c = -1
    if a > 0 and b > 0:
        c = sqrt(a*a + b*b)
    return c

#print(pythagoras(3, 4))
#--------------------------------------

def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

def wortels(a, b, discriminant):
    w1, w2 = None, None
    if discriminant >= 0:
        w1 = (-b + sqrt(discriminant)) / (2 * a)
        w2 = (-b - sqrt(discriminant)) / (2 * a)
    return w1, w2


#wortel1, wortel2 = wortels(2, -1,discriminant(2, -1, - 4))
#print(wortel1, wortel2)
#-------------------------------------
from random import randint

def gooi_muntstuk():
    rg = randint(0, 2)
    muntstuk = "munt"
    if rg == 0:
        muntstuk = 'kop'
    return muntstuk

for i in range(10):
    print(gooi_muntstuk())
#print(rg, muntstuk)
