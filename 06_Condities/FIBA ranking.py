#    Puntenverschil	     Punten winnaar	  Punten verliezer
# Minder dan 10 punten	    600	               400
#Vanaf 10 tot 20 punten	    700 	           300
#Vanaf 20 punten	            800	               200

ploeg_thuis = int(input('score thuisteam: '))
ploeg_uit = int(input('score bezoekteam: '))
verschil = ploeg_thuis - ploeg_uit
#berekenen
if ploeg_thuis > ploeg_uit: #ploeg thuis wint -70
    if ploeg_thuis - ploeg_uit >= 20:
        punten_thuis = 730
        punten_uit = 270
    elif ploeg_thuis - ploeg_uit < 10:
        punten_thuis = 530
        punten_uit = 470
    else:
        punten_thuis = 630
        punten_uit = 370
else: #bezoekende ploeg wint + 70
    if ploeg_uit - ploeg_thuis >= 20:
        punten_thuis = 130
        punten_uit = 870
    elif ploeg_uit - ploeg_thuis < 10:
        punten_thuis = 330
        punten_uit = 670
    else:
        punten_thuis = 230
        punten_uit = 770

thuisploeg = 'thuisploeg: {:.2f}'
uitploeg = 'uitploeg: {:.2f}'

#uitvoer
print(thuisploeg.format(punten_thuis))
print(uitploeg.format(punten_uit))
