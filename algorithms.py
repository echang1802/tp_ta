
from region import Planilla
from neighbors import neighborhood
from swarms import particle_swarm
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
    return backtracking_aux_opt(solution, set())

def backtracking_aux(plan):
    # Caso base, cubrimos el 100% de la region.
    if plan.cubrimiento() >= 1:
        return plan

    # Buscamos la mejor solucion, probando con los diferentes aeropuertos restantes.
    best_solution = None
    agents_in_best_sol = float("Inf")
    for ae in plan.aeropuertos_sin_agentes():
        plan.poner_agente(ae)
        sol = backtracking_aux(plan.copy())
        if sol.cant_agentes() < agents_in_best_sol: # Nos quedamos con la mejor
            best_solution = sol.copy()              # solucion hasta ahora.
            agents_in_best_sol = sol.cant_agentes()
        plan.sacar_agente(ae)
    return best_solution

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def cubrir_rutas_greedy(region, degrees = 1):
    solution = Planilla(region)
    ready = False
    while not ready:
        airport_to_add = [None] * degrees
        covers = [0] * degrees
        worst_cover = 0
        worst_cover_index = 0
        for airport in solution.aeropuertos_sin_agentes():
            solution.poner_agente(airport)
            if solution.cubrimiento() > worst_cover:
                airport_to_add[worst_cover_index] = airport
                covers[worst_cover_index] = solution.cubrimiento()
                worst_cover = 1
                for i in range(degrees):
                    if worst_cover < covers[i]:
                        worst_cover = covers[i]
                        worst_cover_index = i
            solution.sacar_agente(airport)
        solution.poner_agente(random.choice(airport_to_add))
        ready = solution.cubrimiento() == 1
    return solution

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

# Algoritmo grasp
def cubrir_rutas_grasp(region, degrees, iter):
    best_solution = cubrir_rutas_greedy(region, degrees)
    for iteration in range(iter):
        solution = cubrir_rutas_bl(best_solution)
        if solution > best_solution:
            best_solution = solution.copy()
    return best_solution

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Algoritmo de enjambre de particulas
def cubrir_rutas_swarm(region, swarm_size, leaders, max_iter = 1000):
    # definimos N soluciones aleatorias (usar greedy?)
    # seleccionamos las mejores M soluciones
    # definimos N soluciones similares a las M mejores.
    # repetimos hasta que no se tengan mejoras

    # Creamos el enjambre

    ready = False
    iter = 1
    solutions_swarm = particle_swarm(region, swarm_size, leaders, cubrir_rutas_random)
    while not ready:
        # Update the swarm
        solutions_swarm.update_swarm()

        # Select leaders
        solutions_swarm.select_leaders()

        iter += 1
        ready = iter >= max_iter #or solutions_swarm.stop_condition()
    return solutions_swarm.best_solution
