som_kaarten = 0
aantal_keer = 1
while aantal_keer < 5:
    kaart = int(input())
    som_kaarten = som_kaarten + kaart
    aantal_keer = aantal_keer + 1

uitvoer = "{} ({})"
if som_kaarten == 21:
    print("Gewonnen!")
elif som_kaarten > 21:
    print(uitvoer.format("verbrand", som_kaarten))
else:
    print(uitvoer.format("Voorzichtig gespeeld", som_kaarten))


