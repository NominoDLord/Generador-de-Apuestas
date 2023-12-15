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
El resultado de la apuesta se limita a la proporción de los últimos 100 resultados.
- Hasta generar los primeros 100 resultados, la apuesta es siempre la misma (se establece un valor base).
- Una vez generados los 100 resultados:
    · Si el porcentaje de aciertos es igual, la apuesta es el valor base.
    · Si el porcentaje de aciertos es superior, la apuesta es un valor inferior al valor base.
    · Si el porcentaje de aciertos es inferior, la apuesta es un valor superior al valor base.
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

    apuesta = OPCIONES_TOTALES / 2

    if len(LISTA_RESULTADOS) > 100:

        cnt_true = LISTA_RESULTADOS.count(True)

        if cnt_true < PORCENTAJE_TRUE:
            apuesta = OPCIONES_TRUE * 1

        elif cnt_true > PORCENTAJE_TRUE:
            apuesta = OPCIONES_FALSE * 1

        else:
            apuesta = OPCIONES_TOTALES / 2

        del LISTA_RESULTADOS[0]

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
