import random

saldo_inicial = 10000.00
saldos = saldo_inicial

ronda = 0
rondas = 100000

lista_opciones = [True, False]

apuesta = None
apuesta_base  = 1.00
lim_apuesta_max = 100
lim_apuesta_min = 0.3

apuesta_maxima = lim_apuesta_min
apuesta_minima = lim_apuesta_max
beneficio_max = 0
perdida_max = 0

multiplicador = 2

contar_trues, contar_falses = 0, 0
posicion_true, posicion_false = 0, 0

opciones_true = 1
opciones_false = 1
opciones_total = opciones_true + opciones_false

probabilidad_de_acertar_trues = []
probabilidad_de_acertar_falses = []

probabilidad_true = round(opciones_true / opciones_total, 2)
probabilidad_false = round(opciones_false / opciones_total, 2)

probabilidad_porcentual_true = probabilidad_true * 100
probabilidad_porcentual_false = probabilidad_false * 100

while probabilidad_porcentual_true > 0.000001:
    probabilidad_de_acertar_trues.append(round(probabilidad_porcentual_true, 4))
    probabilidad_porcentual_true *= probabilidad_true

while probabilidad_porcentual_false > 0.000001:
    probabilidad_de_acertar_falses.append(round((100 - probabilidad_porcentual_false), 4))
    probabilidad_porcentual_false *= probabilidad_false

longitud_posiciones_true = len(probabilidad_de_acertar_trues)
longitud_posiciones_false = len(probabilidad_de_acertar_falses)

posiciones_true = [0] * longitud_posiciones_true
posiciones_false = [0] * longitud_posiciones_false


while ronda != rondas:
    ronda += 1

    # GENERAR APUESTAS ----------------------------------------------------------------------------------------

    if apuesta is None:
        apuesta = apuesta_base

    else:

        if resultado is True:

            apuesta = apuesta_base * ((probabilidad_de_acertar_trues[posicion_true] / 100) + 1)

        if resultado is False:

            apuesta = apuesta_base * ((probabilidad_de_acertar_falses[posicion_false] / 100) + 1)

        # INCREMENTO ·······················································································

        diferencia = contar_falses - contar_trues

        incremento = 1.00 + (diferencia / 100)

        apuesta *= incremento

        if apuesta < lim_apuesta_min:
            apuesta = lim_apuesta_min

        if apuesta > lim_apuesta_max:
            apuesta = lim_apuesta_max

        apuesta = round(apuesta, 2)

    # OBTENER RESULTADO ALEATORIO -----------------------------------------------------------------------------

    resultado = random.choice(lista_opciones)

    # CONTABILIZAR DATOS --------------------------------------------------------------------------------------

    if resultado is True:
        contar_trues += 1
        posicion_true += 1

        if posicion_false != 0:
            posiciones_false[posicion_false - 1] += 1
            posicion_false = 0

    if resultado is False:
        contar_falses += 1
        posicion_false += 1

        if posicion_true != 0:
            posiciones_true[posicion_true -1] += 1
            posicion_true = 0


    # ACTUALIZAR SALDO ----------------------------------------------------------------------------------------

    saldos -= apuesta
    saldos = saldos + (apuesta * multiplicador) if resultado is True else saldos + 0


    # CALCULAR PERDIDAS Y BENEFICIOS --------------------------------------------------------------------------

    beneficios = round(saldos - saldo_inicial, 2)
    perdidas = round(saldo_inicial - saldos, 2)


    # ANALISIS DE DATOS ---------------------------------------------------------------------------------------

    if apuesta > apuesta_maxima:
        apuesta_maxima = apuesta

    if apuesta < apuesta_minima:
        apuesta_minima = apuesta

    if beneficio_max < beneficios:
        beneficio_max = round(beneficios, 2)

    if perdida_max < perdidas:
        perdida_max = round(perdidas, 2)

    if beneficios > 10000 or perdidas > 10000:
        break


# === IMPRIMIR RESULTADOS =========================================================================================

print(f"NÚMERO DE RONDAS: {ronda}")
print(f"SALDO FINAL: {round(saldos, 2)}")
print(f"APUESTA MÍNIMA: {apuesta_minima}")
print(f"APUESTA MÁXIMA: {apuesta_maxima}")
print(f"BENEFICIO FINAL: {beneficios}")
print(f"BENEFICIO MÁXIMO: {beneficio_max}")
print(f"PERDIDA MÁXIMA: {perdida_max}")
print(f"PROPORCIÓN: {contar_trues} | {contar_falses}")