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

def calcular_apuesta(resultado, opciones_true, opciones_false):
    # -------------------------------------------------------------------------------------------------------------
    # Inicializar proporcion_true y proporcion_false si no existen
    if not hasattr(calcular_apuesta, "proporcion_true"):
        calcular_apuesta.proporcion_true = 0
    if not hasattr(calcular_apuesta, "proporcion_false"):
        calcular_apuesta.proporcion_false = 0
    # -------------------------------------------------------------------------------------------------------------
    total_opciones = opciones_true + opciones_false

    def proporcion():

        if resultado is True:
            calcular_apuesta.proporcion_true += opciones_false

        elif resultado is False:
            calcular_apuesta.proporcion_false += opciones_true

    return apuesta


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    apuesta = calcular_apuesta(True, 3, 1)
    print(apuesta)
    apuesta = calcular_apuesta(False, 3, 1)
    print(apuesta)
    apuesta = calcular_apuesta(True, 3, 1)
    print(apuesta)
    apuesta = calcular_apuesta(True, 3, 1)
    print(apuesta)
    apuesta = calcular_apuesta(True, 3, 1)
    print(apuesta)

# prueba()
