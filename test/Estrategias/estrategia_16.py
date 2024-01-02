from random import choice

iniciar = -1

# === DATOS FIJOS DEL JUEGO =========================================================================================

saldo_inicial = 1000
saldos = saldo_inicial

opciones_true, opciones_false = 3, 1

opciones_total = opciones_true + opciones_false

lista_opciones = ([True] * opciones_true) + ([False] * opciones_false)

multiplicador = 1.32

limite_apuesta_minima = 0.3
limite_apuesta_maxima = 100

apuesta_base = limite_apuesta_minima * opciones_true

apuesta_minima = limite_apuesta_maxima
apuesta_maxima = limite_apuesta_minima

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

while probabilidad_porcentual_false > 0.000001:
    probabilidad_de_acertar_falses.append(round((100 - probabilidad_porcentual_false), 4))
    probabilidad_porcentual_false *= probabilidad_false

longitud_posiciones_true = len(probabilidad_de_acertar_trues)
longitud_posiciones_false = len(probabilidad_de_acertar_falses)

posiciones_true = [0] * longitud_posiciones_true
posiciones_false = [0] * longitud_posiciones_false

cantidad_probabilidad_superior_99 = 0
cantidad_probabilidad_superior_25 = 0

suma_perdidas_posiciones_99 = 0

for propabilidad in probabilidad_de_acertar_trues:
    if propabilidad > 0.25:
        cantidad_probabilidad_superior_25 += 1

for propabilidad in probabilidad_de_acertar_falses:
    if propabilidad > 99:
        cantidad_probabilidad_superior_99 += 1


print("\nDATOS DEL JUEGO")
print("=====================================================================================================\n")
print(f"LISTA PROBABILIDAD ACERTAR (repeticiones True):\n{probabilidad_de_acertar_trues}\n")
print(f"LONGITUD LISTA: {len(probabilidad_de_acertar_trues)}\n")
print("-----------------------------------------------------------------------------------------------------\n")
print(f"LISTA PROBABILIDAD ACERTAR (repeticiones False):\n{probabilidad_de_acertar_falses}\n")
print(f"LONGITUD LISTA: {len(probabilidad_de_acertar_falses)}\n")


rondas_totales = 0
repeticion_true, repeticion_false = 0, 0
lista_apuestas, lista_resultados = [], []

proporcion_true = None
proporcion_false = None

beneficio_max, perdida_max = 0, 0
saldo_maximo = 0
saldo_minimo = saldo_inicial

# ==================================================================================================================== #

ronda = 0
rondas = 1000

saldo_objetivo = saldos

apuesta = None
resultado = None

perdidas_true = 0
perdidas_false = 0

posiciones_perdida_true = [0] * longitud_posiciones_true
posiciones_perdida_false = [0] * longitud_posiciones_false

incremento_por_porcentaje_true = 0

perdidas = 0
beneficios = 0

while saldos < 1500:



        print(saldos)

        ronda += 1
        rondas_totales += 1

        # ··· APUESTA INICIAL ····················································································

        if resultado is None:
           apuesta = apuesta_base

        # ··· GENERAR APUESTAS ···················································································

        else:

            apuesta = limite_apuesta_minima

            if perdidas < 0:
                perdidas = 0

            if resultado is True:

                if perdidas > 0:

                    incremento_posicion_true = (1+(probabilidad_de_acertar_trues[posicion_true] / 100))
                    apuesta += incremento_posicion_true * perdidas

                # else:
                #
                #     apuesta = limite_apuesta_minima * (probabilidad_de_acertar_trues[posicion_true] / 100)


            if resultado is False:

                if perdidas > 0:
                    if probabilidad_de_acertar_falses[posicion_false] > 99:
                        apuesta += (perdidas / cantidad_probabilidad_superior_99)  # ((opciones_false / opciones_total) +1)

                    # if probabilidad_de_acertar_falses[posicion_false] > 99.9:
                    #     apuesta *= 3

                # else:
                #
                #     apuesta = limite_apuesta_minima * (1+(probabilidad_de_acertar_falses[posicion_false] / 100))


            if ronda > 100:

                if proporcion_true < 0.725:
                    incremento_por_porcentaje_true = 1.25

                if proporcion_true > 0.735 and incremento_por_porcentaje_true == 1.25:
                    incremento_por_porcentaje_true = 0

                if incremento_por_porcentaje_true != 0:
                    apuesta *= incremento_por_porcentaje_true

        if apuesta > limite_apuesta_maxima:
            apuesta = limite_apuesta_maxima

        apuesta = round(apuesta, 2)
        print(apuesta)

        # ··· GENERAR RESULTADO ··················································································

        resultado = choice(lista_opciones)

        # ··· CONTABILIZAR RESULTADOS ············································································

        if resultado is True:
            contar_trues += 1

            if posicion_false != 0:
                posiciones_false[posicion_false -1] += 1

                if probabilidad_de_acertar_falses[posicion_false -1] > 0.99:
                    perdidas_true -= (apuesta * multiplicador) - apuesta

            posicion_true += 1
            posicion_false = 0


        if resultado is False:
            contar_falses += 1

            # if probabilidad_de_acertar_falses[posicion_false] > 0.99:
            #     perdidas_true += apuesta

            if posicion_true != 0:
                posiciones_true[posicion_true -1] += 1
                perdidas_true += apuesta

            posicion_true = 0
            posicion_false += 1


        # ··· CALCULAR SALDOS ···················································································

        saldos -= apuesta
        saldos = saldos + (apuesta * multiplicador) if resultado is True else saldos + 0
        saldos = round(saldos, 2)

        beneficios = saldos - saldo_objetivo
        perdidas = saldo_objetivo - saldos

        if beneficios > 10:
            saldo_objetivo += beneficios

        # ··· ANALIZAR LÍMITES ··················································································

        if apuesta_maxima < apuesta:
            apuesta_maxima = round(apuesta, 2)

        if apuesta_minima > apuesta:
            apuesta_minima = round(apuesta, 2)

        if beneficio_max < beneficios:
            beneficio_max = round(beneficios, 2)

        if perdida_max < perdidas:
            perdida_max = round(perdidas, 2)

        if saldo_maximo < saldos:
            saldo_maximo = saldos

        if saldo_minimo > saldos:
            saldo_minimo = saldos

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






# ··· IMPRIMIR RESULTADOS ···················································································

print("=======================================================================================================")
print("=== RESULTADOS ===")
print("·······································································································")
print(f"RONDAS TOTALES: {rondas_totales}")
print(f"SALDO FINAL: {round(saldos, 2)}")
print(f"SALDO MÁXIMO: {saldo_maximo}")
print(f"SALDO MÍNIMO: {saldo_minimo}")
print(f"APUESTA MÍNIMA: {apuesta_minima}")
print(f"APUESTA MÁXIMA: {apuesta_maxima}")
# print(f"BENEFICIO MÁXIMO: {beneficio_max}")
# print(f"PERDIDA MÁXIMA: {perdida_max}")
# print(f"REPETICIONES: {iniciar}")

# print(f"POSICIONES: {posiciones_false}")