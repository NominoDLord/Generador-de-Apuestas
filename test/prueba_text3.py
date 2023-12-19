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

""" PRINCIPAL: pruebas

    Código para ejecutar las estratégias definidas en:

        .../Estrategias/estrategia_0.py

    Para poder ejecutar las estratégias, necesitaremos generar los siguientes resultados:

        > True      (Para los aciertos)
        > False     (Para los fallos)

    Para generar los resultados, tenemos dos opciones:

        · Opción 1: Registros de texto.

            En la carpeta `Registros` se dispone de una variedad de resultados guardados en archivos de texto [.txt].
            Estos resultados han sido generados interactuando dentro de una plataforma (real) de apuestas.

            Para usarlos, tendremos que utilizar el módulo `LecturaTXT_Bools.py` para leer el archivo y guardar
            los resultados en una lista.

            Una vez creada la lista con los resultados guardados, podemos iterar los datos para realizar las pruebas.

        · Opción 2: Generar los resultados con el módulo Random.

            Se dispone del módulo `GenerarBools.py` donde podremos generar los resultados indicando como argumentos
            el número de opciones que hay de acertar y fallar.

            Usando este módulo junto con un bucle (while), podemos generar tantos resultados aleatorios como queramos.
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(subDir1)
from config.configuracion import *

import importlib
from random import choice as aleatorio

from ContarRondas import rondas
# from ContarRepeticiones import contar
from GenerarProporcion import proporcion
from ImprimirDatos import imprimir
from ActualizarSaldo import obtener_saldo
from Saldos import saldos_limite

from LecturaTXT_Bools import leer_bools  # Arg: Nombre_Archivo (El archivo debe estar dentro de la carpeta `Registros`)
from GenerarBools import generar_lista  # Args: trues, falses

# ================================================== [ VARIABLES ] =================================================== #

global saldo, premio, saldo_max, saldo_min, saldo_actual
apuesta_max = 0
total_apostado = 0
lista_apuestas = []
# ================================================== [ FUNCIONES ] =================================================== #

def apuesta_maxima(apuestas):
    global apuesta_max
    if apuesta_max < apuestas:
        apuesta_max = apuestas
    return apuesta_max

def saldo_maximo(saldos):
    global saldo_max
    if saldo_max < saldos:
        saldo_max = saldos
    return saldo_max

def saldo_minimo(saldos):
    global saldo_min
    if saldo_min > saldos:
        saldo_min = saldos
    return saldo_min

def total_apuestas(apuestas):
    global total_apostado
    total_apostado += apuestas
    return total_apostado

# ================================================== [ EJECUCIÓN ] =================================================== #

def generar_prueba_texto(usar: int = 0):
    global saldo, premio, apuesta_max, saldo_max, saldo_min, saldo_actual
    """
    Para 'usar' correctamente la función, se deberá establecer el número que corresponde al módulo que se quiere usar.

    @param usar: Esta variable define el módulo de la estrategia a importar.
    @return: En caso de que `usar` sea 0, la función no será usada.
    """

    if usar == 0:
        return

    nombre_modulo = f"Estrategias.estrategia_{usar}"
    estrategia = importlib.import_module(nombre_modulo)  # Args: resultado, opciones_true, opciones_false

    Nombre_Archivo = input("Nombre del archivo: ")  # Resultados[75-25](1); Total[75-25]
    resultados = leer_bools(f"{Nombre_Archivo}.txt")  # Se crea una lista con los resultados obtenidos del archivo.
    total_rondas = len(resultados)

    ronda = rondas()  # Se inicia la secuencia de rondas.
    resultado = None  # Se establece "None" como valor porque aún no hay ningún resultado generado.

    apuesta_anterior = 0  # Como no hay apuesta anterior, el valor es 0.
    lista_apuestas.append(apuesta_anterior)  # Se añade la apuesta a la lista.
    saldo_actual = SALDO_INICIAL

    apuesta = estrategia.calcular_apuesta(saldo_actual, resultado, apuesta_anterior)  # Se genera la primera apuesta.
    saldo_actual = SALDO_INICIAL - apuesta

    for resultado in resultados:

        lista_apuestas.append(apuesta)  # Se añade la nueva apuesta generada...
        del lista_apuestas[0]  # y se elimina la apuesta anterior.

        premio = apuesta * MULTIPLICADOR if resultado is True else 0

        saldo_actual += premio
        saldo_actual = round(saldo_actual, 2)

        imprimir(ronda, saldo_actual, apuesta, resultado)

        saldo_max, saldo_min = saldos_limite(saldo_actual)
        apuesta_max = apuesta_maxima(apuesta)

    # Final de rondas · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

        ronda = rondas()  # Cada vez que es llamada la función, la variable suma +1 a su valor.

        if (total_rondas == (ronda + 1)) or (saldo_actual < 5):
            break

        apuesta_anterior = lista_apuestas[0]
        apuesta = estrategia.calcular_apuesta(saldo_actual, resultado, apuesta_anterior)
        saldo_actual -= apuesta

    print("==================================================")
    print(f"SALDO [Max|Min]: {saldo_max} | {saldo_min}")
    print(f"APUESTA MÁXIMA: {apuesta_max}")
    print("==================================================")

generar_prueba_texto(10)  # Resultados[75-25](1); Total[75-25]

#
