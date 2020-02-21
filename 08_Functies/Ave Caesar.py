#t = input("letter: ")
#r = int(input("roteren: "))

nieuwe_letter = ""
def is_letter(t):
    return ord("a") <= ord(t) <= ord("z") or ord("A") <= ord(t) <= ord("Z")

def roteer_letter(t, r):
    if ord('a') <= ord(t) <= ord('z'):
        if ord(t) + r > 122:
            nieuwe_letter = chr(ord(t) + r - ord('a'))
        else:
            nieuwe_letter = chr(ord(t) + r)
    else:
        if ord(t) + r > 122:
            nieuwe_letter = chr(ord(t) + r - ord('a'))
        else:
            nieuwe_letter = chr(ord(t) + r)


    nieuwe_letter = chr(ord(t) + r)
    return nieuwe_letter

def versleutel(zin, r):
    uitkomst = ''
    for t in zin:
        uitkomst += roteer_letter(t, r)

    return uitkomst

#print(is_letter(t))
#print(roteer_letter(t, r))
