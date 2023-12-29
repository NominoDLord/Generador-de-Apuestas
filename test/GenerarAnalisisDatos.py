import random

print("GENERAR DATOS DE PRUEBAS")
print("==============================================================================")

opciones_true, opciones_false = 3, 1

opciones_total = opciones_true + opciones_false

lista_opciones = ([True] * opciones_true) + ([False] * opciones_false)

ronda, rondas = 0, 1000000

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

print("------------------------------------------------------------------------------")

while probabilidad_porcentual_false > 0.000001:
    probabilidad_de_acertar_falses.append(round((100 - probabilidad_porcentual_false), 4))
    probabilidad_porcentual_false *= probabilidad_false

print(f"LISTA PROBABILIDAD ACERTAR (repeticiones False):\n{probabilidad_de_acertar_falses}")
print(f"LONGITUD LISTA: {len(probabilidad_de_acertar_falses)}")

longitud_posiciones_true = len(probabilidad_de_acertar_trues)
longitud_posiciones_false = len(probabilidad_de_acertar_falses)

posiciones_true = [0] * longitud_posiciones_true
posiciones_false = [0] * longitud_posiciones_false


while ronda != rondas:
    ronda += 1

    resultado = random.choice(lista_opciones)

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


print("==============================================================================")

print(f"POSICIONES TRUE:\n{posiciones_true}")
print(f"POSICIONES FALSE:\n{posiciones_false}")
print("------------------------------------------------------------------------------")
print(f"CANTIDAD TRUE: {contar_trues}")
print(f"CANTIDAD FALSE: {contar_falses}")
print("------------------------------------------------------------------------------")
print(f"PROPORCIÓN MAX TRUE: {round(proporcion_max_true, 3)}")
print(f"PROPORCIÓN MIN TRUE: {round(proporcion_min_true, 3)}")
print("------------------------------------------------------------------------------")
print(f"PROPORCIÓN MAX FALSE: {round(proporcion_max_false, 3)}")
print(f"PROPORCIÓN MIN FALSE: {round(proporcion_min_false, 3)}")