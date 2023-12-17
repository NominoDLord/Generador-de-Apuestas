########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 09
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

apuesta = APUESTA_MINIMA
contar = 0
saldo_base = SALDO_INICIAL
saldo_objetivo = SALDO_INICIAL + 1
# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(saldos):

    global apuesta, saldo_objetivo, contar, saldo_base

    # print("·····································")
    # print(f"Contar: {contar}")
    # print(f"Saldo Base: {saldo_base}")
    # print(f"Saldo Objetivo: {saldo_objetivo}")
    # print("·····································")

    if saldos > saldo_objetivo:  # Una vez llegado al saldo objetivo...
        saldo_base = saldo_objetivo  # se aumenta el saldo base con el saldo objetivo (actual).
        saldo_objetivo += 3  # y se establece un nuevo saldo objetivo.
        saldo_objetivo = round(saldo_objetivo, 2)
        contar = 0  # Se reinicia el contador de veces que se ha tardado en llegar al saldo objetivo.
        apuesta = APUESTA_MINIMA  # Y se reinician las puestas al mínimo.
        return apuesta

    else:

        if saldos < (saldo_base - 10):
            contar = 1
            apuesta = 1

        # if saldos < (saldo_base - 100):
        #     contar = 1
        #     apuesta = 10
        #
        # if saldos < (saldo_base - 300):
        #     contar = 3
        #     apuesta = 99

    if contar == 0:
        return APUESTA_MINIMA

    else:
        return apuesta



"""
contar += 1

if contar < 10:
    if saldos > saldo_objetivo:
        apuesta = APUESTA_MINIMA
        return round(apuesta, 2)
    else:
        apuesta = APUESTA_MINIMA * 2
        return round(apuesta, 2)

if contar < 30:
    if saldos > saldo_objetivo:
        apuesta = APUESTA_MINIMA * 2
        return round(apuesta, 2)
    else:
        apuesta = APUESTA_MINIMA * 3
        return round(apuesta, 2)

else:
    apuesta = APUESTA_MINIMA * 3 * 2
    return round(apuesta, 2)
"""

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    return None

# prueba()
