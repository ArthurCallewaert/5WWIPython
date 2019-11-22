#invoer
codon = input('codon: ')

if len(codon) = 3:
    if codon == "AUG":
        codon = "start"
    elif condon == "UAG" or codon == "UGA" or codon == "UAA":
        codon = "stop"
    else:
        codon = "gewoon"
else:
    codon = "ongeldig"

uitvoer = "Het codon {} is een gewoon codon."

print(uitvoer.format(codon))
