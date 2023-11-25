########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

from typing import Tuple, List

def contar_resultados(lista: List[bool], lng_t: int, lng_f: int) -> Tuple[List[int], List[int]]:

    """
    La función contabiliza los valores "True" y "False" dentro de una lista.
    Se crean 2 listas para realizar el recuento para "True" y para "False".
    Las listas se crean con valores iniciales 0.
    
    La longitud de las dos listas creadas se define pasándolos como argumentos de la función.
        lng_t → Define la longitud de la lista para los valores "True"
        lng_f → Define la longitud de la lista para los valores "False"
    
    El número de repeticiones definirá en qué índice de la lista se deberá registrar la repetición.
    La repetición incrementará en 1 el índice correspondiente.
    
    [Repeticiones → índice] : [1 → 0], [2 → 1], [3 → 2], ...
            
        EJEMPLO:

        lista_txf = [True, False, True, True, False, False, True, True, True, True, True, True]
        contar_resultados(lista_txf, 5, 5)

        Resultado → lista_true = [1, 1, 0, 0, 1] , lista_false = [1, 1, 0, 0, 1]
    
    Los valores se contabilizarán dentro del bucle, el cual, el número de repeticiones será definido
    por la longitud de la lista introducida.
    ------------------------------------------------------------------------------------------------
    
    @param lista: Valores booleanos.
    @param lng_t: Define la longitud de la lista para los valores "True"
    @param lng_f: Define la longitud de la lista para los valores "False"
    @return:      Devuelve dos listas con los valores booleanos contabilizados.
                  1º lista → "True" // 2º lista → "False"
    """

    if lng_t <= 0 or lng_f <= 0:
        raise ValueError("Las longitudes deben ser mayores a cero.")

    lista_trues, lista_falses = [0] * lng_t, [0] * lng_f

    while lista:
        indice_true, indice_false = -1, -1

        # Se verifica que la lista contenga al menos 1 valor y que ese valor sea "True".
        if lista and lista[0] is True:
            while lista and lista[0] is True:
                lista = lista[1:]
                indice_true += 1
                     
            if indice_true < lng_t:
                lista_trues[indice_true] += 1
            else:
                lista_trues[-1] += 1

        # Se verifica que la lista contenga al menos 1 valor y que ese valor sea "False".
        if lista and lista[0] is False:
            while lista and lista[0] is False:
                lista = lista[1:]
                indice_false += 1

            if indice_false < lng_f:
                lista_falses[indice_false] += 1
            else:
                lista_falses[-1] += 1

    print(f"Lista Trues → {lista_trues}")
    print(f"Lista Falses → {lista_falses}")

    return lista_trues, lista_falses