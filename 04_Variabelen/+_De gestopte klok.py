#invoer
vertrek_uur1 = int(input('vertrek uur thuis: '))
vertrek_min1 = int(input('vertrek min thuis: '))

aankomst_uur1 = int(input('aankomst uur bij vriendin: '))
aankomst_min1 = int(input('aankomst min bij vriendin: '))

vertrek_uur2 = int(input('vertrek uur bij vriendin: '))
vertrek_min2 = int(input('vertrek min bij vriendin: '))

aankomst_uur2 = int(input('aankomst uur thuis: '))
aankomst_min2 = int(input('aankomst min thuis: '))

#berekening
foutieve_min = (aankomst_uur2 - vertrek_uur1)*60 + aankomst_min2 - vertrek_min1
vriendin_min = (vertrek_uur2 - aankomst_uur1)*60 + vertrek_min2 - aankomst_min1
reis = (foutieve_min - vriendin_min) / 2
juist = vertrek_uur2*60 + vertrek_min2 + reis
uur = juist // 60
juist %= 60

#uitvoer
print(int(uur))
print(int(juist))
