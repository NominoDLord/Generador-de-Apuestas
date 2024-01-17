import random

print("\nGENERAR DATOS DE PRUEBAS")
print("==============================================================================")

apuesta_minima = 0.3
apuesta_maxima = 100

opciones_true, opciones_false = 4, 1

print(f"OPCIONES ACIERTO: {opciones_true}")
print(f"OPCIONES FALLO: {opciones_false}")

print("\n------------------------------------------------------------------------------")

opciones_total = opciones_true + opciones_false

lista_opciones = ([True] * opciones_true) + ([False] * opciones_false)

contar_trues, contar_falses = 0, 0
posicion_true, posicion_false = 0, 0

proporcion_max_true, proporcion_max_false = opciones_true / opciones_total, opciones_false / opciones_total
proporcion_min_true, proporcion_min_false = opciones_true / opciones_total, opciones_false / opciones_total

lista_probabilidad_de_acertar_trues = []
lista_probabilidad_de_acertar_falses = []
lista_probabilidad_de_fallar_falses = []

probabilidad_base_true = round(opciones_true / opciones_total, 2)
probabilidad_base_false = round(opciones_false / opciones_total, 2)

porcentaje_base_true = probabilidad_base_true * 100
porcentaje_base_false = probabilidad_base_false * 100

porcentajes_true = porcentaje_base_true
while porcentajes_true > 0.000001:
    lista_probabilidad_de_acertar_trues.append(round(porcentajes_true, 4))
    porcentajes_true *= probabilidad_base_true

print(f"\nLISTA PROBABILIDAD ACERTAR (repeticiones True):\n{lista_probabilidad_de_acertar_trues}")
print(f"\nLONGITUD LISTA: {len(lista_probabilidad_de_acertar_trues)}")

print("\n------------------------------------------------------------------------------")

porcentajes_false = porcentaje_base_false

while porcentajes_false > 0.000001:
    lista_probabilidad_de_acertar_falses.append(round((100 - porcentajes_false), 4))
    porcentajes_false *= probabilidad_base_false

print(f"\nLISTA PROBABILIDAD ACERTAR (repeticiones False):\n{lista_probabilidad_de_acertar_falses}")
print(f"\nLONGITUD LISTA: {len(lista_probabilidad_de_acertar_falses)}")

print("\n------------------------------------------------------------------------------")

porcentajes_false = porcentaje_base_false

while porcentajes_false > 0.000001:
    lista_probabilidad_de_fallar_falses.append(round(porcentajes_false, 4))
    porcentajes_false *= probabilidad_base_false

print(f"\nLISTA PROBABILIDAD FALLAR (repeticiones False):\n{lista_probabilidad_de_fallar_falses}")
print(f"\nLONGITUD LISTA: {len(lista_probabilidad_de_fallar_falses)}")

print("\n------------------------------------------------------------------------------")

longitud_posiciones_true = len(lista_probabilidad_de_acertar_trues)
longitud_posiciones_false = len(lista_probabilidad_de_acertar_falses)

posiciones_true = [0] * longitud_posiciones_true
posiciones_false = [0] * longitud_posiciones_false

repeticiones_de_posicion = [0] * longitud_posiciones_false
lista_de_repeticiones = []

ronda, rondas = 0, 10000

while ronda != rondas:
    ronda += 1

    resultado = random.choice(lista_opciones)

    if resultado is True:
        contar_trues += 1
        posicion_true += 1

        if posicion_false != 0:
            posiciones_false[posicion_false - 1] += 1

            ultima_posicion = posicion_false - 1
            lista_de_repeticiones.append(ultima_posicion)

            posicion_false = 0

    if resultado is False:
        contar_falses += 1
        posicion_false += 1

        if posicion_true != 0:
            posiciones_true[posicion_true -1] += 1
            posicion_true = 0

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


i = 0
while i != longitud_posiciones_false:
    repeticiones = 0
    max_rep = 0

    for numero in lista_de_repeticiones:

        if numero == i:
            repeticiones += 1

        else:

            if repeticiones > max_rep:
                max_rep = repeticiones

            repeticiones = 0

    repeticiones_de_posicion[i] = max_rep
    i += 1


max_error = 0
apuestas = apuesta_minima
listado_de_apuesta = []

while apuestas < apuesta_maxima:
    max_error += 1
    listado_de_apuesta.append(apuestas)
    apuestas *= opciones_true
    apuestas = round(apuestas, 2)


print("\n=== RESULTADOS ===")
print("==============================================================================")

print(f"\nPOSICIONES TRUE:\n{posiciones_true}")
print(f"\nPOSICIONES FALSE:\n{posiciones_false}")
print("\n------------------------------------------------------------------------------\n")
print(f"CANTIDAD TRUE: {contar_trues}")
print(f"CANTIDAD FALSE: {contar_falses}")
print("\n------------------------------------------------------------------------------\n")
print(f"PROPORCIÓN MAX TRUE: {round(proporcion_max_true, 3)}")
print(f"PROPORCIÓN MIN TRUE: {round(proporcion_min_true, 3)}")
print("\n------------------------------------------------------------------------------\n")
print(f"PROPORCIÓN MAX FALSE: {round(proporcion_max_false, 3)}")
print(f"PROPORCIÓN MIN FALSE: {round(proporcion_min_false, 3)}")
print("\n------------------------------------------------------------------------------\n")
print(f"ERRORES MÁXIMOS: {max_error}")
print(f"LISTA DE APUESTAS: {listado_de_apuesta}")
print(f"REPETICIONES DE POSICIÓN: {repeticiones_de_posicion}")


REPETICIONES = 10000
repeticiones = 0

lista_sumatoria_false = [0] * longitud_posiciones_false
lista_promedios_false = [0] * longitud_posiciones_false

while REPETICIONES != 0:
    REPETICIONES -= 1
    repeticiones += 1

    ronda, rondas = 0, 1000

    posicion_true = 0
    posicion_false = 0
    posiciones_false = [0] * longitud_posiciones_false

    while ronda != rondas:
        ronda += 1

        resultado = random.choice(lista_opciones)

        if resultado is True:

            if posicion_false != 0:
                posiciones_false[posicion_false - 1] += 1
                posicion_false = 0

        if resultado is False:
            posicion_false += 1

    i = -1
    for posicion in posiciones_false:
        i += 1
        lista_sumatoria_false[i] += posicion

i = -1
for posicion in lista_sumatoria_false:
    i += 1
    lista_promedios_false[i] += posicion / repeticiones


print("\n==============================================================================")

print(f"\nLISTA PROMEDIO: {lista_promedios_false}")
print(f"\nREPETICIONES: {repeticiones}")


ronda, rondas = 0, 100000
lista_resultados_generados = []

while ronda != rondas:
    ronda += 1

    resultado = random.choice(lista_opciones)
    lista_resultados_generados.append(resultado)

long_list_resultados_generados = len(lista_resultados_generados) -1

probabilidad_limite_true, probabilidades = 10, 0
while lista_probabilidad_de_acertar_trues[probabilidades] > probabilidad_limite_true:
    probabilidades += 1


secuencia = 1
secuencia_max = probabilidades

while secuencia != secuencia_max:

    secuencia += 1

    intentos = 0
    intentos_maximos = 0
    distancia_maxima = 0

    repeticion_true = 0

    buscar_consecutivos = secuencia
    lista_posiciones_de_secuencia = []

    i = -1
    while long_list_resultados_generados != i:
        i += 1

        resultado_generado = lista_resultados_generados[i]

        if resultado_generado is True:
            repeticion_true += 1

            if repeticion_true == 1:
                intentos += 1

        else:

            if repeticion_true >= buscar_consecutivos:

                if intentos_maximos < intentos:
                    intentos_maximos = intentos

                intentos = 0

                lista_posiciones_de_secuencia.append(i)

                if len(lista_posiciones_de_secuencia) == 2:
                    distancia_entre_posiciones = lista_posiciones_de_secuencia[1] - lista_posiciones_de_secuencia[0]

                    if distancia_maxima < distancia_entre_posiciones:
                        distancia_maxima = distancia_entre_posiciones

                    del lista_posiciones_de_secuencia[0]

            repeticion_true = 0

    # ························································································ #

    if secuencia == 2:
        print("\n==============================================================================\n")
        print("DATOS DE SECUENCIAS [True]")
        print("······························")

    print(f"SECUENCIA: {secuencia}")
    print(f"INTENTOS: {intentos_maximos}")
    print(f"DISTANCIA: {distancia_maxima}")
    print("······························")




#
