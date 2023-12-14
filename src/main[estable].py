########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

"""
    El creador de este código no se hace responsable del uso indebido que la persona pueda hacer con él.

    Este programa es para uso personal y está TOTALMENTE PROHIBIDO el uso de este código para obtener beneficios a
    costa de vendérselo a otras personas.

    IMPORTANTE [LEER ANTES DE MANIPULAR EL CÓDIGO]

    Su código estará ÚNICAMENTE alojado en la cuenta de su desarrollador:

        · https://github.com/NominoDLord/Generador-de-Apuestas

    Este programa está diseñado en base a una determinada plataforma de apuestas (no voy a decir cuál porque no es
    mi intención promocionar ninguna plataforma en concreto) y a una determinada resolución de pantalla, por lo que,
    se deberan ajustar algunas variables para poder ejecutar correctamente el código.

    Antes de empezar a ejecutar el código, es importante entender primero cómo funcina y realizar una serie de pruebas
    antes de implementarlo en alguna plataforma real.

    Los principales parámetros que se deben ajustar son los siguientes:

        - Argumentos para el módulo de capturar_pantalla:

            · Esto dependerá principalmente de la resolución en la que se esté ejecutando el código.
            · Crear una carpeta donde guardar las imagenes y poder realizar la comparación.
            · En RUTA_SAVE: Ajustar la ruta de la carpeta donde se guardará la imágen capturada.
                (Cada vez se guarda una nueva captura se eleminará la primera captura)

        -  Argumentos para el módulo de comparar_imagenes:

            · Ajustar la ruta para la comparación de las dos capturas.
                + RUTA_IMG_REFERENCIA: Esta imágen será siempre la misma.
                + RUTA_IMG_CAPTURA: Esta imágen se irá actualizando en cada ronda.

        - Argumentos para las pulsaciones del ratón:

            · Es MUY IMPORTANTE que cuando se ejecute el código no se utilice el PC ya que, de lo contrario,
              las pulsaciones y las capturas de pantalla no se ejecutarán correctamente. Esto incluye que el
              movimiento manual del ratón debe estar desactivado para evitar posibles accidentes en el movimiento
              porque podría perjudicar a la selección de las opciones.

        - Bibliotecas y Módulos:

            · Se deben instalar las bibliotecas adecuadas para poder realizar las importaciones correctamente:

                + Ejecutar en CMD los siguientes comandos...

                    >>> pip3 install Pillow
                    >>> pip3 install pyautogui

            · Los Módulos deberán estar en la misma carpeta que el archivo principal 'main.py'.

        - Ajustar los parámentros del juego:

            El programa está diseñado para los juegos en el que las opciones de acertar & fallar son entre 1 y 5.
            Si se quiere ajustar para juegos con un mayor número de opciones, se deberán modificar los siguientes
            elementos de la función "calcular_apuesta" de este mismo archivo:

                + [ OPCIONES_ACIERTOS / 'Numero' ] → Reducir las opciones a un valor inferior a 5
                + [ OPCIONES_FALLOS / 'Numero' ] → Reducir las opciones a un valor inferior a 5

                    EJEMPLO: Si las opciones de aciertos y fallos son de 16 y 17 (como es el caso del juego
                             de la ruleta), el número divisor debería ser un 3 o 4.
                             (realizar simuladiones para probar antes los resultados).

                    NOTA: Para opciones inferiores a 5, podemos aumentar las apuestas multiplicando (en la función
                          'calcular_apuesta') el 'Numero'. Esto hará que los beneficios sean mucho más altos en
                          un menor número de rondas, pero también aumentará el riesgo de perdidas (sobretodo si se
                          inicia con un saldo bajo). Por lo que, es importante realizar pruebas antes de empezar a
                          ejecutar la estratégia.


Dentro del repositorio se encuentra un archivo llamado 'obtener_coordenadas_cursor.pyw' con el que se pueden obtener
las coordenadas de la posición del cursor para ayudar a generar los valores de las variables.
    https://github.com/NominoDLord/Generador-de-Apuestas/tree/main/src/utils
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

from typing import List
from time import sleep
from pyautogui import press as pulsar
from datetime import datetime

from moduls.ContarRondas import rondas

from moduls.mMouse import definir_posicion_cursor  # (pos_x: int, pos_y: int)
from moduls.mMouse import pulsar_boton_izquierdo  # (pulsar=1)

from moduls.capturar_pantalla import captura  # (nombre, ruta, pos_x=0, pos_y=0, ancho=1920, alto=1080)
from moduls.comparar_imagenes import comparar  # (ruta_img_referencia, ruta_img_capturada, umbral=0.9)

# ================================================== [ VARIABLES ] =================================================== #

nombre_usuario = "Ferran"
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


# ================================================ CLASES & FUNCIONES ================================================ #

def guardar_resultados(rondas, resultados):
    """
    Se guardan los resultados en dos archivos de texto:
        archivo1 → Ronda + Resultado
        archivo2 → Ronda + Saldo + Apuesta + Resultado + Proporción
    """
    with open(RUTA_RESULTADOS1, "a") as archivo1:
        archivo1.write(f"Ronda Nº{str(rondas)}: " + str(resultados) + "\n")

# =================================================== [ EJECUCIÓN ] ================================================== #
sleep(4)

while True:  # SE INICIA LA SECUENCIA DE APUESTAS

    ronda = rondas()

    definir_posicion_cursor(1150, 850)  # Posición → PLAY
    sleep(1)
    pulsar_boton_izquierdo()  # Pulsar → PLAY
    sleep(1)
    definir_posicion_cursor(1575, 820)  # Posición → Opción
    sleep(1)
    pulsar_boton_izquierdo()  # Pulsar → Opción
    sleep(3)  # Esperar resultado
    captura(NOMBRE, RUTA_SAVE, POS_X, POS_Y, ANCHO, ALTO)  # Capturar → Resultado
    sleep(1)
    resultado_ronda = not comparar(RUTA_IMG_REFERENCIA, RUTA_IMG_CAPTURA)  # Analizar → Resultado

    if resultado_ronda is True:
        definir_posicion_cursor(1150, 850)  # Posición → Recibir Premio
        pulsar_boton_izquierdo()  # Pulsar → Recibir premio
        sleep(1)
        pulsar_boton_izquierdo()  # Pulsar → Continuar
        sleep(1)

    if resultado_ronda is False:
        definir_posicion_cursor(1150, 850)  # Posición → Continuar
        sleep(1)
        pulsar_boton_izquierdo()  # Pulsar → Continuar
        sleep(1)

    guardar_resultados(ronda, resultado_ronda)  # Guarda los resultados en archivos de texto.
    sleep(1)
