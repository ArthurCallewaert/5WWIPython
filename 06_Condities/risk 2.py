a1 = int(input('dobbelsteen aanvaller: '))
a2 = int(input('dobbelsteen aanvaller: '))
a3 = int(input('dobbelsteen aanvaller: '))

v1 = int(input('dobbelsteen verdediger: '))
v2 = int(input('dobbelsteen verdediger: '))

#berekenen
if max(a1, a2, a3) <= max(v1, v2):
    if min(max(a1, a2), max(a1, a3), max(a2, a3)) <= min(v1, v2):
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif max(a1, a2, a3) > max(v1, v2):
    if min(max(a1, a2), max(a1, a3), max(a2, a3)) > min(v1, v2):
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
