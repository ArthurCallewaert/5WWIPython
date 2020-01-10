# invoer
tijdstip = int(input(""))
nr_voren = 0
nr_achteren = 0
afstand = 0
#berekenen
for i in range(1, tijdstip + 1):
    if i % 2 != 0:
        nr_voren += 2
        afstand += nr_voren

    else:
        nr_achteren += 1
        afstand -= nr_achteren

print(afstand)
