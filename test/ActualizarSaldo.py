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

import sys
import os

# Obtén la ruta al directorio anterior
subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agrega los directorios anteriores al sys.path
sys.path.append(subDir1)

from config.setup import *


def obtener_saldo(saldos: float, apuesta: float, resultado: bool) -> float:
    """
    @param saldos: Saldo (inicial).
    @param apuesta: Valor de la apuesta.
    @param resultado: True → Acertar, False → Fallar.
    @return: Saldo (final).
    """
    beneficio = (apuesta * MULTIPLICADOR) - apuesta

    saldo = saldos + beneficio if resultado is True else saldos - apuesta
    saldo = round(saldo, 2)
    return saldo


# PRUEBAS --------------------------------------------------------------------------------------------------------------



def prueba():

    introducir_saldo_inicial(300)

    saldo_actualizado = obtener_saldo(300, 5, True)
    print(saldo_actualizado)  # 301.6

    saldo_actualizado = obtener_saldo(301.6, 5, False)
    print(saldo_actualizado)  # 296.6

    saldo_actualizado = obtener_saldo(296.6, 5, True)
    print(saldo_actualizado)  # 298.2

    print(saldo_inicial)  # 300

# prueba()
