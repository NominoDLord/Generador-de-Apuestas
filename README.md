```
##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####  
###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##
## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##
##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##
##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####  
```
---

# Generador de Apuestas

ESTADO: En desarrollo...

> ---
> *LICENSE:*
>
> Creative Commons Attribution-NonCommercial 4.0 International
> > Copyright (c) 2023 Nômino D Lord
>
> ---

### ***::: INFORMACIÓN :::***

*Automatización de apuestas en plataformas OnLine.*

Este programa está pensado para automatizar la acción de apostar en un juego dentro de una plataforma.

El programa toma como referencia unas capturas de imágenes que se realizarán en cada ronda para comprobar el
estado de la apuesta (si se ha acertado o fallado).

Para determinar si una apuesta ha sido acertada o no, se realiza una comparación con una captura que se tomará
como referencia con la captura de pantalla actual después de la realización de la apuesta.

A partir de esta comparación, la función para determinar si el resultado a sido acertado o no devolverá True o
False y lo enviará a la lista de resultados acumulados el cual un algoritmo calculará la diferencia entre
aciertos & fallos con el que a partir de esta comparación (con el de otras variables) determinará el valor
de la siguiente apuesta y lo ejecutará.

Los valores deben ajustarse dependiendo de la plataforma que se utilice, el tipo de juego y el tamaño de pantalla.

Dentro del archivo 'main.py' se especifica más detalladamente a qué hace referencia cada variable en cuestión y
cómo se deben manipular los datos.

---

### ***::: ESTRUCTURA :::***
```
Generador-de-Apuestas/
|
|-- .gitignore
|-- README.md
|
|-- src/
|   |-- main.py
|   |
|   |-- moduls/
|   |   |-- mApuestas.py  (*)
|   |
|   |-- utils/
|       |-- CoordenadasCursor.py
|       |-- CoordenadasCursor.pyw
|
|-- tests/
|   |-- tApuestas.py  (*)
|
|-- docs/
|   |-- README.md
|   |-- WorkFlow  (*)
|
|-- config/
|   |-- config.py (*)
|   |-- constants.py (*)
```
 \(*) (*Pendiente*).

---

### ***::: NORMAS DE USO :::***

El contenido que se encuentra en este repositorio esta sujeto a ciertas normas de uso:

```License
1º Se permite su uso a cualquier persona/entidad siempre y cuando se acredite su procedencia.
2º Se permite compartir, editar y adaptar el contenido según necesidades personales.
3º Bajo ninguna circunstancia el contenido pueden ser usado con fines comerciales.
```

Hacer un mal uso del contenido conllevará a acciones legales contra la persona o entidad responsable.

---

### ***::: CONTACTO :::***

> AUTOR: Nômino D Lord
> 
> E-MAIL: nominodlord@mailfence.com
> 
> DONAR: [PayPal](https://www.paypal.com/donate/?hosted_button_id=V7JFQBUUK5ZYA)
