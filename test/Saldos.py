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

""" MÓDULO: Saldos

"""
valor_min = None
valor_max = None

def saldos_limite(saldos):

    global valor_max, valor_min

    if (valor_max and valor_min) is None:
        valor_min = saldos
        valor_max = saldos

    if valor_max < saldos:
        valor_max = saldos

    if valor_min > saldos:
        valor_min = saldos

    return valor_max, valor_min


# PRUEBAS --------------------------------------------------------------------------------------------------------------

def prueba():
    saldos_limite(10)
    saldos_limite(5)
    saldos_limite(7)
    saldos_limite(12)
    saldos_limite(6)
    saldos_limite(14)
    saldo_max, saldo_min = saldos_limite(11)
    print(f"SALDO [Max|Min]: {saldo_max} | {saldo_min}")

# prueba()
