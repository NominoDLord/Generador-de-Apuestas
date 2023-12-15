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
La apuesta se realiza en base a la proporción entre los aciertos y los fallos.
- Se establece una apuesta base para las veces en el que la proporción es igual.
- Se establece una apuesta superior a la apuesta base cuando la proporción es negativa.
- Se establece una apuesta inferior a la apuesta base cuando la proporción es negativa.
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(subDir1, '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.configuracion import *

from random import choice

# ================================================== [ VARIABLES ] =================================================== #

cnt_resultados = 0  # Variable de inicialización

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados):
    global cnt_resultados

    cnt_resultados = cnt_resultados + OPCIONES_FALSE if resultados is True else cnt_resultados - OPCIONES_TRUE
    # print(cnt_resultados)

    if cnt_resultados > 0:
        apuesta = OPCIONES_FALSE

    elif cnt_resultados < 0:
        apuesta = OPCIONES_TRUE

    else:
        apuesta = (OPCIONES_TOTALES / 2)

    return round(apuesta, 2)

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    ronda = 0
    while ronda < 100:
        ronda += 1

        resultado = choice(LISTA_OPCIONES)
        apuesta = calcular_apuesta(resultado)
        print(f"Ronda {ronda}\nApuesta: {apuesta}\nResultado: {resultado}")
        print("--------------------")

    return None

# prueba()
