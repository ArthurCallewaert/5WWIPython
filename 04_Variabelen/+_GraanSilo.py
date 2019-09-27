#invoer
b = float(input('breedte: '))
l = float(input('lengte: '))
c = float(input('kubieke meter: '))
r = float(input('straal: '))
h = float(input('hoogte: '))
#berekening
opp = (l * b) / 10000
volume_graan = opp * c
volume_silo = (r)**2 * 3.14159265359* h
volle_silos = volume_graan // volume_silo
silo = volume_graan % volume_silo
#uitvoer

print(volle_silos)
print(silo)
