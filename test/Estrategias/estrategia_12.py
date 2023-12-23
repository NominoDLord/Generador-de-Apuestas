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

saldo_objetivo = SALDO_INICIAL

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados, saldos):

    apuesta_nivel_1 = 0

    LISTA_RESULTADOS.append(resultados)  # Se añade el resultado (bool) a la lista.

    repeticion = 0 if resultados is True else repeticion + 1

    """ NIVEL 0:  ------------------------------------------------------------------------------------------------
    
        Excepción en caso de un número de repeticiones excesivas.
    """

    if repeticion <= 6:

        apuesta = APUESTA_MAXIMA
        return apuesta


    """ NIVEL 1:  ------------------------------------------------------------------------------------------------

        Se toman las posiciones repetidas y se compara la posición actual con la posición anterior.
        La posición actual se multiplica por las opciones de aciertos.
        Si el valor de la posición anterior es menor al de la proporción del valor de la posición actual
        la apuesta resultante se incrementará en función de la diferencia entre estos dos valores.
    """

    if repeticion <= 2:

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
    
        En caso de que se llege a un número de repeticiones excesivas, la apuesta a devolver será el valor máximo.
    """

    if saldos < saldo_objetivo:

        diferencia_saldos = saldo_objetivo - saldos
        apuesta_base = APUESTA_MINIMA
        lista_partes = []
        suma = 0

        while diferencia_saldos > suma:

            lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 0))
            lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 1))
            lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 2))
            lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 3))
            lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 4))

            suma = sum(lista_partes)

            if diferencia_saldos < suma:
                apuesta_base += 0.1
                lista_partes = []





    """ NIVEL DE RECUENTO:
        Se suman las apuestas generadas en todos los niveles para determinar el resultado final de la apuesta.
    """



    apuesta = apuesta_nivel_1

    return None


# ===================================================== [ TEST ] ===================================================== #

def prueba():

    ronda, rondas = 0, 30

    while ronda < rondas:

        ronda += 1

        resultado = choice(LISTA_OPCIONES)
        print(resultado)
        calcular_apuesta(resultado)


    return None

prueba()
