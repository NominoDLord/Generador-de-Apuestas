########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA: 08
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(subDir1, '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.configuracion import *
from time import sleep

# ================================================== [ VARIABLES ] =================================================== #

global lista_repeticiones, ultima_repeticion, lista_resultados, repeticion, apuesta
global r01, r02, r03, r04, r05, r06, r07, r08

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(rondas, resultados, saldos):

    global lista_repeticiones, ultima_repeticion, lista_resultados, repeticion, apuesta
    global r01, r02, r03, r04, r05, r06, r07, r08

    if rondas == 1:  # Se inicializan las variables.
        lista_repeticiones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ultima_repeticion = []
        lista_resultados = []
        repeticion = 0

    lista_resultados.append(resultados)
    if len(lista_resultados) > 30:
        del lista_resultados[0]

    contar_falses = lista_resultados.count(False)

    repeticion = 0 if resultados is True else repeticion + 1
    ultima_repeticion.append(repeticion)

    if repeticion == 0:
        """El resultado ha sido True, por lo tanto, se reinicia el valor de la posición repetida"""
        anterior_repeticion = ultima_repeticion[-2]

        if
        lista_repeticiones[anterior_repeticion - 1] = 0

        if len(ultima_repeticion) > 5:
            """Se van eliminando los datos que ya no son necesarios"""
            del ultima_repeticion[0]

        if contar_falses > 10:
            return APUESTA_MINIMA * 2
        elif contar_falses > 15:
            return APUESTA_MINIMA * 3
        elif contar_falses > 20:
            return APUESTA_MINIMA * 4
        elif contar_falses > 25:
            return APUESTA_MINIMA * 5
        else:
            return APUESTA_MINIMA

    if repeticion == 1:
        if lista_repeticiones[repeticion - 1] > 3:

        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_repeticiones[repeticion - 1])
        lista_repeticiones[repeticion - 1] += 1
        r01 = lista_repeticiones[repeticion - 1]

    elif repeticion == 2:
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_repeticiones[repeticion - 1])
        lista_repeticiones[repeticion - 1] += 1
        r02 = lista_repeticiones[repeticion - 1]

    elif repeticion == 3:
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_repeticiones[repeticion - 1])
        lista_repeticiones[repeticion - 1] += 1
        r03 = lista_repeticiones[repeticion - 1]

    elif repeticion == 4:
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_repeticiones[repeticion - 1])
        lista_repeticiones[repeticion - 1] += 1
        r04 = lista_repeticiones[repeticion - 1]

    elif repeticion == 5:
        apuesta = 33
        return apuesta

    elif repeticion == 6:
        apuesta = 99
        return apuesta

    elif repeticion == 7:
        apuesta = 99
        return apuesta

    elif repeticion == 8:
        apuesta = 99
        return apuesta

    else:
        apuesta = APUESTA_MINIMA


    beneficios = (saldos - SALDO_INICIAL)

    if beneficios < 0:
        saldo_inv = abs(beneficios)
        apuesta = saldo_inv * OPCIONES_TRUE
        return round(apuesta, 2)

    if apuesta > 30:
        apuesta = 30
        return round(apuesta, 2)


# PRUEBAS ---------------------------------------------------------------------------------------------------------

def prueba():


    return None

# prueba()