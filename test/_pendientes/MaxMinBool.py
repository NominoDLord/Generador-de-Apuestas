########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" ESTRATEGIA 11
"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
subDir2 = os.path.abspath(os.path.join(subDir1, '..'))

sys.path.append(subDir1)
sys.path.append(subDir2)

from config.configuracion import *

from LecturaTXT_Bools import leer_bools
from GenerarBools import generar_lista

# ================================================== [ VARIABLES ] =================================================== #

global mx_true, mx_false, mn_true, mn_false
lista = []
max_true, max_false, min_true, min_false = 0, 0, 100, 100

# ================================================== [ FUNCIONES ] =================================================== #

def calcular_limites(resultados):

    global max_true, max_false, min_true, min_false
    lista.append(resultados)

    if len(lista) > 100:
        del lista[0]

        trues = lista.count(True)
        falses = lista.count(False)

        if max_true < trues:
            max_true = trues
        if max_false < falses:
            max_false = falses
        if min_true > trues:
            min_true = trues
        if min_false > falses:
            min_false = falses

    return max_true, max_false, min_true, min_false

# ===================================================== [ TEST ] ===================================================== #

def prueba():

    global mx_true, mx_false, mn_true, mn_false

    Nombre_Archivo = "Total[75-25]"
    resultados = leer_bools(f"{Nombre_Archivo}.txt")

    for resultado in resultados:
        mx_true, mx_false, mn_true, mn_false = calcular_limites(resultado)

    print(f"max_true: {mx_true}")
    print(f"max_false: {mx_false}")
    print(f"min_true: {mn_true}")
    print(f"min_false: {mn_false}")

    return None

prueba()
