from Parser.parser import parse_source


def mostrar_ast(nodo, nivel=0):
    """
    Muestra el AST en forma de árbol para que sea fácil de leer.
    """
    espacio = "  " * nivel
    nombre_clase = nodo.__class__.__name__

    print(f"{espacio}{nombre_clase}")

    for atributo, valor in nodo.__dict__.items():
        if isinstance(valor, list):
            print(f"{espacio}  {atributo}:")
            for item in valor:
                mostrar_ast(item, nivel + 2)
        elif hasattr(valor, "__dict__"):
            print(f"{espacio}  {atributo}:")
            mostrar_ast(valor, nivel + 2)
        else:
            print(f"{espacio}  {atributo}: {valor}")


codigo_prueba = """
nombre = "Fredy"
edad = 20
resultado = edad + 5
print nombre
print resultado
"""

ast = parse_source(codigo_prueba)

print("Código fuente analizado:")
print(codigo_prueba)

print("\nAST generado:")
mostrar_ast(ast)