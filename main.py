########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

from random import choice as elegir
from typing import List

# ================================================== [ VARIABLES ] =================================================== #

global saldo_final
global saldo
global lista_resultados

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
    @param resultado:
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
        apostar = OPCIONES_ACIERTOS
        return apostar

    if proporcion_trues < proporcion_falses:
        apostar = OPCIONES_FALLOS
        return apostar

    if proporcion_trues == proporcion_falses:
        apostar = OPCIONES_TOTALES / 2
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

repetir = 1000  # TODO: PRUEBAS
while True:

    # repetir -= 1
    rondas = contar_rondas()
    # resultado_ronda = input("INSERTAR EL RESULTADO EN RONDA: ")
    resultado_ronda = generar_resultado(OPCIONES_ACIERTOS, OPCIONES_FALLOS)  # TODO: PRUEBAS

    lista_definida = generar_lista(resultado_ronda)

    # indice = generar_indice(resultado_ronda)

    cantidad_apostada = calcular_apuesta(lista_definida, resultado_ronda)  # resultado_ronda (Segundo arg en Prueba 1)
    saldo = actualizar_saldo(cantidad_apostada, resultado_ronda)

    print(f"RONDA: {rondas}")
    print(f"APUESTA → {cantidad_apostada}")
    print(f"RESULTADO → {resultado_ronda}")
    print(f"SALDO → {saldo}")
    print("--------------------------")

    if saldo < 1:
        break

    if (saldo - SALDO_INICIAL) > 10000:
        break

print(f"Beneficios → {saldo - SALDO_INICIAL}")