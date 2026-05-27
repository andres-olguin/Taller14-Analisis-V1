import itertools

def vendedor_viajero(matriz_distancias, lista_ciudades):
    # Genera todas las combinaciones posibles de rutas
    rutas_posibles = list(itertools.permutations(lista_ciudades))
    distancia_minima = float('inf')
    mejor_ruta = []

    for ruta in rutas_posibles:
        distancia_actual = 0
        
        # Sumar las distancias de la ruta actual
        for i in range(len(ruta) - 1):
            ciudad_origen = ruta[i]
            ciudad_destino = ruta[i + 1]
            distancia_actual += matriz_distancias[ciudad_origen][ciudad_destino]
        
        # Sumar el regreso a la ciudad de inicio
        ciudad_origen_final = ruta[-1]
        ciudad_destino_final = ruta[0]
        distancia_actual += matriz_distancias[ciudad_origen_final][ciudad_destino_final]

        # Si encontramos una ruta más corta, la guardamos
        if distancia_actual < distancia_minima:
            distancia_minima = distancia_actual
            mejor_ruta = list(ruta)

    return mejor_ruta, distancia_minima

# Ejemplo de uso de la función
if __name__ == "__main__":
    # Matriz de distancias entre 4 ciudades (0, 1, 2, 3)
    distancias = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    ciudades = [0, 1, 2, 3]

    ruta_optima, total_distancia = vendedor_viajero(distancias, ciudades)
    
    print("La ruta óptima encontrada es:", ruta_optima)
    print("La distancia total del recorrido es:", total_distancia)
