########################################################################################################################
##                                                                                                                    ##
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
##                                                                                                                    ##
########################################################################################################################

# pip install Pillow

from PIL import Image
import hashlib

def comparar_imagenes(ruta1, ruta2, umbral=0.9) -> bool:
    """
    Compara dos imágenes para determinar su similitud.

    Args:
        ruta1 (str): Ruta de la primera imagen.
        ruta2 (str): Ruta de la segunda imagen.
        umbral (float): Umbral de similitud (valor predeterminado: 0.9).

    Returns:
        bool: True si las imágenes son suficientemente similares, False en caso contrario.
    """

    def generar_hash(ruta):
        """Calcula el hash MD5 de la imagen en el camino especificado."""
        with Image.open(ruta) as image:
            hash_value = hashlib.md5(image.tobytes()).hexdigest()
        return hash_value

    def comparativa():
        """Compara la similitud entre dos imágenes utilizando sus hashes."""
        hash1 = generar_hash(ruta1)
        hash2 = generar_hash(ruta2)

        similitud = sum(c1 == c2 for c1, c2 in zip(hash1, hash2)) / len(hash1)
        return similitud

    similitud_score = comparativa()

    iguales = similitud_score > umbral
    return iguales
