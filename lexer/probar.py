"""
Script de prueba del lexer.
Lee un archivo .gensoft y muestra todos los tokens reconocidos.
"""
import sys
from antlr4 import FileStream, CommonTokenStream
from grammar.generated.GenSoftLexer import GenSoftLexer


def probar_lexer(ruta_archivo: str) -> None:
    entrada = FileStream(ruta_archivo, encoding="utf-8")
    lexer = GenSoftLexer(entrada)

    print(f"{'TIPO':<20} {'TEXTO':<20} LÍNEA:COL")
    print("-" * 55)

    for token in lexer.getAllTokens():
        nombre_tipo = lexer.symbolicNames[token.type]
        print(f"{nombre_tipo:<20} {token.text:<20} {token.line}:{token.column}")


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "examples/ejemplo1.gensoft"
    probar_lexer(ruta)