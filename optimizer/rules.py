# optimizer/rules.py
# Reglas de optimización aplicadas al AST

class OptimizationRule:
    """Clase base para las reglas de optimización"""
    name = "base_rule"
    description = "Regla base"

    def apply(self, ast: dict) -> dict:
        return ast


class NormalizeValuesRule(OptimizationRule):
    """
    Optimización 1: Normaliza los valores a minúsculas.
    Ejemplo: "React" -> "react", "Python" -> "python"
    """
    name = "normalize_values"
    description = "Normaliza todos los valores de texto a minúsculas"

    def apply(self, ast: dict) -> dict:
        optimized = {}
        for key, value in ast.items():
            if isinstance(value, str):
                optimized[key] = value.lower().strip()
            else:
                optimized[key] = value
        return optimized


class RemoveDuplicateDependenciesRule(OptimizationRule):
    """
    Optimización 2: Elimina dependencias duplicadas.
    Ejemplo: ["fastapi", "fastapi", "uvicorn"] -> ["fastapi", "uvicorn"]
    """
    name = "remove_duplicate_dependencies"
    description = "Elimina dependencias duplicadas en la lista de paquetes"

    def apply(self, ast: dict) -> dict:
        optimized = ast.copy()
        if "dependencies" in optimized:
            original = optimized["dependencies"]
            optimized["dependencies"] = list(dict.fromkeys(original))
            if len(original) != len(optimized["dependencies"]):
                print(f"⚡ Dependencias duplicadas eliminadas: {len(original) - len(optimized['dependencies'])} removidas")
        return optimized


class SetDefaultValuesRule(OptimizationRule):
    """
    Optimización 3: Asigna valores por defecto a campos opcionales no definidos.
    Ejemplo: si no se define 'version', se asigna '1.0.0'
    """
    name = "set_default_values"
    description = "Asigna valores por defecto a campos opcionales"

    DEFAULTS = {
        "version": "1.0.0",
        "author": "unknown",
        "description": "Proyecto generado por GeneradorDeSoftwarePorConsola",
        "output": "./output"
    }

    def apply(self, ast: dict) -> dict:
        optimized = ast.copy()
        for field, default in self.DEFAULTS.items():
            if field not in optimized:
                optimized[field] = default
                print(f" Valor por defecto asignado: '{field}' = '{default}'")
        return optimized