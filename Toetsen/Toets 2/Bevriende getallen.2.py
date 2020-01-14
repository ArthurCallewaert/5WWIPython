#invoer
getal_1 = int(input("getal: "))
getal_2 = int(input("getal: "))
som_1, som_2 = 0, 0

#berekenen
for i in range(1, getal_1):
    if getal_1 % i == 0:
        som_1 += i
for v in range(1, getal_2):
    if getal_2 % v == 0:
        som_2 += v

#uitvoer
if som_1 == getal_2 and som_2 == getal_1:
    uitvoer = "{} en {} zijn bevriende getallen"
else:
    uitvoer = "{} en {} zijn geen bevriende getallen"

print(uitvoer.format(getal_1, getal_2))


