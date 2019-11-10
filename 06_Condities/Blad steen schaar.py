#invoer
speler1 = input("speler 1: ")
speler2 = input("speler 2: ")

if speler1 == speler2:
    print('onbeslist')
else:
    if (speler1 == 'blad' or speler2 == 'blad') and (speler2 == 'steen' or speler1 == 'steen'):
        if speler1 == 'blad':
            wedstrijd = 'speler 1'
        else:
            wedstrijd = 'speler 2'
    elif (speler1 == 'schaar' or speler2 == 'schaar') and (speler2 == 'blad' or speler1 == 'blad'):
        if speler1 == 'schaar':
            wedstrijd = 'speler 1'
        else:
            wedstrijd = 'speler 2'
    else:
        if speler1 == 'steen':
            wedstrijd = 'speler 1'
        else:
            wedstrijd = 'speler 2'

    uitvoer = '{} wint'
    print(uitvoer.format(wedstrijd))
