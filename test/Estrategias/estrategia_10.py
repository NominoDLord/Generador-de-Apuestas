########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 10
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(subDir1, '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.configuracion import *

# ================================================== [ VARIABLES ] =================================================== #

global apuesta
contar_trues, contar_falses = 0, 0
ronda = 0
lista = []

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados):
    global apuesta, lista, contar_trues, contar_falses, ronda


    if resultados is None:
        # Esto es solo para la resolución de la primera apuesta.
        apuesta = 1
        ronda += 1

    else:
        ronda += 1
        if resultados is True:
            contar_trues += 1

        else:
            contar_falses += 2.78


    if ronda > 99:


        if contar_trues > contar_falses:

            apuesta = 1

        else:

            apuesta = 3

        # if contar_trues > (contar_falses + 5):
        #
        #     apuesta = 0.5
        #
        # elif contar_trues > contar_falses:
        #
        #     apuesta = 1.5
        #
        #
        #
        # elif (contar_trues - 10) < contar_falses:
        #
        #     apuesta = 4.5
        #
        #
        # elif contar_trues < contar_falses:
        #
        #     apuesta = 14
        #
        # else:
        #
        #     apuesta = 1


    return round(apuesta, 2)

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    return None

# prueba()
