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

        .../Estrategias/estrategia_00.py

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

global saldo, saldo_max, saldo_min
total_apostado = 0

# ================================================== [ FUNCIONES ] =================================================== #

apuesta_maxima = 0

def apuesta_max(apuestas):
    global apuesta_maxima
    if apuesta_maxima < apuestas:
        apuesta_maxima = apuestas
    return apuesta_maxima

# ================================================== [ EJECUCIÓN ] =================================================== #

def generar_prueba_texto(usar: int = 0):
    global saldo, saldo_max, saldo_min
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

    ronda = rondas()  # Se inicia la secuencia de rondas
    resultado = None  # Se establece "None" como valor porque aún no hay ningún resultado generado.
    apuesta = estrategia.calcular_apuesta(resultado)
    saldo_actual = SALDO_INICIAL - apuesta

    for resultado in resultados:

        premio = apuesta * MULTIPLICADOR if resultado is True else 0

        saldo_actual += premio
        saldo_actual = round(saldo_actual, 2)

        imprimir(ronda, saldo_actual, apuesta, resultado)

        saldo_max, saldo_min = saldos_limite(saldo_actual)
        apuesta_max(apuesta)

    # Final de rondas · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

        ronda = rondas()  # Cada vez que es llamada la función, la variable suma +1 a su valor.

        if (total_rondas == (ronda + 1)) or (saldo_actual < 5):
            break

        apuesta = estrategia.calcular_apuesta(resultado)
        saldo_actual -= apuesta

    print(f"SALDO [Max|Min]: {saldo_max} | {saldo_min}")
    print(f"APUESTA MÁXIMA: {apuesta_maxima}")


generar_prueba_texto(9)  # Resultados[75-25](1); Total[75-25]

#
