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

import sys
import os
subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(subDir1)
from config.configuracion import *

# -------------------------------------------------------------------------------------------------------------------- #

from typing import List
from time import sleep
from random import choice as elegir
from pyautogui import press as pulsar
from datetime import datetime

from moduls.mMouse import definir_posicion_cursor  # (pos_x: int, pos_y: int)
from moduls.mMouse import pulsar_boton_izquierdo  # (pulsar=1)

from moduls.capturar_pantalla import captura  # (nombre, ruta, pos_x=0, pos_y=0, ancho=1920, alto=1080)
from moduls.comparar_imagenes import comparar  # (ruta_img_referencia, ruta_img_capturada, umbral=0.9)

# ================================================== [ VARIABLES ] =================================================== #

global saldo  # Este será el saldo que se irá actualizando en cada ronda.
global saldos
global saldo_final
global lista_resultados
global proporcion_trues
global proporcion_falses

INDEX = 0
RONDA = 0
INCREMENTO = 0.5
V_MIN = 0.30
V_MAX = 99.00
LIMITE_RIESGO = 0.005
SALDO_INICIAL = 250
OPCIONES_ACIERTOS = 3
OPCIONES_FALLOS = 1
OPCIONES_TOTALES = OPCIONES_ACIERTOS + OPCIONES_FALLOS
# MULTIPLICADOR = OPCIONES_FALLOS / OPCIONES_ACIERTOS
PROBABILIDAD = (OPCIONES_ACIERTOS / OPCIONES_TOTALES) * 100
MULTIPLICADOR = 1.32

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

def contar_rondas() -> int:
    global RONDA
    RONDA += 1
    return RONDA

def generar_indice(opcion) -> int:
    global INDEX
    INDEX = INDEX + 1 if opcion is False else 0
    return INDEX

def generar_listas_100() -> tuple[list[bool], list[bool]]:
    trues = [True] * int(OPCIONES_ACIERTOS / OPCIONES_TOTALES)
    falses = [False] * int(OPCIONES_FALLOS / OPCIONES_TOTALES)
    return trues, falses

def generar_lista(resultado) -> List[bool]:
    global lista_resultados
    # Crear lista -------------------------------------------------------------------------------------------------
    if not hasattr(generar_lista, "lista_creada"):
        # Este bloque impedirá que la lista se vacie al volver a llamar a la función.
        lista_resultados = []
    generar_lista.lista_creada = True
    # -------------------------------------------------------------------------------------------------------------
    lista_resultados.append(resultado)
    return lista_resultados


def guardar_resultados(resultado):
    """
    Se guardan los resultados en dos archivos de texto:
        archivo1 → Ronda + Resultado
        archivo2 → Ronda + Saldo + Apuesta + Resultado + Proporción
    """
    with open(RUTA_RESULTADOS1, "a") as archivo1:
        archivo1.write(f"Ronda Nº{str(rondas)}: " + str(resultado) + "\n")
    with open(RUTA_RESULTADOS2, "a") as archivo2:
        archivo2.write(f"RONDA: {str(rondas)}" + "\n")
        archivo2.write(f"SALDO: {str(saldo)}" + "\n")
        archivo2.write(f"APUESTA: {str(cantidad_apostada)}" + "\n")
        archivo2.write(f"RESULTADO: {str(resultado_ronda)}" + "\n")
        # archivo2.write(f"PROPORCIÓN [T|F]: {str(proporcion_trues)} | {str(proporcion_falses)}" + "\n")
        archivo2.write(f"BENEFICIO: {str(round((saldo - SALDO_INICIAL), 2))}" + "\n")
        archivo2.write("--------------------------------------------------" + "\n")


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
        saldo_actual = round(saldos, 2)
        return saldo_actual

    elif resultado is False:
        saldos -= apuesta
        saldo_actual = round(saldos, 2)
        return saldo_actual




def calcular_apuesta(resultado, opciones_true, opciones_false):
    # -------------------------------------------------------------------------------------------------------------
    # Inicializar proporcion_true y proporcion_false si no existen
    if not hasattr(calcular_apuesta, "proporcion_true"):
        calcular_apuesta.proporcion_true = 0
    if not hasattr(calcular_apuesta, "proporcion_false"):
        calcular_apuesta.proporcion_false = 0
    # -------------------------------------------------------------------------------------------------------------
    total_opciones = opciones_true + opciones_false

    def proporcion():

        if resultado is True:
            calcular_apuesta.proporcion_true += opciones_false

        elif resultado is False:
            calcular_apuesta.proporcion_false += opciones_true

    proporcion()
    num = 1

    if calcular_apuesta.proporcion_true > calcular_apuesta.proporcion_false:
        apuesta = opciones_false * num

    elif calcular_apuesta.proporcion_true < calcular_apuesta.proporcion_false:
        apuesta = opciones_true * num

    else:
        apuesta = total_opciones / 2

    return apuesta

# =================================================== [ EJECUCIÓN ] ================================================== #
sleep(6)

lista_variable_trues, lista_variable2_falses = generar_listas_100()

# SE INICIA LA PRIMERA APUESTA ------------------------------------------------------------------------------------
cantidad_apostada = (OPCIONES_TOTALES / 2) * INCREMENTO
definir_posicion_cursor(795, 975)  # El cursor se posiciona en el valor de la apuesta.
pulsar_boton_izquierdo(2)  # Se selecciona el valor de la apuesta existente.

for digito in str(cantidad_apostada):  # Convierte la apuesta en una cadena de texto para poder introducirla.
    # Introduce la apuesta reemplazando la apuesta anterior.
    pulsar(digito)
    sleep(0.5)
# -----------------------------------------------------------------------------------------------------------------

while True:  # SE INICIA LA SECUENCIA DE APUESTAS

    rondas = contar_rondas()

    definir_posicion_cursor(1150, 850)  # El cursor se posiciona encima del botón de "Apostar".
    sleep(1)
    pulsar_boton_izquierdo()  # Pulsar el Botón "Jugar" para aceptar la ronda y la cantidad a apostar.
    sleep(1)
    definir_posicion_cursor(1575, 820)  # El cursor se posiciona encima del botón de la opción a apostar.
    """
    NOTA: La posición de la opción a apostar siempre debe ser la misma. De no ser así, implicaría una variable
          extra de aleatoriedad por nuestra parte con lo que generaría una probabilidad de acierto menor.
    """
    sleep(1)
    pulsar_boton_izquierdo()
    sleep(3)  # Espera a que se genere un resultado.
    captura(NOMBRE, RUTA_SAVE, POS_X, POS_Y, ANCHO, ALTO)  # Captura de la sección en la que se muestra el resultado.
    sleep(1)
    """ ¡IMPORTANTE!
    Antes de iniciar el programa, debemos de generar una captura de la región con un resultado fallido. """
    resultado_ronda = not comparar(RUTA_IMG_REFERENCIA, RUTA_IMG_CAPTURA)  # Se determinar si se ha acertado o fallado.
    """ NOTA:
    El motivo de usar 'not' antes de la función es debido a que la imagen que debemos insertar como referencia debe
    ser la de "Has perdido". Esto se hace así porque la imagen generada al ganar nos muestra el mensaje "Has ganado"
    con el valor del beneficio obtenido y como el beneficio obtenido dependerá del valor de la apuesta y el valor de
    la apuesta dependerá de los anteriores resultados, la imagen resultante variará y como consecuencia, no podemos
    definirla como la imagen de referencia a comparar. """

    if resultado_ronda is True:
        definir_posicion_cursor(1150, 850)  # El cursor se posiciona encima del botón de "Recibir Ganancias".
        sleep(1)
        pulsar_boton_izquierdo()  # Pulsa el botón para recibir las ganancias.
        sleep(1)
        pulsar_boton_izquierdo()  # Pulsa el botón para "Continuar" a la próxima ronda.
        sleep(1)

    if resultado_ronda is False:
        definir_posicion_cursor(1150, 850)  # El cursor se posiciona encima del botón de "Continuar".
        sleep(1)
        pulsar_boton_izquierdo()  # Pulsa el botón para "Continuar" a la próxima ronda.

    lista_definida = generar_lista(resultado_ronda)  # Se guardan los resultados en la variable lista.
    sleep(1)
    # Calcula el valor de la siguiente apuesta.
    cantidad_apostada = calcular_apuesta(resultado_ronda, OPCIONES_ACIERTOS, OPCIONES_FALLOS)
    sleep(1)
    saldo = actualizar_saldo(cantidad_apostada, resultado_ronda)  # Calcula el saldo después de definir la apuesta.
    sleep(1)
    guardar_resultados(resultado_ronda)  # Guarda los resultados en archivos de texto.
    sleep(1)

    print(f"RONDA: {str(rondas)}")
    print(f"SALDO: {str(saldo)}")
    print(f"APUESTA: {str(cantidad_apostada)}")
    print(f"RESULTADO: {str(resultado_ronda)}")
    # 0print(f"PROPORCIÓN [T|F]: {str(proporcion_trues)} | {str(proporcion_falses)}")
    print(f"BENEFICIO: {str(round((saldo - SALDO_INICIAL), 2))}")
    print("--------------------------------------------------")

    definir_posicion_cursor(795, 975)  # El cursor se posiciona en el valor de la apuesta.
    sleep(1)
    pulsar_boton_izquierdo(2)  # Se selecciona el valor de la apuesta existente para reemplazarlo por la nueva.
    sleep(1)
    apostar_txt = str(cantidad_apostada)  # Convierte la apuesta en una cadena de texto para poder introducirla.
    sleep(1)

    for digito in apostar_txt:
        # Introduce la cantidad de la nueva apuesta.
        pulsar(digito)
        sleep(0.5)

    if saldo < 150 or rondas == 10000 or (saldo - SALDO_INICIAL) > 2000:
        break
