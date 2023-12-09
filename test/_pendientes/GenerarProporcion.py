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

""" MÓDULO: GenerarProporcion
Calcula la proporción entre los valores Trues y Falses.
La proporción se basa en la diferencia entre opciones de Aciertos y Fallos.
La función devuelve la cantidad proporcional entre los dos valores.
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

from typing import List, Tuple

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.configuracion import *


# ================================================== [ EJECUCIÓN ] =================================================== #

proporcion_true_max, proporcion_true_min = None, None
proporcion_false_max, proporcion_false_min = None, None


def proporcion(resultados: bool) -> tuple[int, int]:

    # ----------------------------------------------------------------------------------------------
    # Inicializar proporcion_true y proporcion_false si no existen
    if not hasattr(proporcion, "proporcion_true"):
        proporcion.proporcion_true = 0
    if not hasattr(proporcion, "proporcion_false"):
        proporcion.proporcion_false = 0
    # ----------------------------------------------------------------------------------------------

    if resultados is True:
        proporcion.proporcion_true += OPCIONES_FALSE

    elif resultados is False:
        proporcion.proporcion_false += OPCIONES_TRUE

    return proporcion.proporcion_true, proporcion.proporcion_false


def proporciones_limite(resultados: bool):

    global proporcion_true_max, proporcion_true_min, proporcion_false_max, proporcion_false_min

    if (proporcion_true_max and proporcion_false_max) is None:
        proporcion_true_max, proporcion_false_max = proporcion.proporcion_true, proporcion.proporcion_false

    if proporcion_true_max < proporcion.proporcion_true:
        proporcion_true_max = proporcion.proporcion_true

    if proporcion_false_max < proporcion.proporcion_false:
        proporcion_false_max = proporcion.proporcion_false

    pass



# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    pass

# prueba()
