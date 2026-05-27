# Análisis Técnico del Algoritmo (Vendedor Viajero)

### Pseudocódigo

Inicio
    Definir distancia_minima = Infinito
    Definir mejor_ruta = Vacío
    Generar todas las permutaciones posibles de las ciudades
    
    Para cada ruta en las permutaciones:
        Calcular distancia_actual = 0
        
        Para i desde 1 hasta cantidad de ciudades - 1:
            distancia_actual = distancia_actual + distancia entre ruta[i] y ruta[i+1]
            
        distancia_actual = distancia_actual + distancia entre ruta[ultima_ciudad] y ruta[primera_ciudad]
        
        Si distancia_actual < distancia_minima:
            distancia_minima = distancia_actual
            mejor_ruta = ruta
            
    Retornar mejor_ruta, distancia_minima
Fin

### Análisis de Complejidad

* Complejidad Temporal: O(n!). Esto se debe a que el algoritmo evalúa todas las permutaciones posibles, lo cual crece de forma factorial con el número de ciudades (n).
* Complejidad Espacial: O(n), ya que solo requerimos memoria para almacenar la ruta actual y la mejor encontrada, ocupando un espacio lineal.

### Representación Matemática del Costo

$$C=\sum_{i=1}^{n-1}d(v_i,v_{i+1})+d(v_n,v_1)$$

Donde d(v_i, v_{i+1}) representa la distancia entre dos ciudades consecutivas en la ruta propuesta.
