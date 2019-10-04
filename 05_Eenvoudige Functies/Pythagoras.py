#92.06826
#16.1
#In een rechthoekige driehoek met rechthoekszijden a = 3.00 en b = 78.00 is de schuine zijde 78.06
from math import sqrt
#invoer
a = float(input('lengte a: '))
b = float(input('lengte b: '))
#berekening
c = sqrt(pow(a, 2) + pow(b, 2))

#uitvoer
uitvoer = 'In een rechthoekige driehoek met rechthoekszijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'
print(uitvoer.format(a, b, c))
