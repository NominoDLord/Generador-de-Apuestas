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

""" ESTRATEGIA 03
Estrategia personalizada para " Egg Catcher "
"""
from time import sleep

global contador

def calcular_apuesta(resultado):
    global contador
    # Inicializar contador ----------------------------------------------------------------------------------------
    if not hasattr(calcular_apuesta, "iniciar_contador"):
        contador = 0
    calcular_apuesta.iniciar_contador = True
    # -------------------------------------------------------------------------------------------------------------

    contador = 0 if resultado is True else contador + 1

    if contador == 6:
        # lista_apuestas = [0.3, 0.3, 0.3, 0.3, 0.3, 100]
        sleep(5)
        # apuesta = lista_apuestas[contador]
        return 100
    else:
        return 0.3

# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    resultado = calcular_apuesta(False)
    print(resultado)
    resultado = calcular_apuesta(False)
    print(resultado)
    resultado = calcular_apuesta(False)
    print(resultado)
    resultado = calcular_apuesta(True)
    print(resultado)
    resultado = calcular_apuesta(False)
    print(resultado)

# prueba()
