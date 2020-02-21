from math import sqrt

def binnen_of_buiten(middelpunt, punt_op_cirkel, punt):
    straal = sqrt((punt_op_cirkel[0] - middelpunt[0]) ** 2 + (punt_op_cirkel[1] - middelpunt[1]) ** 2)
    afstand_middelpunt = sqrt((punt[0] - middelpunt[0]) ** 2 + (punt[1] - middelpunt[1]) ** 2)

    if afstand_middelpunt > straal:
        plaats = 'buiten'
    elif afstand_middelpunt < straal:
        plaats = 'binnen'
    else:
        plaats = 'op'
    return plaats, round(afstand_middelpunt, 4)
