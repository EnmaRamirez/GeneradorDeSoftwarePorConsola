# test_semantic_optimizer.py
# Prueba básica del analizador semántico y optimizador

from semantic.analyzer import SemanticAnalyzer
from optimizer.optimizer import Optimizer

# AST de prueba simulando lo que vendría del Parser
ast_prueba = {
    "name": "MiProyecto",
    "language": "Python",
    "framework": "FastAPI",
    "version": "1.0.0",
    "dependencies": ["fastapi", "uvicorn", "fastapi"]
}

print("=" * 50)
print("ANÁLISIS SEMÁNTICO")
print("=" * 50)

analyzer = SemanticAnalyzer()
resultado = analyzer.analyze(ast_prueba)
analyzer.report()

print("\n" + "=" * 50)
print("OPTIMIZADOR")
print("=" * 50)

optimizer = Optimizer()
ast_optimizado = optimizer.optimize(ast_prueba)
optimizer.report(ast_prueba, ast_optimizado)

print("\n AST Final:")
for key, value in ast_optimizado.items():
    print(f"  {key}: {value}")