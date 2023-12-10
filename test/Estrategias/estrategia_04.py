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

global lista_resultados, lista_trues, lista_falses

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(rondas, resultados):
    global lista_resultados, lista_trues, lista_falses

    if rondas == 1:
        lista_resultados = []
        lista_trues = [True] * int(PORCENTAJE_TRUE)
        lista_falses = [False] * int(PORCENTAJE_FALSE)

    def contar_valores(listas):
        true_count, false_count = 0, 0

        for elemento in listas:
            true_count += elemento.count(True)
            false_count += elemento.count(False)
        return true_count, false_count

    lista_resultados.append(resultados)

    if resultados is True and len(lista_trues) > 0:
        lista_trues.pop()

    if resultados is False and len(lista_falses) > 0:
        lista_falses.pop()

    listas_trues_falses = [lista_resultados, lista_trues, lista_falses]
    total_trues, total_falses = contar_valores(listas_trues_falses)

    proporcion_trues = total_trues * OPCIONES_FALSE
    proporcion_falses = total_falses * OPCIONES_TRUE

    if proporcion_trues < proporcion_falses:
        apostar = OPCIONES_TRUE * 1
        return apostar

    if proporcion_trues > proporcion_falses:
        apostar = OPCIONES_FALSE * 1
        return apostar

    if proporcion_trues == proporcion_falses:
        apostar = OPCIONES_TOTALES / 2
        return apostar


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    pass

# prueba()
