#invoer
r = float(input('afstand: '))
v = float(input('snelheid: '))
µ = 3.986004418 * pow(10, 14)
#berekening
from math import sqrt, pi
a = (µ * r) / ((2 * µ) - (r * pow(v, 2)))
p1 = 2 * pi * (sqrt(pow(a, 3) / µ))
p2 = p1
dag = p1 // 86400
p1 %= 86400
uur = p1 // 3600
p1 %= 3600
min = p1 // 60
p1 %= 60
#uitvoer
uitvoer1 = 'grote as: {} meter'
uitvoer2 = 'periode: {} seconden'
uitvoer3 = 'periode: {} dagen, {} uren en {} minuten'
print(uitvoer1.format(a))
print(uitvoer2.format(p2))
print(uitvoer3.format(int(dag), int(uur), int(min)))
