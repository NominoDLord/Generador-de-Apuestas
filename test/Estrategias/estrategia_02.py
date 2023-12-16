########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 02
La apuesta se incrementa en cada repetición de fallo en relación al total de perdidas anteriores.
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

repeticiones = 0  # Inicialización del número de repeticiones.

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados):
    global repeticiones
    repeticiones = 0 if resultados is True else repeticiones + 1
    apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** repeticiones)
    return round(apuesta, 2)

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    ronda = 0
    while ronda < 9:

        ronda += 1
        apuesta = calcular_apuesta(False)

        print(f"Ronda {ronda}\nApuesta: {apuesta}\nResultado: {False}")
        print("--------------------")

    return None

# prueba()
