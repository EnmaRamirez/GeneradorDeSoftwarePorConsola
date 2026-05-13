"""
API pública del módulo Lexer + Grammar.

Uso desde el módulo Parser (Fredy):

    from lexer.lexer_wrapper import analizar_archivo

    resultado = analizar_archivo("examples/ejemplo1.gensoft")

    if resultado.exitoso:
        arbol = resultado.arbol     # árbol sintáctico de ANTLR
        # ... construir el AST a partir de aquí
    else:
        for err in resultado.errores:
            print(err)
"""
from dataclasses import dataclass, field
from antlr4 import FileStream, InputStream, CommonTokenStream
from antlr4.ParserRuleContext import ParserRuleContext

from grammar.generated.GenSoftLexer import GenSoftLexer
from grammar.generated.GenSoftParser import GenSoftParser
from lexer.error_listener import ListenerErroresGenSoft, ErrorGenSoft


@dataclass
class ResultadoAnalisis:
    """Resultado del análisis léxico y sintáctico."""
    arbol: ParserRuleContext | None
    tokens: CommonTokenStream | None
    parser: GenSoftParser | None
    errores: list[ErrorGenSoft] = field(default_factory=list)

    @property
    def exitoso(self) -> bool:
        return len(self.errores) == 0


def analizar_archivo(ruta: str) -> ResultadoAnalisis:
    """Analiza un archivo .gensoft y devuelve el resultado."""
    return _analizar(FileStream(ruta, encoding="utf-8"))


def analizar_texto(texto: str) -> ResultadoAnalisis:
    """Analiza una cadena de texto y devuelve el resultado."""
    return _analizar(InputStream(texto))


def _analizar(entrada) -> ResultadoAnalisis:
    # Lexer
    lexer = GenSoftLexer(entrada)
    errores_lexer = ListenerErroresGenSoft(fase="lexer")
    lexer.removeErrorListeners()
    lexer.addErrorListener(errores_lexer)

    tokens = CommonTokenStream(lexer)

    # Parser
    parser = GenSoftParser(tokens)
    errores_parser = ListenerErroresGenSoft(fase="parser")
    parser.removeErrorListeners()
    parser.addErrorListener(errores_parser)

    arbol = parser.programa()

    return ResultadoAnalisis(
        arbol=arbol,
        tokens=tokens,
        parser=parser,
        errores=errores_lexer.errores + errores_parser.errores,
    )