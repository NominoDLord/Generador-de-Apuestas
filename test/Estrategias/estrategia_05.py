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


# ================================================== [ VARIABLES ] =================================================== #

global proporcion_true, proporcion_false

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(rondas, resultados):

    global proporcion_true, proporcion_false

    if rondas == 1:
        proporcion_true = 0
        proporcion_false = 0

    def proporcion():

        global proporcion_true, proporcion_false

        if resultados is True:
            proporcion_true += OPCIONES_FALSE

        elif resultados is False:
            proporcion_false += OPCIONES_TRUE

    proporcion()

    if proporcion_true > proporcion_false:
        apuesta = OPCIONES_FALSE * 1

    elif proporcion_true < proporcion_false:
        apuesta = OPCIONES_TRUE * 1

    else:
        apuesta = OPCIONES_TOTALES / 2

    return apuesta


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    apuesta = calcular_apuesta(1, True)
    print(apuesta)
    apuesta = calcular_apuesta(2, False)
    print(apuesta)
    apuesta = calcular_apuesta(3, True)
    print(apuesta)
    apuesta = calcular_apuesta(4, True)
    print(apuesta)
    apuesta = calcular_apuesta(5, True)
    print(apuesta)

# prueba()
