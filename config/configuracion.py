########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" CONFIGURACIÓN: Global Values """

# ==============================================    IMPORTAR MÓDULOS    ============================================== #

from typing import List, Tuple
from time import sleep
from random import choice
from pyautogui import press
from datetime import datetime

# ===================================================  FUNCIONES  ==================================================== #

def generar_porcentajes_y_posiciones(porcentaje, probabilidad):
    lista_porcentajes, lista_posiciones = [], []
    porcentajes = porcentaje

    while porcentajes > (1/1000):
        lista_porcentajes.append(round(porcentajes, 3))
        porcentajes *= probabilidad

    for _ in lista_porcentajes:
        lista_posiciones.append(0)

    return lista_porcentajes, lista_posiciones

# =================================================  VALORES  FIJOS  ================================================= #

SALDO_INICIAL = 1000

APUESTA_MINIMA = 0.30  # 0.30
APUESTA_MAXIMA = 100.00  # 100.00
MULTIPLICADOR = 1.32  # 1.32

OPCIONES_TRUE = 3  # 3
OPCIONES_FALSE = 1  # 1

# ···············································  VALORES  GENERADOS  ··············································· #

OPCIONES_TOTALES = int(OPCIONES_TRUE + OPCIONES_FALSE)  # 4

PROBABILIDAD_TRUE = round((OPCIONES_TRUE / OPCIONES_TOTALES), 2)  # 0.75
PROBABILIDAD_FALSE = round((OPCIONES_FALSE / OPCIONES_TOTALES), 2)  # 0.25

PORCENTAJE_TRUE = int((OPCIONES_TRUE / OPCIONES_TOTALES) * 100)  # 75
PORCENTAJE_FALSE = int((OPCIONES_FALSE / OPCIONES_TOTALES) * 100)  # 25

PROPORCION = round((OPCIONES_TRUE / OPCIONES_FALSE), 2)  # 3

LISTA_RESULTADOS = []

LISTA_TRUE = [True] * OPCIONES_TRUE  # [True, True, True]
LISTA_FALSE = [False] * OPCIONES_FALSE  # [False]
LISTA_OPCIONES = LISTA_TRUE + LISTA_FALSE  # [True, True, True, False]

LISTA_TRUES = [True] * int(PORCENTAJE_TRUE)  # [True, True, True, True, True, True, True, True, True, ..., True]
LISTA_FALSES = [False] * int(PORCENTAJE_FALSE)  # [False, False, False, ..., False]


LISTA_PORCENTAJES_TRUE, LISTA_POSICIONES_TRUE = generar_porcentajes_y_posiciones(PORCENTAJE_TRUE, PROBABILIDAD_TRUE)
# print(LISTA_PORCENTAJES_TRUE)  # [75, 56.25, 42.188, 31.641, 23.73, (...), 0.002, 0.002, 0.001, 0.001]
# print(LISTA_POSICIONES_TRUE)  # [0, 0, 0, 0, 0, (...), 0, 0, 0, 0]

LISTA_PORCENTAJES_FALSE, LISTA_POSICIONES_FALSE = generar_porcentajes_y_posiciones(PORCENTAJE_FALSE, PROBABILIDAD_FALSE)
# print(LISTA_PORCENTAJES_FALSE)  # [25, 6.25, 1.562, 0.391, 0.098, 0.024, 0.006, 0.002]
# print(LISTA_POSICIONES_FALSE)  # [0, 0, 0, 0, 0, 0, 0, 0]



# ==============================================  PARÁMETROS  PRIVADOS  ============================================== #

USER = "Ferran"

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime('%Y-%m-%d')

# Parámetros para los argumentos del módulo 'capturar_pantalla'.
NOMBRE_CAPTURA = "captura"
RUTA_SAVE = f"C:/Users/{USER}/Pictures/SCREENS/"
POS_X, POS_Y, ANCHO, ALTO = 600, 300, 1080, 600

# Parámetros para los argumentos del módulo 'comparar_imagenes'.
RUTA_IMG_REFERENCIA = f"C:/Users/{USER}/Pictures/SCREENS/referencia.png"
RUTA_IMG_CAPTURA = f"C:/Users/{USER}/Pictures/SCREENS/captura.png"
RUTA_RESULTADOS1 = f"C:/Users/{USER}/Documents/Apuestas/Resultados [{fecha_formateada}].txt"
RUTA_RESULTADOS2 = f"C:/Users/{USER}/Documents/Apuestas/Registros [{fecha_formateada}].txt"

#
