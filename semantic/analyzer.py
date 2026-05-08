# semantic/analyzer.py
# Analizador semántico del compilador .scf

from semantic.errors import (
    DuplicateBlockError,
    InvalidValueError,
    MissingRequiredFieldError,
    UnknownFrameworkError
)

# Valores permitidos por campo
VALID_LANGUAGES = ["python", "javascript", "typescript", "java"]
VALID_FRAMEWORKS = {
    "python": ["fastapi", "flask", "django"],
    "javascript": ["express", "react", "vue", "vanilla"],
    "typescript": ["express", "react", "angular", "nestjs"],
    "java": ["spring", "springboot"]
}
REQUIRED_FIELDS = ["name", "language", "framework"]


class SemanticAnalyzer:
    """
    Recibe el AST del Parser y valida que sea semánticamente correcto.
    """

    def __init__(self):
        self.errors = []
        self.warnings = []

    def analyze(self, ast: dict) -> bool:
        """
        Analiza el AST. Retorna True si no hay errores, False si los hay.
        """
        self.errors = []
        self.warnings = []

        self._check_required_fields(ast)
        self._check_duplicate_blocks(ast)
        self._check_valid_language(ast)
        self._check_valid_framework(ast)

        return len(self.errors) == 0

    def _check_required_fields(self, ast: dict):
        """Verifica que estén todos los campos obligatorios"""
        for field in REQUIRED_FIELDS:
            if field not in ast:
                self.errors.append(
                    MissingRequiredFieldError(f"El campo obligatorio '{field}' no está definido.")
                )

    def _check_duplicate_blocks(self, ast: dict):
        """Verifica que no haya bloques duplicados"""
        seen = []
        for key in ast.keys():
            if key in seen:
                self.errors.append(
                    DuplicateBlockError(f"El bloque '{key}' está duplicado.")
                )
            seen.append(key)

    def _check_valid_language(self, ast: dict):
        """Verifica que el lenguaje sea válido"""
        language = ast.get("language", "").lower()
        if language and language not in VALID_LANGUAGES:
            self.errors.append(
                InvalidValueError(
                    f"El lenguaje '{language}' no es válido. "
                    f"Opciones: {', '.join(VALID_LANGUAGES)}"
                )
            )

    def _check_valid_framework(self, ast: dict):
        """Verifica que el framework sea válido para el lenguaje dado"""
        language = ast.get("language", "").lower()
        framework = ast.get("framework", "").lower()

        if language and framework:
            allowed = VALID_FRAMEWORKS.get(language, [])
            if framework not in allowed:
                self.errors.append(
                    UnknownFrameworkError(
                        f"El framework '{framework}' no es válido para '{language}'. "
                        f"Opciones: {', '.join(allowed)}"
                    )
                )

    def report(self):
        """Imprime el reporte de errores y advertencias"""
        if not self.errors and not self.warnings:
            print("Análisis semántico completado sin errores.")
            return

        for error in self.errors:
            print(f"{error}")

        for warning in self.warnings:
            print(f"{warning}")