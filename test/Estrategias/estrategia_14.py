from random import choice

lista = [True, False]

limite_apuesta_minima = 0.3
limite_apuesta_maxima = 100

apuesta_minima = limite_apuesta_maxima
apuesta_maxima = limite_apuesta_minima

saldo_inicial = 1000
saldos = saldo_inicial

saldo_max = saldo_inicial
saldo_min = saldo_inicial

apuesta = None
resultado = None

beneficios = 0
perdidas = 0

beneficio_max = 0
perdida_max = 0

multiplicador = 2
incremento = 1

contar_true = 0
contar_false = 0

repeticion_true = 0
repeticion_false = 0

repeticion_max_false = 0

posiciones_false = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
posiciones_true = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

fallos_posicion_false = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lista_beneficios = []
lista_perdidas = []
lista_valores = []

ronda = 0
rondas = 100000

while rondas != ronda:
    ronda += 1

    if resultado is None:
        apuesta = limite_apuesta_minima

    else:

        suma_fallos = sum(fallos_posicion_false)

        repartir_cantidades = suma_fallos / len(posiciones_false)

        for _ in posiciones_false:
            lista_valores.append(repartir_cantidades)

        if perdidas > 0:

            longitud_lista_perdidas = len(posiciones_false)
            repartir_perdidas = round((perdidas / longitud_lista_perdidas), 2)

            if resultado is False:

                apuesta = repartir_perdidas * repeticion_false

            if resultado is True:
                apuesta = repartir_perdidas / repeticion_true

        if beneficios > 0:

            if ronda > 100:

                proporcion_false = contar_false / ronda
                proporcion_true = contar_true / ronda

                if proporcion_false > 0.56:
                    incremento = 2

                if proporcion_false > 0.53 and incremento == 2:
                    incremento = 1

            apuesta = 1 * incremento


    # --------------------------------------------------------------------

    if apuesta < limite_apuesta_minima:
        apuesta = limite_apuesta_minima

    if ronda > 100:

        proporcion_false = contar_false / ronda

        if proporcion_false > 60:
            apuesta *= 3

        elif proporcion_false > 55:
            apuesta *= 2

    apuesta = round(apuesta, 2)

    resultado = choice(lista)

    # --------------------------------------------------------------------

    if resultado is False:
        contar_false += 1
        repeticion_false += 1
        fallos_posicion_false[repeticion_false - 1] += apuesta

        if repeticion_true != 0:
            repeticion_true = 0

    elif resultado is True:
        contar_true += 1
        repeticion_true += 1

        if repeticion_false != 0:

            posiciones_false[repeticion_false - 1] += 1
            fallos_posicion_false[repeticion_false - 1] -= (apuesta * multiplicador) - apuesta

        repeticion_false = 0

    if repeticion_max_false < repeticion_false:
        repeticion_max_false = repeticion_false

    # --------------------------------------------------------------------

    saldos -= apuesta
    saldos = saldos + (apuesta * multiplicador) if resultado is True else saldos + 0

    beneficios = saldos - saldo_inicial
    perdidas = saldo_inicial - saldos

    # --------------------------------------------------------------------

    if apuesta > apuesta_maxima:
        apuesta_maxima = apuesta

    if apuesta < apuesta_minima:
        apuesta_minima = apuesta

    if beneficio_max < beneficios:
        beneficio_max = beneficios

    if perdida_max < perdidas:
        perdida_max = perdidas

    if beneficio_max > 100:
        break

lista_invertida = []
for valor in reversed(posiciones_false):
    lista_invertida.append(valor)

print(saldos)
print(posiciones_false)
# print(lista_invertida)
# print(fallos_posicion_false)

print(f"APUESTA MÍNIMA: {apuesta_minima}")
print(f"APUESTA MÁXIMA: {apuesta_maxima}")
print(f"BENEFICIO MÁXIMO: {beneficio_max}")
print(f"PERDIDA MÁXIMA: {perdida_max}")