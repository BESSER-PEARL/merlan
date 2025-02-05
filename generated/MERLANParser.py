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
        4,1,32,216,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        3,0,42,8,0,1,0,3,0,45,8,0,1,0,3,0,48,8,0,1,0,3,0,51,8,0,1,0,3,0,
        54,8,0,1,0,1,0,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,2,1,2,1,
        2,5,2,69,8,2,10,2,12,2,72,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,89,8,3,1,4,1,4,1,4,5,4,94,8,4,10,4,
        12,4,97,9,4,1,5,1,5,1,5,5,5,102,8,5,10,5,12,5,105,9,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,122,8,6,1,
        7,1,7,1,7,4,7,127,8,7,11,7,12,7,128,1,8,1,8,1,8,1,8,1,9,1,9,3,9,
        137,8,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,145,8,10,1,11,1,11,1,
        11,5,11,150,8,11,10,11,12,11,153,9,11,1,12,1,12,3,12,157,8,12,1,
        13,1,13,3,13,161,8,13,1,13,1,13,4,13,165,8,13,11,13,12,13,166,1,
        14,1,14,3,14,171,8,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,
        17,1,17,1,17,4,17,184,8,17,11,17,12,17,185,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,200,8,18,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,214,8,19,1,
        19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        0,2,1,0,9,10,2,0,24,24,27,27,221,0,41,1,0,0,0,2,57,1,0,0,0,4,65,
        1,0,0,0,6,88,1,0,0,0,8,90,1,0,0,0,10,98,1,0,0,0,12,121,1,0,0,0,14,
        123,1,0,0,0,16,130,1,0,0,0,18,136,1,0,0,0,20,144,1,0,0,0,22,146,
        1,0,0,0,24,156,1,0,0,0,26,158,1,0,0,0,28,168,1,0,0,0,30,175,1,0,
        0,0,32,178,1,0,0,0,34,180,1,0,0,0,36,199,1,0,0,0,38,213,1,0,0,0,
        40,42,5,28,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,45,3,
        2,1,0,44,43,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,48,3,8,4,0,47,
        46,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,51,3,14,7,0,50,49,1,0,
        0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,5,28,0,0,53,52,1,0,0,0,53,
        54,1,0,0,0,54,55,1,0,0,0,55,56,5,0,0,1,56,1,1,0,0,0,57,58,5,5,0,
        0,58,62,5,28,0,0,59,61,3,4,2,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,
        1,0,0,0,62,63,1,0,0,0,63,3,1,0,0,0,64,62,1,0,0,0,65,66,5,21,0,0,
        66,70,5,28,0,0,67,69,3,6,3,0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,
        0,0,0,70,71,1,0,0,0,71,5,1,0,0,0,72,70,1,0,0,0,73,74,5,30,0,0,74,
        75,5,13,0,0,75,76,5,31,0,0,76,77,5,22,0,0,77,89,5,28,0,0,78,79,5,
        30,0,0,79,80,5,12,0,0,80,81,5,31,0,0,81,82,5,22,0,0,82,89,5,28,0,
        0,83,84,5,30,0,0,84,85,5,14,0,0,85,86,5,31,0,0,86,87,5,23,0,0,87,
        89,5,28,0,0,88,73,1,0,0,0,88,78,1,0,0,0,88,83,1,0,0,0,89,7,1,0,0,
        0,90,91,5,7,0,0,91,95,5,28,0,0,92,94,3,10,5,0,93,92,1,0,0,0,94,97,
        1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,9,1,0,0,0,97,95,1,0,0,0,98,
        99,5,21,0,0,99,103,5,28,0,0,100,102,3,12,6,0,101,100,1,0,0,0,102,
        105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,11,1,0,0,0,105,103,
        1,0,0,0,106,107,5,30,0,0,107,108,5,13,0,0,108,109,5,31,0,0,109,110,
        5,22,0,0,110,122,5,28,0,0,111,112,5,30,0,0,112,113,5,15,0,0,113,
        114,5,31,0,0,114,115,5,22,0,0,115,122,5,28,0,0,116,117,5,30,0,0,
        117,118,5,16,0,0,118,119,5,31,0,0,119,120,5,26,0,0,120,122,5,28,
        0,0,121,106,1,0,0,0,121,111,1,0,0,0,121,116,1,0,0,0,122,13,1,0,0,
        0,123,126,5,8,0,0,124,125,5,28,0,0,125,127,3,16,8,0,126,124,1,0,
        0,0,127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,15,1,0,0,
        0,130,131,5,21,0,0,131,132,5,28,0,0,132,133,3,18,9,0,133,17,1,0,
        0,0,134,137,3,20,10,0,135,137,3,24,12,0,136,134,1,0,0,0,136,135,
        1,0,0,0,137,19,1,0,0,0,138,139,7,0,0,0,139,140,5,28,0,0,140,145,
        3,22,11,0,141,142,5,11,0,0,142,143,5,28,0,0,143,145,3,18,9,0,144,
        138,1,0,0,0,144,141,1,0,0,0,145,21,1,0,0,0,146,151,3,18,9,0,147,
        148,5,28,0,0,148,150,3,18,9,0,149,147,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,23,1,0,0,0,153,151,1,0,0,0,154,157,
        3,26,13,0,155,157,3,34,17,0,156,154,1,0,0,0,156,155,1,0,0,0,157,
        25,1,0,0,0,158,160,5,4,0,0,159,161,3,28,14,0,160,159,1,0,0,0,160,
        161,1,0,0,0,161,164,1,0,0,0,162,163,5,28,0,0,163,165,3,36,18,0,164,
        162,1,0,0,0,165,166,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,
        27,1,0,0,0,168,170,5,1,0,0,169,171,3,30,15,0,170,169,1,0,0,0,170,
        171,1,0,0,0,171,172,1,0,0,0,172,173,3,32,16,0,173,174,5,2,0,0,174,
        29,1,0,0,0,175,176,5,24,0,0,176,177,5,3,0,0,177,31,1,0,0,0,178,179,
        7,1,0,0,179,33,1,0,0,0,180,183,5,6,0,0,181,182,5,28,0,0,182,184,
        3,38,19,0,183,181,1,0,0,0,184,185,1,0,0,0,185,183,1,0,0,0,185,186,
        1,0,0,0,186,35,1,0,0,0,187,188,5,30,0,0,188,189,5,17,0,0,189,190,
        5,31,0,0,190,200,5,21,0,0,191,192,5,30,0,0,192,193,5,19,0,0,193,
        194,5,31,0,0,194,200,5,22,0,0,195,196,5,30,0,0,196,197,5,20,0,0,
        197,198,5,31,0,0,198,200,5,23,0,0,199,187,1,0,0,0,199,191,1,0,0,
        0,199,195,1,0,0,0,200,37,1,0,0,0,201,202,5,30,0,0,202,203,5,18,0,
        0,203,204,5,31,0,0,204,214,5,21,0,0,205,206,5,30,0,0,206,207,5,19,
        0,0,207,208,5,31,0,0,208,214,5,22,0,0,209,210,5,30,0,0,210,211,5,
        20,0,0,211,212,5,31,0,0,212,214,5,23,0,0,213,201,1,0,0,0,213,205,
        1,0,0,0,213,209,1,0,0,0,214,39,1,0,0,0,22,41,44,47,50,53,62,70,88,
        95,103,121,128,136,144,151,156,160,166,170,185,199,213
    ]

class MERLANParser ( Parser ):

    grammarFileName = "MERLAN.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'..'", "'IMAGE_ENTITY'", 
                     "'IMAGE_ENTITIES'", "'IMAGE_PROPERTY'", "'IMAGE_PROPERTIES'", 
                     "'SCENARIOS'", "'AND'", "'OR'", "'NOT'", "'color'", 
                     "'description'", "'weight'", "'lighting'", "'version'", 
                     "'image_entity'", "'image_property'", "'name'", "'score'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "<INVALID>", "<INVALID>", 
                     "'- '", "': '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IMAGE_ENTITY", "IMAGE_ENTITIES", "IMAGE_PROPERTY", 
                      "IMAGE_PROPERTIES", "SCENARIOS", "AND", "OR", "NOT", 
                      "COLOR", "DESCRIPTION", "WEIGHT", "LIGHTING", "VERSION", 
                      "IMAGE_ENTITY_NAME", "IMAGE_PROPERTY_NAME", "NAME", 
                      "SCORE", "ID", "STRING", "FLOAT", "INT_NONZERO", "INT", 
                      "SIGINT", "STAR", "NEWLINE", "WS", "HYPHEN", "COLON", 
                      "COMMENT" ]

    RULE_script = 0
    RULE_image_entities = 1
    RULE_image_entity = 2
    RULE_image_entity_attribute = 3
    RULE_image_properties = 4
    RULE_image_property = 5
    RULE_image_property_attribute = 6
    RULE_scenarios = 7
    RULE_scenario = 8
    RULE_expression = 9
    RULE_boolean_expression = 10
    RULE_expression_list = 11
    RULE_scenario_requirement = 12
    RULE_scenario_image_entity = 13
    RULE_cardinality = 14
    RULE_min_cardinality = 15
    RULE_max_cardinality = 16
    RULE_scenario_image_property = 17
    RULE_scenario_image_entity_attribute = 18
    RULE_scenario_image_property_attribute = 19

    ruleNames =  [ "script", "image_entities", "image_entity", "image_entity_attribute", 
                   "image_properties", "image_property", "image_property_attribute", 
                   "scenarios", "scenario", "expression", "boolean_expression", 
                   "expression_list", "scenario_requirement", "scenario_image_entity", 
                   "cardinality", "min_cardinality", "max_cardinality", 
                   "scenario_image_property", "scenario_image_entity_attribute", 
                   "scenario_image_property_attribute" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    IMAGE_ENTITY=4
    IMAGE_ENTITIES=5
    IMAGE_PROPERTY=6
    IMAGE_PROPERTIES=7
    SCENARIOS=8
    AND=9
    OR=10
    NOT=11
    COLOR=12
    DESCRIPTION=13
    WEIGHT=14
    LIGHTING=15
    VERSION=16
    IMAGE_ENTITY_NAME=17
    IMAGE_PROPERTY_NAME=18
    NAME=19
    SCORE=20
    ID=21
    STRING=22
    FLOAT=23
    INT_NONZERO=24
    INT=25
    SIGINT=26
    STAR=27
    NEWLINE=28
    WS=29
    HYPHEN=30
    COLON=31
    COMMENT=32

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

        def image_entities(self):
            return self.getTypedRuleContext(MERLANParser.Image_entitiesContext,0)


        def image_properties(self):
            return self.getTypedRuleContext(MERLANParser.Image_propertiesContext,0)


        def scenarios(self):
            return self.getTypedRuleContext(MERLANParser.ScenariosContext,0)


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
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 40
                self.match(MERLANParser.NEWLINE)


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 43
                self.image_entities()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 46
                self.image_properties()


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 49
                self.scenarios()


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 52
                self.match(MERLANParser.NEWLINE)


            self.state = 55
            self.match(MERLANParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_entitiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMAGE_ENTITIES(self):
            return self.getToken(MERLANParser.IMAGE_ENTITIES, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def image_entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Image_entityContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Image_entityContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_image_entities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_entities" ):
                listener.enterImage_entities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_entities" ):
                listener.exitImage_entities(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_entities" ):
                return visitor.visitImage_entities(self)
            else:
                return visitor.visitChildren(self)




    def image_entities(self):

        localctx = MERLANParser.Image_entitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_image_entities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MERLANParser.IMAGE_ENTITIES)
            self.state = 58
            self.match(MERLANParser.NEWLINE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 59
                self.image_entity()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_entityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def image_entity_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Image_entity_attributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Image_entity_attributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_image_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_entity" ):
                listener.enterImage_entity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_entity" ):
                listener.exitImage_entity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_entity" ):
                return visitor.visitImage_entity(self)
            else:
                return visitor.visitChildren(self)




    def image_entity(self):

        localctx = MERLANParser.Image_entityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_image_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MERLANParser.ID)
            self.state = 66
            self.match(MERLANParser.NEWLINE)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 67
                self.image_entity_attribute()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_entity_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HYPHEN(self):
            return self.getToken(MERLANParser.HYPHEN, 0)

        def DESCRIPTION(self):
            return self.getToken(MERLANParser.DESCRIPTION, 0)

        def COLON(self):
            return self.getToken(MERLANParser.COLON, 0)

        def STRING(self):
            return self.getToken(MERLANParser.STRING, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def COLOR(self):
            return self.getToken(MERLANParser.COLOR, 0)

        def WEIGHT(self):
            return self.getToken(MERLANParser.WEIGHT, 0)

        def FLOAT(self):
            return self.getToken(MERLANParser.FLOAT, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_image_entity_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_entity_attribute" ):
                listener.enterImage_entity_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_entity_attribute" ):
                listener.exitImage_entity_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_entity_attribute" ):
                return visitor.visitImage_entity_attribute(self)
            else:
                return visitor.visitChildren(self)




    def image_entity_attribute(self):

        localctx = MERLANParser.Image_entity_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_image_entity_attribute)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(MERLANParser.HYPHEN)
                self.state = 74
                self.match(MERLANParser.DESCRIPTION)
                self.state = 75
                self.match(MERLANParser.COLON)
                self.state = 76
                self.match(MERLANParser.STRING)
                self.state = 77
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(MERLANParser.HYPHEN)
                self.state = 79
                self.match(MERLANParser.COLOR)
                self.state = 80
                self.match(MERLANParser.COLON)
                self.state = 81
                self.match(MERLANParser.STRING)
                self.state = 82
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.match(MERLANParser.HYPHEN)
                self.state = 84
                self.match(MERLANParser.WEIGHT)
                self.state = 85
                self.match(MERLANParser.COLON)
                self.state = 86
                self.match(MERLANParser.FLOAT)
                self.state = 87
                self.match(MERLANParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_propertiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMAGE_PROPERTIES(self):
            return self.getToken(MERLANParser.IMAGE_PROPERTIES, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def image_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Image_propertyContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Image_propertyContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_image_properties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_properties" ):
                listener.enterImage_properties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_properties" ):
                listener.exitImage_properties(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_properties" ):
                return visitor.visitImage_properties(self)
            else:
                return visitor.visitChildren(self)




    def image_properties(self):

        localctx = MERLANParser.Image_propertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_image_properties)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MERLANParser.IMAGE_PROPERTIES)
            self.state = 91
            self.match(MERLANParser.NEWLINE)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 92
                self.image_property()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def image_property_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Image_property_attributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Image_property_attributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_image_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_property" ):
                listener.enterImage_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_property" ):
                listener.exitImage_property(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_property" ):
                return visitor.visitImage_property(self)
            else:
                return visitor.visitChildren(self)




    def image_property(self):

        localctx = MERLANParser.Image_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_image_property)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MERLANParser.ID)
            self.state = 99
            self.match(MERLANParser.NEWLINE)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 100
                self.image_property_attribute()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_property_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HYPHEN(self):
            return self.getToken(MERLANParser.HYPHEN, 0)

        def DESCRIPTION(self):
            return self.getToken(MERLANParser.DESCRIPTION, 0)

        def COLON(self):
            return self.getToken(MERLANParser.COLON, 0)

        def STRING(self):
            return self.getToken(MERLANParser.STRING, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def LIGHTING(self):
            return self.getToken(MERLANParser.LIGHTING, 0)

        def VERSION(self):
            return self.getToken(MERLANParser.VERSION, 0)

        def SIGINT(self):
            return self.getToken(MERLANParser.SIGINT, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_image_property_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_property_attribute" ):
                listener.enterImage_property_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_property_attribute" ):
                listener.exitImage_property_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_property_attribute" ):
                return visitor.visitImage_property_attribute(self)
            else:
                return visitor.visitChildren(self)




    def image_property_attribute(self):

        localctx = MERLANParser.Image_property_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_image_property_attribute)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(MERLANParser.HYPHEN)
                self.state = 107
                self.match(MERLANParser.DESCRIPTION)
                self.state = 108
                self.match(MERLANParser.COLON)
                self.state = 109
                self.match(MERLANParser.STRING)
                self.state = 110
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(MERLANParser.HYPHEN)
                self.state = 112
                self.match(MERLANParser.LIGHTING)
                self.state = 113
                self.match(MERLANParser.COLON)
                self.state = 114
                self.match(MERLANParser.STRING)
                self.state = 115
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(MERLANParser.HYPHEN)
                self.state = 117
                self.match(MERLANParser.VERSION)
                self.state = 118
                self.match(MERLANParser.COLON)
                self.state = 119
                self.match(MERLANParser.SIGINT)
                self.state = 120
                self.match(MERLANParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScenariosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCENARIOS(self):
            return self.getToken(MERLANParser.SCENARIOS, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MERLANParser.NEWLINE)
            else:
                return self.getToken(MERLANParser.NEWLINE, i)

        def scenario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.ScenarioContext)
            else:
                return self.getTypedRuleContext(MERLANParser.ScenarioContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_scenarios

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenarios" ):
                listener.enterScenarios(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenarios" ):
                listener.exitScenarios(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenarios" ):
                return visitor.visitScenarios(self)
            else:
                return visitor.visitChildren(self)




    def scenarios(self):

        localctx = MERLANParser.ScenariosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_scenarios)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MERLANParser.SCENARIOS)
            self.state = 126 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 124
                    self.match(MERLANParser.NEWLINE)
                    self.state = 125
                    self.scenario()

                else:
                    raise NoViableAltException(self)
                self.state = 128 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScenarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def expression(self):
            return self.getTypedRuleContext(MERLANParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_scenario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario" ):
                listener.enterScenario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario" ):
                listener.exitScenario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario" ):
                return visitor.visitScenario(self)
            else:
                return visitor.visitChildren(self)




    def scenario(self):

        localctx = MERLANParser.ScenarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_scenario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MERLANParser.ID)
            self.state = 131
            self.match(MERLANParser.NEWLINE)
            self.state = 132
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_expression(self):
            return self.getTypedRuleContext(MERLANParser.Boolean_expressionContext,0)


        def scenario_requirement(self):
            return self.getTypedRuleContext(MERLANParser.Scenario_requirementContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MERLANParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.boolean_expression()
                pass
            elif token in [4, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.scenario_requirement()
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


    class Boolean_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MERLANParser.Expression_listContext,0)


        def AND(self):
            return self.getToken(MERLANParser.AND, 0)

        def OR(self):
            return self.getToken(MERLANParser.OR, 0)

        def NOT(self):
            return self.getToken(MERLANParser.NOT, 0)

        def expression(self):
            return self.getTypedRuleContext(MERLANParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_boolean_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_expression" ):
                listener.enterBoolean_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_expression" ):
                listener.exitBoolean_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expression" ):
                return visitor.visitBoolean_expression(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expression(self):

        localctx = MERLANParser.Boolean_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_boolean_expression)
        self._la = 0 # Token type
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.match(MERLANParser.NEWLINE)
                self.state = 140
                self.expression_list()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(MERLANParser.NOT)
                self.state = 142
                self.match(MERLANParser.NEWLINE)
                self.state = 143
                self.expression()
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


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MERLANParser.ExpressionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MERLANParser.NEWLINE)
            else:
                return self.getToken(MERLANParser.NEWLINE, i)

        def getRuleIndex(self):
            return MERLANParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = MERLANParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.expression()
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 147
                    self.match(MERLANParser.NEWLINE)
                    self.state = 148
                    self.expression() 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scenario_requirementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scenario_image_entity(self):
            return self.getTypedRuleContext(MERLANParser.Scenario_image_entityContext,0)


        def scenario_image_property(self):
            return self.getTypedRuleContext(MERLANParser.Scenario_image_propertyContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_requirement" ):
                listener.enterScenario_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_requirement" ):
                listener.exitScenario_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_requirement" ):
                return visitor.visitScenario_requirement(self)
            else:
                return visitor.visitChildren(self)




    def scenario_requirement(self):

        localctx = MERLANParser.Scenario_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scenario_requirement)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.scenario_image_entity()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.scenario_image_property()
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


    class Scenario_image_entityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMAGE_ENTITY(self):
            return self.getToken(MERLANParser.IMAGE_ENTITY, 0)

        def cardinality(self):
            return self.getTypedRuleContext(MERLANParser.CardinalityContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MERLANParser.NEWLINE)
            else:
                return self.getToken(MERLANParser.NEWLINE, i)

        def scenario_image_entity_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Scenario_image_entity_attributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Scenario_image_entity_attributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_image_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_image_entity" ):
                listener.enterScenario_image_entity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_image_entity" ):
                listener.exitScenario_image_entity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_image_entity" ):
                return visitor.visitScenario_image_entity(self)
            else:
                return visitor.visitChildren(self)




    def scenario_image_entity(self):

        localctx = MERLANParser.Scenario_image_entityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_scenario_image_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MERLANParser.IMAGE_ENTITY)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 159
                self.cardinality()


            self.state = 164 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 162
                    self.match(MERLANParser.NEWLINE)
                    self.state = 163
                    self.scenario_image_entity_attribute()

                else:
                    raise NoViableAltException(self)
                self.state = 166 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 168
            self.match(MERLANParser.T__0)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 169
                self.min_cardinality()


            self.state = 172
            self.max_cardinality()
            self.state = 173
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
            self.state = 175
            self.match(MERLANParser.INT_NONZERO)
            self.state = 176
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
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==24 or _la==27):
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


    class Scenario_image_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMAGE_PROPERTY(self):
            return self.getToken(MERLANParser.IMAGE_PROPERTY, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MERLANParser.NEWLINE)
            else:
                return self.getToken(MERLANParser.NEWLINE, i)

        def scenario_image_property_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Scenario_image_property_attributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Scenario_image_property_attributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_image_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_image_property" ):
                listener.enterScenario_image_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_image_property" ):
                listener.exitScenario_image_property(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_image_property" ):
                return visitor.visitScenario_image_property(self)
            else:
                return visitor.visitChildren(self)




    def scenario_image_property(self):

        localctx = MERLANParser.Scenario_image_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_scenario_image_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MERLANParser.IMAGE_PROPERTY)
            self.state = 183 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 181
                    self.match(MERLANParser.NEWLINE)
                    self.state = 182
                    self.scenario_image_property_attribute()

                else:
                    raise NoViableAltException(self)
                self.state = 185 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scenario_image_entity_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HYPHEN(self):
            return self.getToken(MERLANParser.HYPHEN, 0)

        def IMAGE_ENTITY_NAME(self):
            return self.getToken(MERLANParser.IMAGE_ENTITY_NAME, 0)

        def COLON(self):
            return self.getToken(MERLANParser.COLON, 0)

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NAME(self):
            return self.getToken(MERLANParser.NAME, 0)

        def STRING(self):
            return self.getToken(MERLANParser.STRING, 0)

        def SCORE(self):
            return self.getToken(MERLANParser.SCORE, 0)

        def FLOAT(self):
            return self.getToken(MERLANParser.FLOAT, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_image_entity_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_image_entity_attribute" ):
                listener.enterScenario_image_entity_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_image_entity_attribute" ):
                listener.exitScenario_image_entity_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_image_entity_attribute" ):
                return visitor.visitScenario_image_entity_attribute(self)
            else:
                return visitor.visitChildren(self)




    def scenario_image_entity_attribute(self):

        localctx = MERLANParser.Scenario_image_entity_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_scenario_image_entity_attribute)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(MERLANParser.HYPHEN)
                self.state = 188
                self.match(MERLANParser.IMAGE_ENTITY_NAME)
                self.state = 189
                self.match(MERLANParser.COLON)
                self.state = 190
                self.match(MERLANParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(MERLANParser.HYPHEN)
                self.state = 192
                self.match(MERLANParser.NAME)
                self.state = 193
                self.match(MERLANParser.COLON)
                self.state = 194
                self.match(MERLANParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(MERLANParser.HYPHEN)
                self.state = 196
                self.match(MERLANParser.SCORE)
                self.state = 197
                self.match(MERLANParser.COLON)
                self.state = 198
                self.match(MERLANParser.FLOAT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scenario_image_property_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HYPHEN(self):
            return self.getToken(MERLANParser.HYPHEN, 0)

        def IMAGE_PROPERTY_NAME(self):
            return self.getToken(MERLANParser.IMAGE_PROPERTY_NAME, 0)

        def COLON(self):
            return self.getToken(MERLANParser.COLON, 0)

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NAME(self):
            return self.getToken(MERLANParser.NAME, 0)

        def STRING(self):
            return self.getToken(MERLANParser.STRING, 0)

        def SCORE(self):
            return self.getToken(MERLANParser.SCORE, 0)

        def FLOAT(self):
            return self.getToken(MERLANParser.FLOAT, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_image_property_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_image_property_attribute" ):
                listener.enterScenario_image_property_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_image_property_attribute" ):
                listener.exitScenario_image_property_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_image_property_attribute" ):
                return visitor.visitScenario_image_property_attribute(self)
            else:
                return visitor.visitChildren(self)




    def scenario_image_property_attribute(self):

        localctx = MERLANParser.Scenario_image_property_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_scenario_image_property_attribute)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(MERLANParser.HYPHEN)
                self.state = 202
                self.match(MERLANParser.IMAGE_PROPERTY_NAME)
                self.state = 203
                self.match(MERLANParser.COLON)
                self.state = 204
                self.match(MERLANParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(MERLANParser.HYPHEN)
                self.state = 206
                self.match(MERLANParser.NAME)
                self.state = 207
                self.match(MERLANParser.COLON)
                self.state = 208
                self.match(MERLANParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(MERLANParser.HYPHEN)
                self.state = 210
                self.match(MERLANParser.SCORE)
                self.state = 211
                self.match(MERLANParser.COLON)
                self.state = 212
                self.match(MERLANParser.FLOAT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





