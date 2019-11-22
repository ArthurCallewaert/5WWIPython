#invoer
dag = int(input("dag: "))
maand = int(input("maand: "))
jaar = int(input("jaar: "))

#berekening
if dag < 27:
    dag += 1
elif maand != 2:
    if maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10 or maand == 12: #maanden met 31 dagen
        if dag == 31 and maand == 12:
            dag = 1
            maand = 1
            jaar += 1
        elif dag == 31:
            maand += 1
            dag = 1
        else:
            dag += 1
    else: #maanden met 30 dagen
        if dag == 30:
            dag = 1
            maand += 1
        else:
            dag += 1
else:
    if (jaar % 4 == 0 and not jaar % 100 == 0) or jaar % 400 == 0:
        if dag == 29:
            dag = 1
            maand += 1
        else:
            dag += 1
    else:
        if dag == 28:
            dag = 1
            maand += 1
        else:
            dag += 1
uitvoer = "{}/{}/{}"
print(uitvoer.format(dag, maand, jaar))




