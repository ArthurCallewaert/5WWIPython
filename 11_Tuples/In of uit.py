from math import sqrt
def binnen_of_buiten(gegevens):
    r_c = sqrt((gegevens[0, 0] - gegevens[1, 0])**2 + (gegevens[0, 1] - gegevens[1, 1])**2)
    t_c = sqrt((gegevens[0, 0] - gegevens[2, 0])**2 + (gegevens[0, 1] - gegevens[2, 1])**2)
    if r_c == t_c:
        locatie = 'op'
    elif r_c > t_c:
        locatie = 'binnen'
    else:
        locatie = 'buiten'

    return locatie, round(t_c, 4)
