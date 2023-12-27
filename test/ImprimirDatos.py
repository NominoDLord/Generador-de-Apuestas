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

""" MÓDULO: ImprimirDatos
Imprime los valores que se van generando en cada ronda.
"""

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(subDir1)
from config.setup import *

from typing import List, Tuple
from GenerarProporcion import proporcion

def imprimir(rondas, saldos, apuestas, resultados):

    cnt_trues, cnt_falses = proporcion(OPCIONES_TRUE, OPCIONES_FALSE, resultados)

    print(f"RONDA: {str(rondas)}")
    print(f"SALDO: {str(saldos)}")
    print(f"APUESTA: {str(apuestas)}")
    print(f"RESULTADO: {str(resultados)}")
    print(f"PROPORCIÓN [T|F]: {str(cnt_trues)} | {str(cnt_falses)}")
    print(f"BENEFICIO: {str(round((saldos - SALDO_INICIAL), 2))}")
    print("--------------------------------------------------")

# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():
    pass

# prueba()
