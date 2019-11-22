#invoer
p1 = input('persoon 1: ')
p2 =  input('persoon 2: ')
omgekeerde_kl = input('persoon omgekeerde kleur: ')

#berekenen
if omgekeerde_kl == '2':
    if p1 == 'zwart':
        p1 = p2
        p2 = 'wit'
    else:
        p1 = p2
        p2 = 'zwart'
else:
    if p2 == 'zwart':
        p2 = p1
        p1 = 'wit'
    else:
        p2 = p1
        p1 = 'zwart'

print(p1)
print(p2)
