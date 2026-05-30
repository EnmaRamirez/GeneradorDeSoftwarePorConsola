# optimizer/rules.py
# Reglas de optimización aplicadas al AST

class OptimizationRule:
    """Clase base para las reglas de optimización"""
    name = "base_rule"
    description = "Regla base"

    def apply(self, ast: dict) -> tuple[dict, dict]:
        return ast, {}


class NormalizeValuesRule(OptimizationRule):
    """
    Optimización 1: Normaliza los valores a minúsculas.
    Ejemplo: "React" -> "react", "Python" -> "python"
    """
    name = "normalize_values"
    description = "Normaliza todos los valores de texto a minúsculas"

    def apply(self, ast: dict) -> tuple[dict, dict]:
        optimized = {}
        normalized = 0
        for key, value in ast.items():
            if isinstance(value, str):
                if key in {"name", "type"}:
                    optimized[key] = value
                else:
                    normalized_value = value.lower().strip()
                    optimized[key] = normalized_value
                    if normalized_value != value:
                        normalized += 1
            elif isinstance(value, list) and key == "dependencies":
                normalized_list = []
                for dep in value:
                    if isinstance(dep, str):
                        dep_normalized = dep.lower().strip()
                        normalized_list.append(dep_normalized)
                        if dep_normalized != dep:
                            normalized += 1
                    else:
                        normalized_list.append(dep)
                optimized[key] = normalized_list
            else:
                optimized[key] = value
        return optimized, {"normalized_values": normalized}


class RemoveDuplicateDependenciesRule(OptimizationRule):
    """
    Optimización 2: Elimina dependencias duplicadas.
    Ejemplo: ["fastapi", "fastapi", "uvicorn"] -> ["fastapi", "uvicorn"]
    """
    name = "remove_duplicate_dependencies"
    description = "Elimina dependencias duplicadas en la lista de paquetes"

    def apply(self, ast: dict) -> tuple[dict, dict]:
        optimized = ast.copy()
        removed = 0
        if "dependencies" in optimized:
            original = optimized["dependencies"]
            deduped = list(dict.fromkeys(original))
            removed = len(original) - len(deduped)
            optimized["dependencies"] = deduped
        return optimized, {"removed_duplicates": removed}


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

    def apply(self, ast: dict) -> tuple[dict, dict]:
        optimized = ast.copy()
        added = []
        for field, default in self.DEFAULTS.items():
            if field not in optimized:
                optimized[field] = default
                added.append(field)
        return optimized, {"defaults_added": added}
