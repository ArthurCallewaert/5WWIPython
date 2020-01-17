#invoer
woord = input("woord: ")
bedrag = int(input("bedrag: "))
letter = input("letter: ")
gegokte_letters, geldsom = "", 0

#berekenen
while letter in woord and not letter in gegokte_letters:
    gegokte_letters += letter
    geldsom += bedrag
    letter = input("letter: ")

#uitvoer
print(geldsom)

