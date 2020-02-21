# --> werk met nieuwe zin
#overloop alle letters van de string
    #indien de letter een spatie is
    #volgende letter wordt hoofdletter
        #plak aan nieuwe zin

def germaniseer(zin):
    #overloop alle letters vn de string
    nieuwe_zin = ''
    for i in range(0, len(zin)):
        # indien de letter een spatie is
        if zin[i] == ' ':
            # volgende letter wordt hoofdletter
            nieuwe_zin += ' ' + zin[i + 1].upper()
        elif zin[i - 1] != ' ':
            nieuwe_zin += zin[i]
    return nieuwe_zin


print(germaniseer('Dit is een test'))
