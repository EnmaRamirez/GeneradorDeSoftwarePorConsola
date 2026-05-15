from dataclasses import dataclass, field
from typing import Any, List, Optional


class ASTNode:
    """
    Clase base para todos los nodos del AST.
    AST significa Abstract Syntax Tree, o Árbol de Sintaxis Abstracta.
    """

    def to_dict(self) -> dict:
        """
        Convierte el nodo en un diccionario para poder verlo de forma clara.
        """
        return {
            "type": self.__class__.__name__,
            **self.__dict__
        }


@dataclass
class ProgramNode(ASTNode):
    """
    Nodo principal del programa.
    Guarda todas las instrucciones que se encuentren en el código.
    """
    statements: List[ASTNode] = field(default_factory=list)


@dataclass
class AssignmentNode(ASTNode):
    """
    Representa una asignación de variable.
    Ejemplo:
        nombre = "Fredy"
        edad = 20
    """
    variable_name: str
    value: ASTNode


@dataclass
class PrintNode(ASTNode):
    """
    Representa una instrucción para mostrar información.
    Ejemplo:
        print nombre
        print "Hola mundo"
    """
    value: ASTNode


@dataclass
class IdentifierNode(ASTNode):
    """
    Representa el nombre de una variable.
    Ejemplo:
        nombre
        edad
    """
    name: str


@dataclass
class NumberNode(ASTNode):
    """
    Representa un número.
    Ejemplo:
        10
        25
        100
    """
    value: float


@dataclass
class StringNode(ASTNode):
    """
    Representa una cadena de texto.
    Ejemplo:
        "Hola"
        "Proyecto compiladores"
    """
    value: str


@dataclass
class BinaryOperationNode(ASTNode):
    """
    Representa una operación matemática.
    Ejemplo:
        5 + 3
        edad * 2
    """
    left: ASTNode
    operator: str
    right: ASTNode


@dataclass
class EmptyNode(ASTNode):
    """
    Nodo vacío.
    Sirve cuando una línea no contiene una instrucción útil.
    """
    value: Optional[Any] = None