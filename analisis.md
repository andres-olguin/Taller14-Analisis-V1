# Análisis Técnico del Algoritmo (Vendedor Viajero)

### Pseudocódigo
```text
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
