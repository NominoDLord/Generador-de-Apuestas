########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 07
Esta estrategia consiste en tomar como referencia las repeticiones como referencia.
Cada repetición es una posición, en caso de fallar, la posición suma +1.
Cuando se vuelve a pasar por la posición repetida, la apuesta se incrementará proporcionalmente al número de veces
falladas en esa posición. En el caso de acertar, la posición se reinicia a su valor inicial (0).
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

global apuesta

repeticion = 0
repeticion_guardada = []
lista_posiciones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Ajustar según necesidad.

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados):

    global apuesta, repeticion

    repeticion = 0 if resultados is True else repeticion + 1
    repeticion_guardada.append(repeticion)

    # ····· ¡ BLOQUE MUY IMPORTANTE ! ········································································
    if len(repeticion_guardada) < 2:
        # Esta acción es necesaria para poder ir acumulando el resultado anterior y el resultado recurrente.
        repeticion_guardada.append(repeticion)
    # ········································································································
    anterior_posicion = repeticion_guardada[0]

    indice = 0
    for _ in lista_posiciones:
        if lista_posiciones[indice] == -1:
            lista_posiciones[indice] = 0
        indice += 1

    print(lista_posiciones)

    if repeticion == 0:

        if (anterior_posicion - 1) == -1:  # Esto es en caso de que se repitan 2 (o más) resultados 'True' seguidos.
            del repeticion_guardada[0]  # Elimina la posición anterior para poder guardar el siguiente nuevo resultado.
            apuesta = APUESTA_MINIMA
            return round(apuesta, 2)

        if lista_posiciones[anterior_posicion - 1] > 3:
            lista_posiciones[anterior_posicion - 1] -= 1
            del repeticion_guardada[0]
            return round(apuesta, 2)

        # En caso de que el último resultado haya sido un 'False'...
        lista_posiciones[anterior_posicion - 1] = -1  # ... esto reiniciará el contador de la posición repetida.
        del repeticion_guardada[0]
        return round(apuesta, 2)


    elif repeticion == 1:

        if lista_posiciones[repeticion - 1] > 3:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 4)
        else:
            # Esto evaluará las veces que se han fallado en esta posición y se incrementará la apuesta en base a ello.
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_posiciones[repeticion - 1])
            # Esto incrementará en 1 la posición en caso de que el siguiente resultado sea 'False'.
            lista_posiciones[repeticion - 1] += 1


    elif repeticion == 2:

        if lista_posiciones[repeticion - 1] > 3:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 4)
        else:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_posiciones[repeticion - 1])
            lista_posiciones[repeticion - 1] += 1


    elif repeticion == 3:

        if lista_posiciones[repeticion - 1] > 3:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 4)
        else:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_posiciones[repeticion - 1])
            lista_posiciones[repeticion - 1] += 1


    elif repeticion == 4:

        if lista_posiciones[repeticion - 1] > 3:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 4)
        else:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_posiciones[repeticion - 1])
            lista_posiciones[repeticion - 1] += 1

    elif repeticion == 5:

        if lista_posiciones[repeticion - 1] > 3:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 4)
        else:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** lista_posiciones[repeticion - 1])
            lista_posiciones[repeticion - 1] += 1

    elif repeticion == 6:
        sleep(5)
        apuesta = 99

    elif repeticion == 7:
        apuesta = 99

    elif repeticion == 8:
        apuesta = 99

    else:
        apuesta = APUESTA_MINIMA

    del repeticion_guardada[0]

    if apuesta > APUESTA_MAXIMA:
        apuesta = APUESTA_MAXIMA

    return round(apuesta, 2)

# ===================================================== [ TEST ] ===================================================== #

def prueba():
    ronda = 0
    while ronda < 1000:
        ronda += 1
        resultado = choice(LISTA_OPCIONES)
        apuesta_calculada = calcular_apuesta(resultado)
        print(f"Ronda {ronda}\nApuesta: {apuesta_calculada}\nResultado: {resultado}")
        print("--------------------")
    return None
# prueba()