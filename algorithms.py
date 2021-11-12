from region import Planilla
import random

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# algoritmo aleatorio.
def cubrir_rutas_random(region):
    sol = Planilla(region)
    while sol.cubrimiento() < 1:
        ae = random.choice(list(sol.aeropuertos_sin_agentes()))
        sol.poner_agente(ae)
    return sol

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Algoritmo de backtraking
def cubrir_rutas_backtracking(region):
    # Definimos la planilla e iniciamos el algoritmo.
    sol = Planilla(region)
    return backtracking_aux(sol)

def backtracking_aux(plan):
    # Caso base, cubrimos el 100% de la region.
    if plan.cubrimiento() >= 1:
        return plan

    # Buscamos la mejor solucion, probando con los diferentes aeropuertos restantes.
    best_solution = None
    agents_in_best_sol = float("Inf")
    for ae in plan.aeropuertos_sin_agentes():
        plan.poner_agente(ae)
        sol = backtracking_aux(plan)
        if sol.cant_agentes() < agents_in_best_sol: # Nos quedamos con la mejor
            best_solution = sol.copy()              # solucion hasta ahora.
            agents_in_best_sol = sol.cant_agentes()
        plan.sacar_agente(ae)
    return best_solution

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
