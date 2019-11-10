antw1 = str(input('antwoord 1: '))
antw2 = str(input('antwoord 2: '))

#if antw1 == 'ja' and antw2 == 'ja':
#   doden = 2
#elif antw1 == 'ja' and antw2 == 'nee':
#    doden = 1
#elif antw1 == 'nee' and antw2 == 'ja':
#    doden = 1
#else:
#    doden = 5

#berekening
if antw1 != antw2:
    doden = 1
elif antw1 == 'ja':
    doden = 2
else:
    doden = 5

#uitvoer
print(doden)
