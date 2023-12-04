########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

# pip install pyautogui
# pip3 install pyautogui

from typing import Tuple, Any

import pyautogui
from time import sleep

"""
    INFO:
    Para el uso de este módulo se deberá tener instalada la biblioteca externa 'pyautogui'.
    En este módulo se han creado acciones específicas para las funciones de pulsación y movimiento del ratón.

    NOTA:
    Las coordenadas [x, y] = [0, 0] pertenecen a la posición superior-izquierda de la pantalla.
    
"""

def recibir_posicion_cursor() -> Tuple[Any, Any]:
    """
    Devuelve las coordenadas X/Y del cursor en el momento de su ejecución.
    Esta función es útil para obtener la posición de un elemento en concreto situando el ratón encima de él.
    """
    coordenada_x, coordenada_y = pyautogui.position()
    return coordenada_x, coordenada_y

# x, y = recibir_posicion_cursor()
# print(f"Coordenada 'X' = {x}\nCoordenada 'Y' = {y}")

def definir_posicion_cursor(pos_x: int, pos_y: int) -> None:
    """
    Posiciona el cursor sobre la coordenada especifiada sin realizar un desplazamiento.

    @param pos_x: Coordenada X a la que se moverá el cursor.
    @param pos_y: Coordenada Y a la que se moverá el cursor.
    """
    pyautogui.moveTo(pos_x, pos_y)
    pass

# definir_posicion_cursor(1150, 850)

def pulsar_boton_izquierdo(pulsar=1) -> None:
    """
    @param pulsar: Número de veces que se pulsará el botón de forma consecutiva.
    """
    while pulsar > 0:
        pyautogui.click()
        pulsar -= 1
    pass

# pulsar_boton_izquierdo()
# pulsar_boton_izquierdo(2)


def pulsar_boton_derecho(pulsar=1) -> None:
    """
    @param pulsar: Número de veces que se pulsará el botón de forma consecutiva.
    """
    while pulsar > 0:
        pyautogui.rightClick()
        pulsar -= 1
    pass

# pulsar_boton_derecho()

def pulsar_boton_central(pulsar=1) -> None:
    """
    @param pulsar: Número de veces que se pulsará el botón de forma consecutiva.
    """
    while pulsar > 0:
        pyautogui.middleClick()
        pulsar -= 1
    pass

# pulsar_boton_central()

def mantener_boton_izquierdo(pos_ini_x, pos_ini_y, seg=0, pos_fin_x=None, pos_fin_y=None) -> None:
    """
    Mantiene pulsado el botón izquierdo del ratón.
    Si no se especifican los argumentos X/Y finales, la pulsación se mantendrá en su posición inicial.
    Al especificar los argumentos X o Y finales, la pulsación del ratón se mantendrá y se moverá seleccionando así
    los elementos existentes entre su podición inicial y su posición final.

    @param pos_ini_x: Posición de Coordenada X Inicial.
    @param pos_ini_y: Posición de Coordenada Y Inicial.
    @param seg: Segundos de pulsado.
    @param pos_fin_x: (Opcional) Posición de Coordenada X Final.
    @param pos_fin_y: (Opcional) Posición de Coordenada Y Final.
    """
    pyautogui.mouseDown(pos_ini_x, pos_ini_y)

    if pos_fin_x is None and pos_fin_y is None:
        sleep(seg)
        pyautogui.mouseUp()
    else:
        sleep(seg)
        pyautogui.moveTo(pos_fin_x, pos_fin_y)
        pyautogui.mouseUp()

    pass

# mantener_boton_izquierdo(1200, 400)
# mantener_boton_izquierdo(1200, 400, 3)
# mantener_boton_izquierdo(1200, 400, 1, 1400, 500)
# mantener_boton_izquierdo(1200, 400, 1, pos_fin_y=500)
