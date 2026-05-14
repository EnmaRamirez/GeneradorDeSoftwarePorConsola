import typer

from compiler.generator.project_generator import ProjectGenerator


app = typer.Typer()


@app.command()
def build(project_name: str):

    folders = [
        "controllers",
        "models",
        "routes"
    ]

    files = [
        "app.py",
        "requirements.txt"
    ]

    generator = ProjectGenerator(
        project_name,
        folders,
        files
    )

    generator.generate()

    print("Proyecto generado correctamente")


if __name__ == "__main__":
    app()