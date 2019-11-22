#invoer
codon = input('codon: ')
codon1 = codon
if len(codon) == 3:
    if codon == "AUG":
        codon = "start"
    elif codon == "UAG" or codon == "UGA" or codon == "UAA":
        codon = "stop"
    else:
        codon = "gewoon"
else:
    codon = "ongeldig"

uitvoer = "Het codon {} is een {} codon."

print(uitvoer.format(codon1, codon))
