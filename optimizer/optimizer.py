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

    def optimize(self, ast: dict) -> dict:
        """
        Aplica todas las reglas al AST y retorna el AST optimizado.
        """
        print("\n🔧 Iniciando optimizaciones...")
        optimized_ast = ast.copy()

        for rule in self.rules:
            print(f"  → Aplicando: {rule.description}")
            optimized_ast = rule.apply(optimized_ast)

        print("Optimizaciones completadas.\n")
        return optimized_ast

    def report(self, original: dict, optimized: dict):
        """
        Muestra un reporte comparando el AST original vs el optimizado.
        """
        print("Reporte de Optimización:")
        print(f"  Campos originales : {len(original)}")
        print(f"  Campos optimizados: {len(optimized)}")

        for key in optimized:
            if key not in original:
                print(f"  ✚ Campo agregado  : '{key}' = '{optimized[key]}'")
            elif original[key] != optimized[key]:
                print(f"  ✎ Campo modificado: '{key}' = '{original[key]}' → '{optimized[key]}'")