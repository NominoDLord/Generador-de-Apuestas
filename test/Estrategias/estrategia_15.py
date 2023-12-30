from random import choice


print("\nDATOS DEL JUEGO")
print("===============================================================================================================")

# === DATOS GENERALES DEL JUEGO ===============================================================================

opciones_true, opciones_false = 3, 1

opciones_total = opciones_true + opciones_false

lista_opciones = ([True] * opciones_true) + ([False] * opciones_false)

contar_trues, contar_falses = 0, 0
posicion_true, posicion_false = 0, 0

proporcion_max_true, proporcion_max_false = opciones_true / opciones_total, opciones_false / opciones_total
proporcion_min_true, proporcion_min_false = opciones_true / opciones_total, opciones_false / opciones_total

probabilidad_de_acertar_trues = []
probabilidad_de_acertar_falses = []

probabilidad_true = round(opciones_true / opciones_total, 2)
probabilidad_false = round(opciones_false / opciones_total, 2)

probabilidad_porcentual_true = probabilidad_true * 100
probabilidad_porcentual_false = probabilidad_false * 100

while probabilidad_porcentual_true > 0.000001:
    probabilidad_de_acertar_trues.append(round(probabilidad_porcentual_true, 4))
    probabilidad_porcentual_true *= probabilidad_true

print(f"LISTA PROBABILIDAD ACERTAR (repeticiones True):\n{probabilidad_de_acertar_trues}")
print(f"LONGITUD LISTA: {len(probabilidad_de_acertar_trues)}")

print("---------------------------------------------------------------------------------------------------------------")

while probabilidad_porcentual_false > 0.000001:
    probabilidad_de_acertar_falses.append(round((100 - probabilidad_porcentual_false), 4))
    probabilidad_porcentual_false *= probabilidad_false

print(f"LISTA PROBABILIDAD ACERTAR (repeticiones False):\n{probabilidad_de_acertar_falses}")
print(f"LONGITUD LISTA: {len(probabilidad_de_acertar_falses)}")

longitud_posiciones_true = len(probabilidad_de_acertar_trues)
longitud_posiciones_false = len(probabilidad_de_acertar_falses)

posiciones_true = [0] * longitud_posiciones_true
posiciones_false = [0] * longitud_posiciones_false

# === DATOS ESPECÍFICOS DEL JUEGO =============================================================================

saldo_inicial = 1000

saldos = saldo_inicial
saldo_objetivo = None

ronda = 0
rondas = 1000

apuesta = None
resultado = None
multiplicador = 1.32

repeticion_true, repeticion_false = 0, 0

lista_apuestas = []
lista_resultados = []

posiciones_perdidas = [0] * longitud_posiciones_false
repeticiones_perdidas = [0] * longitud_posiciones_false

limite_apuesta_minima = 0.3
limite_apuesta_maxima = 100

apuesta_minima = limite_apuesta_maxima
apuesta_maxima = limite_apuesta_minima

beneficio_max = 0
perdida_max = 0

incremento = 0

proporcion_true = None
proporcion_false = None

perdidas = None
beneficio = None

# -------------------------------------------------------------------------------------------------------------

while rondas != ronda:

    ronda += 1

    # ··· APUESTA INICIAL ····················································································

    if resultado is None:
        apuesta = limite_apuesta_minima

    # ··· GENERAR APUESTAS ···················································································

    else:

        apuesta = limite_apuesta_minima

        if resultado is True:

            if posicion_true < 2 and perdidas > 0:
                apuesta *= 1.5


        if resultado is False:

            apuesta += posiciones_perdidas[posicion_false - 1]

            if posiciones_perdidas[posicion_false - 1] > 2:
                apuesta *= 1.5

        if ronda > 100:

            if proporcion_true < 0.715:
                incremento = 0.5

            if proporcion_true > 0.735 and incremento == 0.5:
                incremento = 0

            apuesta += incremento

    # ··· GENERAR RESULTADO ··················································································

    resultado = choice(lista_opciones)

    # ··· CONTABILIZAR RESULTADOS ············································································

    if resultado is True:
        contar_trues += 1
        posicion_true += 1

        if posicion_false > 2:
            repeticiones_perdidas[posicion_false - 1] -= 1

            if repeticiones_perdidas[posicion_false - 1] > 0:
                posiciones_perdidas[posicion_false - 1] -= (apuesta * multiplicador) - apuesta


        if posicion_false != 0:
            posiciones_false[posicion_false - 1] += 1

            posicion_false = 0


    if resultado is False:
        contar_falses += 1
        posicion_false += 1

        if posicion_false > 2:
            repeticiones_perdidas[posicion_false - 1] += 3
            posiciones_perdidas[posicion_false - 1] += apuesta - incremento

        if posicion_true != 0:
            posiciones_true[posicion_true -1] += 1
            posicion_true = 0

    # ··· CALCULAR SALDOS ···················································································

    saldos -= apuesta
    saldos = saldos + (apuesta * multiplicador) if resultado is True else saldos + 0

    beneficios = saldos - saldo_inicial
    perdidas = saldo_inicial - saldos

    # ··· ANALIZAR LÍMITES ··················································································

    if apuesta_maxima < apuesta:
        apuesta_maxima = round(apuesta, 2)

    if apuesta_minima > apuesta:
        apuesta_minima = round(apuesta, 2)

    if beneficio_max < beneficios:
        beneficio_max = round(beneficios, 2)

    if perdida_max < perdidas:
        perdida_max = round(perdidas, 2)

    # ··· CALCULAR PROPORCIÓN ···············································································

    proporcion_true = contar_trues / ronda
    proporcion_false = contar_falses / ronda

    if ronda > 100:

        if proporcion_max_true < proporcion_true:
            proporcion_max_true = proporcion_true

        if proporcion_max_false < proporcion_false:
            proporcion_max_false = proporcion_false

        if proporcion_min_true > proporcion_true:
            proporcion_min_true = proporcion_true

        if proporcion_min_false > proporcion_false:
            proporcion_min_false = proporcion_false

    # ··· REGISTRO DE DATOS ·················································································

    lista_resultados.append(resultado)
    lista_apuestas.append(apuesta)

    # ··· CONDICIONES DE SALIDA ·············································································

    if beneficios > 100:
        break


# === IMPRIMIR RESULTADOS =========================================================================================
print("===============================================================================================================")
print("=== RESULTADOS")
print("···············································································································")
print(f"RONDAS TOTALES: {ronda}")
print(f"SALDO FINAL: {round(saldos, 2)}")
print(f"POSICIONES: {posiciones_false}")
print(f"APUESTA MÍNIMA: {apuesta_minima}")
print(f"APUESTA MÁXIMA: {apuesta_maxima}")
print(f"BENEFICIO MÁXIMO: {beneficio_max}")
print(f"PERDIDA MÁXIMA: {perdida_max}")
