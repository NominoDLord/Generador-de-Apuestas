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

""" MÓDULO: ListasPosiciones

"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

from LecturaTXT_Bools import leer_bools  # Arg: Nombre_Archivo (El archivo debe estar dentro de la carpeta `Registros`)
    # NOTA: El archivo debe estar en la carpeta 'Registros' para que funciones este módulo.
from Porcentuajes import porcentajes, porcentuales  # cantidad, total, rondas
from ContarRepeticiones import contar_posicion  # (lista: List[bool], lng_t: int, lng_f: int)
from GenerarProporcion import proporcion  # trues: int, falses: int, resultado_ronda: bool
from SumarRepeticiones import suma_posicion  # lista

# ================================================== [ VARIABLES ] =================================================== #

SALDO_INICIAL = 250  # float(input("Introducir el saldo inicial: "))
OPCIONES_TRUES = 3  # int(input("Número de opciones 'True': "))
OPCIONES_FALSE = 1  # int(input("Número de opciones 'False': "))
OPCIONES_TOTALES = OPCIONES_TRUES + OPCIONES_FALSE
MULTIPLICADOR = 1.32  # float(input("Introducir 'Multiplicador' [Beneficio = (Apuesta * Multiplicador) - Apuesta]: "))


# ================================================== [ EJECUCIÓN ] =================================================== #



# PRUEBAS ---------------------------------------------------------------------------------------------------------

def prueba():

    Nombre_Archivo = input("Nombre del archivo: ")  # Resultados[75-25](1) → 1883
    Lista_Resultados = leer_bools(f"{Nombre_Archivo}.txt")
    longitud_lista = len(Lista_Resultados)  # La longitud de la lista corresponde al total de rondas

    lista_porcentajes_trues = porcentajes(OPCIONES_TRUES, OPCIONES_TOTALES, longitud_lista)
    lista_porcentajes_false = porcentajes(OPCIONES_FALSE, OPCIONES_TOTALES, longitud_lista)

    llpt = len(lista_porcentajes_trues)
    llpf = len(lista_porcentajes_false)

    lista_contada_trues, lista_contada_false = contar_posicion(Lista_Resultados, llpt, llpf)

    print(f"Posiciones de repetición [Trues]: {lista_contada_trues}")
    print(f"Posiciones de repetición [False]: {lista_contada_false}")

    # proporcion_trues, proporcion_false = proporcion(OPCIONES_TRUES, OPCIONES_FALSE, Lista_Resultados)

    num_trues = Lista_Resultados.count(True)  # 1394
    num_false = Lista_Resultados.count(False)  # 489
    num_total = num_trues + num_false  # 1883 (Debe ser el mismo valor que "longitud_lista" (total de rondas))

    print(f"Proporción [True|False]: {num_trues} | {num_false}")
    print(f"Porcentaje [True|False]: {round(((num_trues / num_total) * 100), 2)}"
          f" | "
          f"{round(((num_false / num_total) * 100), 2)}")

    suma_posiciones_trues = suma_posicion(lista_contada_trues)  # 1394
    suma_posiciones_false = suma_posicion(lista_contada_false)  # 489

    print(f"Suma de posiciones [Trues]: {suma_posiciones_trues}")
    print(f"Suma de posiciones [False]: {suma_posiciones_false}")

    return

prueba()

"""
Nombre del archivo: Resultados[75-25](1)
Posiciones de repetición [Trues]: [103, 80, 49, 44, 27, 23, 23, 9, 8, 3, 2, 5, 1, 4, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Posiciones de repetición [False]: [299, 70, 12, 1, 2, 0, 0, 0]
Proporción [True|False]: 1394 | 489
Porcentaje [True|False]: 74.03 | 25.97
Suma de posiciones [Trues]: 1394
Suma de posiciones [False]: 489
"""

#
