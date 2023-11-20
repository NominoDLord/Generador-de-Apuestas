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

from typing import List

def generar_apuestas(apuesta_minima, apuesta_maxima, multiplicador) -> List[float]:
    """
    La función genera un listado de apuestas que inicia en su valor mínimo.

       1. Se calcula el beneficio base utilizando la fórmula:
            beneficio_base = (apuesta_minima * multiplicador) - apuesta_minima

       2. Se calcula el incremento como apuesta_minima / beneficio_base.

    El incremento máximo está limitado por el valor máximo de apuesta.

    @param apuesta_minima: El valor de apuesta mínima.
    @param apuesta_maxima: El valor de apuesta máxima.
    @param multiplicador: El multiplicador para obtener beneficio.
    @return: Lista de apuestas generadas.
    """
    lista_apuestas = []

    beneficio_base = (apuesta_minima * multiplicador) - apuesta_minima
    incremento = apuesta_minima / beneficio_base if beneficio_base != 0 else 0

    while apuesta_minima < apuesta_maxima:
        lista_apuestas.append(round(apuesta_minima, 2))
        apuesta_minima *= incremento

    return lista_apuestas