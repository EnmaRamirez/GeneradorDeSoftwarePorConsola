# Módulo Lexer + Grammar

Responsable: Luis Gustavo

## Uso desde otros módulos

```python
from lexer.lexer_wrapper import analizar_archivo, analizar_texto

# Desde archivo
resultado = analizar_archivo("examples/ejemplo1.gensoft")

# Desde cadena
resultado = analizar_texto("proyecto Demo tipo web { } generar Demo;")

if resultado.exitoso:
    arbol = resultado.arbol      # ParserRuleContext (raíz: programa)
    parser = resultado.parser    # útil para parser.ruleNames / symbolicNames
    tokens = resultado.tokens    # CommonTokenStream
else:
    for err in resultado.errores:
        print(err)               # [fase] Línea L:C → mensaje
```

## Estructura

- `grammar/GenSoft.g4` — gramática fuente (editar aquí).
- `grammar/generated/` — código generado por ANTLR (no editar a mano).
- `lexer/lexer_wrapper.py` — API pública.
- `lexer/error_listener.py` — captura de errores en español.
- `lexer/probar_parser.py` — script de prueba.

## Regenerar tras editar la gramática

```bash
antlr4 -Dlanguage=Python3 -visitor -o grammar/generated grammar/GenSoft.g4
```