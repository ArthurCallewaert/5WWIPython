aantal = int(input("aantal getallen: "))

# Lees het eerste getal voor de lus in
getal_0 = int(input("geef getal :"))

# Het eerste getal is inmiddelijk de som en het grootste getal
som, grootste = getal_0, getal_0

for i in range(aantal - 1):
    getal = int(input("geef getal :"))
    som += getal
    grootste = max(grootste, getal)

gemiddelde = som / aantal

uitvoer = "Het grootste getal is {} en het gemiddelde is {:.2f}"
print(uitvoer.format(grootste, gemiddelde))

