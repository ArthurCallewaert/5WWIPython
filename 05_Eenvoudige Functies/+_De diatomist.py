#invoer
k_r = float(input('straal kleine cirkel: '))
g_r = float(input('straal grote cirkel: '))

#berekening
n = 0.83 * pow(g_r, 2) / pow(k_r, 2) - 1.9
opp = int(n) * pow(k_r, 2) / pow(g_r, 2) *100
#uitvoer
uitvoer = '{} kleine cirkels bedekken {:.2f}% van de grote cirkel'
print(uitvoer.format(int(n), opp))

