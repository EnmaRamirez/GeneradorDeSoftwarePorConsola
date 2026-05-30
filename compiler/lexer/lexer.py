from Parser.parser import SimpleLexer


class Lexer(SimpleLexer):

    def __init__(self, source_code):
        super().__init__(source_code)
