# Generador de Proyectos de Software por Consola
Proyecto desarrollado para el curso de Compiladores.
El sistema permite generar automáticamente estructuras base de proyectos de software utilizando una herramienta CLI (Command Line Interface).

---

## Tecnologías utilizadas
- Python 3.11
- ANTLR4
- Typer
- Git y GitHub

---

## Estructura del proyecto

```
GeneradorDeSoftwarePorConsola/
│
├── semantic/
│   ├── analyzer.py
│   └── errors.py
│
├── optimizer/
│   ├── optimizer.py
│   └── rules.py
│
├── examples/
│   └── ejemplo1.gensoft
│
├── requirements.txt
└── README.md
```

---

## Módulo: Análisis Semántico

El analizador semántico recibe el árbol generado por ANTLR4 y valida que el código `.gensoft` sea lógicamente correcto.

Validaciones implementadas:
- Proyectos duplicados
- Módulos duplicados dentro de un proyecto
- Campos duplicados dentro de un módulo
- Tipos de datos válidos
- Comando `generar` referencia a un proyecto declarado

---

## Módulo: Optimizador

El optimizador aplica mejoras al AST antes de la generación de código.

Optimizaciones implementadas:
- Normalización de valores a minúsculas
- Eliminación de dependencias duplicadas
- Asignación de valores por defecto