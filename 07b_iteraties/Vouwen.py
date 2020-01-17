# invoer
dikte_papier = int(input("dikte: "))
afstand = int(input("afstand: "))
aantal_vouwen = 0
tot_dikte = dikte_papier

#berekenen
while tot_dikte < afstand:
    aantal_vouwen += 1
    tot_dikte = dikte_papier * (2 ** aantal_vouwen)

#uitvoer
uitvoer = "Na {} keer vouwen bedraagt de dikte van het papier {} mm."
print(uitvoer.format(aantal_vouwen, tot_dikte))
