```
##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####  
###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##
## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##
##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##
##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####  
```

# ESTRATEGIAS

Información sobre el tipo de estrategias.


## Estrategia 00

```

```


## Estrategia 01

Estrategia base que consiste simplemente en realizar siempre la misma apuesta con el mismo valor.


## Estrategia 02

La apuesta se incrementa en cada repetición de fallo en relación al total de perdidas anteriores.

| RONDAS     | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      |
|------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| APUESTA    | 0.3    | 0.9    | 2.7    | 8.1    | 24.3   | 72.9   | 218.7  | 656.1  | 1968.3 |
| RESULTADO  | False  | False  | False  | False  | False  | False  | False  | False  | False  |


## Estrategia 03

La apuesta se realiza en base a la proporción entre los aciertos y los fallos:
- Se establece una apuesta base para las veces en el que la proporción es igual.
- Se establece una apuesta superior a la apuesta base cuando la proporción es negativa.
- Se establece una apuesta inferior a la apuesta base cuando la proporción es negativa.


## Estrategia 04

Se especifica una apuesta en base al número de repeticiones fallidas.


## Estrategia 05

El resultado de la apuesta se limita a la proporción de los últimos 100 resultados.

- Hasta generar los primeros 100 resultados, la apuesta es siempre la misma (se establece un valor base).

- Una vez generados los 100 resultados:

  - Si el porcentaje de aciertos es igual, la apuesta es el valor base.
  - Si el porcentaje de aciertos es superior, la apuesta es un valor inferior al valor base.
  - Si el porcentaje de aciertos es inferior, la apuesta es un valor superior al valor base.


## Estrategia 06

El resultado de la apuesta se limita a la proporción de los últimos 100 resultados.

- Hasta generar los primeros 100 resultados, la apuesta es la mínima.

- Una vez generados los 100 resultados:

  - Cuanto mayor sea la proporción de fallos, la apuesta se incrementará.


## Estrategia 07



## Estrategia 08



## Estrategia 09


