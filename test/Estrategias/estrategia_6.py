########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 06
El resultado de la apuesta se limita a la proporción de los últimos 100 resultados.
- Hasta generar los primeros 100 resultados, la apuesta es la mínima.
- Una vez generados los 100 resultados:
    · Cuanto mayor sea la proporción de fallos, la apuesta se incrementará.
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

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados):

    LISTA_RESULTADOS.append(resultados)

    apuesta = APUESTA_MINIMA

    if len(LISTA_RESULTADOS) > 100:
        del LISTA_RESULTADOS[0]

        contar_falses = LISTA_RESULTADOS.count(False)

        if contar_falses > (PORCENTAJE_FALSE * 1.5):
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 5)

        elif contar_falses > (PORCENTAJE_FALSE * 1.4):
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 4)

        elif contar_falses > (PORCENTAJE_FALSE * 1.3):
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 3)

        elif contar_falses > (PORCENTAJE_FALSE * 1.2):
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 2)

        else:
            apuesta = APUESTA_MINIMA * (OPCIONES_TRUE ** 1)

    return round(apuesta, 2)

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    ronda = 0
    while ronda < 1000:
        ronda += 1

        resultado = choice(LISTA_OPCIONES)
        apuesta = calcular_apuesta(resultado)
        print(f"Ronda {ronda}\nApuesta: {apuesta}\nResultado: {resultado}")
        print("--------------------")

    return None

# prueba()
