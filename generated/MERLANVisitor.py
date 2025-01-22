# Generated from grammar/MERLAN.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MERLANParser import MERLANParser
else:
    from MERLANParser import MERLANParser

# This class defines a complete generic visitor for a parse tree produced by MERLANParser.

class MERLANVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MERLANParser#script.
    def visitScript(self, ctx:MERLANParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_objects.
    def visitImage_objects(self, ctx:MERLANParser.Image_objectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_object.
    def visitImage_object(self, ctx:MERLANParser.Image_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_object_attribute.
    def visitImage_object_attribute(self, ctx:MERLANParser.Image_object_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_properties.
    def visitImage_properties(self, ctx:MERLANParser.Image_propertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_property.
    def visitImage_property(self, ctx:MERLANParser.Image_propertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_property_attribute.
    def visitImage_property_attribute(self, ctx:MERLANParser.Image_property_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenarios.
    def visitScenarios(self, ctx:MERLANParser.ScenariosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario.
    def visitScenario(self, ctx:MERLANParser.ScenarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#expression.
    def visitExpression(self, ctx:MERLANParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#boolean_expression.
    def visitBoolean_expression(self, ctx:MERLANParser.Boolean_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#expression_list.
    def visitExpression_list(self, ctx:MERLANParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario_entity.
    def visitScenario_entity(self, ctx:MERLANParser.Scenario_entityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario_image_object.
    def visitScenario_image_object(self, ctx:MERLANParser.Scenario_image_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario_image_property.
    def visitScenario_image_property(self, ctx:MERLANParser.Scenario_image_propertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_object_expression_attribute.
    def visitImage_object_expression_attribute(self, ctx:MERLANParser.Image_object_expression_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_property_expression_attribute.
    def visitImage_property_expression_attribute(self, ctx:MERLANParser.Image_property_expression_attributeContext):
        return self.visitChildren(ctx)



del MERLANParser