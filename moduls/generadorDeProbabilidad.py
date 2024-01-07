########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" MÓDULO: generadorDeProbabilidad """

def crear_lista_probabilidad(probabilidad):
    lista_probabilidades = []

    probabilidades = probabilidad
    porcentaje = probabilidad / 100

    while probabilidades > 0.000001:
        lista_probabilidades.append(round(probabilidades, 4))
        probabilidades *= porcentaje

    return lista_probabilidades


def crear_lista_probabilidad_inversa(probabilidad):
    lista_probabilidades = []

    probabilidades = probabilidad
    porcentaje = probabilidad / 100

    while probabilidades > 0.000001:
        lista_probabilidades.append(round(100 - probabilidades, 4))
        probabilidades *= porcentaje

    return lista_probabilidades

# === TEST ======================================================================================================= === #

def prueba():
    lista1 = crear_lista_probabilidad(75)
    print(lista1)
    lista2 = crear_lista_probabilidad_inversa(25)
    print(lista2)

# prueba()
