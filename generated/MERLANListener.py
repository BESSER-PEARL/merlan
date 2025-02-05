# Generated from grammar/MERLAN.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MERLANParser import MERLANParser
else:
    from MERLANParser import MERLANParser

# This class defines a complete listener for a parse tree produced by MERLANParser.
class MERLANListener(ParseTreeListener):

    # Enter a parse tree produced by MERLANParser#script.
    def enterScript(self, ctx:MERLANParser.ScriptContext):
        pass

    # Exit a parse tree produced by MERLANParser#script.
    def exitScript(self, ctx:MERLANParser.ScriptContext):
        pass


    # Enter a parse tree produced by MERLANParser#image_entities.
    def enterImage_entities(self, ctx:MERLANParser.Image_entitiesContext):
        pass

    # Exit a parse tree produced by MERLANParser#image_entities.
    def exitImage_entities(self, ctx:MERLANParser.Image_entitiesContext):
        pass


    # Enter a parse tree produced by MERLANParser#image_entity.
    def enterImage_entity(self, ctx:MERLANParser.Image_entityContext):
        pass

    # Exit a parse tree produced by MERLANParser#image_entity.
    def exitImage_entity(self, ctx:MERLANParser.Image_entityContext):
        pass


    # Enter a parse tree produced by MERLANParser#image_entity_attribute.
    def enterImage_entity_attribute(self, ctx:MERLANParser.Image_entity_attributeContext):
        pass

    # Exit a parse tree produced by MERLANParser#image_entity_attribute.
    def exitImage_entity_attribute(self, ctx:MERLANParser.Image_entity_attributeContext):
        pass


    # Enter a parse tree produced by MERLANParser#image_properties.
    def enterImage_properties(self, ctx:MERLANParser.Image_propertiesContext):
        pass

    # Exit a parse tree produced by MERLANParser#image_properties.
    def exitImage_properties(self, ctx:MERLANParser.Image_propertiesContext):
        pass


    # Enter a parse tree produced by MERLANParser#image_property.
    def enterImage_property(self, ctx:MERLANParser.Image_propertyContext):
        pass

    # Exit a parse tree produced by MERLANParser#image_property.
    def exitImage_property(self, ctx:MERLANParser.Image_propertyContext):
        pass


    # Enter a parse tree produced by MERLANParser#image_property_attribute.
    def enterImage_property_attribute(self, ctx:MERLANParser.Image_property_attributeContext):
        pass

    # Exit a parse tree produced by MERLANParser#image_property_attribute.
    def exitImage_property_attribute(self, ctx:MERLANParser.Image_property_attributeContext):
        pass


    # Enter a parse tree produced by MERLANParser#scenarios.
    def enterScenarios(self, ctx:MERLANParser.ScenariosContext):
        pass

    # Exit a parse tree produced by MERLANParser#scenarios.
    def exitScenarios(self, ctx:MERLANParser.ScenariosContext):
        pass


    # Enter a parse tree produced by MERLANParser#scenario.
    def enterScenario(self, ctx:MERLANParser.ScenarioContext):
        pass

    # Exit a parse tree produced by MERLANParser#scenario.
    def exitScenario(self, ctx:MERLANParser.ScenarioContext):
        pass


    # Enter a parse tree produced by MERLANParser#expression.
    def enterExpression(self, ctx:MERLANParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MERLANParser#expression.
    def exitExpression(self, ctx:MERLANParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MERLANParser#boolean_expression.
    def enterBoolean_expression(self, ctx:MERLANParser.Boolean_expressionContext):
        pass

    # Exit a parse tree produced by MERLANParser#boolean_expression.
    def exitBoolean_expression(self, ctx:MERLANParser.Boolean_expressionContext):
        pass


    # Enter a parse tree produced by MERLANParser#expression_list.
    def enterExpression_list(self, ctx:MERLANParser.Expression_listContext):
        pass

    # Exit a parse tree produced by MERLANParser#expression_list.
    def exitExpression_list(self, ctx:MERLANParser.Expression_listContext):
        pass


    # Enter a parse tree produced by MERLANParser#scenario_requirement.
    def enterScenario_requirement(self, ctx:MERLANParser.Scenario_requirementContext):
        pass

    # Exit a parse tree produced by MERLANParser#scenario_requirement.
    def exitScenario_requirement(self, ctx:MERLANParser.Scenario_requirementContext):
        pass


    # Enter a parse tree produced by MERLANParser#scenario_image_entity.
    def enterScenario_image_entity(self, ctx:MERLANParser.Scenario_image_entityContext):
        pass

    # Exit a parse tree produced by MERLANParser#scenario_image_entity.
    def exitScenario_image_entity(self, ctx:MERLANParser.Scenario_image_entityContext):
        pass


    # Enter a parse tree produced by MERLANParser#cardinality.
    def enterCardinality(self, ctx:MERLANParser.CardinalityContext):
        pass

    # Exit a parse tree produced by MERLANParser#cardinality.
    def exitCardinality(self, ctx:MERLANParser.CardinalityContext):
        pass


    # Enter a parse tree produced by MERLANParser#min_cardinality.
    def enterMin_cardinality(self, ctx:MERLANParser.Min_cardinalityContext):
        pass

    # Exit a parse tree produced by MERLANParser#min_cardinality.
    def exitMin_cardinality(self, ctx:MERLANParser.Min_cardinalityContext):
        pass


    # Enter a parse tree produced by MERLANParser#max_cardinality.
    def enterMax_cardinality(self, ctx:MERLANParser.Max_cardinalityContext):
        pass

    # Exit a parse tree produced by MERLANParser#max_cardinality.
    def exitMax_cardinality(self, ctx:MERLANParser.Max_cardinalityContext):
        pass


    # Enter a parse tree produced by MERLANParser#scenario_image_property.
    def enterScenario_image_property(self, ctx:MERLANParser.Scenario_image_propertyContext):
        pass

    # Exit a parse tree produced by MERLANParser#scenario_image_property.
    def exitScenario_image_property(self, ctx:MERLANParser.Scenario_image_propertyContext):
        pass


    # Enter a parse tree produced by MERLANParser#scenario_image_entity_attribute.
    def enterScenario_image_entity_attribute(self, ctx:MERLANParser.Scenario_image_entity_attributeContext):
        pass

    # Exit a parse tree produced by MERLANParser#scenario_image_entity_attribute.
    def exitScenario_image_entity_attribute(self, ctx:MERLANParser.Scenario_image_entity_attributeContext):
        pass


    # Enter a parse tree produced by MERLANParser#scenario_image_property_attribute.
    def enterScenario_image_property_attribute(self, ctx:MERLANParser.Scenario_image_property_attributeContext):
        pass

    # Exit a parse tree produced by MERLANParser#scenario_image_property_attribute.
    def exitScenario_image_property_attribute(self, ctx:MERLANParser.Scenario_image_property_attributeContext):
        pass



del MERLANParser