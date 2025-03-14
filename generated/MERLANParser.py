# Generated from grammar/MERLAN.g4 by ANTLR 4.13.2
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
        4,1,23,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,3,0,36,8,0,1,0,3,0,39,8,0,1,0,
        3,0,42,8,0,1,0,3,0,45,8,0,1,0,1,0,1,1,1,1,1,1,3,1,52,8,1,1,1,3,1,
        55,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,66,8,3,10,3,12,3,
        69,9,3,1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,5,1,5,1,5,5,5,82,
        8,5,10,5,12,5,85,9,5,1,6,1,6,1,6,5,6,90,8,6,10,6,12,6,93,9,6,1,7,
        1,7,1,7,4,7,98,8,7,11,7,12,7,99,1,8,1,8,1,8,1,8,1,9,1,9,3,9,108,
        8,9,1,10,1,10,1,10,4,10,113,8,10,11,10,12,10,114,1,10,1,10,1,10,
        3,10,120,8,10,1,11,1,11,3,11,124,8,11,1,12,1,12,3,12,128,8,12,1,
        12,1,12,5,12,132,8,12,10,12,12,12,135,9,12,1,13,1,13,1,13,5,13,140,
        8,13,10,13,12,13,143,9,13,1,14,1,14,3,14,147,8,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,0,3,2,0,11,13,15,16,1,0,8,9,2,0,14,14,18,18,158,
        0,35,1,0,0,0,2,48,1,0,0,0,4,56,1,0,0,0,6,62,1,0,0,0,8,70,1,0,0,0,
        10,78,1,0,0,0,12,86,1,0,0,0,14,94,1,0,0,0,16,101,1,0,0,0,18,107,
        1,0,0,0,20,119,1,0,0,0,22,123,1,0,0,0,24,125,1,0,0,0,26,136,1,0,
        0,0,28,144,1,0,0,0,30,151,1,0,0,0,32,154,1,0,0,0,34,36,5,19,0,0,
        35,34,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,39,3,2,1,0,38,37,1,
        0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,42,3,14,7,0,41,40,1,0,0,0,41,
        42,1,0,0,0,42,44,1,0,0,0,43,45,5,19,0,0,44,43,1,0,0,0,44,45,1,0,
        0,0,45,46,1,0,0,0,46,47,5,0,0,1,47,1,1,0,0,0,48,49,5,4,0,0,49,51,
        5,19,0,0,50,52,3,6,3,0,51,50,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,
        53,55,3,10,5,0,54,53,1,0,0,0,54,55,1,0,0,0,55,3,1,0,0,0,56,57,5,
        21,0,0,57,58,5,11,0,0,58,59,5,22,0,0,59,60,7,0,0,0,60,61,5,19,0,
        0,61,5,1,0,0,0,62,63,5,5,0,0,63,67,5,19,0,0,64,66,3,8,4,0,65,64,
        1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,7,1,0,0,0,69,
        67,1,0,0,0,70,71,5,11,0,0,71,75,5,19,0,0,72,74,3,4,2,0,73,72,1,0,
        0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,9,1,0,0,0,77,75,
        1,0,0,0,78,79,5,6,0,0,79,83,5,19,0,0,80,82,3,12,6,0,81,80,1,0,0,
        0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,11,1,0,0,0,85,83,
        1,0,0,0,86,87,5,11,0,0,87,91,5,19,0,0,88,90,3,4,2,0,89,88,1,0,0,
        0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,13,1,0,0,0,93,91,
        1,0,0,0,94,95,5,7,0,0,95,97,5,19,0,0,96,98,3,16,8,0,97,96,1,0,0,
        0,98,99,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,15,1,0,0,0,101,
        102,5,11,0,0,102,103,5,19,0,0,103,104,3,18,9,0,104,17,1,0,0,0,105,
        108,3,20,10,0,106,108,3,22,11,0,107,105,1,0,0,0,107,106,1,0,0,0,
        108,19,1,0,0,0,109,110,7,1,0,0,110,112,5,19,0,0,111,113,3,18,9,0,
        112,111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,
        115,120,1,0,0,0,116,117,5,10,0,0,117,118,5,19,0,0,118,120,3,18,9,
        0,119,109,1,0,0,0,119,116,1,0,0,0,120,21,1,0,0,0,121,124,3,26,13,
        0,122,124,3,24,12,0,123,121,1,0,0,0,123,122,1,0,0,0,124,23,1,0,0,
        0,125,127,5,5,0,0,126,128,3,28,14,0,127,126,1,0,0,0,127,128,1,0,
        0,0,128,129,1,0,0,0,129,133,5,19,0,0,130,132,3,4,2,0,131,130,1,0,
        0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,25,1,0,0,
        0,135,133,1,0,0,0,136,137,5,6,0,0,137,141,5,19,0,0,138,140,3,4,2,
        0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,
        0,142,27,1,0,0,0,143,141,1,0,0,0,144,146,5,1,0,0,145,147,3,30,15,
        0,146,145,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,3,32,16,
        0,149,150,5,2,0,0,150,29,1,0,0,0,151,152,5,14,0,0,152,153,5,3,0,
        0,153,31,1,0,0,0,154,155,7,2,0,0,155,33,1,0,0,0,19,35,38,41,44,51,
        54,67,75,83,91,99,107,114,119,123,127,133,141,146
    ]

class MERLANParser ( Parser ):

    grammarFileName = "MERLAN.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'..'", "'ENTITIES'", "'CONCRETE'", 
                     "'ABSTRACT'", "'REQUIREMENTS'", "'AND'", "'OR'", "'NOT'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'?'", "<INVALID>", "'*'", "<INVALID>", 
                     "<INVALID>", "'- '", "': '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENTITIES", "CONCRETE", "ABSTRACT", "REQUIREMENTS", 
                      "AND", "OR", "NOT", "ID", "STRING", "FLOAT", "INT_NONZERO", 
                      "INT", "UNK", "SIGINT", "STAR", "NEWLINE", "WS", "HYPHEN", 
                      "COLON", "COMMENT" ]

    RULE_script = 0
    RULE_entities = 1
    RULE_attribute = 2
    RULE_concrete_entities = 3
    RULE_concrete_entity = 4
    RULE_abstract_entities = 5
    RULE_abstract_entity = 6
    RULE_requirements = 7
    RULE_requirement_definition = 8
    RULE_requirement = 9
    RULE_complex_requirement = 10
    RULE_simple_requirement = 11
    RULE_concrete_requirement = 12
    RULE_abstract_requirement = 13
    RULE_cardinality = 14
    RULE_min_cardinality = 15
    RULE_max_cardinality = 16

    ruleNames =  [ "script", "entities", "attribute", "concrete_entities", 
                   "concrete_entity", "abstract_entities", "abstract_entity", 
                   "requirements", "requirement_definition", "requirement", 
                   "complex_requirement", "simple_requirement", "concrete_requirement", 
                   "abstract_requirement", "cardinality", "min_cardinality", 
                   "max_cardinality" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ENTITIES=4
    CONCRETE=5
    ABSTRACT=6
    REQUIREMENTS=7
    AND=8
    OR=9
    NOT=10
    ID=11
    STRING=12
    FLOAT=13
    INT_NONZERO=14
    INT=15
    UNK=16
    SIGINT=17
    STAR=18
    NEWLINE=19
    WS=20
    HYPHEN=21
    COLON=22
    COMMENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MERLANParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MERLANParser.NEWLINE)
            else:
                return self.getToken(MERLANParser.NEWLINE, i)

        def entities(self):
            return self.getTypedRuleContext(MERLANParser.EntitiesContext,0)


        def requirements(self):
            return self.getTypedRuleContext(MERLANParser.RequirementsContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = MERLANParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 34
                self.match(MERLANParser.NEWLINE)


            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 37
                self.entities()


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 40
                self.requirements()


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 43
                self.match(MERLANParser.NEWLINE)


            self.state = 46
            self.match(MERLANParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntitiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTITIES(self):
            return self.getToken(MERLANParser.ENTITIES, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def concrete_entities(self):
            return self.getTypedRuleContext(MERLANParser.Concrete_entitiesContext,0)


        def abstract_entities(self):
            return self.getTypedRuleContext(MERLANParser.Abstract_entitiesContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_entities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntities" ):
                listener.enterEntities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntities" ):
                listener.exitEntities(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntities" ):
                return visitor.visitEntities(self)
            else:
                return visitor.visitChildren(self)




    def entities(self):

        localctx = MERLANParser.EntitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MERLANParser.ENTITIES)
            self.state = 49
            self.match(MERLANParser.NEWLINE)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 50
                self.concrete_entities()


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 53
                self.abstract_entities()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HYPHEN(self):
            return self.getToken(MERLANParser.HYPHEN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MERLANParser.ID)
            else:
                return self.getToken(MERLANParser.ID, i)

        def COLON(self):
            return self.getToken(MERLANParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def STRING(self):
            return self.getToken(MERLANParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(MERLANParser.FLOAT, 0)

        def INT(self):
            return self.getToken(MERLANParser.INT, 0)

        def UNK(self):
            return self.getToken(MERLANParser.UNK, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = MERLANParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MERLANParser.HYPHEN)
            self.state = 57
            self.match(MERLANParser.ID)
            self.state = 58
            self.match(MERLANParser.COLON)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 60
            self.match(MERLANParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concrete_entitiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCRETE(self):
            return self.getToken(MERLANParser.CONCRETE, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def concrete_entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Concrete_entityContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Concrete_entityContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_concrete_entities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcrete_entities" ):
                listener.enterConcrete_entities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcrete_entities" ):
                listener.exitConcrete_entities(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcrete_entities" ):
                return visitor.visitConcrete_entities(self)
            else:
                return visitor.visitChildren(self)




    def concrete_entities(self):

        localctx = MERLANParser.Concrete_entitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_concrete_entities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(MERLANParser.CONCRETE)
            self.state = 63
            self.match(MERLANParser.NEWLINE)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 64
                self.concrete_entity()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concrete_entityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.AttributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.AttributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_concrete_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcrete_entity" ):
                listener.enterConcrete_entity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcrete_entity" ):
                listener.exitConcrete_entity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcrete_entity" ):
                return visitor.visitConcrete_entity(self)
            else:
                return visitor.visitChildren(self)




    def concrete_entity(self):

        localctx = MERLANParser.Concrete_entityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_concrete_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MERLANParser.ID)
            self.state = 71
            self.match(MERLANParser.NEWLINE)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 72
                self.attribute()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abstract_entitiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABSTRACT(self):
            return self.getToken(MERLANParser.ABSTRACT, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def abstract_entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Abstract_entityContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Abstract_entityContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_abstract_entities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstract_entities" ):
                listener.enterAbstract_entities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstract_entities" ):
                listener.exitAbstract_entities(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstract_entities" ):
                return visitor.visitAbstract_entities(self)
            else:
                return visitor.visitChildren(self)




    def abstract_entities(self):

        localctx = MERLANParser.Abstract_entitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_abstract_entities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MERLANParser.ABSTRACT)
            self.state = 79
            self.match(MERLANParser.NEWLINE)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 80
                self.abstract_entity()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abstract_entityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.AttributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.AttributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_abstract_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstract_entity" ):
                listener.enterAbstract_entity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstract_entity" ):
                listener.exitAbstract_entity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstract_entity" ):
                return visitor.visitAbstract_entity(self)
            else:
                return visitor.visitChildren(self)




    def abstract_entity(self):

        localctx = MERLANParser.Abstract_entityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_abstract_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(MERLANParser.ID)
            self.state = 87
            self.match(MERLANParser.NEWLINE)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 88
                self.attribute()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIREMENTS(self):
            return self.getToken(MERLANParser.REQUIREMENTS, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def requirement_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Requirement_definitionContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Requirement_definitionContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_requirements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirements" ):
                listener.enterRequirements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirements" ):
                listener.exitRequirements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirements" ):
                return visitor.visitRequirements(self)
            else:
                return visitor.visitChildren(self)




    def requirements(self):

        localctx = MERLANParser.RequirementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_requirements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MERLANParser.REQUIREMENTS)
            self.state = 95
            self.match(MERLANParser.NEWLINE)
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.requirement_definition()
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Requirement_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def requirement(self):
            return self.getTypedRuleContext(MERLANParser.RequirementContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_requirement_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirement_definition" ):
                listener.enterRequirement_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirement_definition" ):
                listener.exitRequirement_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirement_definition" ):
                return visitor.visitRequirement_definition(self)
            else:
                return visitor.visitChildren(self)




    def requirement_definition(self):

        localctx = MERLANParser.Requirement_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_requirement_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MERLANParser.ID)
            self.state = 102
            self.match(MERLANParser.NEWLINE)
            self.state = 103
            self.requirement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complex_requirement(self):
            return self.getTypedRuleContext(MERLANParser.Complex_requirementContext,0)


        def simple_requirement(self):
            return self.getTypedRuleContext(MERLANParser.Simple_requirementContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirement" ):
                listener.enterRequirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirement" ):
                listener.exitRequirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirement" ):
                return visitor.visitRequirement(self)
            else:
                return visitor.visitChildren(self)




    def requirement(self):

        localctx = MERLANParser.RequirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_requirement)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.complex_requirement()
                pass
            elif token in [5, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.simple_requirement()
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


    class Complex_requirementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def AND(self):
            return self.getToken(MERLANParser.AND, 0)

        def OR(self):
            return self.getToken(MERLANParser.OR, 0)

        def requirement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.RequirementContext)
            else:
                return self.getTypedRuleContext(MERLANParser.RequirementContext,i)


        def NOT(self):
            return self.getToken(MERLANParser.NOT, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_complex_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplex_requirement" ):
                listener.enterComplex_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplex_requirement" ):
                listener.exitComplex_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplex_requirement" ):
                return visitor.visitComplex_requirement(self)
            else:
                return visitor.visitChildren(self)




    def complex_requirement(self):

        localctx = MERLANParser.Complex_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_complex_requirement)
        self._la = 0 # Token type
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.match(MERLANParser.NEWLINE)
                self.state = 112 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 111
                        self.requirement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 114 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(MERLANParser.NOT)
                self.state = 117
                self.match(MERLANParser.NEWLINE)
                self.state = 118
                self.requirement()
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


    class Simple_requirementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def abstract_requirement(self):
            return self.getTypedRuleContext(MERLANParser.Abstract_requirementContext,0)


        def concrete_requirement(self):
            return self.getTypedRuleContext(MERLANParser.Concrete_requirementContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_simple_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_requirement" ):
                listener.enterSimple_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_requirement" ):
                listener.exitSimple_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_requirement" ):
                return visitor.visitSimple_requirement(self)
            else:
                return visitor.visitChildren(self)




    def simple_requirement(self):

        localctx = MERLANParser.Simple_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_simple_requirement)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.abstract_requirement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.concrete_requirement()
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


    class Concrete_requirementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCRETE(self):
            return self.getToken(MERLANParser.CONCRETE, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def cardinality(self):
            return self.getTypedRuleContext(MERLANParser.CardinalityContext,0)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.AttributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.AttributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_concrete_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcrete_requirement" ):
                listener.enterConcrete_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcrete_requirement" ):
                listener.exitConcrete_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcrete_requirement" ):
                return visitor.visitConcrete_requirement(self)
            else:
                return visitor.visitChildren(self)




    def concrete_requirement(self):

        localctx = MERLANParser.Concrete_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_concrete_requirement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MERLANParser.CONCRETE)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 126
                self.cardinality()


            self.state = 129
            self.match(MERLANParser.NEWLINE)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 130
                self.attribute()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abstract_requirementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABSTRACT(self):
            return self.getToken(MERLANParser.ABSTRACT, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.AttributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.AttributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_abstract_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstract_requirement" ):
                listener.enterAbstract_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstract_requirement" ):
                listener.exitAbstract_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstract_requirement" ):
                return visitor.visitAbstract_requirement(self)
            else:
                return visitor.visitChildren(self)




    def abstract_requirement(self):

        localctx = MERLANParser.Abstract_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_abstract_requirement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MERLANParser.ABSTRACT)
            self.state = 137
            self.match(MERLANParser.NEWLINE)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 138
                self.attribute()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CardinalityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def max_cardinality(self):
            return self.getTypedRuleContext(MERLANParser.Max_cardinalityContext,0)


        def min_cardinality(self):
            return self.getTypedRuleContext(MERLANParser.Min_cardinalityContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_cardinality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCardinality" ):
                listener.enterCardinality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCardinality" ):
                listener.exitCardinality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCardinality" ):
                return visitor.visitCardinality(self)
            else:
                return visitor.visitChildren(self)




    def cardinality(self):

        localctx = MERLANParser.CardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cardinality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(MERLANParser.T__0)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 145
                self.min_cardinality()


            self.state = 148
            self.max_cardinality()
            self.state = 149
            self.match(MERLANParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Min_cardinalityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NONZERO(self):
            return self.getToken(MERLANParser.INT_NONZERO, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_min_cardinality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMin_cardinality" ):
                listener.enterMin_cardinality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMin_cardinality" ):
                listener.exitMin_cardinality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMin_cardinality" ):
                return visitor.visitMin_cardinality(self)
            else:
                return visitor.visitChildren(self)




    def min_cardinality(self):

        localctx = MERLANParser.Min_cardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_min_cardinality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MERLANParser.INT_NONZERO)
            self.state = 152
            self.match(MERLANParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Max_cardinalityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NONZERO(self):
            return self.getToken(MERLANParser.INT_NONZERO, 0)

        def STAR(self):
            return self.getToken(MERLANParser.STAR, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_max_cardinality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMax_cardinality" ):
                listener.enterMax_cardinality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMax_cardinality" ):
                listener.exitMax_cardinality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMax_cardinality" ):
                return visitor.visitMax_cardinality(self)
            else:
                return visitor.visitChildren(self)




    def max_cardinality(self):

        localctx = MERLANParser.Max_cardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_max_cardinality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
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





