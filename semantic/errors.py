# semantic/errors.py
# Clases de errores semánticos del compilador .scf

class SemanticError(Exception):
    """Error base para errores semánticos"""
    def __init__(self, message: str, line: int = None, column: int = None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self._format())

    def _format(self):
        if self.line and self.column:
            return f"[Error Semántico] Línea {self.line}, Columna {self.column}: {self.message}"
        elif self.line:
            return f"[Error Semántico] Línea {self.line}: {self.message}"
        return f"[Error Semántico]: {self.message}"


class DuplicateBlockError(SemanticError):
    """Se repite un bloque con el mismo nombre"""
    pass


class InvalidValueError(SemanticError):
    """El valor de un parámetro no es válido"""
    pass


class MissingRequiredFieldError(SemanticError):
    """Falta un campo obligatorio"""
    pass


class UnknownFrameworkError(SemanticError):
    """El framework especificado no existe"""
    pass