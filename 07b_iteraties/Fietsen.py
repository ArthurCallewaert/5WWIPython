# invoer
v_stijn = int(input("snelheid van stijn: "))
v_kaat = int(input("snelheid van kaat: "))
afstand = int(input("afstand: "))
tot_afstand = 0
tijd = 0

#berekenen
while tot_afstand < afstand:
    tijd += 1
    tot_afstand = tot_afstand + v_kaat + v_stijn

#uitvoer
uitvoer = "Na {} s hebben Stijn en Kaat elkaar ontmoet."
print(uitvoer.format(tijd))
