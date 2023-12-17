import random

contar_true, contar_false = 0, 0

def estrategia_apuesta(puntos, apuesta_actual):
    # Genera un resultado aleatorio (True para acierto, False para fallo)
    global contar_true, contar_false
    resultado = random.choice([True, False])

    # Aplica la estrategia de apuesta
    if puntos > 1000:
        apuesta_actual = 5
    elif resultado:
        apuesta_actual = min(20, apuesta_actual * 2)
    else:
        apuesta_actual = 10

    # Actualiza los puntos según el resultado y la apuesta actual
    if resultado:
        puntos += apuesta_actual
    else:
        puntos -= apuesta_actual

    if resultado is True:
        contar_true += 1
    if resultado is False:
        contar_false += 1

    return puntos, apuesta_actual, resultado, contar_true, contar_false

def simular_estrategia():
    puntos = 1000
    apuesta_actual = 10
    resultados = []

    while True:
        puntos, apuesta_actual, resultado, trues, falses = estrategia_apuesta(puntos, apuesta_actual)
        resultados.append(resultado)

        print(f'Puntos: {puntos}, Apuesta actual: {apuesta_actual}, Último resultado: {resultado}')
        print(f"{trues}|{falses}")


# Llamamos a la función para simular la estrategia
simular_estrategia()
