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


    # Visit a parse tree produced by MERLANParser#image_entities.
    def visitImage_entities(self, ctx:MERLANParser.Image_entitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_entity.
    def visitImage_entity(self, ctx:MERLANParser.Image_entityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#image_entity_attribute.
    def visitImage_entity_attribute(self, ctx:MERLANParser.Image_entity_attributeContext):
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


    # Visit a parse tree produced by MERLANParser#scenario_requirement.
    def visitScenario_requirement(self, ctx:MERLANParser.Scenario_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario_image_entity.
    def visitScenario_image_entity(self, ctx:MERLANParser.Scenario_image_entityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#cardinality.
    def visitCardinality(self, ctx:MERLANParser.CardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#min_cardinality.
    def visitMin_cardinality(self, ctx:MERLANParser.Min_cardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#max_cardinality.
    def visitMax_cardinality(self, ctx:MERLANParser.Max_cardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario_image_property.
    def visitScenario_image_property(self, ctx:MERLANParser.Scenario_image_propertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario_image_entity_attribute.
    def visitScenario_image_entity_attribute(self, ctx:MERLANParser.Scenario_image_entity_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#scenario_image_property_attribute.
    def visitScenario_image_property_attribute(self, ctx:MERLANParser.Scenario_image_property_attributeContext):
        return self.visitChildren(ctx)



del MERLANParser