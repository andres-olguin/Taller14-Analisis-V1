# TSP — implementaciones de referencia y límites

El ejemplo histórico `vendedor_viajero.py` materializa `list(permutations(...))`, lo que incrementa el uso de memoria de forma factorial.

La propuesta adicional `src/tsp_reference.py` **no modifica ni sustituye el trabajo original**: recorre permutaciones incrementalmente y fija la ciudad 0 para eliminar rotaciones equivalentes. Valida matrices cuadradas, pesos no negativos y números finitos. Impone un máximo de diez ciudades de forma intencional.

```bash
python -m src.tsp_reference
python -m unittest discover -s tests -v
```

Es un algoritmo exacto, pero el tiempo sigue creciendo factorialmente. No se presenta como optimizador logístico para producción. Conservar atribuciones del trabajo original: Andrés Olguín, Maximiliano Valdés y Enrique Chamy. Comparar con `tsp-backtracking-lab` antes de fusionar o eliminar repositorios.