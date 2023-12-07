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

    Estrategia personalizada para...

        > Egg Catcher

"""

global contador

def calcular_apuesta(resultado):
    global contador
    # Inicializar contador ----------------------------------------------------------------------------------------
    if not hasattr(calcular_apuesta, "iniciar_contador"):
        contador = 0
    calcular_apuesta.iniciar_contador = True
    # -------------------------------------------------------------------------------------------------------------

    contador = 0 if resultado is True else contador + 1

    if contador < 6:
        lista_apuestas = [0.3, 0.3, 0.3, 9, 60, 100]
        apuesta = lista_apuestas[contador]
        return apuesta
    else:
        return 50

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
