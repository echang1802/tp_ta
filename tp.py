from region import Region
from algorithms import cubrir_rutas_random, cubrir_rutas_backtracking, cubrir_rutas_greedy, cubrir_rutas_bl, cubrir_rutas_bli
from datetime import datetime
import click
import multiprocessing

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Variables auxiliares para la ejecucion.
valid_regions = ['Estrella', 'Completa', 'Rueda', 'Ochoa', 'Multihub', 'Grande66', 'Grande50']
algorithms = {
    "random" : cubrir_rutas_random,
    "backtraking" : cubrir_rutas_backtracking,
    "greedy" : cubrir_rutas_greedy,
    "busqueda_local" : cubrir_rutas_bl,
    "busqueda_local_iter" : cubrir_rutas_bli
}


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Funcion auxiliar para la detencion despues de la hora de procesamiento
def apply_algorithm(region, algorithm, solution, iterations):
    if algorithm == "busqueda_local":
        starting_solution = cubrir_rutas_random(region)
        solution["best"] = algorithms[algorithm](starting_solution)
    elif algorithm == "busqueda_local_iter":
        solution["best"] = algorithms[algorithm](region, iterations)
    else:
        solution["best"] = algorithms[algorithm](region)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# función principal, acepta parametros para seleccionar la region y el
# algoritmo a usar.
@click.command()
@click.option("-region", type = click.Choice(valid_regions), help = "Region to process.")
@click.option("-algorithm", type = click.Choice(algorithms.keys()), help = "Algorithm to use.")
@click.option("-iterations", default = 1000, help = "Iterations on Iterative local search algorithm.")
def run(region, algorithm, iterations):
    # Cargo la region seleccionada.
    region_name = region
    region = Region(region)

    # Busco una asignacion usando el algoritmo seleccionado, calculando
    # el tiempo de ejecucion, si se tarda mas de una hora se detiene el proceso.
    manager = multiprocessing.Manager()
    solution = manager.dict()
    p = multiprocessing.Process(target=apply_algorithm, name="apply_algorithm", args=(region, algorithm, solution, iterations))
    ended = True
    start_at = datetime.now()
    p.start()
    p.join(3600)
    if p.is_alive():
        print("Algoritm did not end before an hour")
        ended = False
        p.terminate()
        p.join()
    process_time = datetime.now() - start_at

    # Imprimo un resumen de los resultados.
    print(f"Algoritmo: {algorithm}")
    if ended:
        print(f"Region: {region_name} - ", region)
        print("Solucion:", solution["best"])
    print("Tiempo:", process_time)

    with open("executions.csv", "a") as file:
        file.write(f"{region_name},{algorithm},{region.cant_aeropuertos},{solution['best'].cant_agentes()},{process_time}\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    run()
