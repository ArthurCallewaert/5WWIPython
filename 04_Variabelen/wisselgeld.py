#invoer
eurocent = int(input('geef aantal eurocent: '))

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
eurocent %= 1

print(aantal_muntstukken, eurocent)
#uitvoer
