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

""" MÓDULO: ActualizarSaldo
Actualiza el saldo en base a la apuesta, el resultado y el multiplicador.
"""

global saldo_inicial

def introducir_saldo_inicial(saldo_introducido):
    global saldo_inicial
    saldo_inicial = saldo_introducido

def obtener_saldo(saldos: float, apuesta: float, multiplicador: float, resultado: bool) -> float:
    """
    @param saldos: Saldo (inicial).
    @param apuesta: Valor de la apuesta.
    @param multiplicador: Incremento del valor de la apuesta en caso de acertar.
    @param resultado: True → Acertar, False → Fallar.
    @return: Saldo (final).
    """
    beneficio = (apuesta * multiplicador) - apuesta

    saldo = saldos + beneficio if resultado is True else saldos - apuesta
    saldo = round(saldo, 2)
    return saldo


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
