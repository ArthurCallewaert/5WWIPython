#invoer
t = float(input('luchttemperatuur: '))
w = float(input('windsnelheid: '))

#berekening
g_temp = 13.12 + 0.6215 * t - 11.37 * pow(w, 0.16) + 0.3965 * t * pow(w, 0.16)

#uitvoer
print(g_temp)
