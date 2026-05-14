import os


class ProjectGenerator:

    def __init__(self, project_name, folders, files):

        self.project_name = project_name
        self.folders = folders
        self.files = files

    def generate(self, output_path="."):

        project_path = os.path.join(
            output_path,
            self.project_name
        )

        os.makedirs(project_path, exist_ok=True)

        print(f"Proyecto creado: {project_path}")

        self.create_folders(project_path)
        self.create_files(project_path)

    def create_folders(self, project_path):

        for folder in self.folders:

            folder_path = os.path.join(
                project_path,
                folder
            )

            os.makedirs(folder_path, exist_ok=True)

            print(f"Carpeta creada: {folder}")

    def create_files(self, project_path):

        for file_name in self.files:

            file_path = os.path.join(
                project_path,
                file_name
            )

            with open(file_path, "w", encoding="utf-8") as file:
                file.write("")

            print(f"Archivo creado: {file_name}")