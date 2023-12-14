########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA: 07
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
global incremento_1, incremento_2, incremento_3, incremento_4, incremento_5
global incremento_6, incremento_7, incremento_8, incremento_9

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(rondas, resultados):
    global contador, lista, incremento_1, incremento_2, incremento_3, incremento_4, incremento_5
    global incremento_6, incremento_7, incremento_8, incremento_9

    if rondas == 1:
        lista = []
        contador = 0
        incremento_1 = 0
        incremento_2 = 0
        incremento_3 = 0
        incremento_4 = 0
        incremento_5 = 0
        incremento_6 = 0
        incremento_7 = 0
        incremento_8 = 0
        incremento_9 = 0

    lista.append(resultados)
    if len(lista) > 10:
        del lista[0]
    print(lista)

    if lista[-9:] == [False, False, False, False, False, False, False, False, True]:
        incremento_8 = 0

    elif lista[-8:] == [False, False, False, False, False, False, False, True]:
        incremento_7 = 0

    elif lista[-7:] == [False, False, False, False, False, False, True]:
        incremento_6 = 0

    elif lista[-6:] == [False, False, False, False, False, True]:
        incremento_5 = 0

    elif lista[-5:] == [False, False, False, False, True]:
        incremento_4 = 0

    elif lista[-4:] == [False, False, False, True]:
        incremento_3 = 0

    elif lista[-3:] == [False, False, True]:
        incremento_2 = 0

    elif lista[-2:] == [False, True]:
        incremento_1 = 0

    # elif lista[-1:] == [True]:
    #     incremento_1 = 0


    contador = 0 if resultados is True else contador + 1

    if contador == 1:
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_1)
        return round(apuesta, 2)

    elif contador == 2:
        incremento_1 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_2)
        return round(apuesta, 2)

    elif contador == 3:
        incremento_2 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_3)
        return round(apuesta, 2)

    elif contador == 4:
        incremento_3 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_4)
        return round(apuesta, 2)

    elif contador == 5:
        incremento_4 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_5)
        return round(apuesta, 2)

    elif contador == 6:
        incremento_5 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_6)
        return round(apuesta, 2)

    elif contador == 7:
        incremento_6 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_7)
        return round(apuesta, 2)

    elif contador == 8:
        incremento_7 += 1
        apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** incremento_8)
        return round(apuesta, 2)

    else:
        return APUESTA_MINIMA



# PRUEBAS ---------------------------------------------------------------------------------------------------------

def prueba():

    apuesta = calcular_apuesta(1, False)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(2, False)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(3, True)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(4, False)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(5, False)
    print(apuesta)  # 0.9
    apuesta = calcular_apuesta(6, False)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(7, True)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(8, False)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(9, True)
    print(apuesta)  # 2.7
    apuesta = calcular_apuesta(10, False)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(11, False)
    print(apuesta)  # 0.3
    apuesta = calcular_apuesta(12, True)
    print(apuesta)
    apuesta = calcular_apuesta(13, False)
    print(apuesta)
    apuesta = calcular_apuesta(14, False)
    print(apuesta)
    apuesta = calcular_apuesta(15, True)
    print(apuesta)
    apuesta = calcular_apuesta(16, False)
    print(apuesta)
    apuesta = calcular_apuesta(17, False)
    print(apuesta)
    apuesta = calcular_apuesta(18, True)
    print(apuesta)
    apuesta = calcular_apuesta(19, False)
    print(apuesta)
    apuesta = calcular_apuesta(20, False)
    print(apuesta)
    apuesta = calcular_apuesta(21, False)
    print(apuesta)
    apuesta = calcular_apuesta(22, True)
    print(apuesta)
    apuesta = calcular_apuesta(23, False)
    print(apuesta)
    apuesta = calcular_apuesta(24, False)
    print(apuesta)
    return None

# prueba()