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

"""
    PRUEBAS

    Código para ejecutar las estratégias definidas en:

        .../Estrategias/estrategia_00.py

    Para poder ejecutar las estratégias, necesitaremos generar los siguientes resultados:

        > True      (Para los aciertos)
        > False     (Para los fallos)

    Para generar los resultados, tenemos dos opciones:

        · Opción 1

            En la carpeta `Registros` se dispone de una variedad de resultados guardados en archivos de texto [.txt].
            Estos resultados han sido generados interactuando dentro de una plataforma (real) de apuestas.

            Para usarlos, tendremos que utilizar el módulo `LecturaTXT_Bools.py` para leer el archivo y guardar
            los resultados en una lista.

            Una vez creada la lista con los resultados guardados, podemos iterar los datos para realizar las pruebas.

        · Opción 2

            Se dispone del módulo `GenerarBools.py` donde podremos generar los resultados indicando como argumentos
            el número de opciones que hay de acertar y fallar.

            Usando este módulo junto con un bucle (while), podemos generar tantos resultados aleatorios como queramos.

"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import importlib
from random import choice as aleatorio

from LecturaTXT_Bools import leer_bools  # Arg: Nombre_Archivo (El archivo debe estar dentro de la carpeta `Registros`)
from GenerarBools import generar_lista  # Args: trues, falses

# ================================================== [ VARIABLES ] =================================================== #

global saldos

RONDA = 0
SALDO_INICIAL = 250  # float(input("Introducir el saldo inicial: "))
OPCIONES_TRUE = 3  # int(input("Número de opciones 'True': "))
OPCIONES_FALSE = 1  # int(input("Número de opciones 'False': "))
MULTIPLICADOR = 1.32  # float(input("Introducir 'Multiplicador' [Beneficio = (Apuesta * Multiplicador) - Apuesta]: "))

# ================================================ CLASES & FUNCIONES ================================================ #

def contar_rondas() -> int:
    global RONDA
    RONDA += 1
    return RONDA


def actualizar_saldo(apuesta: float, resultado: bool) -> float:

    global saldos

    """
    @param apuesta: Cantidad apostada.
    @param resultado: bool
        True → Acertar
        False → Fallar
    @return: Saldo final.
    """

    # Iniciar variable 'saldo_actual' -----------------------------------------------------------------------------
    if not hasattr(actualizar_saldo, "guardar_saldo_inicial"):
        # Este bloque impedirá que el saldo se regenere al volver a llamar a la función.
        saldos = SALDO_INICIAL
    actualizar_saldo.guardar_saldo_inicial = True
    # -------------------------------------------------------------------------------------------------------------

    beneficio = (apuesta * MULTIPLICADOR) - apuesta

    if resultado is True:
        saldos += beneficio
        saldo = round(saldos, 2)
        return saldo

    elif resultado is False:
        saldos -= apuesta
        saldo = round(saldos, 2)
        return saldo

def generar_proporcion(resultado_ronda):

    # -------------------------------------------------------------------------------------------------------------
    # Inicializar proporcion_true y proporcion_false si no existen
    if not hasattr(generar_proporcion, "proporcion_true"):
        generar_proporcion.proporcion_true = 0
    if not hasattr(generar_proporcion, "proporcion_false"):
        generar_proporcion.proporcion_false = 0
    # -------------------------------------------------------------------------------------------------------------

    if resultado_ronda is True:
        generar_proporcion.proporcion_true += OPCIONES_FALSE

    elif resultado_ronda is False:
        generar_proporcion.proporcion_false += OPCIONES_TRUE

    return generar_proporcion.proporcion_true, generar_proporcion.proporcion_false


def imprimir_datos(rondas, saldo, cantidad_apostada, resultado_ronda):

    proporcion_trues, proporcion_falses = generar_proporcion(resultado_ronda)

    print(f"RONDA: {str(rondas)}")
    print(f"SALDO: {str(saldo)}")
    print(f"APUESTA: {str(cantidad_apostada)}")
    print(f"RESULTADO: {str(resultado_ronda)}")
    print(f"PROPORCIÓN [T|F]: {str(proporcion_trues)} | {str(proporcion_falses)}")
    print(f"BENEFICIO: {str(round((saldo - SALDO_INICIAL), 2))}")
    print("--------------------------------------------------")


# =================================================== [ EJECUCIÓN ] ================================================== #

# PRUEBAS: TEXTO --------------------------------------------------------------------------------------------------

def generar_prueba_texto(usar: int = 0):

    global RONDA

    """
    Para 'usar' correctamente la función, se deberá establecer el número que corresponde al módulo que se quiere usar.

    @param usar: Esta variable define el módulo a importar.
    @return: En caso de que `usar` sea 0, la función no será usada.
    """

    if usar == 0:
        return

    nombre_modulo = f"Estrategias.estrategia_0{usar}"
    estrategia = importlib.import_module(nombre_modulo)  # Args: resultado, opciones_true, opciones_false

    Nombre_Archivo = input("Nombre del archivo: ")  # Resultados[75-25](1)
    resultados = leer_bools(f"{Nombre_Archivo}.txt")

    for resultado in resultados:

        RONDA = contar_rondas()
        apuesta_generada = estrategia.calcular_apuesta(resultado, OPCIONES_TRUE, OPCIONES_FALSE)
        saldo = actualizar_saldo(apuesta_generada, resultado)

        imprimir_datos(RONDA, saldo, apuesta_generada, resultado)

        if saldo < 100:
            break


# PRUEBAS: RANDOM -------------------------------------------------------------------------------------------------

def generar_prueba_random(usar: int = 0, rondas: int = 0):

    global RONDA

    if usar == 0:
        return

    """
    Para 'usar' correctamente la función, se deberá establecer el número que corresponde al módulo que se quiere usar.

    @param usar: Esta variable define el módulo a importar.
    @return: En caso de que `usar` sea 0, la función no será usada.
    """

    nombre_modulo = f"Estrategias.estrategia_0{usar}"
    estrategia = importlib.import_module(nombre_modulo)  # Args: resultado, opciones_true, opciones_false

    lista = generar_lista(OPCIONES_TRUE, OPCIONES_FALSE)

    while RONDA < rondas:

        RONDA = contar_rondas()
        resultado = aleatorio(lista)
        apuesta_generada = estrategia.calcular_apuesta(resultado, OPCIONES_TRUE, OPCIONES_FALSE)
        saldo = actualizar_saldo(apuesta_generada, resultado)

        imprimir_datos(RONDA, saldo, apuesta_generada, resultado)

        if saldo < 100:
            break

generar_prueba_texto(1)  # Pruebas en caso de usar el módulo 'LecturaTXT_Bools'
generar_prueba_random(0, 1000)  # Pruebas en caso de usar el módulo 'GenerarBools'.
