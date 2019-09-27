#invoer
sol = int(input('aantal marsdagen (sol): '))
duur = 88775.244
#berekening
duur_sec = sol * duur
dagen = duur_sec // 86400
duur_sec %= 86400
uren = duur_sec // 3600
duur_sec %= 3600
min = duur_sec // 60
duur_sec %= 60

#uitvoer
print(int(sol), 'sol =', int(dagen), 'dagen,', int(uren), 'uren,', int(min), 'minuten en', int(duur_sec), 'seconden')
