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
from ContarRepeticiones import contar_por_posicion  # (lista: List[bool], lng_t: int, lng_f: int)


# ================================================== [ VARIABLES ] =================================================== #

SALDO_INICIAL = 250  # float(input("Introducir el saldo inicial: "))
OPCIONES_TRUE = 3  # int(input("Número de opciones 'True': "))
OPCIONES_FALSE = 1  # int(input("Número de opciones 'False': "))
MULTIPLICADOR = 1.32  # float(input("Introducir 'Multiplicador' [Beneficio = (Apuesta * Multiplicador) - Apuesta]: "))


# ================================================== [ EJECUCIÓN ] =================================================== #

def crear_listas(lista):

    """

    """



    lst_psc_True, lst_psc_False = contar_por_posicion(lista, 30, 10)


    return lst_psc_True, lst_psc_False



# PRUEBAS ---------------------------------------------------------------------------------------------------------

def prueba():

    Nombre_Archivo = input("Nombre del archivo: ")  # Resultados[75-25](1)
    Lista_Resultados = leer_bools(f"{Nombre_Archivo}.txt")

    print(Lista_Resultados)

    pass

crear_listas()

#
