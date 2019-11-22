g1 = int(input('getal 1: '))
g2 = int(input('getal 2: '))
g3 = int(input('getal 3: '))
g4 = int(input('getal 4: '))
g5 = int(input('getal 5: '))

maxi = max(g1, g2, g3, g4, g5)
som = g1 + g2 + g3 + g4 + g5
gem = som / 5

uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'
print(uitvoer.format(maxi, gem))
