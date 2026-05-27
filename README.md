# Taller 14 - El Vendedor Viajero
**Integrantes:** Andrés Olguín, Maximiliano Valdés, Enrique Chamy.

### 1. ¿En qué consiste el problema?
Consiste en encontrar la ruta más corta para un vendedor que debe visitar varias ciudades y volver al punto de partida. 
* **Entradas:** Una lista de ciudades y las distancias entre cada una de ellas.
* **Salidas:** La ruta o recorrido más corto posible.
* **Restricciones:** Solo se puede pasar una vez por cada ciudad y se debe terminar en la ciudad donde se empezó.

### 2. Problema de decisión asociado
¿Existe una ruta que pase por todas las ciudades y vuelva al inicio cuya distancia total sea menor o igual a un número límite "X"?

### 3. Clase de problema
Pertenece a la clase de problemas NP-Completo.

### 4. Aplicaciones
* Reparto de paquetes o logística.
* Rutas de los furgones escolares.
* Perforación automática de placas de circuitos.

### 5. Pseudocódigo del Algoritmo (Fuerza Bruta)

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
