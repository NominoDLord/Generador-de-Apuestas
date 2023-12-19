########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 11
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
lista = []
saldo_objetivo = SALDO_INICIAL
# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(saldos, resultados, apuestas):
    global lista, apuesta, saldo_objetivo

    if resultados is None:
        # Esto es solo para la resolución de la primera apuesta.
        apuesta = 1

    else:
        lista.append(resultados)

        if len(lista) < 6:
            falses = lista.count(False)
            apuesta = min(99, apuestas * (OPCIONES_TRUE ** falses))

        else:
            del lista[0]
            print(lista)
            i = 1.25 if (saldos < saldo_objetivo) else 0.75

            # if saldos > saldo_objetivo:
            #     saldo_objetivo += 0.1

            falses = lista.count(False)
            apuesta = min(APUESTA_MAXIMA, (APUESTA_MINIMA * (OPCIONES_TRUE ** falses)) * i)

            if apuesta < APUESTA_MINIMA:
                apuesta = APUESTA_MINIMA

            # if resultados is False and saldos > SALDO_INICIAL:
            #     apuesta = min(99, apuestas * 3)
            #
            # if saldos > SALDO_INICIAL:
            #     apuesta = 0.3
            # elif resultados is False:
            #     apuesta = min(99, apuestas * 3)
            # else:
            #     apuesta = 0.9

    return round(apuesta, 2)

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    return None

# prueba()
