########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

""" Bool-To-Int
INFO:
Se realiza una lectura del archivo de texto (~.txt) que contiene valores booleanos y a partir de este se genera
otro archivo de texto en el que los valores True se convierten en un valor '1' y los valores False en valor '0'.

NOTA:
Los valores quedan separados por una tabulación.
Cada 100 valores registrados, se realiza un salto de línea y se continúa el proceso.

¡CUIDADO!
Si el archivo ya existe, este programa lo re-escrivirá eliminando los datos del archivo anterior.
"""

def convertir_booleanos_a_numeros(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f_entrada, open(archivo_salida, 'w') as f_salida:
        for i, linea in enumerate(f_entrada, 1):
            # Convertir "True" a 1 y "False" a 0
            valor_numerico = int(linea.strip() == 'True')

            # Escribir el valor numerico seguido de una tabulación
            f_salida.write(f"{valor_numerico}\t")

            # Agregar un salto de línea después de cada X valores
            if i % 20 == 0:  # Modificar este valor para conseguir el salto de línea cada X valores
                f_salida.write("\n")

archivo_original = input("Nombre del archivo de origen: ")
archivo_generado = input("Nombre del archivo de salida: ")

convertir_booleanos_a_numeros(f"{archivo_original}.txt",  # Total[75-25]
                              f"{archivo_generado}.txt")  # int_bools[100]
