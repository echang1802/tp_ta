
# Clase auxiliar para manejar el concepto de vecinos
class neighborhood:

    def __init__(self, solution):
        self.solution = solution.copy()
        self.neighbors = []
        # Definimos como vecinos todas aquellas soluciones con un aereopuerto menos
        for airport in self.solution.aeropuertos_con_agentes():
            self.solution.sacar_agente(airport)
            if self.solution.cubrimiento() == 1:
                self.neighbors.append(self.solution.copy())
            self.solution.poner_agente(airport)

    # Devuelve la cantidad de vecinos de la solucion
    def total_neighbors(self):
        return len(self.neighbors)

    # Función que devuelve el "mejor" vecino
    # seleccionamos el vecino que tenga mas rutas duplicadas
    # (tiene mas chances de que se le pueda eliminar otro aeropuerto)
    def select_best_neightbor(self):
        best_neightbor = self.neighbors[0].copy()
        for neighbor in self.neighbors[1:]:
            if neighbor > best_neightbor:
                best_neightbor = neighbor.copy()
        return best_neightbor
