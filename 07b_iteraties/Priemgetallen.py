#invoer
getal = int(input("getal: "))
deler = 2

#berekenen
while getal % deler != 0 and deler < getal:
    deler += 1

#uitvoer
uivoer = "{} is {} priemgetal"
if deler < getal or getal == 1:
    print(uivoer.format(getal, "geen"))
else:
    print(uivoer.format(getal, "een"))
