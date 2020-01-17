totale_prijs = 0
product = float(input())

while product != 0:
    totale_prijs = totale_prijs + product
    product = float(input())

uitvoer = "De totale prijs is € {:.2f}"
print(uitvoer.format(totale_prijs))
