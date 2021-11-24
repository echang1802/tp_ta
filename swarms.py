
import random

class particle_swarm:

    def __init__(self, region, swarm_size, leaders, cubrir_rutas_greedy):

        self.region = region
        self.swarm_size = swarm_size
        self.total_leaders = leaders

        self.swarm = [cubrir_rutas_greedy(self.region) for i in range(self.swarm_size)]

        self.best_solution = self.swarm[0]
        self.select_leaders()

    def select_leaders(self):
        sorted_swarm = self._sort_swarm((0, self.swarm_size))
        self.leaders = [sorted_swarm[l] for l in range(self.total_leaders)]
        self.stop = self.best_solution > self.leaders[0]
        if not self.stop:
            self.best_solution = self.leaders[0].copy()

    def _sort_swarm(self, index):
        if index[1] - index[0] == 1:
            return [self.swarm[index[0]].copy()]
        m = (index[1] + index[0]) // 2
        left_side =self._sort_swarm((index[0], m))
        right_side =self._sort_swarm((m, index[1]))
        sorted = []
        ready = False
        l = 0
        r = 0
        while not ready:
            if left_side[l] > right_side[r]:
                sorted.append(left_side[l])
                l += 1
                if l == len(left_side):
                    sorted += right_side[r:]
            else:
                sorted.append(right_side[r])
                r += 1
                if r == len(right_side):
                    sorted += left_side[l:]
            ready = l ==len(left_side) or r == len(right_side)
        return sorted

    def update_swarm(self):
        self.swarm = [self.leader_mutation() for i in range(self.swarm_size)]

    def leader_mutation(self):
        # Elegimos un leader a mutar
        leader = random.choice(self.leaders).copy()

        # eliminamos un agente aleatorio
        airport_to_remove = random.choice(list(leader.aeropuertos_con_agentes()))
        leader.sacar_agente(airport_to_remove)
        if leader.cubrimiento() == 1:
            return leader

        # Agregamos agentes hasta tener cubrimiento = 1
        airports = leader.aeropuertos_sin_agentes()
        airports.remove(airport_to_remove)
        for airport in airports:
            leader.poner_agente(airport)
            if leader.cubrimiento() == 1:
                return leader
            leader.sacar_agente(airport)

        # Si ningun otro agente genera un cubrimiento de 1 regresamos el mismo lider
        leader.poner_agente(airport_to_remove)
        return leader

    def stop_condition(self):
        return self.stop
