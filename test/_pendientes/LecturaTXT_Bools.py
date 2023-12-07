########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

"""
    INFO:
    Se realiza una lectura del archivo de texto (~.txt) que contiene valores booleanos y los almacena en una lista.
"""

def leer_bools(nombre_archivo):

    valores = []  # Lista para almacenar los valores
    
    # Intentar abrir y leer el archivo
    try:
        # Incluir la carpeta "Registros" en la ruta del archivo
        ruta_completa = f"Registros/{nombre_archivo}"

        with open(ruta_completa, 'r') as archivo:
            # Leer cada línea del archivo
            for linea in archivo:
                # Convertir el valor a booleano y agregarlo a la lista
                valor = linea.strip().lower() == 'true'
                valores.append(valor)

    except FileNotFoundError:
        print(f"El archivo '{ruta_completa}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    return valores

""" EJEMPLO DE USO:
    
    RUTA [TXT] → .../Registros/valores.txt
        
        True
        True
        False
        False
        True
        False
        True
    
    RUTA [PY] → .../LecturaTXT [Bools].py
    
    nombre_txt = "valores.txt"
    resultados = leer_bools(nombre_txt)
    print(resultados)
    
    >>> [True, True, False, False, True, False, True]

"""
