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

""" GenerarProporcion

    MÓDULO: Calcula la proporción entre los valores Trues y Falses.
    
    La proporción se basa en la diferencia entre opciones de Aciertos y Fallos.
    
    La función devuelve la cantidad proporcional entre los dos valores.
"""

from typing import List, Tuple


def proporcion(trues: int, falses: int, resultado_ronda: bool) -> tuple[int, int]:

    # -------------------------------------------------------------------------------------------------------------
    # Inicializar proporcion_true y proporcion_false si no existen
    if not hasattr(proporcion, "proporcion_true"):
        proporcion.proporcion_true = 0
    if not hasattr(proporcion, "proporcion_false"):
        proporcion.proporcion_false = 0
    # -------------------------------------------------------------------------------------------------------------

    if resultado_ronda is True:
        proporcion.proporcion_true += falses

    elif resultado_ronda is False:
        proporcion.proporcion_false += trues

    return proporcion.proporcion_true, proporcion.proporcion_false


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    calcular_proporcion = proporcion(3, 1, True)
    print(calcular_proporcion)  # (1, 0)

    calcular_proporcion = proporcion(3, 1, True)
    print(calcular_proporcion)  # (2, 0)

    calcular_proporcion = proporcion(3, 1, False)
    print(calcular_proporcion)  # (2, 3)

    calcular_proporcion = proporcion(3, 1, True)
    print(calcular_proporcion)  # (3, 3)

# prueba()
