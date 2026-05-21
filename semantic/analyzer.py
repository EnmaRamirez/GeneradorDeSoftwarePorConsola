# semantic/analyzer.py
# Analizador semántico del compilador .gensoft - compatible con árbol ANTLR4

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNode
from grammar.generated.GenSoftParser import GenSoftParser
from semantic.errors import (
    DuplicateBlockError,
    InvalidValueError,
    MissingRequiredFieldError,
    UnknownFrameworkError
)

TIPOS_VALIDOS = ["string", "entero", "decimal", "booleano"]
TIPOS_PROYECTO = ["web", "consola", "api"]


class SemanticAnalyzer:
    """
    Recibe el árbol ANTLR4 y valida que sea semánticamente correcto.
    """

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.proyectos_declarados = []
        self.proyectos_a_generar = []

    def analyze(self, arbol: ParserRuleContext) -> bool:
        self.errors = []
        self.warnings = []
        self.proyectos_declarados = []
        self.proyectos_a_generar = []

        self._recorrer(arbol)
        self._check_generar_existe()

        return len(self.errors) == 0

    def _recorrer(self, nodo):
        """Recorre el árbol y valida cada nodo."""
        if isinstance(nodo, GenSoftParser.DeclaracionProyectoContext):
            self._check_proyecto(nodo)
        elif isinstance(nodo, GenSoftParser.ComandoGenerarContext):
            self._check_comando_generar(nodo)

        for i in range(nodo.getChildCount()):
            hijo = nodo.getChild(i)
            if not isinstance(hijo, TerminalNode):
                self._recorrer(hijo)

    def _check_proyecto(self, nodo: GenSoftParser.DeclaracionProyectoContext):
        """Valida un bloque proyecto."""
        if nodo.ID() is None:
            self.errors.append(
                MissingRequiredFieldError("Un proyecto no tiene nombre definido.")
            )
            return

        nombre = nodo.ID().getText()

        # Verificar proyectos duplicados
        if nombre in self.proyectos_declarados:
            self.errors.append(
                DuplicateBlockError(f"El proyecto '{nombre}' está declarado más de una vez.")
            )
        else:
            self.proyectos_declarados.append(nombre)

        # Verificar módulos duplicados dentro del proyecto
        nombres_modulos = []
        for modulo in nodo.modulo():
            if modulo.ID() is None:
                self.errors.append(
                    MissingRequiredFieldError(f"Un módulo en '{nombre}' no tiene nombre definido.")
                )
                continue
            nombre_modulo = modulo.ID().getText()
            if nombre_modulo in nombres_modulos:
                self.errors.append(
                    DuplicateBlockError(
                        f"El módulo '{nombre_modulo}' está duplicado en el proyecto '{nombre}'."
                    )
                )
            else:
                nombres_modulos.append(nombre_modulo)
                self._check_modulo(modulo, nombre)

    def _check_modulo(self, nodo: GenSoftParser.ModuloContext, nombre_proyecto: str):
        """Valida los campos dentro de un módulo."""
        nombre_modulo = nodo.ID().getText()
        nombres_campos = []

        for campo in nodo.campo():
            if campo.ID() is None or campo.tipoDato() is None:
                continue
            nombre_campo = campo.ID().getText()
            tipo = campo.tipoDato().getText()

            # Verificar campos duplicados
            if nombre_campo in nombres_campos:
                self.errors.append(
                    DuplicateBlockError(
                        f"El campo '{nombre_campo}' está duplicado en el módulo '{nombre_modulo}'."
                    )
                )
            else:
                nombres_campos.append(nombre_campo)

            # Verificar tipo de dato válido
            if tipo not in TIPOS_VALIDOS:
                self.errors.append(
                    InvalidValueError(
                        f"El tipo '{tipo}' no es válido en '{nombre_modulo}.{nombre_campo}'. "
                        f"Tipos permitidos: {', '.join(TIPOS_VALIDOS)}"
                    )
                )

    def _check_comando_generar(self, nodo: GenSoftParser.ComandoGenerarContext):
        """Registra los proyectos que se quieren generar."""
        if nodo.ID() is None:
            self.errors.append(
                MissingRequiredFieldError(
                    "El comando 'generar' no tiene un nombre de proyecto."
                )
            )
            return
        nombre = nodo.ID().getText()
        self.proyectos_a_generar.append(nombre)

    def _check_generar_existe(self):
        """Verifica que el proyecto a generar esté declarado."""
        for nombre in self.proyectos_a_generar:
            if nombre not in self.proyectos_declarados:
                self.errors.append(
                    MissingRequiredFieldError(
                        f"El comando 'generar {nombre}' hace referencia a un proyecto no declarado."
                    )
                )

    def report(self):
        if not self.errors and not self.warnings:
            print(" Análisis semántico completado sin errores.")
            return
        for error in self.errors:
            print(f" {error}")
        for warning in self.warnings:
            print(f"  {warning}")