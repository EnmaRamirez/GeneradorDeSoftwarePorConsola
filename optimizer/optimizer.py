# optimizer/optimizer.py
# Optimizador principal del compilador .scf

from optimizer.rules import (
    NormalizeValuesRule,
    RemoveDuplicateDependenciesRule,
    SetDefaultValuesRule
)


class Optimizer:
    """
    Aplica las reglas de optimización al AST antes de la generación de código.
    """

    def __init__(self):
        # Reglas de optimización activas
        self.rules = [
            NormalizeValuesRule(),
            RemoveDuplicateDependenciesRule(),
            SetDefaultValuesRule()
        ]

    def optimize(self, ast: dict) -> tuple[dict, dict]:
        """
        Aplica todas las reglas al AST y retorna el AST optimizado y estadísticas.
        """
        print("\n🔧 Iniciando optimizaciones...")
        optimized_ast = ast.copy()
        stats = {}

        for rule in self.rules:
            print(f"  → Aplicando: {rule.description}")
            optimized_ast, rule_stats = rule.apply(optimized_ast)
            stats[rule.name] = rule_stats

        print("Optimizaciones completadas.\n")
        return optimized_ast, stats

    def report(self, original: dict, optimized: dict, stats: dict | None = None):
        """
        Muestra un reporte comparando el AST original vs el optimizado.
        """
        print("Reporte de Optimización:")
        try:
            orig_len = len(original)
        except Exception:
            orig_len = "n/a"
        try:
            opt_len = len(optimized)
        except Exception:
            opt_len = "n/a"

        print(f"  Campos originales : {orig_len}")
        print(f"  Campos optimizados: {opt_len}")

        if stats:
            for rule_name, rule_stats in stats.items():
                if rule_name == "normalize_values":
                    print(f"  ⚡ Valores normalizados: {rule_stats.get('normalized_values', 0)}")
                elif rule_name == "remove_duplicate_dependencies":
                    print(f"  ⚡ Dependencias duplicadas removidas: {rule_stats.get('removed_duplicates', 0)}")
                elif rule_name == "set_default_values":
                    added = rule_stats.get('defaults_added', [])
                    if added:
                        print(f"  ⚡ Valores por defecto agregados: {', '.join(added)}")
                    else:
                        print("  ⚡ No se agregaron valores por defecto.")

        # Sólo intentar comparación campo-a-campo si ambos son diccionarios
        if isinstance(original, dict) and isinstance(optimized, dict):
            for key in optimized:
                try:
                    in_orig = key in original
                except TypeError:
                    in_orig = False

                if not in_orig:
                    # Evitamos intentar indexar si la clave no existe o no es hashable
                    val = optimized.get(key, optimized[key] if hasattr(optimized, '__getitem__') else repr(key))
                    print(f"  ✚ Campo agregado  : '{key}' = '{val}'")
                else:
                    if original.get(key) != optimized.get(key):
                        print(f"  ✎ Campo modificado: '{key}' = '{original.get(key)}' → '{optimized.get(key)}'")
        else:
            print(f"  Comparación campo-a-campo omitida: tipos originales/optimizado = {type(original).__name__}/{type(optimized).__name__}")
