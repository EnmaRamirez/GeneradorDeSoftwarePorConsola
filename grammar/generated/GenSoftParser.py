# Generated from grammar/GenSoft.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,3,
        1,3,1,4,1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,
        14,0,2,1,0,6,8,1,0,9,12,61,0,17,1,0,0,0,2,25,1,0,0,0,4,27,1,0,0,
        0,6,40,1,0,0,0,8,42,1,0,0,0,10,53,1,0,0,0,12,59,1,0,0,0,14,61,1,
        0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,
        20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,26,3,4,2,
        0,24,26,3,14,7,0,25,23,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,
        5,1,0,0,28,29,5,17,0,0,29,30,5,4,0,0,30,31,3,6,3,0,31,35,5,13,0,
        0,32,34,3,8,4,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,14,0,0,39,5,1,0,0,0,
        40,41,7,0,0,0,41,7,1,0,0,0,42,43,5,2,0,0,43,44,5,17,0,0,44,48,5,
        13,0,0,45,47,3,10,5,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,14,0,0,52,9,1,
        0,0,0,53,54,5,3,0,0,54,55,5,17,0,0,55,56,5,15,0,0,56,57,3,12,6,0,
        57,58,5,16,0,0,58,11,1,0,0,0,59,60,7,1,0,0,60,13,1,0,0,0,61,62,5,
        5,0,0,62,63,5,17,0,0,63,64,5,16,0,0,64,15,1,0,0,0,4,19,25,35,48
    ]

class GenSoftParser ( Parser ):

    grammarFileName = "GenSoft.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'proyecto'", "'modulo'", "'campo'", "'tipo'", 
                     "'generar'", "'web'", "'consola'", "'api'", "'string'", 
                     "'entero'", "'decimal'", "'booleano'", "'{'", "'}'", 
                     "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "PROYECTO", "MODULO", "CAMPO", "TIPO", 
                      "GENERAR", "WEB", "CONSOLA", "API", "STRING", "ENTERO", 
                      "DECIMAL", "BOOLEANO", "LLAVE_ABRE", "LLAVE_CIERRA", 
                      "DOS_PUNTOS", "PUNTO_COMA", "ID", "WS", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_declaracionProyecto = 2
    RULE_tipoProyecto = 3
    RULE_modulo = 4
    RULE_campo = 5
    RULE_tipoDato = 6
    RULE_comandoGenerar = 7

    ruleNames =  [ "programa", "sentencia", "declaracionProyecto", "tipoProyecto", 
                   "modulo", "campo", "tipoDato", "comandoGenerar" ]

    EOF = Token.EOF
    PROYECTO=1
    MODULO=2
    CAMPO=3
    TIPO=4
    GENERAR=5
    WEB=6
    CONSOLA=7
    API=8
    STRING=9
    ENTERO=10
    DECIMAL=11
    BOOLEANO=12
    LLAVE_ABRE=13
    LLAVE_CIERRA=14
    DOS_PUNTOS=15
    PUNTO_COMA=16
    ID=17
    WS=18
    COMENTARIO_LINEA=19
    COMENTARIO_BLOQUE=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GenSoftParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GenSoftParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(GenSoftParser.SentenciaContext,i)


        def getRuleIndex(self):
            return GenSoftParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = GenSoftParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.sentencia()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==5):
                    break

            self.state = 21
            self.match(GenSoftParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionProyecto(self):
            return self.getTypedRuleContext(GenSoftParser.DeclaracionProyectoContext,0)


        def comandoGenerar(self):
            return self.getTypedRuleContext(GenSoftParser.ComandoGenerarContext,0)


        def getRuleIndex(self):
            return GenSoftParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = GenSoftParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.declaracionProyecto()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.comandoGenerar()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionProyectoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROYECTO(self):
            return self.getToken(GenSoftParser.PROYECTO, 0)

        def ID(self):
            return self.getToken(GenSoftParser.ID, 0)

        def TIPO(self):
            return self.getToken(GenSoftParser.TIPO, 0)

        def tipoProyecto(self):
            return self.getTypedRuleContext(GenSoftParser.TipoProyectoContext,0)


        def LLAVE_ABRE(self):
            return self.getToken(GenSoftParser.LLAVE_ABRE, 0)

        def LLAVE_CIERRA(self):
            return self.getToken(GenSoftParser.LLAVE_CIERRA, 0)

        def modulo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GenSoftParser.ModuloContext)
            else:
                return self.getTypedRuleContext(GenSoftParser.ModuloContext,i)


        def getRuleIndex(self):
            return GenSoftParser.RULE_declaracionProyecto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionProyecto" ):
                listener.enterDeclaracionProyecto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionProyecto" ):
                listener.exitDeclaracionProyecto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionProyecto" ):
                return visitor.visitDeclaracionProyecto(self)
            else:
                return visitor.visitChildren(self)




    def declaracionProyecto(self):

        localctx = GenSoftParser.DeclaracionProyectoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracionProyecto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(GenSoftParser.PROYECTO)
            self.state = 28
            self.match(GenSoftParser.ID)
            self.state = 29
            self.match(GenSoftParser.TIPO)
            self.state = 30
            self.tipoProyecto()
            self.state = 31
            self.match(GenSoftParser.LLAVE_ABRE)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 32
                self.modulo()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(GenSoftParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoProyectoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WEB(self):
            return self.getToken(GenSoftParser.WEB, 0)

        def CONSOLA(self):
            return self.getToken(GenSoftParser.CONSOLA, 0)

        def API(self):
            return self.getToken(GenSoftParser.API, 0)

        def getRuleIndex(self):
            return GenSoftParser.RULE_tipoProyecto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoProyecto" ):
                listener.enterTipoProyecto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoProyecto" ):
                listener.exitTipoProyecto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoProyecto" ):
                return visitor.visitTipoProyecto(self)
            else:
                return visitor.visitChildren(self)




    def tipoProyecto(self):

        localctx = GenSoftParser.TipoProyectoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipoProyecto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULO(self):
            return self.getToken(GenSoftParser.MODULO, 0)

        def ID(self):
            return self.getToken(GenSoftParser.ID, 0)

        def LLAVE_ABRE(self):
            return self.getToken(GenSoftParser.LLAVE_ABRE, 0)

        def LLAVE_CIERRA(self):
            return self.getToken(GenSoftParser.LLAVE_CIERRA, 0)

        def campo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GenSoftParser.CampoContext)
            else:
                return self.getTypedRuleContext(GenSoftParser.CampoContext,i)


        def getRuleIndex(self):
            return GenSoftParser.RULE_modulo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo" ):
                listener.enterModulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo" ):
                listener.exitModulo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulo" ):
                return visitor.visitModulo(self)
            else:
                return visitor.visitChildren(self)




    def modulo(self):

        localctx = GenSoftParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(GenSoftParser.MODULO)
            self.state = 43
            self.match(GenSoftParser.ID)
            self.state = 44
            self.match(GenSoftParser.LLAVE_ABRE)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 45
                self.campo()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(GenSoftParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPO(self):
            return self.getToken(GenSoftParser.CAMPO, 0)

        def ID(self):
            return self.getToken(GenSoftParser.ID, 0)

        def DOS_PUNTOS(self):
            return self.getToken(GenSoftParser.DOS_PUNTOS, 0)

        def tipoDato(self):
            return self.getTypedRuleContext(GenSoftParser.TipoDatoContext,0)


        def PUNTO_COMA(self):
            return self.getToken(GenSoftParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return GenSoftParser.RULE_campo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampo" ):
                listener.enterCampo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampo" ):
                listener.exitCampo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampo" ):
                return visitor.visitCampo(self)
            else:
                return visitor.visitChildren(self)




    def campo(self):

        localctx = GenSoftParser.CampoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_campo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(GenSoftParser.CAMPO)
            self.state = 54
            self.match(GenSoftParser.ID)
            self.state = 55
            self.match(GenSoftParser.DOS_PUNTOS)
            self.state = 56
            self.tipoDato()
            self.state = 57
            self.match(GenSoftParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoDatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GenSoftParser.STRING, 0)

        def ENTERO(self):
            return self.getToken(GenSoftParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(GenSoftParser.DECIMAL, 0)

        def BOOLEANO(self):
            return self.getToken(GenSoftParser.BOOLEANO, 0)

        def getRuleIndex(self):
            return GenSoftParser.RULE_tipoDato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoDato" ):
                listener.enterTipoDato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoDato" ):
                listener.exitTipoDato(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoDato" ):
                return visitor.visitTipoDato(self)
            else:
                return visitor.visitChildren(self)




    def tipoDato(self):

        localctx = GenSoftParser.TipoDatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipoDato)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoGenerarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GENERAR(self):
            return self.getToken(GenSoftParser.GENERAR, 0)

        def ID(self):
            return self.getToken(GenSoftParser.ID, 0)

        def PUNTO_COMA(self):
            return self.getToken(GenSoftParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return GenSoftParser.RULE_comandoGenerar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoGenerar" ):
                listener.enterComandoGenerar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoGenerar" ):
                listener.exitComandoGenerar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoGenerar" ):
                return visitor.visitComandoGenerar(self)
            else:
                return visitor.visitChildren(self)




    def comandoGenerar(self):

        localctx = GenSoftParser.ComandoGenerarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comandoGenerar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(GenSoftParser.GENERAR)
            self.state = 62
            self.match(GenSoftParser.ID)
            self.state = 63
            self.match(GenSoftParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





