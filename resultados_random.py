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

from random import choice as aleatorio
from typing import Tuple

def generar_resultado_random(cnt_op: int) -> bool:
    """
    1º- El número introducido generará una lista de opciones.
    2º- Se eligirá una opción de la lista de opciones.
    3º- Se evalua si la opción elegida coincide con la 1r opción generada.

    @param cnt_op: Cantidad de opciones.
    @return: Devuelve "True" si las opciones NO coinciden y "False" si las opciones SÍ coinciden.
    """

    def generar_lista_cadena_opciones() -> Tuple[str]:
        """ Define un nombre para cada posible opción y lo añade a una lista"""

        contador = cnt_op
        prefijo = "OP_"
        lista = []

        while 10 < contador:
            lista.insert(0, prefijo + str(contador))
            contador -= 1

        while 0 < contador <= 10:
            lista.insert(0, prefijo + "0" + str(contador))
            contador -= 1

        listado_de_opciones = tuple(lista)

        return listado_de_opciones


    def generar_opcion_random(lista: Tuple) -> str:
        """
        Elige una opción de una lista de opciones.
        @param lista: Lista de opciones
        @return: Devuelve una opción de la lista
        """
        opcion_random = aleatorio(lista)
        return opcion_random
    
    
    def generar_resultado(lista, opcion):
        """
        @return: Devuelve "False" si la opción random coincide con la opción 1r opción.
        @return: Devuelve "True" si la opción random no coincide con la 1r opción.
        """
        opcion_fija = lista[0]

        if opcion_fija == opcion:
            resultado = False
        else:
            resultado = True

        return resultado

    listado = generar_lista_cadena_opciones()
    opcion_aleatoria = generar_opcion_random(listado)
    resultados = generar_resultado(listado, opcion_aleatoria)

    return resultados
