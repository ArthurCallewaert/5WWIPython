#invoer
bruto = float(input("bruto jaar: "))
rsz = (bruto / 100) * 13.07
bruto_rsz = bruto - rsz
schijf1 = 0
schijf2 = 0
schijf3 = 0
schijf4 = 0
if bruto_rsz < 8860.00:
    pass
else:
    if bruto_rsz <= 13250.00: #schijf 1
        schijf1 = (bruto_rsz - 8860.00) / 100 * 25
    elif bruto_rsz <= 23390.00: #schijf 1 en 2
        schijf1 = 1097.50
        schijf2 = (bruto_rsz - 13250.00) / 100 * 40
    elif bruto_rsz <= 40480.00: #schijf 1, 2 en 3
        schijf1 = 1097.50
        schijf2 = 4056
        schijf3 = (bruto_rsz - 23390.00) /100 * 45
    else:                       #schijf 1, 2, 3 en 4
        schijf1 = 1097.50
        schijf2 = 4056
        schijf3 = 7690.5
        schijf4 = (bruto_rsz - 40480.00) /100 * 50

voorheffing = schijf1 + schijf2 + schijf3 + schijf4
netto_jaar = bruto - rsz - voorheffing
netto_maand = netto_jaar / 12
uitvoer1 = "+ bruto jaarsalaris{:>11.2f}"
uitvoer2 = "- rsz{:>25.2f}"
uitvoer3 = "- voorheffing{:>17.2f}"
uitvoer4 = "=============================="
uitvoer5 = "+ netto jaarsalaris{:>11.2f}"
uitvoer6 = "+ netto maandsalaris{:>10.2f}"

print(uitvoer1.format(bruto))
print(uitvoer2.format(rsz))
print(uitvoer3.format(voorheffing))
print(uitvoer4)
print(uitvoer5.format(netto_jaar))
print(uitvoer6.format(netto_maand))
