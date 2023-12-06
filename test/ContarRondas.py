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

global ronda

def rondas() -> int:
    # Iniciar contador de rondas ----------------------------------------------------------------------------------
    global ronda
    if not hasattr(rondas, "iniciar"):
        # Este bloque impedirá que la ronda vuelva a obtener el valor inicial.
        ronda = 0
    rondas.iniciar = True
    # -------------------------------------------------------------------------------------------------------------
    ronda += 1
    return ronda


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():

    global ronda

    ronda = rondas()
    print(type(ronda))  # <class 'int'>
    print(ronda)  # 1
    ronda = rondas()
    print(ronda)  # 2
    ronda = rondas()
    print(ronda)  # 3
    ronda = rondas()
    print(ronda)  # 4
    ronda = rondas()
    print(ronda)  # 5

# prueba()
