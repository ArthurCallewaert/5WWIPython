# invoer
basen, soorten = "", 0
aantal = int(input("aantal: "))

#berekenen
for i in range(aantal):
    base = input("")
    if base not in basen:
        soorten += 1
        basen = basen + " " + base

#uitvoer
uitvoer1 = "De DNA-keting bevat {} verschillende soorten basen: {}"
uitvoer2 = "De DNA-keting bevat 1 soort base: {}"
if soorten != 1:
    print(uitvoer1.format(soorten, basen))
else:
    print(uitvoer2.format(basen))

