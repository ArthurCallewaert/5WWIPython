#invoer
t1 = int(input('aantal nanoseconden: '))
t2 = t1 * 10**-9
c = 299792458
n = 1.000277
#berkening
d = (c * t2) / (2 * n)
#uitvoer
print(d, 'meter')
