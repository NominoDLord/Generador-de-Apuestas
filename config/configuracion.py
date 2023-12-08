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

""" CONFIGURACIÓN: En este archivo se configuran los parámetros fijos que usa el programa/módulos."""

# ==============================================    IMPORTAR MÓDULOS    ============================================== #

from typing import List
from time import sleep
from random import choice as elegir
from pyautogui import press as pulsar
from datetime import datetime


# ==============================================  PARÁMETROS  GLOBALES  ============================================== #

SALDO_INICIAL = 300

APUESTA_MIN = 0.30
APUESTA_MAX = 99.00
MULTIPLICADOR = 1.32

OPCIONES_TRUE = 3
OPCIONES_FALSE = 1

OPCIONES_TOTALES = OPCIONES_TRUE + OPCIONES_FALSE

PROBABILIDAD_TRUE = OPCIONES_TRUE / OPCIONES_TOTALES
PROBABILIDAD_FALSE = OPCIONES_FALSE / OPCIONES_TOTALES

PORCENTAJE_TRUE = OPCIONES_TRUE / OPCIONES_TOTALES
PORCENTAJE_FALSE = OPCIONES_FALSE / OPCIONES_TOTALES

# ==============================================  PARÁMETROS  PRIVADOS  ============================================== #

USER = "Ferran"

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime('%Y-%m-%d')

# Parámetros para los argumentos del módulo 'capturar_pantalla'.
NOMBRE = "captura"
RUTA_SAVE = f"C:/Users/{nombre_usuario}/Pictures/SCREENS/"
POS_X, POS_Y = 600, 300
ANCHO, ALTO = 1080, 600

# Parámetros para los argumentos del módulo 'comparar_imagenes'.
RUTA_IMG_REFERENCIA = f"C:/Users/{nombre_usuario}/Pictures/SCREENS/referencia.png"
RUTA_IMG_CAPTURA = f"C:/Users/{nombre_usuario}/Pictures/SCREENS/captura.png"
RUTA_RESULTADOS1 = f"C:/Users/{nombre_usuario}/Documents/Apuestas/Resultados [{fecha_formateada}].txt"
RUTA_RESULTADOS2 = f"C:/Users/{nombre_usuario}/Documents/Apuestas/Registros [{fecha_formateada}].txt"

#
