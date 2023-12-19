# import sys
# import os
#
# subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#
# sys.path.append(subDir1)
#
# from config.configuracion import *

from LecturaTXT_Bools import leer_bools

contar_true, contar_false = 0, 0

def estrategia_apuesta(puntos, apuesta_actual, resultados_preexistentes):
    global contar_true, contar_false

    # Obtiene el siguiente resultado de la lista preexistente
    resultado = resultados_preexistentes.pop(0) if resultados_preexistentes else None

    # Aplica la estrategia de apuesta
    if puntos > 1000:
        apuesta_actual = 7.5
    elif resultado:
        apuesta_actual = min(30, apuesta_actual * 3)
    else:
        apuesta_actual = 15

    # Actualiza los puntos según el resultado y la apuesta actual
    if resultado:
        # Incrementa el beneficio en caso de True
        puntos += round((apuesta_actual * 1.32) - apuesta_actual, 2)
    else:
        puntos -= apuesta_actual

    if resultado is True:
        contar_true += 1
    if resultado is False:
        contar_false += 1

    return puntos, round(apuesta_actual, 2), contar_true, contar_false, resultado

def simular_estrategia():
    puntos = 1000
    apuesta_actual = 15
    resultados = []

    while lista_resultados:
        resultado = lista_resultados.pop(0)
        puntos, apuesta_actual, trues, falses, _ = estrategia_apuesta(puntos, apuesta_actual, [resultado])
        resultados.append(resultado)

        print(f'Puntos: {puntos}, Apuesta actual: {apuesta_actual}, Último resultado: {resultado}')
        print(f"{trues}|{falses}")

# Lista preexistente de resultados True y False
lista_resultados = leer_bools("Total[75-25].txt")

# Llamamos a la función para simular la estrategia
simular_estrategia()
