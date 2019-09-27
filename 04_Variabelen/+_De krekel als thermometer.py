#invoer
N60 = int(input('N60: '))
#berekening
Tc = 10 + (N60 - 40) / 7
Tf = 50 + (N60 - 40) / 4
#uitvoer
print('temperatuur (Fahrenheit):', Tf)
print('temperatuur (Celsius):', Tc)
