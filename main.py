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

                    NOTAS: Para opciones inferiores a 5, podemos aumentar las apuestas multiplicando (en la función
                           'calcular_apuesta') el 'Numero'. Esto hará que los beneficios sean mucho más altos en
                           un menor número de rondas, pero también aumentará el riesgo de perdidas (sobretodo si se
                           inicia con un saldo bajo). Por lo que, es importante realizar pruebas antes de empezar a
                           ejecutar la estratégia.

"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

from typing import List
from time import sleep
from random import choice as elegir

from capturar_pantalla import captura  # (nombre, ruta, pos_x=0, pos_y=0, ancho=1920, alto=1080)
from comparar_imagenes import comparar  # (img_referencia, img_capturada, umbral=0.9) -> bool
from click_raton import pulsar_boton_izquierdo


# ================================================== [ VARIABLES ] =================================================== #

global saldo_final
global saldo
global lista_resultados

nombre_usuario = Ferran
# Argumentos para el módulo de capturar_pantalla
NOMBRE = "captura"
RUTA_SAVE = f"C:/Users/{nombre_usuario}/Pictures/SCREENS/"
POS_X, POS_Y = 600, 300
ANCHO, ALTO = 1080, 600

# Argumentos para el módulo de comparar_imagenes
RUTA_IMG_REFERENCIA = f"C:/Users/{nombre_usuario}/Pictures/SCREENS/referencia.png"
RUTA_IMG_CAPTURA = f"C:/Users/{nombre_usuario}/Pictures/SCREENS/captura.png"


INDEX = 0
RONDA = 0
V_MIN = 0.30
V_MAX = 99.00
LIMITE_RIESGO = 0.005
SALDO_INICIAL = 300
OPCIONES_ACIERTOS = 3
OPCIONES_FALLOS = 1
OPCIONES_TOTALES = OPCIONES_ACIERTOS + OPCIONES_FALLOS
MULTIPLICADOR = OPCIONES_FALLOS / OPCIONES_ACIERTOS
PROBABILIDAD = (OPCIONES_ACIERTOS / OPCIONES_TOTALES) * 100

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

def actualizar_saldo(apuesta: float, resultado: bool) -> float:
    """
    @param apuesta: Cantidad apostada.
    @param resultado: bool
        True → Acertar
        False → Fallar
    @return: Saldo final.
    """
    global saldo_final
    # Crear lista inicial -----------------------------------------------------------------------------------------
    if not hasattr(actualizar_saldo, "guardar_saldo_inicial"):
        # Este bloque impedirá que el saldo se regenere al volver a llamar a la función.
        saldo_final = SALDO_INICIAL
    actualizar_saldo.guardar_saldo_inicial = True
    # -------------------------------------------------------------------------------------------------------------

    beneficio = apuesta * MULTIPLICADOR

    if resultado is False:
        saldo_final -= apuesta
        return saldo_final

    elif resultado is True:
        saldo_final += beneficio
        return saldo_final

    pass

def calcular_apuesta(lista, resultado):

    def contar_valores(listas):
        true_count, false_count = 0, 0

        for elemento in listas:
            true_count += elemento.count(True)
            false_count += elemento.count(False)
        return true_count, false_count

    if resultado is True and len(lista_variable_trues) > 0:
        lista_variable_trues.pop()

    if resultado is False and len(lista_variable_falses) > 0:
        lista_variable_falses.pop()


    listas_trues_falses = [lista, lista_variable_trues, lista_variable_falses]
    total_trues, total_falses = contar_valores(listas_trues_falses)

    proporcion_trues = total_trues * OPCIONES_FALLOS
    proporcion_falses = total_falses * OPCIONES_ACIERTOS

    if proporcion_trues > proporcion_falses:
        apostar = OPCIONES_ACIERTOS * 20
        return apostar

    elif proporcion_trues < proporcion_falses:
        apostar = OPCIONES_FALLOS * 3
        return apostar

    else:
        apostar = OPCIONES_TOTALES
        return apostar

    pass



# ==================================================== [ PRUEBAS ] =================================================== #

def generar_probabilidades() -> List[float]:
    lista = []
    lista_probabilidades = []

    probabilidad_fallar = (OPCIONES_FALLOS / OPCIONES_TOTALES) * 100

    while LIMITE_RIESGO < probabilidad_fallar:
        lista_probabilidades.append(round(probabilidad_fallar, 3))
        probabilidad_fallar *= (OPCIONES_FALLOS / OPCIONES_TOTALES)

    for elemento in lista_probabilidades:
        resultado = 100 - elemento
        lista.append(resultado)

    return lista

probabilidad_ronda = generar_probabilidades()

def generar_resultado(trues: int, falses: int) -> bool:
    # Función para la generación de pruebas.
    """
    Simulación de un resultado random en base a las probabilidades de acertar y fallar.
    @param trues: Indica el número de opciones posibles de acertar.
    @param falses: Indica el número de opciones posibles de fallar.
    @return:
        True → Acertar
        False → Fallar
    """
    lista_trues = [True] * trues
    lista_falses = [False] * falses
    lista_opciones = lista_trues + lista_falses
    resultado = elegir(lista_opciones)
    return resultado

# =================================================== [ EJECUCIÓN ] ================================================== #

lista_variable_trues, lista_variable_falses = generar_listas_100()

# sleep(seg)
"""
    ¡¡¡MUY IMPORTANTE!!!

    Ajustar MUY cuidadosamente los elementos dentro del bucle 'while' antes de ejecutar el código.
    
    Los datos de las posiciones al realizar las capturas de pantalla y las pulsaciones del ratón dependerán
    de la resolución de pantalla en la que es ejecutada, por lo que, es de vital importancia realizar antes
    las pruebas necesarias para ajustar estos parámetros.
    
"""

while True:

    rondas = contar_rondas()

    captura(NOMBRE, RUTA_SAVE, POS_X, POS_Y, ANCHO, ALTO)
    resultado_ronda = not comparar(RUTA_IMG_REFERENCIA, RUTA_IMG_CAPTURA)
    """
    NOTA:
    La imagen de referencia es una captura inicial cuando NO has acertado, por ese motivo,
    se añade 'not' en la salida del resultado para la función 'comparar' del módulo 'comprar_imagenes'.
    """
    # resultado_ronda = generar_resultado(OPCIONES_ACIERTOS, OPCIONES_FALLOS)  # PRUEBAS

    lista_definida = generar_lista(resultado_ronda)

    # indice = generar_indice(resultado_ronda)

    cantidad_apostada = calcular_apuesta(lista_definida, resultado_ronda)
    saldo = actualizar_saldo(cantidad_apostada, resultado_ronda)

    print(f"RONDA: {rondas}")
    print(f"APUESTA → {cantidad_apostada}")
    print(f"RESULTADO → {resultado_ronda}")
    print(f"SALDO → {saldo}")
    print("--------------------------")

    if saldo < 100 or rondas == 10000 or (saldo - SALDO_INICIAL) > 1000:
        break


print(f"Beneficios → {saldo - SALDO_INICIAL}")
