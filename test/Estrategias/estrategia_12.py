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

from config.configuracion import *

from ContarRepeticiones import contar_posicion

# ================================================== [ VARIABLES ] =================================================== #

global apuesta

saldo_objetivo = SALDO_INICIAL
contar_trues = 0
contar_falses = 0
repeticion = 0

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados, saldos):
    global saldo_objetivo, repeticion, contar_trues, contar_falses, apuesta

    """ CONTABILIZAR DATOS:  -------------------------------------------------------------------------------------

        Se contabilizan los datos antes de realizar los cálculos de las apuestas en los distintos niveles.
    """

    apuesta_nivel_1, apuesta_nivel_2, apuesta_nivel_3 = 0, 0, 0

    LISTA_RESULTADOS.append(resultados)  # Se añade el resultado (bool) a la lista.

    repeticion = 0 if resultados is True else repeticion + 1


    if resultados is True:
        contar_trues += 1

    else:
        contar_falses += 2.75


    """ NIVEL 0:  ------------------------------------------------------------------------------------------------
    
        Excepción en caso de un número de repeticiones excesivas.
    """

    if repeticion >= 6:

        apuesta = APUESTA_MAXIMA
        return apuesta

    # En caso de que se "active" este nivel, no se procederá a analizar ningún dato más.

    """ NIVEL 1:  ------------------------------------------------------------------------------------------------

        Se toman las posiciones repetidas y se compara la posición actual con la posición anterior.
        La posición actual se multiplica por las opciones de aciertos.
        Si el valor de la posición anterior es menor al de la proporción del valor de la posición actual
        la apuesta resultante se incrementará en función de la diferencia entre estos dos valores.
    """

    if repeticion >= 2:

        # Se toman las longitudes de la lista de porcentajes para crear la lista de posiciones.
        longitud_trues, longitud_falses = len(LISTA_PORCENTAJES_TRUE), len(LISTA_PORCENTAJES_FALSE)

        # Llama a la función para contar el número de repeticiones.
        lista_repeticion_true, lista_repeticion_false = contar_posicion(LISTA_RESULTADOS,
                                                                        longitud_trues, longitud_falses)
        # print(f"{lista_repeticion_true}\n{lista_repeticion_false}")

        posicion_actual = repeticion - 1
        posicion_anterior = repeticion - 2

        valor_posicion_actual = lista_repeticion_false[posicion_actual]
        valor_posicion_anterior = lista_repeticion_false[posicion_anterior]

        if repeticion == 5:

            if (valor_posicion_actual * OPCIONES_TRUE) >= valor_posicion_anterior:
                diferencia_posiciones = (valor_posicion_actual * OPCIONES_TRUE) - valor_posicion_anterior

                if diferencia_posiciones >= 1:
                    apuesta_nivel_1 = (APUESTA_MAXIMA / OPCIONES_TRUE) * diferencia_posiciones


        elif (valor_posicion_actual * OPCIONES_TRUE) >= valor_posicion_anterior:

            diferencia_posiciones = (valor_posicion_actual * OPCIONES_TRUE) - valor_posicion_anterior

            apuesta_nivel_1 = APUESTA_MINIMA * (OPCIONES_TRUE ** (diferencia_posiciones + 1))

        else:
            apuesta_nivel_1 = APUESTA_MINIMA


    """ NIVEL 2:  ------------------------------------------------------------------------------------------------
    
        ---
    """

    if saldos < saldo_objetivo:

        diferencia_saldos = saldo_objetivo - saldos
        apuesta_base = APUESTA_MINIMA
        lista_partes = []
        exponente = 0
        suma = 0

        while suma < diferencia_saldos:

            while exponente <= 5:
                valor = apuesta_base * ((OPCIONES_TOTALES / 2) ** exponente)
                lista_partes.append(round(valor, 2))
                exponente += 1

            suma = round(sum(lista_partes), 2)

            if suma < diferencia_saldos:
                apuesta_base += 0.03
                lista_partes = []
                exponente = 0

        apuesta_nivel_2 = lista_partes[repeticion]


    """ NIVEL 3:  ------------------------------------------------------------------------------------------------

        ---
    """

    if len(LISTA_RESULTADOS) > 99:

        diferencia_proporcional = contar_trues - contar_falses

        if diferencia_proporcional < 0:

            nivel_3 = abs(diferencia_proporcional)
            apuesta_nivel_3 = nivel_3 * (APUESTA_MINIMA * OPCIONES_TRUE)

        else:

            nivel_3 = 1 / diferencia_proporcional
            apuesta_nivel_3 = nivel_3 * (APUESTA_MINIMA * OPCIONES_TRUE)



    """ EVALUACIÓN DE BENEFICIO:  --------------------------------------------------------------------------------

        Actualización del Saldo Objetivo.
    """

    if saldos > (saldo_objetivo + 100):
        saldo_objetivo += 50


    """ RECUENTO:  -----------------------------------------------------------------------------------------------
    
        Se suman las apuestas generadas en todos los niveles para determinar el resultado final de la apuesta.
    """

    recuento_apuestas = apuesta_nivel_1 + apuesta_nivel_2 + apuesta_nivel_3

    if recuento_apuestas <= APUESTA_MINIMA:
        apuesta = APUESTA_MINIMA

    elif (recuento_apuestas >= APUESTA_MAXIMA) and repeticion == 4:
        apuesta = APUESTA_MAXIMA * 0.9

    elif (recuento_apuestas >= APUESTA_MAXIMA) and repeticion == 3:
        apuesta = APUESTA_MAXIMA * 0.8

    elif (recuento_apuestas >= APUESTA_MAXIMA) and repeticion == 2:
        apuesta = APUESTA_MAXIMA * 0.7

    elif (recuento_apuestas >= APUESTA_MAXIMA) and repeticion == 1:
        apuesta = APUESTA_MAXIMA * 0.6


    return round(apuesta, 2)


# ===================================================== [ TEST ] ===================================================== #

def prueba():

    ronda, rondas = 0, 1000

    while ronda < rondas:

        ronda += 1

        resultado = choice(LISTA_OPCIONES)
        print(resultado)
        apuestas = calcular_apuesta(resultado, 1000)  # TODO
        print(apuestas)

    return None

prueba()
