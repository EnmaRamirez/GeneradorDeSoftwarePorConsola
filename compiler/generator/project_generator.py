import os


class ProjectGenerator:

    def __init__(self, project_name, folders, files, models, output_dir='.', project_type='web'):
        self.project_name = project_name
        self.folders = folders
        self.files = files
        self.models = models
        self.output_dir = output_dir
        self.project_type = project_type

    def generate(self):
        base_path = os.path.abspath(os.path.join(self.output_dir, self.project_name))
        os.makedirs(base_path, exist_ok=True)

        print(f"Proyecto creado: {base_path}")

        # CREAR CARPETAS
        for folder in self.folders:
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            print(f"Carpeta creada: {folder}")

        # Crear carpetas internas necesarias
        for required in ['models', 'routes', 'controllers']:
            os.makedirs(os.path.join(base_path, required), exist_ok=True)

        if self.project_type == 'web':
            os.makedirs(os.path.join(base_path, 'templates'), exist_ok=True)
            os.makedirs(os.path.join(base_path, 'static'), exist_ok=True)

        # CREAR ARCHIVOS
        for file in self.files:
            file_path = os.path.join(base_path, file)
            with open(file_path, 'w', encoding='utf-8') as f:
                if file == 'app.py':
                    f.write(self._render_app())
                elif file == 'requirements.txt':
                    f.write(self._render_requirements())
                elif file == 'Dockerfile':
                    f.write(self._render_dockerfile())
                elif file == 'README.md':
                    f.write(self._render_readme())
                elif file == '.dockerignore':
                    f.write(self._render_dockerignore())

        if self.project_type == 'web':
            self._write_template(base_path)

        # GENERAR MODELOS Y RUTAS
        for model_name, attributes in self.models.items():
            self._write_model(base_path, model_name, attributes)
            self._write_route(base_path, model_name, attributes)

    def _render_app(self):
        if self.project_type == 'consola':
            return (
                'def main():\n'
                '    print(\'Aplicación de consola generada.\')\n'
                '    print(\'Use este archivo como punto de partida para su aplicativo.\')\n\n'
                'if __name__ == \'__main__\':\n'
                '    main()\n'
            )

        imports = []
        routers = []
        for model_name in self.models.keys():
            imports.append(
                f"from routes.{model_name.lower()}_routes import router as {model_name.lower()}_router"
            )
            routers.append(f"app.include_router({model_name.lower()}_router)")

        template_lines = ['from fastapi import FastAPI']

        if self.project_type == 'web':
            template_lines.extend([
                'from fastapi import Request',
                'from fastapi.templating import Jinja2Templates',
                'from fastapi.staticfiles import StaticFiles',
            ])

        template_lines.append('')
        template_lines.append('app = FastAPI()')
        template_lines.append('')

        if self.project_type == 'web':
            template_lines.append('templates = Jinja2Templates(directory="templates")')
            template_lines.append('app.mount("/static", StaticFiles(directory="static"), name="static")')
            template_lines.append('')

        template_lines.extend(imports)
        template_lines.append('')
        template_lines.extend(routers)
        template_lines.append('')

        if self.project_type == 'web':
            template_lines.extend([
                '@app.get("/")',
                'async def home(request: Request):',
                '    return templates.TemplateResponse(request=request, name="index.html")',
            ])
        else:
            template_lines.extend([
                '@app.get("/")',
                'async def root():',
                '    return {"status": "OK"}',
            ])

        return '\n'.join(template_lines) + '\n'

    def _render_requirements(self):
        if self.project_type == 'consola':
            return 'python>=3.11\n'

        return 'fastapi\nuvicorn\njinja2\npydantic\n'

    def _render_dockerfile(self):
        return 'FROM python:3.11\n\nWORKDIR /app\n\nCOPY . .\n\nRUN pip install -r requirements.txt\n\nCMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]\n'

    def _render_readme(self):
        return f"# {self.project_name}\n\nProyecto generado automáticamente desde DSL GenSoft/SCF.\n"

    def _render_dockerignore(self):
        return 'venv\n__pycache__\n*.pyc\n.git\n'

    def _write_template(self, base_path):
        templates_dir = os.path.join(base_path, 'templates')
        index_path = os.path.join(templates_dir, 'index.html')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(
                '<!DOCTYPE html>\n'
                '<html lang="es">\n'
                '<head>\n'
                '    <meta charset="UTF-8">\n'
                '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
                f'    <title>Proyecto {self.project_name}</title>\n'
                '</head>\n'
                '<body>\n'
                f'    <h1>Proyecto {self.project_name}</h1>\n'
                '    <p>Proyecto generado automáticamente con GenSoft DSL.</p>\n'
                '</body>\n'
                '</html>\n'
            )

    def _write_model(self, base_path, model_name, attributes):
        model_path = os.path.join(base_path, 'models', f"{model_name.lower()}.py")
        model_class_name = model_name[0].upper() + model_name[1:] if model_name else model_name
        with open(model_path, 'w', encoding='utf-8') as model_file:
            params = []
            assignments = []
            for attr in attributes:
                attr_name = attr.split(':')[0].strip()
                params.append(attr_name)
                assignments.append(f"        self.{attr_name} = {attr_name}")

            params_str = ', '.join(params)
            assignments_str = '\n'.join(assignments)
            model_file.write(
                f"class {model_class_name}:\n\n"
                f"    def __init__(self, {params_str}):\n\n"
                f"{assignments_str}\n"
            )
        print(f"Modelo generado: {model_name}")

    def _write_route(self, base_path, model_name, attributes):
        route_path = os.path.join(base_path, 'routes', f"{model_name.lower()}_routes.py")
        resource_name = model_name.lower()
        collection_name = resource_name if resource_name.endswith('s') else f"{resource_name}s"
        schema_name = model_name[0].upper() + model_name[1:] + "Schema" if model_name else "Schema"

        with open(route_path, 'w', encoding='utf-8') as route_file:
            fields = []
            for attr in attributes:
                attr_name = attr.split(':')[0].strip()
                attr_type = attr.split(':')[1].strip()
                python_type = 'str'
                if attr_type == 'entero':
                    python_type = 'int'
                elif attr_type == 'decimal':
                    python_type = 'float'
                elif attr_type == 'booleano':
                    python_type = 'bool'
                fields.append(f"    {attr_name}: {python_type}")

            fields_str = '\n'.join(fields)
            route_file.write(
                f"from fastapi import APIRouter\n"
                f"from pydantic import BaseModel\n\n"
                f"router = APIRouter()\n\n"
                f"class {schema_name}(BaseModel):\n\n"
                f"{fields_str}\n\n"
                f"{collection_name} = []\n\n"
                f"@router.get(\"/{collection_name}\")\n"
                f"async def get_{collection_name}():\n"
                f"    return {collection_name}\n\n"
                f"@router.post(\"/{collection_name}\")\n"
                f"async def create_{resource_name}(data: {schema_name}):\n"
                f"    new_item = data.dict()\n"
                f"    {collection_name}.append(new_item)\n"
                f"    return {{\"message\": \"{resource_name} creado\", \"data\": new_item}}\n\n"
                f"@router.put(\"/{collection_name}/{{id}}\")\n"
                f"async def update_{resource_name}(id: int, data: {schema_name}):\n"
                f"    updated_item = data.dict()\n"
                f"    for index, item in enumerate({collection_name}):\n"
                f"        if item.get(\"id\") == id:\n"
                f"            {collection_name}[index] = updated_item\n"
                f"            return {{\"message\": \"{resource_name} actualizado\", \"data\": updated_item}}\n\n"
                f"    return {{\"error\": \"{resource_name} no encontrado\"}}\n"
            )
