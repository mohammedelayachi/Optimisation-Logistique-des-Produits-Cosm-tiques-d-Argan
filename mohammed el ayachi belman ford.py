import sys

# Définition des sommets et des arêtes
V = ["Agadir", "Marakesh", "Casablanca", "Meknes", "Oujda", "Al hoceima", "Tangier"]
E = [
    ["Agadir", "Casablanca", 976.5],
    ["Agadir", "Marakesh", 528.5],
    ["Marakesh", "Meknes", 313.5],
    ["Marakesh", "Casablanca", 484.5],
    ["Casablanca", "Meknes", 456],
    ["Casablanca", "Tangier", 679],
    ["Tangier", "Meknes", 513.5],
    ["Meknes", "Al hoceima", 578],
    ["Al hoceima", "Tangier", 436.5],
    ["Meknes", "Oujda", 778.5],
    ["Oujda", "Al hoceima", 385.5]
]

# Fonction pour l'algorithme de Bellman-Ford
def bellman_ford(source, V, E):
    distance = {vertex: sys.maxsize for vertex in V}
    predecessor = {vertex: None for vertex in V}
    distance[source] = 0

    for _ in range(len(V) - 1):
        for edge in E:
            u, v, weight = edge[0], edge[1], edge[2]
            if distance[u] != sys.maxsize and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u

    # Vérification des cycles négatifs
    for edge in E:
        u, v, weight = edge[0], edge[1], edge[2]
        if distance[u] != sys.maxsize and distance[u] + weight < distance[v]:
            return "Le graphe contient un cycle négatif"

    return distance, predecessor


source_vertex = "Agadir"
result_distance, result_predecessor = bellman_ford(source_vertex, V, E)
print("Distances les plus courtes depuis", source_vertex, ":", result_distance)
