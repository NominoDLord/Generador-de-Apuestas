# probabilidad_de_acertar_falses = [98.7, 98.8, 98.9, 99.0, 99.1, 99.2, 99.3, 99.4]
# posiciones_perdidas = [0] * len(probabilidad_de_acertar_falses)
#
# cantidad = 0
# for probabilidad in probabilidad_de_acertar_falses:
#     if probabilidad > 99:
#         cantidad += 1
#
# cantidad_probabilidad_superior_99 = cantidad
#
# suma_perdidas_posiciones_99 = 12
#
# if suma_perdidas_posiciones_99 > 0:
#     repartir_perdidas_false = suma_perdidas_posiciones_99 / cantidad_probabilidad_superior_99
#
#     i = 0
#     for valor in posiciones_perdidas:
#         if probabilidad_de_acertar_falses[i] > 99:
#             posiciones_perdidas[i] = repartir_perdidas_false
#         i += 1
#
# print(posiciones_perdidas)


num1 = 0
while num1 < 10:

    num1 += 1
    num2 = 0

    print("1r bucle")

    while True:

        num2 += 1
        print("2n bucle")
        if num2 < 5:
            break