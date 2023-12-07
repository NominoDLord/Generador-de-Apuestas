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

from typing import List, Tuple
from GenerarProporcion import proporcion

def imprimir(saldo_inicial, ronda, saldo_actual, trues, falses, cantidad_apostada, resultado_ronda):

    proporcion_trues, proporcion_falses = proporcion(trues, falses, resultado_ronda)

    print(f"RONDA: {str(ronda)}")
    print(f"SALDO: {str(saldo_actual)}")
    print(f"APUESTA: {str(cantidad_apostada)}")
    print(f"RESULTADO: {str(resultado_ronda)}")
    print(f"PROPORCIÓN [T|F]: {str(proporcion_trues)} | {str(proporcion_falses)}")
    print(f"BENEFICIO: {str(round((saldo_actual - saldo_inicial), 2))}")
    print("--------------------------------------------------")


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    imprimir(300, 1, 300, 3, 1, 5, True)
    imprimir(300, 2, 305, 3, 1, 5, True)
    imprimir(300, 3, 300, 3, 1, 5, False)
    imprimir(300, 4, 305, 3, 1, 5, True)

# prueba()
