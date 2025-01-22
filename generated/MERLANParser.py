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
        4,1,28,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,3,0,36,8,0,1,0,3,0,39,8,0,1,0,
        3,0,42,8,0,1,0,3,0,45,8,0,1,0,3,0,48,8,0,1,0,1,0,1,1,1,1,1,1,5,1,
        55,8,1,10,1,12,1,58,9,1,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        83,8,3,1,4,1,4,1,4,5,4,88,8,4,10,4,12,4,91,9,4,1,5,1,5,1,5,5,5,96,
        8,5,10,5,12,5,99,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,116,8,6,1,7,1,7,1,7,4,7,121,8,7,11,7,12,7,122,
        1,8,1,8,1,8,1,8,1,9,1,9,3,9,131,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        3,10,139,8,10,1,11,1,11,1,11,5,11,144,8,11,10,11,12,11,147,9,11,
        1,12,1,12,3,12,151,8,12,1,13,1,13,1,13,4,13,156,8,13,11,13,12,13,
        157,1,14,1,14,1,14,4,14,163,8,14,11,14,12,14,164,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,3,15,187,8,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,3,16,201,8,16,1,16,0,0,17,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,0,1,1,0,6,7,211,0,35,1,0,0,
        0,2,51,1,0,0,0,4,59,1,0,0,0,6,82,1,0,0,0,8,84,1,0,0,0,10,92,1,0,
        0,0,12,115,1,0,0,0,14,117,1,0,0,0,16,124,1,0,0,0,18,130,1,0,0,0,
        20,138,1,0,0,0,22,140,1,0,0,0,24,150,1,0,0,0,26,152,1,0,0,0,28,159,
        1,0,0,0,30,186,1,0,0,0,32,200,1,0,0,0,34,36,5,24,0,0,35,34,1,0,0,
        0,35,36,1,0,0,0,36,38,1,0,0,0,37,39,3,2,1,0,38,37,1,0,0,0,38,39,
        1,0,0,0,39,41,1,0,0,0,40,42,3,8,4,0,41,40,1,0,0,0,41,42,1,0,0,0,
        42,44,1,0,0,0,43,45,3,14,7,0,44,43,1,0,0,0,44,45,1,0,0,0,45,47,1,
        0,0,0,46,48,5,24,0,0,47,46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,
        50,5,0,0,1,50,1,1,0,0,0,51,52,5,2,0,0,52,56,5,24,0,0,53,55,3,4,2,
        0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,3,1,
        0,0,0,58,56,1,0,0,0,59,60,5,20,0,0,60,64,5,24,0,0,61,63,3,6,3,0,
        62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,5,1,0,
        0,0,66,64,1,0,0,0,67,68,5,26,0,0,68,69,5,10,0,0,69,70,5,27,0,0,70,
        71,5,21,0,0,71,83,5,24,0,0,72,73,5,26,0,0,73,74,5,9,0,0,74,75,5,
        27,0,0,75,76,5,21,0,0,76,83,5,24,0,0,77,78,5,26,0,0,78,79,5,11,0,
        0,79,80,5,27,0,0,80,81,5,22,0,0,81,83,5,24,0,0,82,67,1,0,0,0,82,
        72,1,0,0,0,82,77,1,0,0,0,83,7,1,0,0,0,84,85,5,4,0,0,85,89,5,24,0,
        0,86,88,3,10,5,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,
        1,0,0,0,90,9,1,0,0,0,91,89,1,0,0,0,92,93,5,20,0,0,93,97,5,24,0,0,
        94,96,3,12,6,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,
        0,0,0,98,11,1,0,0,0,99,97,1,0,0,0,100,101,5,26,0,0,101,102,5,10,
        0,0,102,103,5,27,0,0,103,104,5,21,0,0,104,116,5,24,0,0,105,106,5,
        26,0,0,106,107,5,12,0,0,107,108,5,27,0,0,108,109,5,21,0,0,109,116,
        5,24,0,0,110,111,5,26,0,0,111,112,5,13,0,0,112,113,5,27,0,0,113,
        114,5,23,0,0,114,116,5,24,0,0,115,100,1,0,0,0,115,105,1,0,0,0,115,
        110,1,0,0,0,116,13,1,0,0,0,117,120,5,5,0,0,118,119,5,24,0,0,119,
        121,3,16,8,0,120,118,1,0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,15,1,0,0,0,124,125,5,20,0,0,125,126,5,24,0,0,126,
        127,3,18,9,0,127,17,1,0,0,0,128,131,3,20,10,0,129,131,3,24,12,0,
        130,128,1,0,0,0,130,129,1,0,0,0,131,19,1,0,0,0,132,133,7,0,0,0,133,
        134,5,24,0,0,134,139,3,22,11,0,135,136,5,8,0,0,136,137,5,24,0,0,
        137,139,3,18,9,0,138,132,1,0,0,0,138,135,1,0,0,0,139,21,1,0,0,0,
        140,145,3,18,9,0,141,142,5,24,0,0,142,144,3,18,9,0,143,141,1,0,0,
        0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,23,1,0,0,0,
        147,145,1,0,0,0,148,151,3,26,13,0,149,151,3,28,14,0,150,148,1,0,
        0,0,150,149,1,0,0,0,151,25,1,0,0,0,152,155,5,1,0,0,153,154,5,24,
        0,0,154,156,3,30,15,0,155,153,1,0,0,0,156,157,1,0,0,0,157,155,1,
        0,0,0,157,158,1,0,0,0,158,27,1,0,0,0,159,162,5,3,0,0,160,161,5,24,
        0,0,161,163,3,32,16,0,162,160,1,0,0,0,163,164,1,0,0,0,164,162,1,
        0,0,0,164,165,1,0,0,0,165,29,1,0,0,0,166,167,5,26,0,0,167,168,5,
        14,0,0,168,169,5,27,0,0,169,187,5,20,0,0,170,171,5,26,0,0,171,172,
        5,18,0,0,172,173,5,27,0,0,173,187,5,21,0,0,174,175,5,26,0,0,175,
        176,5,17,0,0,176,177,5,27,0,0,177,187,5,23,0,0,178,179,5,26,0,0,
        179,180,5,16,0,0,180,181,5,27,0,0,181,187,5,23,0,0,182,183,5,26,
        0,0,183,184,5,19,0,0,184,185,5,27,0,0,185,187,5,22,0,0,186,166,1,
        0,0,0,186,170,1,0,0,0,186,174,1,0,0,0,186,178,1,0,0,0,186,182,1,
        0,0,0,187,31,1,0,0,0,188,189,5,26,0,0,189,190,5,15,0,0,190,191,5,
        27,0,0,191,201,5,20,0,0,192,193,5,26,0,0,193,194,5,18,0,0,194,195,
        5,27,0,0,195,201,5,21,0,0,196,197,5,26,0,0,197,198,5,19,0,0,198,
        199,5,27,0,0,199,201,5,22,0,0,200,188,1,0,0,0,200,192,1,0,0,0,200,
        196,1,0,0,0,201,33,1,0,0,0,20,35,38,41,44,47,56,64,82,89,97,115,
        122,130,138,145,150,157,164,186,200
    ]

class MERLANParser ( Parser ):

    grammarFileName = "MERLAN.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IMAGE_OBJECT'", "'IMAGE_OBJECTS'", "'IMAGE_PROPERTY'", 
                     "'IMAGE_PROPERTIES'", "'SCENARIOS'", "'AND'", "'OR'", 
                     "'NOT'", "'color'", "'description'", "'weight'", "'lighting'", 
                     "'version'", "'image_object'", "'image_property'", 
                     "'max'", "'min'", "'name'", "'score'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'- '", "': '" ]

    symbolicNames = [ "<INVALID>", "IMAGE_OBJECT", "IMAGE_OBJECTS", "IMAGE_PROPERTY", 
                      "IMAGE_PROPERTIES", "SCENARIOS", "AND", "OR", "NOT", 
                      "COLOR", "DESCRIPTION", "WEIGHT", "LIGHTING", "VERSION", 
                      "IMAGE_OBJECT_NAME", "IMAGE_PROPERTY_NAME", "MAX", 
                      "MIN", "NAME", "SCORE", "ID", "STRING", "FLOAT", "INT", 
                      "NEWLINE", "WS", "HYPHEN", "COLON", "COMMENT" ]

    RULE_script = 0
    RULE_image_objects = 1
    RULE_image_object = 2
    RULE_image_object_attribute = 3
    RULE_image_properties = 4
    RULE_image_property = 5
    RULE_image_property_attribute = 6
    RULE_scenarios = 7
    RULE_scenario = 8
    RULE_expression = 9
    RULE_boolean_expression = 10
    RULE_expression_list = 11
    RULE_scenario_entity = 12
    RULE_scenario_image_object = 13
    RULE_scenario_image_property = 14
    RULE_scenario_image_object_attribute = 15
    RULE_scenario_image_property_attribute = 16

    ruleNames =  [ "script", "image_objects", "image_object", "image_object_attribute", 
                   "image_properties", "image_property", "image_property_attribute", 
                   "scenarios", "scenario", "expression", "boolean_expression", 
                   "expression_list", "scenario_entity", "scenario_image_object", 
                   "scenario_image_property", "scenario_image_object_attribute", 
                   "scenario_image_property_attribute" ]

    EOF = Token.EOF
    IMAGE_OBJECT=1
    IMAGE_OBJECTS=2
    IMAGE_PROPERTY=3
    IMAGE_PROPERTIES=4
    SCENARIOS=5
    AND=6
    OR=7
    NOT=8
    COLOR=9
    DESCRIPTION=10
    WEIGHT=11
    LIGHTING=12
    VERSION=13
    IMAGE_OBJECT_NAME=14
    IMAGE_PROPERTY_NAME=15
    MAX=16
    MIN=17
    NAME=18
    SCORE=19
    ID=20
    STRING=21
    FLOAT=22
    INT=23
    NEWLINE=24
    WS=25
    HYPHEN=26
    COLON=27
    COMMENT=28

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

        def image_objects(self):
            return self.getTypedRuleContext(MERLANParser.Image_objectsContext,0)


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
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 34
                self.match(MERLANParser.NEWLINE)


            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 37
                self.image_objects()


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 40
                self.image_properties()


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 43
                self.scenarios()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 46
                self.match(MERLANParser.NEWLINE)


            self.state = 49
            self.match(MERLANParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_objectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMAGE_OBJECTS(self):
            return self.getToken(MERLANParser.IMAGE_OBJECTS, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def image_object(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Image_objectContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Image_objectContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_image_objects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_objects" ):
                listener.enterImage_objects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_objects" ):
                listener.exitImage_objects(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_objects" ):
                return visitor.visitImage_objects(self)
            else:
                return visitor.visitChildren(self)




    def image_objects(self):

        localctx = MERLANParser.Image_objectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_image_objects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MERLANParser.IMAGE_OBJECTS)
            self.state = 52
            self.match(MERLANParser.NEWLINE)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 53
                self.image_object()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_objectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(MERLANParser.NEWLINE, 0)

        def image_object_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Image_object_attributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Image_object_attributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_image_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_object" ):
                listener.enterImage_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_object" ):
                listener.exitImage_object(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_object" ):
                return visitor.visitImage_object(self)
            else:
                return visitor.visitChildren(self)




    def image_object(self):

        localctx = MERLANParser.Image_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_image_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(MERLANParser.ID)
            self.state = 60
            self.match(MERLANParser.NEWLINE)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 61
                self.image_object_attribute()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_object_attributeContext(ParserRuleContext):
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
            return MERLANParser.RULE_image_object_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_object_attribute" ):
                listener.enterImage_object_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_object_attribute" ):
                listener.exitImage_object_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage_object_attribute" ):
                return visitor.visitImage_object_attribute(self)
            else:
                return visitor.visitChildren(self)




    def image_object_attribute(self):

        localctx = MERLANParser.Image_object_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_image_object_attribute)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(MERLANParser.HYPHEN)
                self.state = 68
                self.match(MERLANParser.DESCRIPTION)
                self.state = 69
                self.match(MERLANParser.COLON)
                self.state = 70
                self.match(MERLANParser.STRING)
                self.state = 71
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(MERLANParser.HYPHEN)
                self.state = 73
                self.match(MERLANParser.COLOR)
                self.state = 74
                self.match(MERLANParser.COLON)
                self.state = 75
                self.match(MERLANParser.STRING)
                self.state = 76
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(MERLANParser.HYPHEN)
                self.state = 78
                self.match(MERLANParser.WEIGHT)
                self.state = 79
                self.match(MERLANParser.COLON)
                self.state = 80
                self.match(MERLANParser.FLOAT)
                self.state = 81
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
            self.state = 84
            self.match(MERLANParser.IMAGE_PROPERTIES)
            self.state = 85
            self.match(MERLANParser.NEWLINE)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 86
                self.image_property()
                self.state = 91
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
            self.state = 92
            self.match(MERLANParser.ID)
            self.state = 93
            self.match(MERLANParser.NEWLINE)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 94
                self.image_property_attribute()
                self.state = 99
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

        def INT(self):
            return self.getToken(MERLANParser.INT, 0)

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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(MERLANParser.HYPHEN)
                self.state = 101
                self.match(MERLANParser.DESCRIPTION)
                self.state = 102
                self.match(MERLANParser.COLON)
                self.state = 103
                self.match(MERLANParser.STRING)
                self.state = 104
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(MERLANParser.HYPHEN)
                self.state = 106
                self.match(MERLANParser.LIGHTING)
                self.state = 107
                self.match(MERLANParser.COLON)
                self.state = 108
                self.match(MERLANParser.STRING)
                self.state = 109
                self.match(MERLANParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(MERLANParser.HYPHEN)
                self.state = 111
                self.match(MERLANParser.VERSION)
                self.state = 112
                self.match(MERLANParser.COLON)
                self.state = 113
                self.match(MERLANParser.INT)
                self.state = 114
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
            self.state = 117
            self.match(MERLANParser.SCENARIOS)
            self.state = 120 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 118
                    self.match(MERLANParser.NEWLINE)
                    self.state = 119
                    self.scenario()

                else:
                    raise NoViableAltException(self)
                self.state = 122 
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
            self.state = 124
            self.match(MERLANParser.ID)
            self.state = 125
            self.match(MERLANParser.NEWLINE)
            self.state = 126
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


        def scenario_entity(self):
            return self.getTypedRuleContext(MERLANParser.Scenario_entityContext,0)


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
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.boolean_expression()
                pass
            elif token in [1, 3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.scenario_entity()
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
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.match(MERLANParser.NEWLINE)
                self.state = 134
                self.expression_list()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(MERLANParser.NOT)
                self.state = 136
                self.match(MERLANParser.NEWLINE)
                self.state = 137
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
            self.state = 140
            self.expression()
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 141
                    self.match(MERLANParser.NEWLINE)
                    self.state = 142
                    self.expression() 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scenario_entityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scenario_image_object(self):
            return self.getTypedRuleContext(MERLANParser.Scenario_image_objectContext,0)


        def scenario_image_property(self):
            return self.getTypedRuleContext(MERLANParser.Scenario_image_propertyContext,0)


        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_entity" ):
                listener.enterScenario_entity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_entity" ):
                listener.exitScenario_entity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_entity" ):
                return visitor.visitScenario_entity(self)
            else:
                return visitor.visitChildren(self)




    def scenario_entity(self):

        localctx = MERLANParser.Scenario_entityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scenario_entity)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.scenario_image_object()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
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


    class Scenario_image_objectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMAGE_OBJECT(self):
            return self.getToken(MERLANParser.IMAGE_OBJECT, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MERLANParser.NEWLINE)
            else:
                return self.getToken(MERLANParser.NEWLINE, i)

        def scenario_image_object_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MERLANParser.Scenario_image_object_attributeContext)
            else:
                return self.getTypedRuleContext(MERLANParser.Scenario_image_object_attributeContext,i)


        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_image_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_image_object" ):
                listener.enterScenario_image_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_image_object" ):
                listener.exitScenario_image_object(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_image_object" ):
                return visitor.visitScenario_image_object(self)
            else:
                return visitor.visitChildren(self)




    def scenario_image_object(self):

        localctx = MERLANParser.Scenario_image_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_scenario_image_object)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MERLANParser.IMAGE_OBJECT)
            self.state = 155 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 153
                    self.match(MERLANParser.NEWLINE)
                    self.state = 154
                    self.scenario_image_object_attribute()

                else:
                    raise NoViableAltException(self)
                self.state = 157 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_scenario_image_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(MERLANParser.IMAGE_PROPERTY)
            self.state = 162 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 160
                    self.match(MERLANParser.NEWLINE)
                    self.state = 161
                    self.scenario_image_property_attribute()

                else:
                    raise NoViableAltException(self)
                self.state = 164 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scenario_image_object_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HYPHEN(self):
            return self.getToken(MERLANParser.HYPHEN, 0)

        def IMAGE_OBJECT_NAME(self):
            return self.getToken(MERLANParser.IMAGE_OBJECT_NAME, 0)

        def COLON(self):
            return self.getToken(MERLANParser.COLON, 0)

        def ID(self):
            return self.getToken(MERLANParser.ID, 0)

        def NAME(self):
            return self.getToken(MERLANParser.NAME, 0)

        def STRING(self):
            return self.getToken(MERLANParser.STRING, 0)

        def MIN(self):
            return self.getToken(MERLANParser.MIN, 0)

        def INT(self):
            return self.getToken(MERLANParser.INT, 0)

        def MAX(self):
            return self.getToken(MERLANParser.MAX, 0)

        def SCORE(self):
            return self.getToken(MERLANParser.SCORE, 0)

        def FLOAT(self):
            return self.getToken(MERLANParser.FLOAT, 0)

        def getRuleIndex(self):
            return MERLANParser.RULE_scenario_image_object_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_image_object_attribute" ):
                listener.enterScenario_image_object_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_image_object_attribute" ):
                listener.exitScenario_image_object_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenario_image_object_attribute" ):
                return visitor.visitScenario_image_object_attribute(self)
            else:
                return visitor.visitChildren(self)




    def scenario_image_object_attribute(self):

        localctx = MERLANParser.Scenario_image_object_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_scenario_image_object_attribute)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(MERLANParser.HYPHEN)
                self.state = 167
                self.match(MERLANParser.IMAGE_OBJECT_NAME)
                self.state = 168
                self.match(MERLANParser.COLON)
                self.state = 169
                self.match(MERLANParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(MERLANParser.HYPHEN)
                self.state = 171
                self.match(MERLANParser.NAME)
                self.state = 172
                self.match(MERLANParser.COLON)
                self.state = 173
                self.match(MERLANParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(MERLANParser.HYPHEN)
                self.state = 175
                self.match(MERLANParser.MIN)
                self.state = 176
                self.match(MERLANParser.COLON)
                self.state = 177
                self.match(MERLANParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(MERLANParser.HYPHEN)
                self.state = 179
                self.match(MERLANParser.MAX)
                self.state = 180
                self.match(MERLANParser.COLON)
                self.state = 181
                self.match(MERLANParser.INT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(MERLANParser.HYPHEN)
                self.state = 183
                self.match(MERLANParser.SCORE)
                self.state = 184
                self.match(MERLANParser.COLON)
                self.state = 185
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
        self.enterRule(localctx, 32, self.RULE_scenario_image_property_attribute)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(MERLANParser.HYPHEN)
                self.state = 189
                self.match(MERLANParser.IMAGE_PROPERTY_NAME)
                self.state = 190
                self.match(MERLANParser.COLON)
                self.state = 191
                self.match(MERLANParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(MERLANParser.HYPHEN)
                self.state = 193
                self.match(MERLANParser.NAME)
                self.state = 194
                self.match(MERLANParser.COLON)
                self.state = 195
                self.match(MERLANParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(MERLANParser.HYPHEN)
                self.state = 197
                self.match(MERLANParser.SCORE)
                self.state = 198
                self.match(MERLANParser.COLON)
                self.state = 199
                self.match(MERLANParser.FLOAT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





