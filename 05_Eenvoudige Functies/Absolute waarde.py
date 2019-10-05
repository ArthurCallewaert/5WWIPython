#42.06826283274985
#13.510020196930185
#print('\N{LESS-THAN OR EQUAL TO}')

#invoer
x = float(input('x: '))
y = float(input('y: '))
#berekening
a = abs(abs(x) - abs(y))
b = abs(x-y)
teken = str('\N{LESS-THAN OR EQUAL TO}')
#uitvoer
uitvoer = '{:.4f} {} {:.4f}'
print(uitvoer.format(a, teken, b))
