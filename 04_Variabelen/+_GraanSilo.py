#invoer
b = float(input('breedte: '))
l = float(input('lengte: '))
c = float(input('kubieke meter: '))
r = float(input('straal: '))
h = float(input('hoogte: '))
pi = 3.14159265359
#berekening
opp = (l * b) / 10000
volume_graan = opp * c
volume_silo = (r)**2 * pi * h
aantal_silo = volume_graan // volume_silo
rest = (volume_graan / volume_silo - aantal_silo) * volume_silo
hoogte = rest / ((r)**2 * pi)
#uitvoer

print(aantal_silo + 1)
print(hoogte)
