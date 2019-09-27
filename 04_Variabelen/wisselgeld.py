#invoer
eurocent = int(input('geef aantal eurocent: '))
bedrag = eurocent
#berekenen
aantal_muntstukken = eurocent // 100
eurocent = eurocent % 100

aantal_muntstukken += (eurocent // 50)
eurocent = eurocent % 50

aantal_muntstukken += (eurocent // 20)
eurocent %= 20

aantal_muntstukken += (eurocent // 10)
eurocent %= 10

aantal_muntstukken += (eurocent // 5)
eurocent %= 5

aantal_muntstukken += (eurocent // 2)
eurocent %= 2

aantal_muntstukken += (eurocent // 1)

#uitvoer
print(bedrag, 'cent kan je omwisselen in', aantal_muntstukken, 'muntstukken')
