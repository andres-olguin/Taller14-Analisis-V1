# TSP Brute Force Lab — Vendedor viajero por búsqueda exhaustiva

Laboratorio académico de algoritmos para resolver el **problema del vendedor viajero (TSP)** en instancias pequeñas mediante enumeración de recorridos. Contiene un ejercicio Python original, una implementación de referencia más controlada, pruebas y una demostración web.

**Autores del trabajo académico:** Andrés Olguín, Maximiliano Valdés y Enrique Chamy.

> **Estado:** algoritmo exacto didáctico con complejidad factorial. No es un optimizador logístico para ciudades o rutas a gran escala.

## Problema

Dadas las distancias entre ciudades, encontrar el circuito de costo mínimo que visite cada una exactamente una vez y regrese al origen. El problema de decisión asociado es NP-completo; la versión de optimización se considera NP-difícil.

## Ejecutar

**Requisitos:** Python 3.10+ para la referencia independiente.

```bash
python vendedor_viajero.py
python -m src.tsp_reference
python -m unittest discover -s tests -v
```

Ambos scripts muestran un ejemplo pequeño. La referencia fija la ciudad inicial en 0, valida una matriz numérica no negativa y limita a 10 ciudades para evitar ejecuciones accidentales excesivamente costosas.

## Archivos principales

| Ruta | Uso |
|---|---|
| [`vendedor_viajero.py`](vendedor_viajero.py) | Implementación original con `itertools.permutations` |
| [`src/tsp_reference.py`](src/tsp_reference.py) | Solver de referencia que itera permutaciones incrementalmente |
| [`tests/`](tests/) | Tests de ruta, costo conocido y entradas inválidas |
| [`docs/index.html`](docs/index.html) | Demostración visual educativa independiente |
| [`.github/workflows/tsp-tests.yml`](.github/workflows/tsp-tests.yml) | Tests automáticos |

## Comparación de métodos

| Variante | Característica | Límite |
|---|---|---|
| Código histórico | Materializa todas las permutaciones en memoria | Consumo factorial de memoria |
| Referencia nueva | Itera las permutaciones y fija ciudad de salida | Tiempo factorial, tamaño limitado |
| [Backtracking con poda](https://github.com/andres-olguin/tsp-backtracking-lab) | Descarta algunas ramas por costo | Peor caso sigue siendo factorial |

La solución exacta crece demasiado rápido con `n` para usos a gran escala. Para problemas reales se deben evaluar restricciones, heurísticas, optimización matemática y criterios de calidad distintos de la optimalidad garantizada.

## Evidencia, complejidad y evolución

Las pruebas automáticas validan casos acotados; no hay benchmark de producción ni datos de tráfico real. Próximos pasos: comparar tiempos y memoria por número de ciudades, repetir resultados con matrices de referencia y documentar qué podas ayudan.

[Estudio TSP](docs/ESTUDIO_DE_EVOLUCION_2026-10-30.md) · [Seguridad y escalabilidad](docs/ARCHITECTURE_SCALABILITY_2026-11-04.md).

**Titularidad:** trabajo académico con coautoría; respetar permisos y créditos antes de reutilizar sus materiales comercialmente.
