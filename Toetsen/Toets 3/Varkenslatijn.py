def verwijder_medeklinkers(woord):
   for i in range(0, len(woord)):
        if woord[i] in 'auoie':
            if i != 0:
                woord = woord[i:]
            return woord

def varkenslatijn(woord):
    if woord[0] in 'auoie':
        woord += 'ibus'
    elif woord[-1] in 'aiu':
        woord += 'nt'
    else:
        woord = verwijder_medeklinkers(woord) + 'itum'

    for i in range(0, len(woord)):
        if woord[i] == 'j' or woord[i] == 'y':
            if woord[i] == 'j':
                woord = woord[:i] + 'i' + woord[i+1:]
            else:
                woord = woord[:i] + 'z' + woord[i+1:]


    return woord

def vertaal(zin):
    zin = zin.split()
    for i in range(0, len(zin)):
        zin = zin + zin[i]
    return zin



 
