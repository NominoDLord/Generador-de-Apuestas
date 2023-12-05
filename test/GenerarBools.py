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

""" GenerarBools

    MÓDULO: Crea una lista con valores True y False.
    
    La lista se genera pasando como argumentos:
    
        1º Arg: El número de opciones opsitivas (True)
        2º Arg: El número de opciones negativas (False)

    La función devuelve una lista con el número de opciones positivas y negativas juntas.
"""

from random import choice as elegir, shuffle
from typing import List


def generar_lista(trues: int, falses: int) -> list[bool]:

    lista_trues = [True] * trues
    lista_falses = [False] * falses

    lista_opciones = lista_trues.copy()  # Copia para evitar modificar la lista original
    lista_opciones.extend(lista_falses)

    shuffle(lista_opciones)  # Mezclar la lista de opciones

    return lista_opciones


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():
    lista_bools = generar_lista(3, 1)

    print(lista_bools)  # Resultado esperado: [True, True, True, False]

# prueba()
