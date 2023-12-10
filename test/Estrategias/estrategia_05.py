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

"""
ESTRATEGIA 01

    En esta estrategía se procede a calcular el valor de la apuesta en base a la proporción que existe entre los
    aciertos y los fallos generados en cada una de las rondas.

    El valor de la apuesta constará de 3 posibles opciones:
        · El número de opciones para aciertos.
        · El número de opciones para fallos.
        · La suma de las opciones para aciertos y fallos dividida entre dos.

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

global contador, lista
global incremento_2, incremento_3, incremento_4, incremento_5, incremento_6, incremento_7, incremento_8, incremento_9

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(rondas, resultados):
    global contador, lista, incremento_2, incremento_3, incremento_4, incremento_5
    global incremento_6, incremento_7, incremento_8, incremento_9

    if rondas == 1:
        lista = []
        contador = 0
        incremento_2 = 0
        incremento_3 = 0
        incremento_4 = 0
        incremento_5 = 0
        incremento_6 = 0
        incremento_7 = 0
        incremento_8 = 0
        incremento_9 = 0

    lista.append(resultados)

    if lista[-3:] == [False, False, True]:
        incremento_2 = 0

    if lista[-4:] == [False, False, False, True]:
        incremento_3 = 0

    if lista[-5:] == [False, False, False, False, True]:
        incremento_4 = 0

    if lista[-6:] == [False, False, False, False, False, True]:
        incremento_5 = 0

    if lista[-7:] == [False, False, False, False, False, False, True]:
        incremento_6 = 0

    if lista[-8:] == [False, False, False, False, False, False, False, True]:
        incremento_7 = 0

    if lista[-9:] == [False, False, False, False, False, False, False, False, True]:
        incremento_8 = 0

    if lista[-10:] == [False, False, False, False, False, False, False, False, False, True]:
        incremento_9 = 0

    contador = 0 if resultados is True else contador + 1

    if contador == 2:
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_2 + 1)
        return round(apuesta, 2)

    elif contador == 3:
        incremento_2 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_3 + 1)
        return round(apuesta, 2)

    elif contador == 4:
        incremento_3 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_4 + 1)
        return round(apuesta, 2)

    elif contador == 5:
        incremento_4 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_5 + 1)
        return round(apuesta, 2)

    elif contador == 6:
        incremento_5 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_6)
        return round(apuesta, 2)

    elif contador == 7:
        incremento_6 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_7)
        return round(apuesta, 2)

    elif contador == 8:
        incremento_7 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_8)
        return round(apuesta, 2)

    elif contador == 9:
        incremento_8 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE * contador) * (contador ** incremento_9)
        return round(apuesta, 2)

    else:
        incremento_9 += 1
        return APUESTA_MINIMA


# PRUEBAS ---------------------------------------------------------------------------------------------------------

def prueba():

    pass

# prueba()