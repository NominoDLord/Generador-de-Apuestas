########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" CONFIGURACIÓN: Parámetros fijos """

# ==============================================    IMPORTAR MÓDULOS    ============================================== #

from typing import List
from time import sleep
from random import choice
from pyautogui import press
from datetime import datetime

# =================================================  VALORES  FIJOS  ================================================= #

SALDO_INICIAL = 500

APUESTA_MINIMA = 0.30
APUESTA_MAXIMA = 99.00
MULTIPLICADOR = 1.32

OPCIONES_TRUE = 3
OPCIONES_FALSE = 1

# ···············································  VALORES  GENERADOS  ··············································· #

OPCIONES_TOTALES = OPCIONES_TRUE + OPCIONES_FALSE

PROBABILIDAD_TRUE = OPCIONES_TRUE / OPCIONES_TOTALES
PROBABILIDAD_FALSE = OPCIONES_FALSE / OPCIONES_TOTALES

PORCENTAJE_TRUE = (OPCIONES_TRUE / OPCIONES_TOTALES) * 100
PORCENTAJE_FALSE = (OPCIONES_FALSE / OPCIONES_TOTALES) * 100

PROPORCION = OPCIONES_TRUE / OPCIONES_FALSE

LISTA_RESULTADOS = []

LISTA_TRUE = [True] * OPCIONES_TRUE
LISTA_FALSE = [False] * OPCIONES_FALSE
LISTA_OPCIONES = LISTA_TRUE + LISTA_FALSE

LISTA_TRUES = [True] * int(PORCENTAJE_TRUE)
LISTA_FALSES = [False] * int(PORCENTAJE_FALSE)

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
