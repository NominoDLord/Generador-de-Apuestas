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

# ============================================ [ BIBLIOTECAS y MÓDULOS ] ============================================= #

# ==================================================== [ CLASES ] ==================================================== #

class VariablesFijas:

    def __init__(self, saldo_inicial, apuesta_min, apuesta_max, op_positivas, op_negativas, multi_pos, multi_neg,
                 riesgo_lim_pos, riesgo_lim_neg) -> None:
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

        self.lista_porcentual_true = [True] * int(self.porcentaje_base_pos)
        self.lista_porcentual_false = [False] * int(self.porcentaje_base_neg)


# =================================================== [ FUNCIONES ] ================================================== #





# =================================================== [ EJECUCIÓN ] ================================================== #






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