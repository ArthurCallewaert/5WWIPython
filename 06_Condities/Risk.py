#maxi = max(x1, x2, x3, x4)
#mini = min(x1, x2, x3, x4)
#mid1 = max(min(x1, x2), min(x2, x3), min(x1, x3))
#mid2 = x1 + x2 + x3 + x4 -mini - maxi - mid1

a1 = int(input('dobbelsteen aanvaller: '))
a2 = int(input('dobbelsteen aanvaller: '))
a3 = int(input('dobbelsteen aanvaller: '))

v1 = int(input('dobbelsteen verdediger: '))
v2 = int(input('dobbelsteen verdediger: '))

#berekenen
if max(a1, a2, a3) == max(v1, v2):
    if min(max(a1, a2), max(a1, a3), max(a2, a3)) <= min(v1, v2):
        aanvaller = 2
        verdediger = 0
    else:
        aanvaller = 1
        verdediger = 1
elif max(a1, a2, a3) > max(v1, v2):
    if min(max(a1, a2), max(a1, a3), max(a2, a3)) <= min(v1, v2):
        aanvaller = 1
        verdediger = 1
    else:
        aanvaller = 0
        verdediger = 2
else:
    if min(max(a1, a2), max(a1, a3), max(a2, a3)) <= min(v1, v2):
        aanvaller = 2
        verdediger = 0
    else:
        aanvaller = 1
        verdediger = 1

uitvoer = 'aanvaller verliest {} legers, verdediger verliest {} legers'
uitvoer2 = 'aanvaller verliest {} leger, verdediger verliest {} leger'
if aanvaller != verdediger:
    print(uitvoer.format(aanvaller, verdediger))
else:
    print(uitvoer2.format(aanvaller, verdediger))


