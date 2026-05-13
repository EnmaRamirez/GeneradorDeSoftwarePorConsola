# Generated from grammar/GenSoft.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GenSoftParser import GenSoftParser
else:
    from GenSoftParser import GenSoftParser

# This class defines a complete listener for a parse tree produced by GenSoftParser.
class GenSoftListener(ParseTreeListener):

    # Enter a parse tree produced by GenSoftParser#programa.
    def enterPrograma(self, ctx:GenSoftParser.ProgramaContext):
        pass

    # Exit a parse tree produced by GenSoftParser#programa.
    def exitPrograma(self, ctx:GenSoftParser.ProgramaContext):
        pass


    # Enter a parse tree produced by GenSoftParser#sentencia.
    def enterSentencia(self, ctx:GenSoftParser.SentenciaContext):
        pass

    # Exit a parse tree produced by GenSoftParser#sentencia.
    def exitSentencia(self, ctx:GenSoftParser.SentenciaContext):
        pass


    # Enter a parse tree produced by GenSoftParser#declaracionProyecto.
    def enterDeclaracionProyecto(self, ctx:GenSoftParser.DeclaracionProyectoContext):
        pass

    # Exit a parse tree produced by GenSoftParser#declaracionProyecto.
    def exitDeclaracionProyecto(self, ctx:GenSoftParser.DeclaracionProyectoContext):
        pass


    # Enter a parse tree produced by GenSoftParser#tipoProyecto.
    def enterTipoProyecto(self, ctx:GenSoftParser.TipoProyectoContext):
        pass

    # Exit a parse tree produced by GenSoftParser#tipoProyecto.
    def exitTipoProyecto(self, ctx:GenSoftParser.TipoProyectoContext):
        pass


    # Enter a parse tree produced by GenSoftParser#modulo.
    def enterModulo(self, ctx:GenSoftParser.ModuloContext):
        pass

    # Exit a parse tree produced by GenSoftParser#modulo.
    def exitModulo(self, ctx:GenSoftParser.ModuloContext):
        pass


    # Enter a parse tree produced by GenSoftParser#campo.
    def enterCampo(self, ctx:GenSoftParser.CampoContext):
        pass

    # Exit a parse tree produced by GenSoftParser#campo.
    def exitCampo(self, ctx:GenSoftParser.CampoContext):
        pass


    # Enter a parse tree produced by GenSoftParser#tipoDato.
    def enterTipoDato(self, ctx:GenSoftParser.TipoDatoContext):
        pass

    # Exit a parse tree produced by GenSoftParser#tipoDato.
    def exitTipoDato(self, ctx:GenSoftParser.TipoDatoContext):
        pass


    # Enter a parse tree produced by GenSoftParser#comandoGenerar.
    def enterComandoGenerar(self, ctx:GenSoftParser.ComandoGenerarContext):
        pass

    # Exit a parse tree produced by GenSoftParser#comandoGenerar.
    def exitComandoGenerar(self, ctx:GenSoftParser.ComandoGenerarContext):
        pass



del GenSoftParser