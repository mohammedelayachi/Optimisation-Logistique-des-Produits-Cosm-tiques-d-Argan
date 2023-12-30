from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Capacité résiduelle initiale

    def bfs(self, source, sink, parent):
        visited = {v: False for v in self.graph}
        queue = [source]
        visited[source] = True
        parent[source] = None

        while queue:
            u = queue.pop(0)
            for v, capacity in self.graph[u].items():
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[sink]

    def ford_fulkerson(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Données
capacities = {
    ("Agadir", "Casablanca"): 976.5,
    ("Agadir", "Marakesh"): 528.5,
    # Ajoutez toutes les capacités ici
}

demands = {
    "Casablanca": 200,
    "Marakesh": 130,
    "Oujda": 80,
    "Tangier": 160,
    "Al hoceima": 100,
    "Meknes": 130
}

# Création du graphe avec les capacités
graph = Graph()
for (u, v), capacity in capacities.items():
    graph.add_edge(u, v, capacity)

# Ajout des demandes comme capacités sortantes des villes vers le puits (sink)
sink = "Meknes"
for city, demand in demands.items():
    graph.add_edge(city, sink, demand)

# Calcul du flot maximal
max_flow = graph.ford_fulkerson("Agadir", sink)

print("Flot maximal transporté :", max_flow)
