########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" MÓDULO: CalcularPorcentajes

"""

# ============================================ [ BIBLIOTECAS & MÓDULOS ] ============================================= #


def porcentajes(cantidad, total, rondas):
    """
    Crea una lista con la probabilidad que hay de que una opción se repita de forma consecutiva.
    @param cantidad: Número de opciones
    @param total: Total de opciones
    @param rondas: El número total de rondas límita el límite de la lista de probabilidades]
    @return: Devuelve la lista con los porcentajes.
    """
    lista_porcentajes = []

    redondear = len(str(rondas)) - 1

    limite = (1 / rondas)

    multiplicador = (cantidad / total)
    porcentaje = (cantidad / total) * 100

    while porcentaje > limite:
        lista_porcentajes.append(round(porcentaje, redondear))
        porcentaje *= multiplicador
    return lista_porcentajes


def porcentuales(cantidad, total, rondas):
    """
    Crea una lista con el número de veces que es posible que se repita un número determinado de veces una misma opción.
    @param cantidad: Número de opciones
    @param total: Total de opciones
    @param rondas: Total de rondas.
    @return: Devuelve la lista con los valores porcentuales.
    """
    lista_porcentual = []

    lista_porcentajes = porcentajes(cantidad, total, rondas)

    for porcentaje in lista_porcentajes:
        # print(f"Rondas: {rondas}")
        # print(f"Porcentaje: {porcentaje}")
        # print(f"Total: {total}")
        # print(f"Cantidad: {cantidad}")
        repeticiones = int(((rondas * porcentaje) / 100) * ((total - cantidad) / total))
        lista_porcentual.append(repeticiones)

    return lista_porcentual


def suma_repeticion_ronda(lista):

    repeticiones = 1
    suma = 0

    for cantidad in lista:

        suma += cantidad * repeticiones
        repeticiones += 1

    return suma


# PRUEBAS ---------------------------------------------------------------------------------------------------------

# int()
# [18, 14, 10, 7, 5, 4, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [18, 4, 1, 0, 0, 0]

# round()
# [19, 14, 11, 8, 6, 4, 3, 3, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [19, 5, 1, 0, 0, 0]

def pruebas():

    cantidad_rondas = 1000
    opciones_aciertos = 3
    opciones_fallos = 1
    opciones_totales = opciones_aciertos + opciones_fallos

    lista_porcentaje_trues = porcentajes(opciones_aciertos, opciones_totales, cantidad_rondas)

    lista_porcentaje_false = porcentajes(opciones_fallos, opciones_totales, cantidad_rondas)

    print(f"Porcentajes [Trues]\n{lista_porcentaje_trues}")
    print(f"Porcentajes [False]\n{lista_porcentaje_false}")

    lista_porcentual_trues = porcentuales(opciones_aciertos, opciones_totales, cantidad_rondas)
    lista_porcentual_false = porcentuales(opciones_fallos, opciones_totales, cantidad_rondas)

    print(f"Porcentual [Trues]\n{lista_porcentual_trues}")
    print(f"Porcentual [False]\n{lista_porcentual_false}")

    suma_repeticion_trues = suma_repeticion_ronda(lista_porcentual_trues)
    suma_repeticion_false = suma_repeticion_ronda(lista_porcentual_false)

    print(f"Suma Repeticiones [Trues]: {suma_repeticion_trues}")
    print(f"Suma Repeticiones [False]:{suma_repeticion_false}")
    print(f"Suma Repeticiones [Total]:{suma_repeticion_trues + suma_repeticion_false}")
    return

# pruebas()
