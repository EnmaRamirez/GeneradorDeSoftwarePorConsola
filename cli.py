from pathlib import Path

import typer
from lexer.lexer_wrapper import analizar_archivo
from semantic.analyzer import SemanticAnalyzer
from optimizer.optimizer import Optimizer
from compiler.generator.project_generator import ProjectGenerator
from compiler.scf_ast import build_project_spec

app = typer.Typer(help="Generador de proyectos desde DSL GenSoft/SCF")


def _print_errors(errors):
    for err in errors:
        typer.secho(f"{err}", fg=typer.colors.RED)


# =========================================
# BUILD
# =========================================
@app.command()
def build(
    file: str = typer.Argument(..., help="Archivo .gensoft o .scf a compilar."),
    output: str = typer.Option(
        ".",
        "--output",
        "-o",
        help="Directorio de salida donde se generará el proyecto."
    ),
    optimize_level: int = typer.Option(
        0,
        "--optimize-level",
        "-O",
        min=0,
        max=2,
        help="Nivel de optimización: 0=no optimiza, 1=optimiza."
    ),
    preview: bool = typer.Option(False, "--preview", help="Muestra qué archivos se generarían sin escribirlos."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Mostrar información detallada.")
):

    file_path = Path(file)
    if not file_path.exists():
        typer.secho(f"El archivo no existe: {file}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    resultado = analizar_archivo(str(file_path))

    if not resultado.exitoso:
        typer.secho("Errores de análisis léxico/sintáctico:", fg=typer.colors.RED)
        _print_errors(resultado.errores)
        raise typer.Exit(code=1)

    analyzer = SemanticAnalyzer()
    valido = analyzer.analyze(resultado.arbol)
    if not valido:
        typer.secho("Errores semánticos:", fg=typer.colors.RED)
        analyzer.report()
        raise typer.Exit(code=1)

    spec = build_project_spec(resultado.arbol)
    if not spec["generate"]:
        typer.secho("No se encontró ningún comando 'generar' en el archivo.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    target_name = spec["generate"][0]
    project = next((p for p in spec["projects"] if p["name"] == target_name), None)
    if project is None:
        typer.secho(
            f"El proyecto a generar '{target_name}' no está declarado.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    project_data = {
        "name": project["name"],
        "type": project["project_type"],
        "modules": project["modules"],
        "dependencies": [
            "fastapi",
            "uvicorn",
            "jinja2",
            "pydantic",
            "antlr4-python3-runtime",
            "typer",
        ],
        "description": "Proyecto generado automáticamente desde DSL GenSoft/SCF.",
    }

    if optimize_level > 0:
        optimizer = Optimizer()
        optimized, optimization_stats = optimizer.optimize(project_data)
        optimizer.report(project_data, optimized, optimization_stats)
        project_data = optimized

    folders = ["controllers", "models", "routes"]
    if project_data["type"] == "web":
        folders.extend(["templates", "static"])

    files = ["app.py", "requirements.txt", "Dockerfile", "README.md", ".dockerignore"]
    models = {
        module["name"]: [f"{field['name']}:{field['type']}" for field in module["fields"]]
        for module in project_data["modules"]
    }

    if preview:
        typer.secho("Vista previa de generación:\n", fg=typer.colors.YELLOW)
        typer.secho(f"Proyecto: {project_data['name']} ({project_data['type']})", fg=typer.colors.BLUE)
        typer.secho("Carpetas:", fg=typer.colors.BLUE)
        for folder in folders:
            typer.echo(f"  - {folder}")
        typer.secho("Archivos:", fg=typer.colors.BLUE)
        for file_name in files:
            typer.echo(f"  - {file_name}")
        typer.secho("Módulos:", fg=typer.colors.BLUE)
        for module_name, attrs in models.items():
            typer.echo(f"  - {module_name}: {', '.join(attrs)}")
        raise typer.Exit()

    generator = ProjectGenerator(
        project_name=project_data["name"],
        folders=folders,
        files=files,
        models=models,
        output_dir=output,
        project_type=project_data["type"],
    )

    generator.generate()

    typer.secho("Proyecto generado correctamente.", fg=typer.colors.GREEN)


# =========================================
# CHECK
# =========================================
@app.command()
def check(
    file: str = typer.Argument(..., help="Archivo .gensoft o .scf a validar."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Mostrar información detallada.")
):

    file_path = Path(file)
    if not file_path.exists():
        typer.secho(f"El archivo no existe: {file}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    resultado = analizar_archivo(str(file_path))

    if not resultado.exitoso:
        typer.secho("Errores de análisis léxico/sintáctico:", fg=typer.colors.RED)
        _print_errors(resultado.errores)
        raise typer.Exit(code=1)

    analyzer = SemanticAnalyzer()
    valido = analyzer.analyze(resultado.arbol)
    analyzer.report()

    if not valido:
        raise typer.Exit(code=1)

    typer.secho("Archivo válido y semánticamente correcto.", fg=typer.colors.GREEN)


# =========================================
# INIT
# =========================================
@app.command()
def init(
    output: str = typer.Option(
        "proyecto.gensoft",
        "--output",
        "-o",
        help="Nombre del archivo de plantilla a crear."
    )
):

    template = """proyecto MiProyecto tipo web {
    modulo usuarios {
        campo id: entero;
        campo nombre: string;
        campo activo: booleano;
    }
}

generar MiProyecto;
"""

    with open(output, "w", encoding="utf-8") as f:
        f.write(template)

    typer.secho(f"Archivo de plantilla creado: {output}", fg=typer.colors.GREEN)


# =========================================
# TEMPLATES
# =========================================
@app.command()
def templates(
    list: bool = typer.Option(False, "--list", "-l", help="Listar templates disponibles."),
):
    """Muestra los templates disponibles o la lista de opciones."""
    templates = ["web", "api", "consola"]
    if list:
        typer.echo("Templates disponibles:")
        for template in templates:
            typer.echo(f"- {template}")
        return

    typer.echo("Use '--list' para ver los templates disponibles:")
    typer.echo("  proyectocli templates --list")


if __name__ == "__main__":
    app()