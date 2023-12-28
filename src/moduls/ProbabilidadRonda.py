########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

from typing import Tuple, Union

def lista_probabilidad(aciertos: int, fallos: int, limit_positivos: float = 0.03, limit_negativos: float = 0.01) -> \
                       Tuple[Tuple[Union[int, float], ...], Tuple[Union[int, float], ...]]:
    """
    Esta función genera dos tuplas que contendrán en su índice la probabilidad
    que hay de que se repita un mismo resultado.

    :param aciertos: Número de opciones aciertos
    :param fallos: Número de opciones fallos
    :param limit_positivos: Define un límite al generar la lista
    :param limit_negativos: Define un límite al generar la lista
    :return: Devuelve dos tuplas con los porcentajes calculados por ronda
    """
    total = aciertos + fallos

    porcentaje_base_aciertos = (aciertos / total) * 100
    porcentaje_base_fallos = (fallos / total) * 100

    def generar_lista_probabilidades_aciertos() -> Tuple[Union[int, float], ...]:
        """Genera una lista sobre la probabilidad que existe de acertar X veces seguidas"""

        lista_probabilidad_aciertos = []  # Se crea una lista vacía para añadir los valores
        probabilidad_acertar = porcentaje_base_aciertos

        while limit_positivos < probabilidad_acertar:
            lista_probabilidad_aciertos.append(round(probabilidad_acertar, 3))
            probabilidad_acertar *= porcentaje_base_aciertos / 100

        deslizamiento = 0
        lista_probabilidad_aciertos.append(deslizamiento)

        return tuple(lista_probabilidad_aciertos)

    def generar_lista_probabilidades_fallos() -> Tuple[Union[int, float], ...]:
        """Genera una lista sobre la probabilidad que existe de fallar X veces seguidas"""

        lista_probabilidad_fallos = []
        probabilidad_fallar = porcentaje_base_fallos

        while limit_negativos < probabilidad_fallar:
            lista_probabilidad_fallos.append(round(probabilidad_fallar, 3))
            probabilidad_fallar *= porcentaje_base_fallos / 100

        deslizamiento = 0
        lista_probabilidad_fallos.append(deslizamiento)

        return tuple(lista_probabilidad_fallos)

    lista_aciertos = generar_lista_probabilidades_aciertos()
    lista_fallos = generar_lista_probabilidades_fallos()

    return lista_aciertos, lista_fallos
