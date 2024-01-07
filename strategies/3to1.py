import sys
import os

subDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(subDir1)

from config.setup import SALDO_INICIAL, APUESTA_MINIMA, APUESTA_MAXIMA, MULTIPLICADOR, OPCIONES_TRUE, OPCIONES_FALSE

from moduls.generadorDeRonda import generar_ronda






ronda = generar_ronda()












#
