#invoer
getal = int(input('cijfer: '))
som = 0

#berekenen
for veelvoud in range(getal, 101, getal):
    som += veelvoud

#uitvoer
print(som)
