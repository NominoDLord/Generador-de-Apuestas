########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 04
Se especifica una apuesta en base al número de repeticiones fallidas.
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

repeticiones = 0

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados):
    global repeticiones

    repeticiones = 0 if resultados is True else repeticiones + 1

    if repeticiones == 0:
        return 1

    elif repeticiones == 1:
        return 1

    elif repeticiones == 2:
        return 2

    elif repeticiones == 3:
        return 2

    elif repeticiones == 4:
        return 5

    elif repeticiones == 5:
        return 10

    elif repeticiones == 6:
        return 20

    elif repeticiones == 7:
        return 50

    elif repeticiones == 8:
        return 50

    elif repeticiones == 9:
        return 80

    else:
        return 99

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    ronda = 0
    while ronda < 50:
        ronda += 1

        resultado = choice(LISTA_OPCIONES)
        apuesta = calcular_apuesta(resultado)
        print(f"Ronda {ronda}\nApuesta: {apuesta}\nResultado: {resultado}")
        print("--------------------")

    return None

# prueba()
