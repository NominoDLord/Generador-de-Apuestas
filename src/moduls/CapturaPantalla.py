########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

from PIL import ImageGrab

def captura(nombre, ruta, pos_x=0, pos_y=0, ancho=1920, alto=1080):
    """
    Este código realiza una captura de pantalla sobre una región específica de la pantalla.
    Si no se definen las coordenadas y dimensiones de la región se utilizarán los valores pre-definidos.

    Al llamar a la función, deben establecerse el nombre de la imagen a capturar y la ruta dónde se desea guardar.

        NOTA: La posición [x|y] = [0|0] corresponde al punto superior-izquierdo de la pantalla.
              Los valores [ancho|alto] corresponden a la distancia en píxeles sobre el punto [x|y].
        
        IMPORTANTE: Cada vez que se realice una captura, la primera será reemplazada por la segunda.

    @param nombre: Nombre de la imagen a capturar.
    @param ruta: Dirección dónde se guardará la imagen capturada.
    @param pos_x: Posición en el eje X.
    @param pos_y: Posición en el eje Y.
    @param ancho: Establece la lóngitud del ancho partiendo de la posición x_y.
    @param alto: Establece la lóngitud de la altura partiendo de la posición x_y.
    """
    def capturar_pantalla():
        imagen = ImageGrab.grab(bbox=(pos_x, pos_y, pos_x + ancho, pos_y + alto))
        return imagen

    def guardar_imagen(imagen, nombre_archivo):
        imagen.save(nombre_archivo)

    imagen_capturada = capturar_pantalla()
    guardar = f"{ruta}{nombre}.png"
    guardar_imagen(imagen_capturada, guardar)