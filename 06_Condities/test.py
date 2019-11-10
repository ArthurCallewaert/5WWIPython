
getal = int(input('geef getal: '))

if getal < 0:
    if getal % 2 == 0:
        print('negatief even getal')
    else:
        print('negatief oneven getal')
elif getal > 0:
    if getal % 2 == 0:
        print('positief even getal')
    else:
        print('positief oneven getal')
else:
    print('getal is nul')


a = max(min(g1, g2), min(g2, g3), min(g1, g3))
