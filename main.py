########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

# GENERADOR DE APUESTAS

# ======================================= [ BIBLIOTECAS, MÓDULOS y VARIABLES ] ======================================= #

from typing import List, Tuple
from contabilizar_repeticiones import contar_resultados
from probabilidades_por_ronda import lista_probabilidad

RONDA = 0
global lst_var_true, lst_var_false
global lista_resultados

# ==================================================== [ CLASES ] ==================================================== #

class VariablesFijas:

    def __init__(self, saldo_inicial=300, apuesta_min=0.3, apuesta_max=100, op_positivas=3, op_negativas=1,
                 multi_pos=1.32, multi_neg=0, riesgo_lim_pos=0.03, riesgo_lim_neg=0.01) -> None:
        """Variables de inicialización necesarias para realizar los cálculos"""

        self.saldo_inicial = saldo_inicial
        self.apuesta_min = apuesta_min
        self.apuesta_max = apuesta_max
        self.op_positivas = op_positivas
        self.op_negativas = op_negativas
        self.multi_pos = multi_pos
        self.multi_neg = multi_neg
        self.riesgo_lim_pos = riesgo_lim_pos
        self.riesgo_lim_neg = riesgo_lim_neg

        self.total_num_opciones = op_positivas + op_negativas
        self.porcentaje_base_pos = (op_positivas / self.total_num_opciones) * 100
        self.porcentaje_base_neg = (op_negativas / self.total_num_opciones) * 100

# =================================================== [ FUNCIONES ] ================================================== #
def contar_rondas():
    global RONDA
    RONDA += 1
    return RONDA

def listas_variables_base_100(resultado) -> tuple[list[bool], list[bool]]:
    """
    Se crean dos listas bases para los valores True y False respecto a su diferencia porcentual.
    Se usa la función round para redondear a un número entero para poder crear las listas.
    Estas listas se usarán como referencia inicial ya que la lista de generación de resultados inicial estará vacía.
    A medida que se vayan introduciendo los resultados a la lista general, estas listas se irán vaciando.
    """
    global lst_var_true, lst_var_false
    # Definir la lista inicial base -------------------------------------------------------------------------------
    if not hasattr(listas_variables_base_100, "definir_base"):
        """Este bloque impedirá que la lista se regenere para así poder ir actualizando los datos"""
        lst_var_true = round(PORCENTAJE_BASE_POS) * [True]
        lst_var_false = round(PORCENTAJE_BASE_NEG) * [False]
    listas_variables_base_100.definir_base = True
    # -------------------------------------------------------------------------------------------------------------
    if len(lst_var_true) > 0 and resultado == True:
        lst_var_true.pop()

    elif len(lst_var_false) > 0 and resultado == False:
        lst_var_false.pop()

    return lst_var_true, lst_var_false

def generar_lista(resultado):
    global lista_resultados
    # Crear lista inicial -----------------------------------------------------------------------------------------
    if not hasattr(generar_lista, "lista_creada"):
        """Este bloque impedirá que la lista se regenere para así poder ir actualizando los datos"""
        lista_resultados = []
    generar_lista.lista_creada = True
    # -------------------------------------------------------------------------------------------------------------
    lista_resultados.insert(0, resultado)
    return lista_resultados

def imprimir_datos_definidos():
    print(f"Saldo inicial: {SALDO_INICIAL}")
    print(f"Apuesta mínima: {APUESTA_MIN}")
    print(f"Apuesta máxima: {APUESTA_MAX}")
    print(f"Número de aciertos: {OPCIONES_ACIERTOS}")
    print(f"Número de fallos: {OPCIONES_FALLOS}")
    print(f"Número de opciones: {CANTIDAD_OPCIONES}")
    print(f"Porcentaje base positivo: {PORCENTAJE_BASE_POS}")
    print(f"Porcentaje base negativo: {PORCENTAJE_BASE_NEG}")
    print(f"Multiplicador positivo: {MULTI_POSITIVO}")
    print(f"Multiplicador negativo: {MULTI_NEGATIVO}")
    print(f"Riesgo límite positivo: {RIESGO_LIM_POSITIVO}")
    print(f"Riesgo límite negativo: {RIESGO_LIM_NEGATIVO}")
    pass

# =================================================== [ EJECUCIÓN ] ================================================== #

# Se definen las variables fijas.
""" ··········································································································· TODO ···
# _sld = float(input("Introducir cantidad de saldo inicial: "))
# _min = float(input("Introducir cantidad de apuesta mínima: "))
# _max = float(input("Introducir cantidad de apuesta máxima: "))
# _opp = float(input("Introducir cantidad de opciones positivas: "))
# _opn = float(input("Introducir cantidad de opciones negativas: "))
# _mps = float(input("Introducir multiplcador positivo: "))
# _mpn = float(input("Introducir multiplcador negativo: "))
# _rlp = float(input("Introducir el riesgo límite positivo: "))
# _rln = float(input("Introducir el riesgo límite negativo: "))

# instancia_var = VariablesFijas(_sld, _min, _max, _opp, _opn, _mps, _mpn, _rlp, _rln)
···················································································································· """
# Se crea la instancia para las variables fijas.
variables_fijas = VariablesFijas()

SALDO_INICIAL = variables_fijas.saldo_inicial
APUESTA_MIN = variables_fijas.apuesta_min
APUESTA_MAX = variables_fijas.apuesta_max
OPCIONES_ACIERTOS = variables_fijas.op_positivas
OPCIONES_FALLOS = variables_fijas.op_negativas
MULTI_POSITIVO = variables_fijas.multi_pos
MULTI_NEGATIVO = variables_fijas.multi_neg
RIESGO_LIM_POSITIVO = variables_fijas.riesgo_lim_pos
RIESGO_LIM_NEGATIVO = variables_fijas.riesgo_lim_neg

CANTIDAD_OPCIONES = variables_fijas.total_num_opciones
PORCENTAJE_BASE_POS = variables_fijas.porcentaje_base_pos
PORCENTAJE_BASE_NEG = variables_fijas.porcentaje_base_neg

list_aciertos, list_fallos = lista_probabilidad(OPCIONES_ACIERTOS, OPCIONES_FALLOS)  # lista_aciertos, lista_fallos
PROBABILIDAD_BASE_ACIERTOS = list_aciertos
long_pba = len(PROBABILIDAD_BASE_ACIERTOS)
PROBABILIDAD_BASE_FALLOS = list_fallos
long_pbf = len(PROBABILIDAD_BASE_FALLOS)


"""··················································································································"""
imprimir_datos_definidos()
"""··················································································································"""

def realizar_calculos(resultado):
    contar_rondas()  # RONDA
    listas_variables_base_100(resultado)  # lst_var_true, lst_var_false
    generar_lista(resultado)  # lista_resultados

    contar_resultados(lista_resultados, long_pba, long_pbf)  # lista_aciertos, lista_fallos

    pass

realizar_calculos(True)
realizar_calculos(True)
realizar_calculos(False)

# ================================================= [ CONSTRUCCIÓN ] ================================================= #

# Estructuración -------------------------------------------------------------------------------------------------------

"""
1º GENERAR LAS VARIABLES FIJAS:

   - Saldo inicial                       ::: Define un saldo inicial
   
   - Cantidad de opciones (T)            ::: Define la cantidad de posibles opciones a acertar
   - Cantidad de opciones (F)            ::: Define la cantidad de posibles opciones a fallar
   
   - Apuesta (Mínima)                    ::: Define la apuesta mínima del juego
   - Apuesta (Máxima)                    ::: Define la apuesta máxima del juego
   
   - Multiplicador (True)                ::: Múltiplica el valor de la apuesta en caso de acertar
   - Multiplicador (False)               ::: Múltiplica el valor de la apuesta en caso de fallar
   
   - Riesgo límite (Aciertos)            ::: Limita el número de repeticiones en caso de acertar
   - Riesgo límite (Fallos)              ::: Limita el número de repeticiones en caso de fallar
   
2º CALCULAR VALORES INICIALES:

   - Generar lista apuestas              ::: Define el valor de las apuestas
   - Opciones totales                    ::: Se suman las opciones de acertar y fallar
   
   - Probabilidad Base (T)               ::: Se calcula la probabilidad de acertar (ronda individual)
   - Probabilidad Base (F)               ::: Se calcula la probabilidad de fallar (ronda individual)
   
   - Probabilidad repetición (T)         ::: Se calcula probabilidad de acertar (ronda repetida)
   - Probabilidad repetición (F)         ::: Se calcula probabilidad de fallar (ronda repetida)
   
   - Lista (T)                           ::: Se contabilizan las opciones a acertar × 100
   - Lista (F)                           ::: Se contabilizan las opciones a fallar × 100

3º DEFINIR LA ENTRADA DE DATOS

   - Agregar datos a lista (ttl)         ::: Se agregan los datos a la lista Datos_Totales
   - Agregar datos a lista (100)         ::: Se agregan los datos a la lista Datos_x100
   
   - Eliminar datos de listas            ::: Se suprime dato según valor en lista aciertos o fallos
    
4º CONTABILIZAR DATOS RECIBIDOS

   - Contabilizar repeticiones (T-ttl)   ::: Recuento repeticiones acertadas (rondas totales)
   - Contabilizar repeticiones (F-ttl)   ::: Recuento repeticiones falladas (rondas totales)
   - Contabilizar repeticiones (T-100)   ::: Recuento repeticiones acertadas (rondas × 100)
   - Contabilizar repeticiones (F-100)   ::: Recuento repeticiones falladas (rondas × 100)
   
   - Contabilizar resultados (T-ttl)     ::: Recuento aciertos (rondas totales)
   - Contabilizar resultados (F-ttl)     ::: Recuento fallos (rondas totales)
   - Contabilizar resultados (T-100)     ::: Recuento aciertos (rondas × 100)
   - Contabilizar resultados (F-100)     ::: Recuento fallos (rondas × 100)

5º PROPORCIÓN DATOS CONTABILIZADOS

   - Proporción repeticiones (T-ttl)     ::: Proporción entre repeticiones acertadas (rondas totales) 
   - Proporción repeticiones (F-ttl)     ::: Proporción entre repeticiones falladas (rondas totales)
   - Proporción repeticiones (T-100)     ::: Proporción entre repeticiones acertadas (rondas × 100)
   - Proporción repeticiones (F-100)     ::: Proporción entre repeticiones falladas (rondas × 100)

   - Proporción resultados (T-ttl)       ::: Se calcula la proporción de aciertos (rondas totales)
   - Proporción resultados (F-ttl)       ::: Se calcula la proporción de fallos (rondas totales)
   - Proporción resultados (T-100)       ::: Se calcula la proporción de aciertos (rondas × 100)
   - Proporción resultados (F-100)       ::: Se calcula la proporción de fallos (rondas × 100)

6º COMPARAR DATOS

   - Repeticiones (T-ttl)                ::: Diferencia proporción repetición y lista de probabilidad
   - Repeticiones (F-ttl)                ::: Diferencia proporción repetición y lista de probabilidad
   - Repeticiones (T-100)                ::: Diferencia proporción repetición y lista de probabilidad
   - Repeticiones (F-100)                ::: Diferencia proporción repetición y lista de probabilidad

   - Probabilidad (T-ttl)                ::: Diferencia proporción resultados y probabilidad Base
   - Probabilidad (F-ttl)                ::: Diferencia proporción resultados y probabilidad Base
   - Probabilidad (T-100)                ::: Diferencia proporción resultados y probabilidad Base
   - Probabilidad (F-100)                ::: Diferencia proporción resultados y probabilidad Base

7º DEFINR VALOR DE LA APUESTA

   - Recoger los datos comparados
   - Establecer el valor de la apuesta

"""

# Check List -----------------------------------------------------------------------------------------------------------

# X → Completado || R → Revisar || P → En proceso

# TODO [ ] > Imports    →  Tkinter (Interfaz gráfica)

# TODO [X] > Classes    →  VARIABLES FIJAS (Introducción de los valores)
#                       →  [Saldo inicial]
#                       →  [Apuesta mínima, Apuesta máxima]
#                       →  [Opciones opsitivas, Opciones negativas]
#                       →  [Multiplicador positivo, Multiplicador negativo]
#                       →  [Riesgo límite positivo, Riesgo límite negativo]

# TODO [ ] > Función    →  VALORES BASE (Calcular a partir de variables fijas)
#                       →  [(True/Total)×100, (False/Total)×100]
#                       →  [True % Repeticiones, False % Repeticiones]
#                       →  [Calcular Ronda de apuestas]

# TODO [ ] > Función    →  generar_lista
# TODO [ ] > Módulos    →
# TODO [ ] > Módulos    →
# TODO [ ] > Módulos    →
# TODO [ ] > Módulos    →  Comparativa [Valores Base × Resutados]

# TODO [ ] > Módulos    →  Contabilizar Repeticiones

# TODO [ ] > Módulos    →  Capturar pantalla



# TODO [ ] > Módulos    →  Pruebas

#                       →  [Lista de opciones]
#                       →  [Generar random]
#

# Work Flow ------------------------------------------------------------------------------------------------------------
# TODO
#   ----------------------------------
#   Step 1 → Intr : valores fijos
#   Step 2 → Calc : valores fijos
#   Step 3 → Calc : valores variables
#   Step 4 → Intr : resultados por ronda
#   Step 5 → calc :