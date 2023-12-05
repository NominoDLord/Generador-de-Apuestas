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

"""
ESTRATEGIA 02

    En esta estrategía se procede a calcular el valor de la apuesta en base a la proporción que existe entre los
    aciertos y los fallos generados en cada una de las rondas.

    El valor de la apuesta constará de 3 posibles opciones:
        · El número de opciones para aciertos.
        · El número de opciones para fallos.
        · La suma de las opciones para aciertos y fallos dividida entre dos.

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

    proporcion()

    if calcular_apuesta.proporcion_true > calcular_apuesta.proporcion_false:
        apuesta = opciones_false * 2

    elif calcular_apuesta.proporcion_true < calcular_apuesta.proporcion_false:
        apuesta = opciones_true * 2

    else:
        apuesta = (total_opciones / 2) * 2

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
