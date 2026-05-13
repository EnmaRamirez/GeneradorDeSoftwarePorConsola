# test_semantic_optimizer.py
# Prueba del analizador semántico con el árbol real de ANTLR4

from lexer.lexer_wrapper import analizar_archivo
from semantic.analyzer import SemanticAnalyzer
from optimizer.optimizer import Optimizer

print("=" * 50)
print("PRUEBA CON ejemplo1.gensoft")
print("=" * 50)

# Paso 1: Lexer + Parser
resultado = analizar_archivo("examples/ejemplo1.gensoft")

if not resultado.exitoso:
    print("Errores en Lexer/Parser:")
    for err in resultado.errores:
        print(f"  {err}")
else:
    print("Lexer/Parser sin errores.\n")

    # Paso 2: Análisis Semántico
    print("=" * 50)
    print("ANÁLISIS SEMÁNTICO")
    print("=" * 50)
    analyzer = SemanticAnalyzer()
    analyzer.analyze(resultado.arbol)
    analyzer.report()

    # Paso 3: Optimizador con datos extraídos del árbol
    print("\n" + "=" * 50)
    print("⚡ OPTIMIZADOR")
    print("=" * 50)

    ast_dict = {
        "proyectos": analyzer.proyectos_declarados,
        "a_generar": analyzer.proyectos_a_generar,
        "language": "Python",
        "framework": "FastAPI",
        "dependencies": ["antlr4-python3-runtime", "typer", "antlr4-python3-runtime"]
    }

    optimizer = Optimizer()
    ast_optimizado = optimizer.optimize(ast_dict)
    optimizer.report(ast_dict, ast_optimizado)