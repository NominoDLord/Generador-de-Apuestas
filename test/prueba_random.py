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

from GenerarBools import generar_lista  # Args: trues, falses
from LecturaTXT_Bools import leer_bools  # Arg: Nombre_Archivo
# El archivo debe estar dentro de la carpeta 'Registros'

# ================================================== [ VARIABLES ] =================================================== #

global saldo, premio, apuesta_max, saldo_max, saldo_min, saldo_actual
total_apostado = 0

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

def generar_prueba_random(usar: int = 0, max_rondas: int = 0):
    global saldo, premio, apuesta_max, saldo_max, saldo_min, saldo_actual

    """
    El argumento 'usar' indica el tipo de "módulo/estratégia" que será será usado.
    Este módulo estará contenido en el directorio "Estrategias".

    @param usar: Esta variable define el módulo de la estrategia a importar.
    @return: En caso de que `usar` sea 0, la función no será usada.
    """

    if usar == 0:
        return

    nombre_modulo = f"Estrategias.estrategia_0{usar}"
    estrategia = importlib.import_module(nombre_modulo)

    print("====================================")
    ronda = rondas()  # 1ª Ronda
    print(f"Ronda Nº {ronda}")
    saldo_min = SALDO_INICIAL  # Se traza el Saldo Inicial como valor incial
    saldo_max = SALDO_INICIAL  # Se traza el Saldo Inicial como valor incial
    print(f"Saldo inicial: {SALDO_INICIAL}")
    apuesta = APUESTA_MINIMA
    apuesta_max = APUESTA_MINIMA
    total_apuestas(apuesta)
    print(f"Cantidad a apostar: {apuesta}")
    saldo_actual = SALDO_INICIAL - apuesta
    saldo_actual = round(saldo_actual, 2)
    print(f"Saldo actual: {saldo_actual}")
    resultado = aleatorio(LISTA_OPCIONES)
    print(f"Resultado: {resultado}")
    if resultado is False:
        premio = -apuesta
        print(f"Premio: {premio}")
    elif resultado is True:
        premio = apuesta * MULTIPLICADOR
        round(premio, 2)
        print(f"Premio: {premio}")
    saldo_actual += premio
    saldo_actual = round(saldo_actual, 2)
    saldo_minimo(saldo_actual)
    print(f"Saldo actualizado: {saldo_actual}")
    print("------------------------------")  # Fin de la 1ª Ronda.

    while ronda <= max_rondas:

        ronda = rondas()
        print(f"Ronda Nº {ronda}")
        print(f"Saldo: {saldo_actual}")

        # Se introduce el resultado de la apuesta anterior para generar una nueva apuesta.
        apuesta = estrategia.calcular_apuesta(resultado)
        if apuesta > saldo_actual:
            break
        apuesta_max = apuesta_maxima(apuesta)
        total_apuestas(apuesta)
        print(f"Cantidad a apostar: {apuesta}")

        saldo_actual -= apuesta
        saldo_actual = round(saldo_actual, 2)
        saldo_maximo(saldo_actual)
        saldo_minimo(saldo_actual)
        print(f"Saldo actual: {saldo_actual}")

        # Se genera un nuevo resultado para la apuesta actual.
        resultado = aleatorio(LISTA_OPCIONES)
        print(f"Resultado: {resultado}")

        if resultado is False:
            premio = -apuesta
            premio = round(premio, 2)
            print(f"Premio: {premio}")
        elif resultado is True:
            premio = apuesta * MULTIPLICADOR
            premio = round(premio, 2)
            print(f"Premio: {premio}")

        saldo_actual += premio
        saldo_actual = round(saldo_actual, 2)
        saldo_maximo(saldo_actual)
        saldo_minimo(saldo_actual)

        print(f"Saldo actualizado: {saldo_actual}")
        print("------------------------------")

    # Final de rondas · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

        if (max_rondas == (ronda + 1)) or (saldo_actual < 5):
            break

generar_prueba_random(8, 10000)

beneficios = saldo_actual - SALDO_INICIAL

print("=============================================")
print("RESULTADO FINAL")
print("···············")
print(f"Apuesta Máxima: {apuesta_max}"
      f"\nSaldo Máximo: {saldo_max}"
      f"\nSaldo Mínimo: {saldo_min}"
      f"\nBeneficio: {beneficios}"
      f"\nTotal Apostado: {round(total_apostado, 2)}")

devolucion = round((total_apostado * 0.05), 2)
print(f"Devolución: {devolucion}")

#
