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

        # CREAR __init__.py
        open(os.path.join(base_path, "models", "__init__.py"), "w").close()
        open(os.path.join(base_path, "routes", "__init__.py"), "w").close()
        open(os.path.join(base_path, "controllers", "__init__.py"), "w").close()

        # CREAR ARCHIVOS
        for file in self.files:

            file_path = os.path.join(base_path, file)

            with open(file_path, "w", encoding="utf-8") as f:

                # FASTAPI APP
                if file == "app.py":

                    imports = ""
                    routers = ""

                    for model_name in self.models.keys():

                        imports += (
                            f"from routes.{model_name.lower()}_routes "
                            f"import router as {model_name.lower()}_router\n"
                        )

                        routers += (
                            f"app.include_router({model_name.lower()}_router)\n"
                        )

                    f.write(
f"""from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

{imports}

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

{routers}

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
pydantic
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
                elif file == ".dockerignore":
                    f.write(
"""venv
__pycache__
*.pyc
.git
"""
                    )



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

            # GENERAR CRUD ROUTES
            route_path = os.path.join(
                base_path,
                "routes",
                f"{model_name.lower()}_routes.py"
            )

            with open(route_path, "w", encoding="utf-8") as route_file:

                fields = []

                for attr in attributes:

                    attr_name = attr.split(":")[0].strip()
                    attr_type = attr.split(":")[1].strip()

                    python_type = "str"

                    if attr_type == "int":
                        python_type = "int"

                    elif attr_type == "float":
                        python_type = "float"

                    fields.append(
                        f"    {attr_name}: {python_type}"
                    )

                fields_str = "\n".join(fields)

                route_file.write(
f"""from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class {model_name}Schema(BaseModel):

{fields_str}


# BASE DE DATOS EN MEMORIA
{model_name.lower()}s = []


# GET ALL
@router.get("/{model_name.lower()}s")
async def get_{model_name.lower()}s():

    return {model_name.lower()}s


# CREATE
@router.post("/{model_name.lower()}s")
async def create_{model_name.lower()}(
    data: {model_name}Schema
):

    new_item = data.dict()

    {model_name.lower()}s.append(new_item)

    return {{
        "message": "{model_name} creado",
        "data": new_item
    }}


# UPDATE
@router.put("/{model_name.lower()}s/{{id}}")
async def update_{model_name.lower()}(
    id: int,
    data: {model_name}Schema
):

    updated_item = data.dict()

    for index, item in enumerate({model_name.lower()}s):

        if item.get("id") == id:

            {model_name.lower()}s[index] = updated_item

            return {{
                "message": "{model_name} actualizado",
                "data": updated_item
            }}

    return {{
        "error": "{model_name} no encontrado"
    }}


# DELETE
@router.delete("/{model_name.lower()}s/{{id}}")
async def delete_{model_name.lower()}(id: int):

    for index, item in enumerate({model_name.lower()}s):

        if item.get("id") == id:

            deleted = {model_name.lower()}s.pop(index)

            return {{
                "message": "{model_name} eliminado",
                "data": deleted
            }}

    return {{
        "error": "{model_name} no encontrado"
    }}
"""
                )

            print(f"CRUD generado: {model_name}")

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