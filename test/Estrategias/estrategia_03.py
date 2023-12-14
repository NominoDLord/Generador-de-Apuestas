########################################################################################################################
##                                                                                                                    ##
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 03
Estrategia personalizada para " Egg Catcher "
"""

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(subDir1, '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.configuracion import *

from time import sleep

global contador

def calcular_apuesta(rondas, resultados):
    global contador

    if rondas == 1:
        contador = 0

    contador = 0 if resultados is True else contador + 1

    if contador == 1:
        return 50

    elif contador == 2:
        return APUESTA_MAXIMA

    elif contador == 3:
        return APUESTA_MAXIMA

    elif contador == 5:
        return APUESTA_MAXIMA

    elif contador == 6:
        return APUESTA_MAXIMA

    else:
        return APUESTA_MINIMA


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():
    return None

# prueba()
