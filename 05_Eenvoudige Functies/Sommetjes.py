#invoer
a = int(input('a: '))
b = int(input('b: '))

#berekening
c1 = a * pow(10, 0) + b * pow(10, 0)
c2 = a * pow(10, 1) + b * pow(10, 1)
c3 = a * pow(10, 2) + b * pow(10, 2)
c4 = a * pow(10, 3) + b * pow(10, 3)
c5 = a * pow(10, 4) + b * pow(10, 4)

#uitvoer
uitvoer = '{:>6} + {:<6} = {:<}'
print(uitvoer.format(a * pow(10, 0), b * pow(10, 0), c1))
print(uitvoer.format(a * pow(10, 1), b * pow(10, 1), c2))
print(uitvoer.format(a * pow(10, 2), b * pow(10, 2), c3))
print(uitvoer.format(a * pow(10, 3), b * pow(10, 3), c4))
print(uitvoer.format(a * pow(10, 4), b * pow(10, 4), c5))
