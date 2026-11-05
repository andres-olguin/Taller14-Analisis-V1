# tsp-bruteforce-lab — Ingeniería, pruebas y escalabilidad realista

**Estado:** plan técnico documentado el 04-11-2026. No constituye resultado experimental ejecutado.

## Evidencia de partida

TSP académico Python con fuerza bruta histórica y referencia exacta incremental que fija origen y limita cantidad de ciudades.

## Incrementos de ingeniería

Añadir tests asimétricos, validaciones de matrices y mediciones de memoria/tiempo por cantidad de ciudades. Comparar con solver por backtracking y heurísticas separadas.

## Estrategia de escalabilidad

La complejidad factorial domina: documentar tamaño máximo reproducible y exponer crecimiento exponencial en gráfica, no prometer resolver instancias grandes mediante nube.

## Riesgos y condición de aprobación

Preservar autores Andrés Olguín, Maximiliano Valdés y Enrique Chamy; no confundir ruta aproximada con óptima.

## Protocolo de experimentación y calidad

Cada comparativa debe incluir referencia de código/commit, entorno, versiones, semilla cuando corresponda, entrada reproducible, comando de ejecución, datos brutos, repetición y límites. Separar datos de ejemplo de resultados realmente ejecutados. Mantener código histórico y coautoría intactos; publicar evidencias de tests de CI y pruebas manuales en su contexto, sin inventar métricas.

## Referencias consultadas (2026-11-04)

- [AWS Well-Architected — rendimiento y costo](https://docs.aws.amazon.com/wellarchitected/).
- [NIST SSDF — prácticas seguras de software](https://csrc.nist.gov/pubs/sp/800/218/final).
- [Google SRE — medición y objetivos](https://sre.google/workbook/implementing-slos/).

Las referencias son metodológicas; no corroboran los benchmarks particulares de este repositorio.
