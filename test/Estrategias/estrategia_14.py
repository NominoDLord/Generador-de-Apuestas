from random import choice

lista = [True, False]

limite_apuesta_minima = 0.3
limite_apuesta_maxima = 100

apuesta_minima = limite_apuesta_maxima
apuesta_maxima = limite_apuesta_minima

saldo_inicial = 1000
saldos = saldo_inicial
saldo_objetivo = saldo_inicial + 10

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

posiciones_false = [0] * 20
posiciones_true = [0] * 20

posicion_perdidas = [0] * 20
posicion_beneficios = [0] * 20

lista_beneficios = []
lista_perdidas = []

lista_valores = []
lista_apuestas = []

ronda = 0
rondas = 1000

while rondas != ronda:
    ronda += 1

    # GENERAR APUESTA ----------------------------------------------------------------------------------------

    if resultado is None:
        apuesta = limite_apuesta_minima

    # -------------------------------------------------------------------------

    else:

        # for valor in posicion_perdidas:
        #     if valor > 0:
        #         lista_valores.append(0)
        #     else:
        #         lista_valores.append(valor)

        lista_valores = [round(valor1 + valor2, 2) for valor1, valor2 in zip(posicion_beneficios, posicion_perdidas)]

        suma_valores = sum(lista_valores)

        # for valor in lista_valores:
        #     if valor < 0:
        #         suma_valores += valor

        suma_valores = round(suma_valores, 2)

        print(f"SUMA VALORES: {suma_valores}")

        suma_valores = abs(suma_valores)
        apuesta = suma_valores * (1 - (0.5 ** repeticion_false))



        if apuesta < 0.3:
            apuesta = 0.3

        elif apuesta > 100:
            apuesta = 100

        else:
            apuesta = round(apuesta, 2)

        # print(lista_valores)
        print(f"APUESTA: {apuesta}")

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

    # GENERAR RESULTADO --------------------------------------------------------------------------------------

    resultado = choice(lista)
    print(f"RESULTADO: {resultado}")

    # CONTABILIZAR DATOS -------------------------------------------------------------------------------------

    if resultado is False:
        contar_false += 1
        posicion_perdidas[repeticion_false] -= round(apuesta, 2)
        repeticion_false += 1

        if repeticion_true != 0:
            repeticion_true = 0

    elif resultado is True:
        contar_true += 1
        posicion_beneficios[repeticion_true] += (apuesta * multiplicador) - apuesta
        repeticion_true += 1

        if repeticion_false != 0:
            # posicion_perdidas[repeticion_false - 1] += round((apuesta * multiplicador) - apuesta, 2)
            posiciones_false[repeticion_false- 1] += 1
            repeticion_false = 0

    index = 0
    for valor in posicion_perdidas:
        posicion_perdidas[index] = round(posicion_perdidas[index], 2)
        index += 1

    # CALCULAR SALDOS ---------------------------------------------------------------------------------------

    saldos -= apuesta
    saldos = saldos + (apuesta * multiplicador) if resultado is True else saldos + 0

    beneficios = saldos - saldo_inicial
    perdidas = saldo_inicial - saldos

    # ANALIZAR DATOS ----------------------------------------------------------------------------------------

    if apuesta > apuesta_maxima:
        apuesta_maxima = apuesta

    if apuesta < apuesta_minima:
        apuesta_minima = apuesta

    if beneficio_max < beneficios:
        beneficio_max = round(beneficios, 2)

    if perdida_max < perdidas:
        perdida_max = round(perdidas, 2)

    if beneficios > 100:
        break

# lista_invertida = []
# for valor in reversed(posiciones_false):
#     lista_invertida.append(valor)


print(f"RONDAS TOTALES: {ronda}")
print(f"SALDO FINAL: {round(saldos, 2)}")
print(f"POSICIONES: {posiciones_false}")

# print(lista_invertida)
# print(fallos_posicion_false)

print(f"APUESTA MÍNIMA: {apuesta_minima}")
print(f"APUESTA MÁXIMA: {apuesta_maxima}")
print(f"BENEFICIO MÁXIMO: {beneficio_max}")
print(f"PERDIDA MÁXIMA: {perdida_max}")