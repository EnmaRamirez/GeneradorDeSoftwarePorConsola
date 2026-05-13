# Generated from grammar/GenSoft.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GenSoftParser import GenSoftParser
else:
    from GenSoftParser import GenSoftParser

# This class defines a complete generic visitor for a parse tree produced by GenSoftParser.

class GenSoftVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GenSoftParser#programa.
    def visitPrograma(self, ctx:GenSoftParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GenSoftParser#sentencia.
    def visitSentencia(self, ctx:GenSoftParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GenSoftParser#declaracionProyecto.
    def visitDeclaracionProyecto(self, ctx:GenSoftParser.DeclaracionProyectoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GenSoftParser#tipoProyecto.
    def visitTipoProyecto(self, ctx:GenSoftParser.TipoProyectoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GenSoftParser#modulo.
    def visitModulo(self, ctx:GenSoftParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GenSoftParser#campo.
    def visitCampo(self, ctx:GenSoftParser.CampoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GenSoftParser#tipoDato.
    def visitTipoDato(self, ctx:GenSoftParser.TipoDatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GenSoftParser#comandoGenerar.
    def visitComandoGenerar(self, ctx:GenSoftParser.ComandoGenerarContext):
        return self.visitChildren(ctx)



del GenSoftParser