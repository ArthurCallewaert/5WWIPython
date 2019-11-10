#naam= input('geef naam: ')
#aantal_klinkers = 0
#for letter in naam:
#    if letter in 'aeuoi':
#        aantal_klinkers += 1


#print(aantal_klinkers, len(naam) - aantal_klinkers)
#------------------------------------------------------------------------
#naam = input('geef naam: ')
#i = 1
#for letter in naam:
#    print(i * letter)
#    i += 1
#------------------------------------------------------------------------
#for i in range(2, 7):
#    print(i)
#------------------------------------------------------------------------
#for i in range(2, 7, 2):
#    print(i)
#------------------------------------------------------------------------
#for i in range(6):
#    print('m')

naam = (input('geef naam: '))
i = 1
for letter in naam: # "1234"
    print(i * int(letter)) # "1" "2" ...
    i += 1
