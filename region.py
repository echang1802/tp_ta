
from copy import deepcopy

################### AEROPUERTOS Y RUTAS DE UNA REGION #################
class Region:

    # Inicializa una nueva region.
    def __init__(self, nombre):
        self.cant_aeropuertos = 0
        self.rutas = set()
        if nombre == "Estrella":
            self._region_estrella()
        elif nombre == "Completa":
            self._region_completa()
        elif nombre == "Rueda":
            self._region_rueda()
        elif nombre == "Ochoa":
            self._region_ochoa()
        elif nombre == "Multihub":
            self._region_multihub()
        elif nombre == "Grande66":
            self._region_grande66()
        elif nombre == "Grande50":
            self._region_grande50()
        else:
            print("Región no reconocida: " + str(nombre))

    # Devuelve, como representación string de la region, la cantidad de
    # aeropuertos y las rutas (ordenadas).
    def __repr__(self):
        return "Aeropuertos: " + str(self.cant_aeropuertos) + \
               ". Rutas: " + str(sorted(self.rutas))

    # Inicializa regiones de ejemplo.
    def _region_estrella(self):
        self.cant_aeropuertos = 7
        self.rutas = set([(0,1), (0,2), (0,3), (0,4), (0,5), (0,6)])

    def _region_completa(self):
        self.cant_aeropuertos = 6
        self.rutas = set([(0,1), (0,2), (0,3), (0,4), (0,5),
                          (1,2), (1,3), (1,4), (1,5), (2,3),
                          (2,4), (2,5), (3,4), (3,5), (4,5)])

    def _region_rueda(self):
        self.cant_aeropuertos = 9
        self.rutas = set([(1,2), (2,3), (3,4), (4,5), (5,6), (6,7),
                          (7,8), (8,1), (1,0), (3,0), (5,0), (7,0)])

    def _region_ochoa(self):
        self.cant_aeropuertos = 8
        self.rutas = set([(0,1), (0,4), (0,6), (0,3), (1,2),
                          (4,2), (4,5), (4,6), (4,7)])

    def _region_multihub(self):
        self.cant_aeropuertos = 12
        self.rutas = set([(0,1), (0,2), (0,3), (4,5), (4,6), (4,7),
                          (8,9), (8,10), (8,11), (0,4), (0,8), (4,8)])

    def _region_grande66(self):
        self.cant_aeropuertos = 66
        self.rutas = set([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,0),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(19,10),(20,21),(21,22),(22,23),(23,24),(24,25),(25,26),(26,27),(27,28),(28,29),(29,20),(30,31),(31,32),(32,33),(33,34),(34,35),(35,36),(36,37),(37,38),(38,39),(39,30),(40,41),(41,42),(42,43),(43,44),(44,45),(45,46),(46,47),(47,48),(48,49),(49,40),(50,51),(51,52),(52,53),(53,54),(54,55),(55,56),(56,57),(57,58),(58,59),(59,50),(60,0),(60,2),(60,4),(60,6),(60,8),(61,10),(61,12),(61,14),(61,16),(61,18),(62,20),(62,22),(62,24),(62,26),(62,28),(63,30),(63,32),(63,34),(63,36),(63,38),(64,40),(64,42),(64,44),(64,46),(64,48),(65,50),(65,52),(65,54),(65,56),(65,58)])

    def _region_grande50(self):
        self.cant_aeropuertos = 50

############# PLANILLA CON ASIGNACIONES DE AGENTES A AEROPUERTOS ############
        self.rutas = set([(0,1),(0,6),(0,7),(0,9),(0,10),(0,11),(0,12),(0,13),(0,15),(0,18),(0,20),(0,21),(0,24),(0,25),(0,26),(0,29),(0,31),(0,34),(0,36),(0,39),(0,41),(0,42),(0,45),(0,46),(0,47),(0,48),(1,5),(1,6),(1,9),(1,12),(1,13),(1,15),(1,17),(1,20),(1,22),(1,23),(1,24),(1,25),(1,27),(1,28),(1,29),(1,32),(1,33),(1,35),(1,37),(1,40),(1,41),(1,42),(1,44),(1,45),(1,46),(2,4),(2,6),(2,7),(2,8),(2,10),(2,12),(2,17),(2,18),(2,19),(2,21),(2,22),(2,25),(2,26),(2,27),(2,29),(2,30),(2,31),(2,34),(2,37),(2,38),(2,39),(2,40),(2,41),(2,45),(2,46),(2,47),(2,49),(3,4),(3,5),(3,6),(3,9),(3,11),(3,12),(3,14),(3,16),(3,18),(3,19),(3,21),(3,23),(3,24),(3,25),(3,26),(3,28),(3,30),(3,32),(3,33),(3,35),(3,36),(3,37),(3,40),(3,42),(3,43),(3,45),(3,46),(3,47),(3,48),(3,49),(4,5),(4,6),(4,8),(4,12),(4,13),(4,14),(4,15),(4,19),(4,20),(4,21),(4,24),(4,33),(4,34),(4,36),(4,37),(4,41),(4,42),(4,47),(4,48),(4,49),(5,7),(5,8),(5,12),(5,15),(5,16),(5,17),(5,19),(5,23),(5,27),(5,28),(5,30),(5,31),(5,32),(5,33),(5,34),(5,35),(5,38),(5,39),(5,42),(5,43),(5,44),(5,45),(5,46),(6,8),(6,9),(6,10),(6,14),(6,16),(6,17),(6,20),(6,21),(6,23),(6,25),(6,27),(6,28),(6,29),(6,30),(6,31),(6,32),(6,34),(6,35),(6,36),(6,39),(6,41),(6,43),(6,44),(6,45),(6,47),(6,49),(7,8),(7,10),(7,11),(7,12),(7,16),(7,18),(7,19),(7,21),(7,22),(7,23),(7,25),(7,28),(7,29),(7,30),(7,33),(7,34),(7,35),(7,37),(7,38),(7,39),(7,41),(7,46),(7,48),(7,49),(8,9),(8,11),(8,12),(8,13),(8,15),(8,16),(8,21),(8,22),(8,23),(8,25),(8,29),(8,32),(8,34),(8,35),(8,36),(8,37),(8,42),(8,43),(8,45),(8,46),(8,47),(8,48),(8,49),(9,12),(9,13),(9,15),(9,18),(9,22),(9,24),(9,30),(9,32),(9,34),(9,35),(9,36),(9,40),(9,41),(9,43),(9,44),(9,45),(9,48),(10,12),(10,14),(10,18),(10,19),(10,20),(10,21),(10,22),(10,32),(10,33),(10,34),(10,36),(10,37),(10,39),(10,44),(10,46),(10,47),(11,12),(11,13),(11,16),(11,18),(11,22),(11,24),(11,25),(11,29),(11,32),(11,34),(11,35),(11,36),(11,38),(11,40),(11,42),(11,43),(11,44),(11,47),(12,15),(12,17),(12,18),(12,22),(12,27),(12,29),(12,30),(12,31),(12,32),(12,34),(12,35),(12,37),(12,39),(12,40),(12,41),(12,46),(12,48),(13,14),(13,15),(13,16),(13,22),(13,25),(13,26),(13,27),(13,28),(13,30),(13,32),(13,35),(13,36),(13,40),(13,44),(13,45),(13,46),(14,19),(14,20),(14,21),(14,22),(14,23),(14,28),(14,29),(14,30),(14,32),(14,33),(14,34),(14,35),(14,37),(14,39),(14,40),(14,42),(14,43),(14,46),(14,47),(15,17),(15,20),(15,21),(15,22),(15,23),(15,27),(15,28),(15,31),(15,34),(15,37),(15,40),(15,41),(15,42),(15,48),(16,17),(16,18),(16,19),(16,20),(16,21),(16,22),(16,25),(16,27),(16,28),(16,29),(16,30),(16,34),(16,36),(16,37),(16,39),(16,42),(16,43),(16,47),(16,49),(17,22),(17,24),(17,27),(17,29),(17,32),(17,33),(17,37),(17,38),(17,44),(17,45),(17,46),(17,47),(17,48),(18,20),(18,21),(18,22),(18,23),(18,24),(18,25),(18,27),(18,28),(18,29),(18,32),(18,35),(18,36),(18,38),(18,39),(18,44),(18,47),(18,48),(18,49),(19,20),(19,22),(19,23),(19,26),(19,27),(19,31),(19,32),(19,33),(19,34),(19,35),(19,37),(19,39),(19,41),(19,46),(19,47),(19,48),(19,49),(20,22),(20,24),(20,25),(20,26),(20,29),(20,30),(20,33),(20,36),(20,38),(20,42),(20,43),(20,44),(20,45),(21,27),(21,28),(21,30),(21,32),(21,33),(21,34),(21,40),(21,43),(21,45),(21,46),(21,47),(21,48),(21,49),(22,27),(22,28),(22,29),(22,30),(22,33),(22,34),(22,40),(22,42),(22,43),(22,46),(22,47),(22,48),(22,49),(23,27),(23,28),(23,29),(23,32),(23,33),(23,35),(23,44),(23,45),(23,46),(23,48),(24,26),(24,28),(24,30),(24,31),(24,35),(24,36),(24,38),(24,40),(24,43),(24,44),(24,46),(24,49),(25,26),(25,27),(25,28),(25,29),(25,31),(25,32),(25,34),(25,37),(25,39),(25,41),(25,49),(26,28),(26,29),(26,33),(26,36),(26,38),(26,45),(26,46),(26,47),(26,48),(27,28),(27,29),(27,30),(27,31),(27,32),(27,33),(27,34),(27,37),(27,41),(27,42),(27,45),(27,48),(28,31),(28,32),(28,33),(28,34),(28,35),(28,36),(28,37),(28,38),(28,41),(28,43),(28,45),(28,46),(28,47),(28,49),(29,33),(29,34),(29,35),(29,36),(29,39),(29,41),(29,43),(29,44),(29,48),(30,31),(30,33),(30,36),(30,37),(30,38),(30,39),(30,43),(30,44),(30,45),(31,32),(31,35),(31,39),(31,44),(31,47),(31,48),(32,34),(32,36),(32,37),(32,38),(32,40),(32,42),(32,43),(32,44),(32,45),(32,46),(33,35),(33,40),(33,41),(33,45),(33,47),(33,49),(34,42),(34,44),(34,45),(34,46),(35,36),(35,37),(35,38),(35,46),(35,48),(35,49),(36,38),(36,40),(36,41),(36,43),(36,44),(37,38),(37,40),(38,41),(38,42),(38,46),(38,47),(38,49),(39,40),(39,45),(39,46),(39,47),(40,43),(40,49),(41,43),(41,46),(41,49),(42,44),(42,45),(42,48),(43,44),(43,46),(43,47),(44,46),(45,46),(45,47),(45,49),(46,48),(47,48)])



class Planilla:
    # Para comenzar una nueva planilla, necesitamos conocer la region.
    def __init__(self, region):
        self._region = region
        self._aeropuertos_con_agentes = set()
        self._aeropuertos_sin_agentes = set(range(region.cant_aeropuertos))
        self.vecinos = []

    # Devuelve una copia de la planilla.
    def copy(self):
        return deepcopy(self)

    # Pone un agente en el aeropuerto ae.
    def poner_agente(self, ae):
        if ae in self._aeropuertos_sin_agentes:
            self._aeropuertos_sin_agentes.remove(ae)
            self._aeropuertos_con_agentes.add(ae)

    # Saca un agente del aeropuerto ae.
    def sacar_agente(self, ae):
        if ae in self._aeropuertos_con_agentes:
            self._aeropuertos_con_agentes.remove(ae)
            self._aeropuertos_sin_agentes.add(ae)

    # Devuelve el conjunto de aeropuertos que no tienen agentes.
    def aeropuertos_sin_agentes(self):
        return self._aeropuertos_sin_agentes.copy()

    # Devuelve el conjunto de las aeropuertos que tienen agentes.
    def aeropuertos_con_agentes(self):
        return self._aeropuertos_con_agentes.copy()

    # Devuelve la cantidad de agentes asignados.
    def cant_agentes(self):
        return len(self._aeropuertos_con_agentes)

    # Devuelve el porcentaje de rutas cubiertas (float entre 0 y 1).
    def cubrimiento(self):
        rutas_cubiertas = 0
        for ruta in self._region.rutas:
            if self._ruta_protegida(ruta):
                rutas_cubiertas = rutas_cubiertas + 1
        return rutas_cubiertas / len(self._region.rutas)

    # Función privada que devuelve True si la ruta dada tiene un agente
    # en al menos uno de sus aeropuertos, o False en caso contrario.
    def _ruta_protegida(self, ruta):
        aeropuerto1 = ruta[0]
        aeropuerto2 = ruta[1]
        return (aeropuerto1 in self._aeropuertos_con_agentes or
                aeropuerto2 in self._aeropuertos_con_agentes)

    # Devuelve, como representación string de la planilla, los códigos
    # de los aeropuertos que tienen un agente, ordenados.
    def __repr__(self):
        return f"Aereopuertos: {len(self._aeropuertos_con_agentes)} -> {str(sorted(self._aeropuertos_con_agentes))}"

    # Función privada que devuelve True si la ruta dada tiene un agente
    # en sus dos aeropuertos, o False en caso contrario.
    def _ruta_duplicada(self, ruta):
        aeropuerto1 = ruta[0]
        aeropuerto2 = ruta[1]
        return (aeropuerto1 in self._aeropuertos_con_agentes and
                aeropuerto2 in self._aeropuertos_con_agentes)

    # Función privada que devuelve la cantidad de rutas duplicadas
    # (protegidas por ambos extremos)
    def _total_rutas_duplicadas(self):
        cantidad_duplicadas = 0
        for ruta in self._region.rutas:
            if self._ruta_duplicada(ruta):
                cantidad_duplicadas += 1
        return cantidad_duplicadas

    # Define que una solución es mayor a otra si tiene una mayor cantidad
    # de rutas duplicadas
    def __gt__(self, other):
        if self.cant_agentes() == other.cant_agentes():
            return self._total_rutas_duplicadas() > other._total_rutas_duplicadas()
        return self.cant_agentes() < other.cant_agentes()
