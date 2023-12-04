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
Este programa consta de una sencilla interfaz la cual contiene un botón que al presionarlo, espera 3 segundos y
imprime la posición en la que se encuentre el cursor al acabar la cuenta atras.

Este programa se ha creado para obtener las coordenadas específicas de la posición del cursos, las cuales, podremos
usar para definir las variables que usará el programa `main.py` para establecer las posiciones donde el cursor deberá
de realizar las acciones.

La posición del cursor se tomará 3 segundos después de pulsar el botón "Obtener coordenadas" y  su información
se mostrará dentro de la ventana del programa.
"""

# pip install pyautogui
# pip3 install pyautogui

import tkinter as tk
from typing import Tuple, Any
import pyautogui
from time import sleep


def recibir_posicion_cursor() -> Tuple[int, int]:
    coordenada_x, coordenada_y = pyautogui.position()
    return coordenada_x, coordenada_y


def obtener_coordenadas_con_retraso():
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Obtener Coordenadas")

    # Establecer el tamaño de la ventana
    ventana.geometry("300x100")

    # Etiqueta para mostrar el contador
    etiqueta_contador = tk.Label(ventana, text="")
    etiqueta_contador.pack(side=tk.TOP, pady=5)
    def iniciar_contador():
        for i in range(3, 0, -1):
            etiqueta_contador.config(text=f"{i}...")
            ventana.update()
            sleep(1)
        coord_x, coord_y = recibir_posicion_cursor()
        x, y = str(coord_x), str(coord_y)

        etiqueta_contador.config(text="¡Coordenadas obtenidas!")
        etiqueta_coordenadas.config(text=f"x = {x}, y = {y}")

    # Botón para obtener coordenadas
    boton_obtener_coordenadas = tk.Button(ventana, text="Obtener coordenadas", command=iniciar_contador)
    boton_obtener_coordenadas.pack(side=tk.TOP, pady=5)

    # Etiqueta para mostrar las coordenadas
    etiqueta_coordenadas = tk.Label(ventana, text="")
    etiqueta_coordenadas.pack(side=tk.TOP, pady=5)

    # Ejecutar la aplicación
    ventana.mainloop()

# Llamar a la función para iniciar la interfaz
obtener_coordenadas_con_retraso()
