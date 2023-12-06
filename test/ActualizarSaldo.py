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

""" ContarRondas

    MÓDULO: Realiza la cuenta del número de rondas generadas.

"""
global saldo_inicial

def introducir_saldo_inicial(saldo_introducio):
    global saldo_inicial
    saldo_inicial = saldo_introducio

def obtener_saldo(saldos: float, apuesta: float, multiplicador: float, resultado: bool) -> float:
    """
    @param saldos: Saldo (inicial).
    @param apuesta: Valor de la apuesta.
    @param multiplicador: Incremento del valor de la apuesta en caso de acertar.
    @param resultado: True → Acertar, False → Fallar.
    @return: Saldo (final).
    """
    global saldo_inicial

    # Inicializa la variable global si aún no se ha hecho
    if saldo_inicial is None:
        saldo_inicial = saldos

    beneficio = (apuesta * multiplicador) - apuesta

    saldo = saldos + beneficio if resultado is True else saldos - apuesta
    saldo = round(saldo, 2)

    return saldo

"""

    # Iniciar variable 'saldo_actual' -----------------------------------------------------------------------------
    if not hasattr(saldos, "guardar_saldo_inicial"):
        # Este bloque impedirá que el saldo se regenere al volver a llamar a la función.
        saldos = saldo_actual
    obtener_saldo.guardar_saldo_inicial = True
    # -------------------------------------------------------------------------------------------------------------

    beneficio = (apuesta * multiplicador) - apuesta

    saldo = saldos + beneficio if resultado is True else saldos - apuesta
    saldo = round(saldo, 2)
"""

# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    introducir_saldo_inicial(300)

    saldo_actualizado = obtener_saldo(300, 5, 1.32, True)
    print(saldo_actualizado)  # 301.6

    saldo_actualizado = obtener_saldo(301.6, 5, 1.32, False)
    print(saldo_actualizado)  # 296.6

    saldo_actualizado = obtener_saldo(296.6, 5, 1.32, True)
    print(saldo_actualizado)  # 298.2

    print(saldo_inicial)  # 300

# prueba()
