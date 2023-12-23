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
saldo_objetivo = SALDO_INICIAL

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(saldos):
    global apuesta, saldo_objetivo

    # Saldos Negativos · · · · · · · · · · · · · · · · · · · · · ·

    if saldo_objetivo > saldos:
        apuesta = APUESTA_MINIMA * (2 ** 3)

        if (saldo_objetivo - 20) >= saldos:
            apuesta = APUESTA_MINIMA * (2 ** 4)

            if (saldo_objetivo - 50) >= saldos:
                apuesta = APUESTA_MINIMA * (2 ** 5)

    # Saldos Positivos · · · · · · · · · · · · · · · · · · · · · ·

    elif saldo_objetivo <= saldos:
        apuesta = APUESTA_MINIMA * (2 ** 2)

        if (saldo_objetivo + 20) < saldos:
            apuesta = APUESTA_MINIMA * (2 ** 1)

            if (saldo_objetivo + 30) < saldos:
                apuesta = APUESTA_MINIMA * (2 ** 0)

    # Actualizar Saldo Objetivo  · · · · · · · · · · · · · · · · ·

    if (saldo_objetivo + 50) < saldos:
        saldo_objetivo += 50
        nivel = 1

    if nivel == 1:

        if (saldo_objetivo - 100) > saldos:
            saldo_objetivo -= 100
            nivel = 0

    return round(apuesta, 2)


# ===================================================== [ TEST ] ===================================================== #

def prueba():



    return None

# prueba()
