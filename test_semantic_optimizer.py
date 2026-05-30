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
    ast_optimizado, optimization_stats = optimizer.optimize(ast_dict)
    optimizer.report(ast_dict, ast_optimizado, optimization_stats)

print("\n" + "=" * 50)
print(" PRUEBA CON ejemplo_con_errores.gensoft")
print("=" * 50)

resultado_errores = analizar_archivo("examples/ejemplo_con_errores.gensoft")

if not resultado_errores.exitoso:
    print(f" Errores en Lexer/Parser: {len(resultado_errores.errores)}")
    for err in resultado_errores.errores:
        print(f"  {err}")
    print("\n⚠️  El árbol puede estar incompleto, analizando semántica de todas formas...\n")

analyzer2 = SemanticAnalyzer()
analyzer2.analyze(resultado_errores.arbol)
analyzer2.report()