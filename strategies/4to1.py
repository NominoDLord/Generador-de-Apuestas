from random import choice
from math import floor

import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(subDir1)

from config.setup import SALDO_INICIAL, APUESTA_MINIMA, APUESTA_MAXIMA

from moduls.generadorDeRonda import generar_ronda
from moduls.generadorDeProbabilidad import crear_lista_probabilidad, crear_lista_probabilidad_inversa

OP_T, OP_F = 4, 1

lista_opciones = ([True] * OP_T) + ([False] * OP_F)

porcentaje_true = (OP_T / (OP_T + OP_F)) * 100
porcentaje_false = (OP_F / (OP_T + OP_F)) * 100

MULTI_LVL1 = 1.23
MULTI_LVL2 = 1.54
MULTI_LVL3 = 1.93
MULTI_LVL4 = 2.41
MULTI_LVL5 = 4.02

lista_probabilidad_posiciones_true = crear_lista_probabilidad(porcentaje_true)
lista_probabilidad_posiciones_false_inv = crear_lista_probabilidad_inversa(porcentaje_false)

# lista_probabilidad_posiciones_true

# 80.0000, 64.0000, 51.2000, 40.9600, 32.7680, 26.2144, 20.9715, 16.7772, 13.4218, 10.7374,  8.5899,  6.8719,
#  5.4976,  4.3980,  3.5184,  2.8147,  2.2518,  1.8014,  1.4412,  1.1529,  0.9223,  0.7379,  0.5903,  0.4722,
#  0.3778,  0.3022,  0.2418,  0.1934,  0.1547,  0.1238,  0.0990,  0.0792,  0.0634,  0.0507,  0.0406,  0.0325,
#  0.0260,  0.0208,  0.0166,  0.0133,  0.0106,  0.0085,  0.0068,  0.0054,  0.0044,  0.0035,  0.0028,  0.0022,
#  0.0018,  0.0014,  0.0011,  0.0009,  0.0007,  0.0006,  0.0005,  0.0004,  0.0003,  0.0002,  0.0002,  0.0002,
#  0.0001,  0.0001,  0.0001,  0.0001,  0.0001,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,
#  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000

# lista_probabilidad_posiciones_false_inv

# 80.0000, 96.0000, 99.2000, 99.8400, 99.9680, 99.9936, 99.9987, 99.9997, 99.9999, 100.000, 100.000

contar_posiciones_con_probabilidad_superior_a_20 = 0
for probabilidad in lista_probabilidad_posiciones_true:
    if probabilidad > porcentaje_false:
        contar_posiciones_con_probabilidad_superior_a_20 += 1

print(lista_probabilidad_posiciones_true)
print(lista_probabilidad_posiciones_false_inv)

registro_posiciones_true = [0] * len(lista_probabilidad_posiciones_true)
registro_posiciones_false = [0] * len(lista_probabilidad_posiciones_false_inv)

distribucion_fallos_en_lista_true = [0] * len(lista_probabilidad_posiciones_true)
distribucion_fallos_en_lista_false = [0] * len(lista_probabilidad_posiciones_false_inv)

distribucion_fallos_en_lista_true_cuando_saldo_positivo = [0] * len(lista_probabilidad_posiciones_true)
distribucion_fallos_en_lista_false_cuando_saldo_positivo = [0] * len(lista_probabilidad_posiciones_false_inv)

distribucion_fallos_en_lista_true_cuando_saldo_negativo = [0] * len(lista_probabilidad_posiciones_true)
distribucion_fallos_en_lista_false_cuando_saldo_negativo = [0] * len(lista_probabilidad_posiciones_false_inv)


cnt_t, cnt_f = 0, 0
pos_t, pos_f = 0, 0

saldo_actual = SALDO_INICIAL
saldo_objetivo = SALDO_INICIAL + 1
apuesta = 0
beneficio = 0


ronda = 0
resultado = None

perdidas_en_posiciones_1y2 = 0
perdidas_en_posiciones_super_5 = 0

while ronda != 100000:

    ronda = generar_ronda()

    if resultado is None:
        apuesta = APUESTA_MINIMA

    else:  # ESTRATEGIAS: El resultado es generado en la anterior ronda.

        # SALDO POSITIVO ·········································································

        if SALDO_INICIAL < saldo_actual:

            if resultado is True:
                probabilidad = lista_probabilidad_posiciones_true[pos_t -1]
                porcentaje = 1 + (probabilidad / 100)
                apuesta = OP_T * (perdidas_en_posiciones_1y2 / (len(lista_probabilidad_posiciones_true) / 2)) * porcentaje


            if resultado is False:
                probabilidad = lista_probabilidad_posiciones_false_inv[pos_f -1]
                porcentaje = 1 + (probabilidad / 100)

                if pos_f == 1:
                    apuesta = APUESTA_MINIMA * porcentaje
                elif pos_f == 2:
                    apuesta = APUESTA_MINIMA * porcentaje
                else:
                    apuesta = distribucion_fallos_en_lista_false[pos_f - 1] * 4

        # SALDO NEGATIVO ·········································································

        else:

            diferencia = SALDO_INICIAL - saldo_actual

            if resultado is True:
                probabilidad = lista_probabilidad_posiciones_true[pos_t -1]
                porcentaje = 1 + (probabilidad / 100)
                apuesta = diferencia * porcentaje * OP_T

            if resultado is False:

                if pos_f == 1:
                    apuesta = APUESTA_MINIMA

                elif pos_f == 2:
                    apuesta = APUESTA_MINIMA * 2

                elif pos_f == 2:
                    apuesta = diferencia * 4

                    if apuesta > APUESTA_MAXIMA / 2:
                        while apuesta > APUESTA_MAXIMA / 2:
                            apuesta *= 0.8

                else:
                    apuesta = APUESTA_MINIMA * pos_f * OP_T


    apuesta = round(apuesta, 2)

    # GENERAR RESULTADOS =============================================================================== #

    resultado = choice(lista_opciones)

    # ACTUALIZAR SALDO ================================================================================= #

    if resultado is True:

        obtener = apuesta * MULTI_LVL1
        redondear = floor(obtener * 100) / 100
        beneficio = redondear - apuesta

    if resultado is False:

        beneficio = -apuesta

    saldo_actual += beneficio

    saldo_actual = round(saldo_actual, 2)
    print(saldo_actual)


    # REGISTRAR DATOS ================================================================================== #

    if resultado is True:
        pos_t += 1

        if pos_f != 0:
            if 1 <= pos_f <= 2:
                perdidas_en_posiciones_1y2 -= beneficio
            if 3 <= pos_f <= 5:
                distribucion_fallos_en_lista_false[pos_f -1] -= beneficio
            if 5 < pos_f:
                perdidas_en_posiciones_super_5 -= beneficio

            pos_f = 0  # ¡IMPORTANTE! No cambiar de lugar esta acción.

        else:
            perdidas_en_posiciones_1y2 -= beneficio




    if resultado is False:
        pos_f += 1
        pos_t = 0

        distribucion_fallos_en_lista_false[pos_f -1] += apuesta

        perdidas_en_posiciones_1y2 += distribucion_fallos_en_lista_false[0] + distribucion_fallos_en_lista_false[1]
        distribucion_fallos_en_lista_false[0] = 0
        distribucion_fallos_en_lista_false[1] = 0

        i = -1
        for perdidas in distribucion_fallos_en_lista_false:
            i += 1
            if i > 5:
                perdidas_en_posiciones_super_5 += distribucion_fallos_en_lista_false[i]
                distribucion_fallos_en_lista_false[i] = 0



    if perdidas_en_posiciones_1y2 < 0:
        perdidas_en_posiciones_1y2 = 0

    if perdidas_en_posiciones_super_5 < 0:
        perdidas_en_posiciones_super_5 = 0

    i = -1
    for perdidas in distribucion_fallos_en_lista_false:
        i += 1
        if perdidas < 0:
            distribucion_fallos_en_lista_false[i] = 0



    i = -1
    mover_perdidas = 0
    for perdidas in distribucion_fallos_en_lista_false:
        i += 1

        if i == 2 and perdidas > 18:  # 2nd Repetición & 3rd Posición
            mover_perdidas += distribucion_fallos_en_lista_false[i] / 2
            distribucion_fallos_en_lista_false[i] /= 2
        elif i == 3 and perdidas > 18:
            mover_perdidas += distribucion_fallos_en_lista_false[i] / 2
            distribucion_fallos_en_lista_false[i] /= 2
        elif i == 4 and perdidas > 18:
            mover_perdidas += distribucion_fallos_en_lista_false[i] / 2
            distribucion_fallos_en_lista_false[i] /= 2

        elif i == 5 and mover_perdidas > 0:
            distribucion_fallos_en_lista_false[i] += mover_perdidas

        if i == 5:
            mover_perdidas = 0

        if i == 5 and distribucion_fallos_en_lista_false[i] > 18:

            mover_perdidas = distribucion_fallos_en_lista_false[i] - 18
            distribucion_fallos_en_lista_false[i] = 18

        if mover_perdidas > 0:

            if perdidas_en_posiciones_super_5 > 0:
                mover_perdidas += perdidas_en_posiciones_super_5
                perdidas_en_posiciones_super_5 = 0

            if i == 6:
                distribucion_fallos_en_lista_false[i] += mover_perdidas / 3
            elif i == 7:
                distribucion_fallos_en_lista_false[i] += mover_perdidas / 3
            elif i == 8:
                distribucion_fallos_en_lista_false[i] += mover_perdidas / 3

        if i == 9:
            mover_perdidas = 0




    # CONDICIONES DE SALIDA ============================================================================ #

    if saldo_actual > (SALDO_INICIAL + 100):
        break

    if saldo_actual < (SALDO_INICIAL - 300):
        break

    if apuesta > APUESTA_MAXIMA:
        break

# -------------------------------------------------------------------------------------------------------------------- #


print(f"\nSALDO FINAL: {saldo_actual}")



#
