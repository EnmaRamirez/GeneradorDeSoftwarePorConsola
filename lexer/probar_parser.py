"""
Script de prueba: usa el wrapper como lo hará Fredy.
"""
import sys
from antlr4 import Token
from antlr4.tree.Tree import TerminalNode
from lexer.lexer_wrapper import analizar_archivo


def imprimir_arbol(nodo, parser, nivel: int = 0) -> None:
    sangria = "  " * nivel
    if isinstance(nodo, TerminalNode):
        token = nodo.getSymbol()
        if token.type == Token.EOF:
            return
        nombre_tipo = parser.symbolicNames[token.type]
        print(f"{sangria}└─ {nombre_tipo}: '{token.text}'")
    else:
        nombre_regla = parser.ruleNames[nodo.getRuleIndex()]
        print(f"{sangria}{nombre_regla}")
        for i in range(nodo.getChildCount()):
            imprimir_arbol(nodo.getChild(i), parser, nivel + 1)


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "examples/ejemplo1.gensoft"
    resultado = analizar_archivo(ruta)

    if resultado.exitoso:
        print("✓ Análisis exitoso, sin errores.\n")
    else:
        print("=== ERRORES ENCONTRADOS ===")
        for err in resultado.errores:
            print(err)
        print(f"\nTotal: {len(resultado.errores)} error(es).")
        print("⚠ El árbol puede estar incompleto.\n")

    print("=== ÁRBOL CON INDENTACIÓN ===")
    imprimir_arbol(resultado.arbol, resultado.parser)