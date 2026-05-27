
import os


class ProjectGenerator:

    def __init__(self, project_name, folders, files, models):

        self.project_name = project_name
        self.folders = folders
        self.files = files
        self.models = models

    def generate(self):

        base_path = f"./{self.project_name}"

        os.makedirs(base_path, exist_ok=True)

        print(f"Proyecto creado: {base_path}")

        # CREAR CARPETAS
        for folder in self.folders:

            folder_path = os.path.join(base_path, folder)

            os.makedirs(folder_path, exist_ok=True)

            print(f"Carpeta creada: {folder}")

        # CREAR ARCHIVOS
        for file in self.files:

            file_path = os.path.join(base_path, file)

            with open(file_path, "w", encoding="utf-8") as f:

                # FASTAPI APP
                if file == "app.py":

                    f.write(
"""from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
"""
                    )

                # REQUIREMENTS
                elif file == "requirements.txt":

                    f.write(
"""fastapi
uvicorn
jinja2
"""
                    )

                # DOCKERFILE
                elif file == "Dockerfile":

                    f.write(
"""FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""
                    )

                # README
                elif file == "README.md":

                    f.write(
f"# {self.project_name}\n\nProyecto generado automáticamente con DSL SCF."
                    )

            print(f"Archivo creado: {file}")

        # GENERAR MODELOS
        for model_name, attributes in self.models.items():

            model_path = os.path.join(
                base_path,
                "models",
                f"{model_name.lower()}.py"
            )

            with open(model_path, "w", encoding="utf-8") as model_file:

                params = []
                assignments = []

                for attr in attributes:

                    attr_name = attr.split(":")[0].strip()

                    params.append(attr_name)

                    assignments.append(
                        f"        self.{attr_name} = {attr_name}"
                    )

                params_str = ", ".join(params)

                assignments_str = "\n".join(assignments)

                model_file.write(
f"""class {model_name}:

    def __init__(self, {params_str}):

{assignments_str}
"""
                )

            print(f"Modelo generado: {model_name}")

        # TEMPLATE HTML
        template_path = os.path.join(
            base_path,
            "templates",
            "index.html"
        )

        with open(template_path, "w", encoding="utf-8") as html:

            html.write(
"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SCF Generator</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

</head>
<body>

<div class="container mt-5">

    <div class="card shadow p-5 text-center">

        <h1 class="text-primary">
            Proyecto generado correctamente 🚀
        </h1>

        <p class="mt-3">
            Generado automáticamente con DSL SCF + FastAPI
        </p>

    </div>

</div>

</body>
</html>
"""
            )

        print("Template index.html creado")