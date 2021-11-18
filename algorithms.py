
from region import Planilla
from neighbors import neighborhood
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
    solution = Planilla(region)
    return backtracking_aux(solution)

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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def cubrir_rutas_greedy():
    pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Algoritmo de busqueda local
def cubrir_rutas_bl(solucion_inicial):
    ready = False
    while not ready:
        neighbors = neighborhood(solucion_inicial)
        if neighbors.total_neighbors() == 0: # Sino se consiguen vecinos
            return solucion_inicial          # devolvemos la ultima solucion
        best_neightbor = neighbors.select_best_neightbor()
        ready = not best_neightbor > solucion_inicial # Paramos si el mejor
        solucion_inicial = best_neightbor.copy()      # vecino no es mejor que
    return solucion_inicial                           # la solucion actual

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Algoritmo de busqueda local iterativa
def cubrir_rutas_bli(region, iter):
    best_solution = cubrir_rutas_random(region)
    for iteration in range(iter):
        solution = cubrir_rutas_bl(best_solution)
        if solution > best_solution:
            best_solution = solution.copy()
    return best_solution

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
