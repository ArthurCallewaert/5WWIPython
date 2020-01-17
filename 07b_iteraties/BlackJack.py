#invoer
som_kaarten, aantal_keer = 0, 1

#berekenen
while aantal_keer < 5:
    kaart = int(input())
    som_kaarten = som_kaarten + kaart
    aantal_keer = aantal_keer + 1

#uitvoer
uitvoer = "{} ({})"
if som_kaarten == 21:
    print("Gewonnen!")
elif som_kaarten > 21:
    print(uitvoer.format("verbrand", som_kaarten))
else:
    print(uitvoer.format("Voorzichtig gespeeld", som_kaarten))


