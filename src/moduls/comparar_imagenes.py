########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

# pip3 install opencv-python

import cv2
from pathlib import Path

def comparar(ruta_img_referencia, ruta_img_capturada, umbral=0.9) -> bool:
    """
    Compara la similitud entre dos imágenes utilizando OpenCV.

    @param ruta_img_referencia: Ruta de la imagen de referencia.
    @param ruta_img_capturada: Ruta de la imagen capturada para comparar.
    @param umbral: Umbral de similitud. Por defecto, 0.9 (90% de similitud).
    @return: True si las imágenes son suficientemente similares, False en caso contrario.
    """
    img_referencia = cv2.imread(str(ruta_img_referencia), cv2.IMREAD_GRAYSCALE)
    img_capturada = cv2.imread(str(ruta_img_capturada), cv2.IMREAD_GRAYSCALE)

    result = cv2.matchTemplate(img_referencia, img_capturada, cv2.TM_CCOEFF_NORMED)
    _, score, _, _ = cv2.minMaxLoc(result)

    return score > umbral