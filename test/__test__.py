# import markdown
#
# texto_markdown = """
# # Título
# Párrafo con **negrita**.
# Párrafo con *cursiva*.
# ## Título de Lista
# - Lista 1
# - Lista 2
# - Lista 3
# """
# convertir_a_html = markdown.markdown(texto_markdown)
# print(convertir_a_html)

if saldos < saldo_objetivo:

    diferencia_saldos = saldo_objetivo - saldos
    apuesta_base = APUESTA_MINIMA
    lista_partes = []
    suma = 0

    while diferencia_saldos > suma:

        lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 0))
        lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 1))
        lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 2))
        lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 3))
        lista_partes.append(apuesta_base * (OPCIONES_TRUE ** 4))

        suma = sum(lista_partes)

        if diferencia_saldos < suma:
            apuesta_base += 0.1
            lista_partes = []