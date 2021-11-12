from region import Region
from algorithms import cubrir_rutas_random, cubrir_rutas_backtracking
from datetime import datetime
import click
import multiprocessing

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Variables auxiliares para la ejecucion.
valid_regions = ['Estrella', 'Completa', 'Rueda', 'Ochoa', 'Multihub', 'Grande66', 'Grande50']
algorithms = {
    "random" : cubrir_rutas_random,
    "backtraking" : cubrir_rutas_backtracking
}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Funcion auxiliar para la detencion despues de la hora de procesamiento
def apply_algorithm(region, algorithm_function, solution):
    solution["best"] = algorithm_function(region)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# función principal, acepta parametros para seleccionar la region y el
# algoritmo a usar.
@click.command()
@click.option("-region", type = click.Choice(valid_regions), help = "Region to process.")
@click.option("-algorithm", type = click.Choice(algorithms.keys()), help = "Algorithm to use.")
def run(region, algorithm):
    # Cargo la region seleccionada.
    region = Region(region)

    # Busco una asignacion usando el algoritmo seleccionado, calculando
    # el tiempo de ejecucion, si se tarda mas de una hora se detiene el proceso.
    manager = multiprocessing.Manager()
    solution = manager.dict()
    p = multiprocessing.Process(target=apply_algorithm, name="apply_algorithm", args=(region, algorithms[algorithm], solution))
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
    if ended:
        print("Region:", region)
        print("Solucion:", solution["best"])
    print("Tiempo:", process_time)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    run()
