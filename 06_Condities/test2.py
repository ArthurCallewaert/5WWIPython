getal = int(input('geef getal: '))

if getal < 0 and getal % 2 == 0:
    print('negatief en even getal')
elif getal < 0 and getal % 2 != 0:
    print('negatief en oneven getal')
elif getal > 0 and getal % 2 == 0:
    print('positief en even getal')
elif getal > 0 and getal % 2 != 0:
    print('positief en oneven getal')
else:
    print('getal is 0')
#eerst voorwaarden!! en met pass
#dan pas programmeren
