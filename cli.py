import typer

from compiler.generator.project_generator import ProjectGenerator

app = typer.Typer()


@app.command()
def build(config_file: str):

    with open(config_file, "r") as file:

        lines = [
            line.strip()
            for line in file.readlines()
            if line.strip()
        ]

    project_name = ""
    folders = []
    files = []
    models = {}

    mode = None
    current_model = None

    for line in lines:

        # PROJECT
        if line.startswith("project"):

            project_name = line.split(" ")[1]

        # MODOS
        elif line == "folders:":

            mode = "folders"

        elif line == "files:":

            mode = "files"

        elif line == "models:":

            mode = "models"

        # FOLDERS
        elif mode == "folders":

            folders.append(line)

        # FILES
        elif mode == "files":

            files.append(line)

        # MODELS
        elif mode == "models":

            if line.startswith("model"):

                model_name = line.split()[1].replace(":", "")

                current_model = model_name

                models[current_model] = []

            elif current_model and ":" in line:

                models[current_model].append(line)

    generator = ProjectGenerator(
        project_name,
        folders,
        files,
        models
    )

    generator.generate()

    print("Proyecto generado correctamente")


if __name__ == "__main__":

    app()