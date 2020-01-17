# invoer
tijdstip = int(input(""))
nr_voren, nr_achteren, afstand = 0, 0, 0

#berekenen
for i in range(1, tijdstip + 1):
    if i % 2 != 0:
        nr_voren += 2
        afstand += nr_voren

    else:
        nr_achteren += 1
        afstand -= nr_achteren

#uitvoer
print(afstand)
