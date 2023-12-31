from random import choice

iniciar = -1

global opciones_true, opciones_false, opciones_total, lista_opciones, contar_trues, contar_falses, \
    posicion_true, posicion_false, proporcion_max_true, proporcion_max_false, proporcion_min_true, \
    proporcion_min_false, probabilidad_de_acertar_trues, probabilidad_de_acertar_falses, probabilidad_true, \
    probabilidad_false, probabilidad_porcentual_true, probabilidad_porcentual_false, posiciones_true, \
    posiciones_false, longitud_posiciones_true, suma_perdidas_posiciones_99, saldos, saldo_objetivo, \
    ronda, rondas, apuesta, resultado, multiplicador, repeticion_true, repeticion_false, lista_apuestas, \
    lista_resultados, posiciones_perdidas, repeticiones_perdidas, limite_apuesta_minima, limite_apuesta_maxima, \
    apuesta_minima, apuesta_maxima, beneficio_max, perdida_max, incremento_por_porcentaje, proporcion_true, \
    proporcion_false, perdidas, beneficio, saldo_inicial, cantidad_probabilidad_superior_99, ronda_totales

def generar_datos_iniciales(saldo):

    global opciones_true, opciones_false, opciones_total, lista_opciones,contar_trues, contar_falses,\
        posicion_true, posicion_false, proporcion_max_true, proporcion_max_false, proporcion_min_true,\
        proporcion_min_false, probabilidad_de_acertar_trues, probabilidad_de_acertar_falses, probabilidad_true,\
        probabilidad_false, probabilidad_porcentual_true, probabilidad_porcentual_false, posiciones_true,\
        posiciones_false, longitud_posiciones_true, suma_perdidas_posiciones_99, saldos, saldo_objetivo, \
        ronda, rondas, apuesta, resultado, multiplicador, repeticion_true, repeticion_false, lista_apuestas,\
        lista_resultados, posiciones_perdidas, repeticiones_perdidas, limite_apuesta_minima, limite_apuesta_maxima,\
        apuesta_minima, apuesta_maxima, beneficio_max, perdida_max, incremento_por_porcentaje, proporcion_true,\
        proporcion_false, perdidas, beneficio, saldo_inicial, cantidad_probabilidad_superior_99

    global iniciar, saldo_inicial

    # === DATOS GENERALES DEL JUEGO =============================================================================

    iniciar += 1

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

    while probabilidad_porcentual_false > 0.000001:
        probabilidad_de_acertar_falses.append(round((100 - probabilidad_porcentual_false), 4))
        probabilidad_porcentual_false *= probabilidad_false

    longitud_posiciones_true = len(probabilidad_de_acertar_trues)
    longitud_posiciones_false = len(probabilidad_de_acertar_falses)

    posiciones_true = [0] * longitud_posiciones_true
    posiciones_false = [0] * longitud_posiciones_false

    cantidad_probabilidad_superior_99 = 0
    suma_perdidas_posiciones_99 = 0

    for propabilidad in probabilidad_de_acertar_falses:
        if propabilidad > 99:
            cantidad_probabilidad_superior_99 += 1

    if iniciar == 1:
        print("\nDATOS DEL JUEGO")
        print("=====================================================================================================\n")
        print(f"LISTA PROBABILIDAD ACERTAR (repeticiones True):\n{probabilidad_de_acertar_trues}\n")
        print(f"LONGITUD LISTA: {len(probabilidad_de_acertar_trues)}\n")
        print("-----------------------------------------------------------------------------------------------------\n")
        print(f"LISTA PROBABILIDAD ACERTAR (repeticiones False):\n{probabilidad_de_acertar_falses}\n")
        print(f"LONGITUD LISTA: {len(probabilidad_de_acertar_falses)}\n")

    # === DATOS ESPECÍFICOS DEL JUEGO =============================================================================

    saldo_inicial = saldo

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

    incremento_por_porcentaje = 0

    proporcion_true = None
    proporcion_false = None

    perdidas = None
    beneficio = None

    realizar_estrategia()

# -------------------------------------------------------------------------------------------------------------

def realizar_estrategia():

    global opciones_true, opciones_false, opciones_total, lista_opciones,contar_trues, contar_falses,\
        posicion_true, posicion_false, proporcion_max_true, proporcion_max_false, proporcion_min_true,\
        proporcion_min_false, probabilidad_de_acertar_trues, probabilidad_de_acertar_falses, probabilidad_true,\
        probabilidad_false, probabilidad_porcentual_true, probabilidad_porcentual_false, posiciones_true,\
        posiciones_false, longitud_posiciones_true, suma_perdidas_posiciones_99, saldos, saldo_objetivo, \
        ronda, rondas, apuesta, resultado, multiplicador, repeticion_true, repeticion_false, lista_apuestas,\
        lista_resultados, posiciones_perdidas, repeticiones_perdidas, limite_apuesta_minima, limite_apuesta_maxima,\
        apuesta_minima, apuesta_maxima, beneficio_max, perdida_max, incremento_por_porcentaje, proporcion_true,\
        proporcion_false, perdidas, beneficio, cantidad_probabilidad_superior_99

    global iniciar, saldo_inicial

    while True:

        ronda += 1

        # ··· APUESTA INICIAL ····················································································

        if resultado is None:
            apuesta = limite_apuesta_minima

        # ··· GENERAR APUESTAS ···················································································

        else:

            apuesta = limite_apuesta_minima

            suma_perdidas_posiciones_99 = sum(posiciones_perdidas)

            if suma_perdidas_posiciones_99 > 0:
                repartir_perdidas_false = suma_perdidas_posiciones_99 / cantidad_probabilidad_superior_99

                i = 0
                for _ in posiciones_perdidas:
                    if probabilidad_de_acertar_falses[i] > 99:
                        posiciones_perdidas[i] = repartir_perdidas_false
                    i += 1
            else:

                posiciones_perdidas = [0 for _ in posiciones_perdidas]


            if resultado is True:
                if perdidas > 0:

                # if posicion_true < 5 and perdidas > 0:
                    incremento_por_perdidas = 1 + ((probabilidad_de_acertar_trues[posicion_true]) / 100)
                    apuesta += incremento_por_perdidas * perdidas

            if apuesta < 3:
                apuesta *= opciones_true
            else:
                apuesta /= 3

            # if resultado is False:
            #
            #
            #
            #     if probabilidad_de_acertar_falses[posicion_false] > 99:
            #
            #         apuesta += posiciones_perdidas[posicion_false - 1]
            #
            #     if posiciones_perdidas[posicion_false - 1] > 2:
            #         apuesta *= 1.5

            if ronda > 100:

                if proporcion_true < 0.725:
                    incremento_por_porcentaje = 1.25

                if proporcion_true > 0.735 and incremento_por_porcentaje == 0.5:
                    incremento_por_porcentaje = 0

                if incremento_por_porcentaje != 0:
                    apuesta *= incremento_por_porcentaje

        # ··· GENERAR RESULTADO ··················································································

        resultado = choice(lista_opciones)

        # ··· CONTABILIZAR RESULTADOS ············································································

        if resultado is True:
            contar_trues += 1


            # if posicion_false > 2:
            #     repeticiones_perdidas[posicion_false - 1] -= 1
            #
            #     if repeticiones_perdidas[posicion_false - 1] > 0:
            #         posiciones_perdidas[posicion_false - 1] -= (apuesta * multiplicador) - apuesta


            if posicion_false != 0:
                posiciones_false[posicion_false -1] += 1

                if probabilidad_de_acertar_falses[posicion_false -1] > 0.99:
                    posiciones_perdidas[posicion_false -1] -= (apuesta * multiplicador) - apuesta

            posicion_true += 1
            posicion_false = 0


        if resultado is False:
            contar_falses += 1

            if probabilidad_de_acertar_falses[posicion_false] > 0.99:
                posiciones_perdidas[posicion_false] += apuesta - incremento_por_porcentaje

            if posicion_true != 0:
                posiciones_true[posicion_true -1] += 1

            posicion_true = 0
            posicion_false += 1


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

        print(saldos)

        if saldos > 2000:
            imprimir_datos()
            break

        if beneficios > 10 or perdidas > 1000:
            play(saldos)

        if apuesta > limite_apuesta_maxima:
            error_de_estrategia()



def error_de_estrategia():
    print("ERROR")

def play(saldo):
    global saldo_inicial
    saldo_inicial = saldo
    print("PLAY")
    generar_datos_iniciales(saldo_inicial)
    return None

if iniciar == -1:
    iniciar += 1
    play(1000)

# ··· IMPRIMIR RESULTADOS ···················································································
def imprimir_datos():
    global ronda_totales, saldos, iniciar
    print("=======================================================================================================")
    print("=== RESULTADOS ===")
    print("·······································································································")
    print(f"RONDAS TOTALES: {ronda_totales}")
    print(f"SALDO FINAL: {round(saldos, 2)}")
    # print(f"POSICIONES: {posiciones_false}")
    # print(f"APUESTA MÍNIMA: {apuesta_minima}")
    # print(f"APUESTA MÁXIMA: {apuesta_maxima}")
    # print(f"BENEFICIO MÁXIMO: {beneficio_max}")
    # print(f"PERDIDA MÁXIMA: {perdida_max}")
    print(f"REPETICIONES: {iniciar}")

