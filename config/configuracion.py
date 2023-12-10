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

""" CONFIGURACIÓN: Parámetros fijos."""

# ==============================================    IMPORTAR MÓDULOS    ============================================== #

from typing import List
from time import sleep
from random import choice as elegir
from pyautogui import press as pulsar
from datetime import datetime


# ==============================================  PARÁMETROS  GLOBALES  ============================================== #

SALDO_INICIAL = 300

APUESTA_MINIMA = 0.30
APUESTA_MAXIMA = 99.00
MULTIPLICADOR = 1.32

OPCIONES_TRUE = 3
OPCIONES_FALSE = 1

OPCIONES_TOTALES = OPCIONES_TRUE + OPCIONES_FALSE

PROBABILIDAD_TRUE = OPCIONES_TRUE / OPCIONES_TOTALES
PROBABILIDAD_FALSE = OPCIONES_FALSE / OPCIONES_TOTALES

PORCENTAJE_TRUE = (OPCIONES_TRUE / OPCIONES_TOTALES) * 100
PORCENTAJE_FALSE = (OPCIONES_FALSE / OPCIONES_TOTALES) * 100

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
