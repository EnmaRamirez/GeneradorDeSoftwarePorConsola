"""
Manejo de errores para el análisis léxico y sintáctico.
"""
from dataclasses import dataclass
from antlr4.error.ErrorListener import ErrorListener


@dataclass
class ErrorGenSoft:
    """Representa un error detectado durante el análisis."""
    fase: str          # 'lexer' o 'parser'
    linea: int
    columna: int
    mensaje: str

    def __str__(self) -> str:
        return f"[{self.fase}] Línea {self.linea}:{self.columna} → {self.mensaje}"


class ListenerErroresGenSoft(ErrorListener):
    """Captura errores del lexer y parser en una lista común."""

    # Traducciones de los mensajes más frecuentes de ANTLR
    _TRADUCCIONES = {
        "missing": "falta",
        "extraneous input": "entrada inesperada",
        "mismatched input": "símbolo inesperado",
        "no viable alternative at input": "construcción no válida en",
        "expecting": "se esperaba",
        "token recognition error at": "carácter no reconocido en",
        " at ": " en ",
    }

    def __init__(self, fase: str):
        super().__init__()
        self.fase = fase
        self.errores: list[ErrorGenSoft] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        mensaje = self._traducir(msg)
        self.errores.append(ErrorGenSoft(self.fase, line, column, mensaje))

    @classmethod
    def _traducir(cls, msg: str) -> str:
        for ingles, espanol in cls._TRADUCCIONES.items():
            msg = msg.replace(ingles, espanol)
        return msg

    @property
    def hay_errores(self) -> bool:
        return len(self.errores) > 0