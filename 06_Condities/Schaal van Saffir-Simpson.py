#windsnelheid (km/h)	Categorie	119-153	1	154-177	2	178-209	3	210-249	4	≥ 250	5
windsnelheid = int(input('windsnelheid: '))

#berekenen
if windsnelheid >= 119:
    if windsnelheid < 154: #1
        print('categorie 1')
    elif windsnelheid < 178: #2
        print('categorie 2')
    elif windsnelheid < 210: #3
        print('categorie 3')
    elif windsnelheid < 250: #4
        print('categorie 4')
    else:
        print('categorie 5')
else:
     print('geen orkaan')


