from region import Region, Planilla
from datetime import datetime
import random

# algoritmo aleatorio.
def cubrir_rutas_random(region):
    sol = Planilla(region)
    while sol.cubrimiento() < 1:
        ae = random.choice(list(sol.aeropuertos_sin_agentes()))
        sol.poner_agente(ae)
    return sol

#def cubrir_rutas_backtracking(region):
# COMPLETAR
#
#def cubrir_rutas_greedy(region):
# COMPLETAR
#
#def cubrir_rutas_bl(solucion_inicial):
# COMPLETAR
#
#def cubrir_rutas_bli(region, iter):
# COMPLETAR
#

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Cargo una region de ejemplo.
region = Region("Estrella")

# Busco una asignacion completa (con un algoritmo aleatorio en este
# caso), calculando el tiempo de ejecucion.
comienzo = datetime.now()
solucion = cubrir_rutas_random(region)
tiempo_usado = datetime.now() - comienzo

# Imprimo un resumen de los resultados.
print("Region:", region)
print("Solucion:", solucion)
print("Tiempo:", tiempo_usado)
