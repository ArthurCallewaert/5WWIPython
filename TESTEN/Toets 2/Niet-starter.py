#invoer
getal = float(input("getal: "))
som, nieuw_getal, aantal_keren = 0.5, 0.5, 1
#berekenen
while som < getal:
    nieuw_getal /= 2
    som += nieuw_getal
    aantal_keren += 1
#uitvoer
print(aantal_keren, som)

