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

from ContarRondas import rondas
from ContarRepeticiones import contar
from GenerarProporcion import proporcion
from ImprimirDatos import imprimir
from ActualizarSaldo import introducir_saldo_inicial, obtener_saldo

from LecturaTXT_Bools import leer_bools  # Arg: Nombre_Archivo (El archivo debe estar dentro de la carpeta `Registros`)
from GenerarBools import generar_lista  # Args: trues, falses

# ================================================== [ VARIABLES ] =================================================== #

global saldo

SALDO_INICIAL = 250  # float(input("Introducir el saldo inicial: "))
OPCIONES_TRUE = 3  # int(input("Número de opciones 'True': "))
OPCIONES_FALSE = 1  # int(input("Número de opciones 'False': "))
MULTIPLICADOR = 1.32  # float(input("Introducir 'Multiplicador' [Beneficio = (Apuesta * Multiplicador) - Apuesta]: "))


# ================================================== [ EJECUCIÓN ] =================================================== #

# PRUEBAS: RANDOM -------------------------------------------------------------------------------------------------

def generar_prueba_random(usar: int = 0, max_rondas: int = 0):
    global saldo

    """
    Para 'usar' correctamente la función, se deberá establecer el número que corresponde al módulo que se quiere usar.

    @param usar: Esta variable define el módulo de la estrategia a importar.
    @return: En caso de que `usar` sea 0, la función no será usada.
    """

    if usar == 0:
        return

    introducir_saldo_inicial(SALDO_INICIAL)
    saldo = SALDO_INICIAL

    nombre_modulo = f"Estrategias.estrategia_0{usar}"
    estrategia = importlib.import_module(nombre_modulo)  # Args: resultado, opciones_true, opciones_false

    lista = generar_lista(OPCIONES_TRUE, OPCIONES_FALSE)

    ronda = rondas()

    while ronda <= max_rondas:

        resultado = aleatorio(lista)
        apuesta = estrategia.calcular_apuesta(resultado, OPCIONES_TRUE, OPCIONES_FALSE)
        saldo = obtener_saldo(saldo, apuesta, MULTIPLICADOR, resultado)

        imprimir(SALDO_INICIAL, ronda, saldo, OPCIONES_TRUE, OPCIONES_FALSE, apuesta, resultado)
        ronda = rondas()

        if saldo < 100:
            break


generar_prueba_random(0, 1000)  # Pruebas en caso de usar el módulo 'GenerarBools'.


# PRUEBAS: TEXTO --------------------------------------------------------------------------------------------------

def generar_prueba_texto(usar: int = 0):
    global saldo
    """
    Para 'usar' correctamente la función, se deberá establecer el número que corresponde al módulo que se quiere usar.

    @param usar: Esta variable define el módulo de la estrategia a importar.
    @return: En caso de que `usar` sea 0, la función no será usada.
    """

    if usar == 0:
        return

    saldo = SALDO_INICIAL  # Se inicializa el saldo con el saldo inicial.

    nombre_modulo = f"Estrategias.estrategia_0{usar}"
    estrategia = importlib.import_module(nombre_modulo)  # Args: resultado, opciones_true, opciones_false

    Nombre_Archivo = input("Nombre del archivo: ")  # Resultados[75-25](1)
    resultados = leer_bools(f"{Nombre_Archivo}.txt")

    for resultado in resultados:

        ronda = rondas()
        apuesta = estrategia.calcular_apuesta(resultado)
        saldo = obtener_saldo(saldo, apuesta, MULTIPLICADOR, resultado)

        imprimir(SALDO_INICIAL, ronda, saldo, OPCIONES_TRUE, OPCIONES_FALSE, apuesta, resultado)

        if saldo < 5:
            break

generar_prueba_texto(0)  # Pruebas en caso de usar el módulo 'LecturaTXT_Bools'