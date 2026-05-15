import re

try:
    from Parser.ast_nodes import (
        ProgramNode,
        AssignmentNode,
        PrintNode,
        IdentifierNode,
        NumberNode,
        StringNode,
        BinaryOperationNode,
        EmptyNode,
    )
except ImportError:
    from ast_nodes import (
        ProgramNode,
        AssignmentNode,
        PrintNode,
        IdentifierNode,
        NumberNode,
        StringNode,
        BinaryOperationNode,
        EmptyNode,
    )


class Token:
    """
    Representa una parte pequeña del código fuente.
    Ejemplo: una palabra, un número, un signo +, un signo =, etc.
    """

    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class SimpleLexer:
    """
    Lexer sencillo para dividir el código fuente en tokens.
    Esto ayuda al parser a entender el código paso por paso.
    """

    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        token_patterns = [
            ("NUMBER", r"\d+(\.\d+)?"),
            ("STRING", r'"[^"]*"'),
            ("PRINT", r"\bprint\b"),
            ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
            ("EQUALS", r"="),
            ("PLUS", r"\+"),
            ("MINUS", r"-"),
            ("STAR", r"\*"),
            ("SLASH", r"/"),
            ("LPAREN", r"\("),
            ("RPAREN", r"\)"),
            ("NEWLINE", r"\n"),
            ("SKIP", r"[ \t]+"),
            ("MISMATCH", r"."),
        ]

        combined_regex = "|".join(
            f"(?P<{name}>{pattern})" for name, pattern in token_patterns
        )

        for match in re.finditer(combined_regex, self.source_code):
            token_type = match.lastgroup
            value = match.group()

            if token_type == "SKIP":
                continue

            if token_type == "MISMATCH":
                raise SyntaxError(f"Caracter no reconocido: {value}")

            self.tokens.append(Token(token_type, value))

        self.tokens.append(Token("EOF", None))
        return self.tokens


class SimpleParser:
    """
    Parser sencillo para construir un AST.
    Recibe tokens y los convierte en nodos del árbol.
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        return self.tokens[self.position]

    def consume(self, expected_type):
        token = self.current_token()

        if token.type == expected_type:
            self.position += 1
            return token

        raise SyntaxError(
            f"Se esperaba {expected_type}, pero se encontró {token.type}"
        )

    def parse(self):
        statements = []

        while self.current_token().type != "EOF":
            if self.current_token().type == "NEWLINE":
                self.consume("NEWLINE")
                continue

            statement = self.parse_statement()
            statements.append(statement)

            if self.current_token().type == "NEWLINE":
                self.consume("NEWLINE")

        return ProgramNode(statements)

    def parse_statement(self):
        token = self.current_token()

        if token.type == "PRINT":
            return self.parse_print()

        if token.type == "IDENTIFIER":
            next_token = self.tokens[self.position + 1]

            if next_token.type == "EQUALS":
                return self.parse_assignment()

            return self.parse_expression()

        return EmptyNode()

    def parse_assignment(self):
        variable_token = self.consume("IDENTIFIER")
        self.consume("EQUALS")
        value = self.parse_expression()

        return AssignmentNode(
            variable_name=variable_token.value,
            value=value
        )

    def parse_print(self):
        self.consume("PRINT")
        value = self.parse_expression()

        return PrintNode(value=value)

    def parse_expression(self):
        left = self.parse_term()

        while self.current_token().type in ("PLUS", "MINUS"):
            operator = self.current_token().value
            self.position += 1
            right = self.parse_term()

            left = BinaryOperationNode(
                left=left,
                operator=operator,
                right=right
            )

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.current_token().type in ("STAR", "SLASH"):
            operator = self.current_token().value
            self.position += 1
            right = self.parse_factor()

            left = BinaryOperationNode(
                left=left,
                operator=operator,
                right=right
            )

        return left

    def parse_factor(self):
        token = self.current_token()

        if token.type == "NUMBER":
            self.consume("NUMBER")
            return NumberNode(float(token.value))

        if token.type == "STRING":
            self.consume("STRING")
            return StringNode(token.value.strip('"'))

        if token.type == "IDENTIFIER":
            self.consume("IDENTIFIER")
            return IdentifierNode(token.value)

        if token.type == "LPAREN":
            self.consume("LPAREN")
            expression = self.parse_expression()
            self.consume("RPAREN")
            return expression

        raise SyntaxError(f"Token inesperado: {token.type}")


def parse_source(source_code):
    """
    Función principal que se usará desde otros archivos.
    Recibe código fuente y devuelve el AST.
    """

    lexer = SimpleLexer(source_code)
    tokens = lexer.tokenize()

    parser = SimpleParser(tokens)
    ast = parser.parse()

    return ast