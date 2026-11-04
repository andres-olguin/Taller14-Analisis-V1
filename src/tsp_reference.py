"""Solución exacta del TSP para instancias educativas pequeñas."""
from itertools import permutations
import math

def solve(distances, max_cities=10):
    n = len(distances)
    if not 2 <= n <= max_cities:
        raise ValueError(f"Se admiten entre 2 y {max_cities} ciudades.")
    if any(len(row) != n for row in distances):
        raise ValueError("La matriz de distancias debe ser cuadrada.")
    if any(isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0 for row in distances for value in row):
        raise ValueError("Solo se aceptan distancias finitas y no negativas.")
    shortest, route = math.inf, None
    for remaining in permutations(range(1, n)):
        candidate = (0, *remaining)
        total = sum(distances[candidate[i]][candidate[(i + 1) % n]] for i in range(n))
        if total < shortest:
            shortest, route = total, candidate
    return {"route": list(route) + [0], "cost": shortest}

if __name__ == "__main__":
    matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print(solve(matrix))
