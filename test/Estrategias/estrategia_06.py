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

global contador, lista, apuesta


# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(rondas, resultados):
    global contador, lista, apuesta

    if rondas == 1:
        apuesta = APUESTA_MINIMA
        lista = []
        contador = 0


    lista.append(resultados)

    contador = 0 if resultados is True else contador + 1

    if len(lista) > 60:
        lista_recortada = lista[-60:]

        count_true = lista_recortada.count(True)
        count_false = lista_recortada.count(False)

        if (count_true / 60) < 0.6:
            apuesta = round(OPCIONES_TRUE, 2)

        elif (count_true / 60) > 0.72:
            apuesta = round(OPCIONES_FALSE, 2)

        # if contador == 5:
        #     apuesta *= OPCIONES_TRUE

        if contador == 6:
            apuesta **= OPCIONES_TRUE
        return apuesta

    return APUESTA_MINIMA


# PRUEBAS ---------------------------------------------------------------------------------------------------------

def prueba():

    pass

# prueba()
