########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

# pip install Pillow

from PIL import Image
import hashlib

def comparar(img_referencia, img_capturada, umbral=0.9) -> bool:
    """
    Compara dos imágenes para determinar su similitud.

    Args:
        img_referencia (str): Ruta de la primera imagen.
        img_capturada (str): Ruta de la segunda imagen.
        umbral (float): Umbral de similitud (valor predeterminado: 0.9).

    Returns:
        bool: True → Iguales / False → No iguales.
    """

    def generar_hash(ruta):
        """Calcula el hash MD5 de la imagen en el camino especificado."""
        with Image.open(ruta) as image:
            """
            La función hashlib.md5() crea un objeto hash MD5, y image.tobytes() convierte la imagen en una
            secuencia de bytes. Luego, hexdigest() se utiliza para obtener la representación hexadecimal del hash.
            """
            hash_value = hashlib.md5(image.tobytes()).hexdigest()
        return hash_value

    def comparativa():
        """Compara la similitud entre dos imágenes utilizando sus hashes."""
        hash1 = generar_hash(img_referencia)
        hash2 = generar_hash(img_capturada)

        similitud = sum(c1 == c2 for c1, c2 in zip(hash1, hash2)) / len(hash1)
        return similitud

    similitud_score = comparativa()

    iguales = similitud_score > umbral
    
    return iguales