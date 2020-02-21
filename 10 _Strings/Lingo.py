
def hint1(gok, woord):
    hint = '' #output
    for i in range(0, len(woord)):
        if gok[i] in woord:
            if gok[i] == woord[i]: # letter in woord en juiste plaats
                hint += gok[i].upper()
            else: # letter in woord maar niet op juiste plaats
                hint += gok[i]
        else:
            hint += '.' #letter niet in het woord
    return hint

def hint2(gok, woord):
    hint = '' #output
    for i in range(0, len(woord)):
        if woord.find(gok[i]) != -1:
            if gok[i] == woord[i]: # letter in woord en juiste plaats
                hint += gok[i].upper()
            else: # letter in woord maar niet op juiste plaats
                hint += gok[i]
        else:
            hint += '.' #letter niet in het woord
    return hint
print(hint1('absec', 'aceet'))
print(hint2('absec', 'aceet'))
