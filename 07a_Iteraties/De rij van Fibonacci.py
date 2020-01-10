# invoer
n = int(input("hoeveelste getal: "))
getal_1 = 1
getal_2 = 1
#berekenen
getal = 1
for i in range(n-2):
    getal = getal_1 + getal_2
    getal_1 = getal_2
    getal_2 = getal
print(getal)
