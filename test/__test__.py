from random import choice

lista = [True, False]

saldo_inicial = 1000
saldos = saldo_inicial
multiplicador = 2

repeticion_true = 0
repeticion_false = 0

posiciones_false = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fallos_posicion_false = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista_perdidas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

repeticion_max_false = 0

rondas = 100000
ronda = 0
minimo = 0.3

apuesta = None
resultado = None
beneficios = None
perdidas = None

while rondas != ronda:
    ronda += 1

    if resultado is None:
        apuesta = 0.3

    else:

        if perdidas > 0:

            longitud_lista = len(fallos_posicion_false)
            repartir_perdidas = round((perdidas / longitud_lista), 2)

            for posicion in lista_perdidas:
                lista_perdidas.append(repartir_perdidas)
                repartir_perdidas *= 1.3

        else:

            beneficios


        if resultado is False:
            apuesta = 0.3



        else:
            apuesta = 0.3

    resultado = choice(lista)

    # --------------------------------------------------------------------

    if resultado is False:
        repeticion_false += 1
        fallos_posicion_false[repeticion_false - 1] += 1

    elif resultado is True:

        if repeticion_false != 0:

            posiciones_false[repeticion_false - 1] += 1
            fallos_posicion_false[repeticion_false - 1] -= 1

        repeticion_false = 0

    if repeticion_max_false < repeticion_false:
        repeticion_max_false = repeticion_false

    # --------------------------------------------------------------------

    saldos -= apuesta
    saldos = saldos + (apuesta * multiplicador) if resultado is True else saldos + 0

    beneficios = saldos - saldo_inicial
    perdidas = saldo_inicial - saldos



lista_invertida = []
for valor in reversed(posiciones_false):
    lista_invertida.append(valor)

print(saldos)
print(posiciones_false)
# print(lista_invertida)
print(fallos_posicion_false)

