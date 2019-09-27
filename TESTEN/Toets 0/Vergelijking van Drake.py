#invoer
i = float(input('i: '))
fi = float(input('fi: '))
L = float(input('L: '))
R = 2
fc = 0.2
#berekening
N = R * i * fi * fc * L

#uitvoer
print('samenlevingen in de melkweg waarmee we zouden kunnen communiceren:', int(N))
