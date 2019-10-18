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
vertrek1 = (vertrek_uur1 * 60) + vertrek_min1
aankomst1 = (aankomst_uur1 * 60) + aankomst_min1
vertrek2 = (vertrek_uur2 * 60) + vertrek_min2
aankomst2 = (aankomst_uur2 * 60) + aankomst_min2

f_t = aankomst2 - vertrek1
j_t = vertrek2 - aankomst1
reis = (f_t - groen) / 2
j_min = vertrek2 + j_t
j_uur = j_min // 60
j_min %= 60

#uitvoer
print(int(c_uur))
print(int(c_min))
