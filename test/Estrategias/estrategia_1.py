########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 01
Estrategia base que consiste simplemente en realizar siempre la misma apuesta con el mismo valor.
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(subDir1, '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.configuracion import *

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_apuesta(resultados):
    """El argumento 'resultados' no es necesario, pero se incluye porque en los otros métodos sí que se usa,
    por lo que implicaría modificar la llamada a la función, pero de esta forma, se pueden seguir usando sin
    ninguna modificación y sin provocar errores"""
    apuesta = APUESTA_MINIMA
    return apuesta

# ===================================================== [ TEST ] ===================================================== #

def prueba():
    ronda = 0
    while ronda < 9:
        ronda += 1
        resultado = choice(LISTA_OPCIONES)
        apuesta = calcular_apuesta(resultado)
        print(f"Ronda {ronda}\nApuesta: {apuesta}\nResultado: {resultado}")
        print("--------------------")
    return None
# prueba()
