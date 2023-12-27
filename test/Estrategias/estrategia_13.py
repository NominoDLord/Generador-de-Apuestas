########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 12
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(subDir1, '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.setup import *

from ContarRepeticiones import contar_posicion

from time import sleep

# ================================================== [ VARIABLES ] =================================================== #

global generar_apuesta, apuesta

saldo_base = SALDO_INICIAL
saldo_objetivo = saldo_base + 10

contar_true, contar_false = 0, 0  # Recuento total
posicion_true, posicion_false = 0, 0  # Recuento repetición

registro_resultados = []  # Lista total
registro_posiciones_true, registro_posiciones_false = LISTA_POSICIONES_TRUE, LISTA_POSICIONES_FALSE
registro_apuestas = []

unidad_minima = 0.03

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados=None, saldos=None, apuestas=None):
    global apuesta, saldo_objetivo, contar_true, contar_false, posicion_true, posicion_false, generar_apuesta

    """
    
    """

    apuesta = 0  # La apuesta se irá incrementando en cada evaluación.
    ganancias = saldos - saldo_base

    registro_resultados.append(resultados)

    if resultados is True:
        contar_true += 1
        posicion_true += 1

        if posicion_false != 0:
            registro_posiciones_false[(posicion_false - 1)] += 1
            posicion_false = 0  # Se reinicia la posición

    elif resultados is False:
        contar_false += 1
        posicion_false += 1

        if posicion_true != 0:
            registro_posiciones_true[(posicion_true - 1)] += 1
            posicion_true = 0  # Se reinicia la posición


    """ 1º EVALUACIÓN """

    if resultados is True:

        incremento_true = 1 + (PROBABILIDAD_TRUE * (PROBABILIDAD_TRUE ** posicion_true))

        if ganancias < 0:
            perdidas = abs(ganancias)
            lista_apuestas_true = []

            while perdidas > 0.3:
                perdidas *= PROBABILIDAD_TRUE
                lista_apuestas_true.append(perdidas)

            while len(lista_apuestas_true) < 30:
                lista_apuestas_true.append(APUESTA_MINIMA)

            if len(lista_apuestas_true) > 0 and len(lista_apuestas_true) >= (posicion_true - 1):
                elegir_apuesta = lista_apuestas_true[posicion_true - 1]
                generar_apuesta = elegir_apuesta * incremento_true

        else:

            generar_apuesta = OPCIONES_FALSE * incremento_true

        apuesta += generar_apuesta


    elif resultados is False:

        if posicion_false == 0:
            apuesta = 0.3

        elif posicion_false == 1:
            apuesta = 0.6

        elif posicion_false == 4:
            apuesta = 20

        elif posicion_false <= 5:
            apuesta = 30

        else:

            incremento_false = 1 - (PROBABILIDAD_FALSE * (PROBABILIDAD_FALSE ** posicion_false))

            if ganancias < 0:
                perdidas = abs(ganancias)
                lista_apuestas_false = []

                while perdidas > 0.3:
                    perdidas *= PROBABILIDAD_FALSE
                    lista_apuestas_false.append(perdidas)

                exponente = 1
                while len(lista_apuestas_false) < 10:
                    lista_apuestas_false.append(OPCIONES_TRUE * exponente)
                    exponente += 1

                    lista_apuestas_false.sort()

                if len(lista_apuestas_false) > 0 and len(lista_apuestas_false) >= (posicion_false - 1):
                    elegir_apuesta = lista_apuestas_false[posicion_false - 1]
                    generar_apuesta = elegir_apuesta * incremento_false


            else:

                generar_apuesta = OPCIONES_TRUE * incremento_false

            apuesta += generar_apuesta


    else:
        apuesta += APUESTA_MINIMA


    # --- RESOLUCIÓN FINAL -----------------------------------------------------------------------------------

    if apuesta < 0.3:
        apuesta = 0.3

    apuesta = round(apuesta, 2)
    registro_apuestas.append(apuesta)

    print(posicion_false)
    print("-----------------------------------------------------------------------------------------")
    return apuesta


# ===================================================== [ TEST ] ===================================================== #

def prueba():

    return None

# prueba()
