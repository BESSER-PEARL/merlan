# import sys
# sys.path.append("D:\\MARCOS\\Git\\merlan")

from antlr4 import *
from generated.MERLANLexer import MERLANLexer
from generated.MERLANParser import MERLANParser
from generated.MERLANVisitor import MERLANVisitor


class SymbolTable:

    def __init__(self):
        self.image_entities: set = set()
        self.image_properties: set = set()
        self.scenarios: set = set()

    def add_image_entity(self, name: str):
        if name in self.image_entities | self.image_properties | self.scenarios:
            raise ValueError(f"'{name}' is already defined")
        self.image_entities.add(name)

    def add_image_property(self, name: str):
        if name in self.image_entities | self.image_properties | self.scenarios:
            raise ValueError(f"'{name}' is already defined")
        self.image_properties.add(name)

    def add_scenario(self, name: str):
        if name in self.image_entities | self.image_properties | self.scenarios:
            raise ValueError(f"'{name}' is already defined")
        self.scenarios.add(name)

    def is_image_entity_defined(self, name: str) -> bool:
        return name in self.image_entities

    def is_image_property_defined(self, name: str) -> bool:
        return name in self.image_properties

    def is_scenario_defined(self, name: str) -> bool:
        return name in self.scenarios


class BESSERGenerator(MERLANVisitor):
    def __init__(self):
        super().__init__()
        self.symbol_table: SymbolTable = SymbolTable()
        self.code: list[str] = [
            "from besser.agent.core.image.image_entity import ImageEntity",
            "from besser.agent.core.image.image_property import ImageProperty",
            "from besser.agent.core.scenario.scenario import Scenario, AND, OR, NOT",
            "from besser.agent.core.scenario.scenario_image_entity import ScenarioImageEntity",
            "from besser.agent.core.scenario.scenario_image_property import ScenarioImageProperty",
        ]

    # Visit a parse tree produced by MERLANParser#script.
    def visitScript(self, ctx: MERLANParser.ScriptContext):
        self.visit(ctx.image_entities())
        self.visit(ctx.image_properties())
        self.visit(ctx.scenarios())
        return '\n'.join(self.code)

    # Visit a parse tree produced by MERLANParser#image_entities.
    def visitImage_entities(self, ctx: MERLANParser.Image_entitiesContext):
        self.code.append('# Image Entities')
        for image_entity in ctx.image_entity():
            self.visit(image_entity)

    # Visit a parse tree produced by MERLANParser#image_entity.
    def visitImage_entity(self, ctx: MERLANParser.Image_entityContext):
        id = ctx.ID().getText()
        self.symbol_table.add_image_entity(id)
        attribute_list = []
        for attribute in ctx.image_entity_attribute():
            attribute_list.append(self.visit(attribute))
        attributes = ', '.join(attribute_list)
        self.code.append(f'{id} = ImageEntity(name="{id}", attributes={{{attributes}}})')

    # Visit a parse tree produced by MERLANParser#image_entity_attribute.
    def visitImage_entity_attribute(self, ctx: MERLANParser.Image_entity_attributeContext):
        attribute_name = ctx.getChild(1).getText()
        attribute_value = ctx.getChild(3).getText()
        return f'"{attribute_name}": {attribute_value}'

    # Visit a parse tree produced by MERLANParser#image_properties.
    def visitImage_properties(self, ctx: MERLANParser.Image_propertiesContext):
        self.code.append('# Image Properties')
        for image_property in ctx.image_property():
            self.visit(image_property)

    # Visit a parse tree produced by MERLANParser#image_property.
    def visitImage_property(self, ctx: MERLANParser.Image_propertyContext):
        id = ctx.ID().getText()
        self.symbol_table.add_image_property(id)
        attribute_list = []
        for attribute in ctx.image_property_attribute():
            attribute_list.append(self.visit(attribute))
        attributes = ', '.join(attribute_list)
        self.code.append(f'{id} = ImageProperty(name="{id}", attributes={{{attributes}}})')

    # Visit a parse tree produced by MERLANParser#image_property_attribute.
    def visitImage_property_attribute(self, ctx: MERLANParser.Image_property_attributeContext):
        attribute_name = ctx.getChild(1).getText()
        attribute_value = ctx.getChild(3).getText()
        return f'"{attribute_name}": {attribute_value}'

    # Visit a parse tree produced by MERLANParser#scenarios.
    def visitScenarios(self, ctx: MERLANParser.ScenariosContext):
        self.code.append('# Scenarios')
        for scenario in ctx.scenario():
            self.visit(scenario)

    # Visit a parse tree produced by MERLANParser#scenario.
    def visitScenario(self, ctx: MERLANParser.ScenarioContext):
        id = ctx.ID().getText()
        self.symbol_table.add_scenario(id)
        self.code.append(f'{id} = Scenario("{id}")')
        expression = self.visit(ctx.expression())
        self.code.append(f'{id}.set_expression({expression})')

    # Visit a parse tree produced by MERLANParser#expression.
    def visitExpression(self, ctx: MERLANParser.ExpressionContext):
        if ctx.boolean_expression():
            return self.visit(ctx.boolean_expression())
        if ctx.scenario_requirement():
            return self.visit(ctx.scenario_requirement())

    # Visit a parse tree produced by MERLANParser#boolean_expression.
    def visitBoolean_expression(self, ctx: MERLANParser.Boolean_expressionContext):
        # TODO: Fix indentation
        operator = ctx.getChild(0).getText()
        if ctx.expression():
            expression_list = [self.visit(ctx.expression())]
        if ctx.expression_list():
            expression_list = self.visit(ctx.expression_list())
        indentation = "    " * (ctx.depth() - 1)
        expressions = indentation + "    " + f',\n{indentation}    '.join(expression_list) if expression_list else ''
        boolean_expression = (f'\n{indentation}{operator}([\n'
                              f'{expressions}\n'
                              f'{indentation}])')
        return boolean_expression

    # Visit a parse tree produced by MERLANParser#expression_list.
    def visitExpression_list(self, ctx: MERLANParser.Expression_listContext):
        expression_list = []
        for expression in ctx.expression():
            expression_list.append(self.visit(expression))
        return expression_list

    # Visit a parse tree produced by MERLANParser#scenario_requirement.
    def visitScenario_requirement(self, ctx:MERLANParser.Scenario_requirementContext):
        if ctx.scenario_image_entity():
            return self.visit(ctx.scenario_image_entity())
        if ctx.scenario_image_property():
            return self.visit(ctx.scenario_image_property())

    # Visit a parse tree produced by MERLANParser#scenario_image_entity.
    def visitScenario_image_entity(self, ctx:MERLANParser.Scenario_image_entityContext):
        attribute_list = []
        name = None
        image_entity = None
        if ctx.cardinality():
            min, max = self.visit(ctx.cardinality())
            attribute_list.append(f'min={min}')
            attribute_list.append(f'max={max}')
        for attribute in ctx.scenario_image_entity_attribute():
            if attribute.IMAGE_ENTITY_NAME():
                image_entity = attribute.ID().getText()
            elif attribute.NAME():
                name = attribute.STRING().getText()
            else:
                attribute_list.append(self.visit(attribute))
        if not name:
            raise ValueError(f"Missing 'name' in ScenarioImageEntity")
        if not image_entity:
            raise ValueError(f"Missing 'image_entity' reference in ScenarioImageEntity")
        attributes = ', '.join(attribute_list)
        expression = f'ScenarioImageEntity(name={name}, image_entity={image_entity}, {attributes})'
        return expression

    # Visit a parse tree produced by MERLANParser#cardinality.
    def visitCardinality(self, ctx: MERLANParser.CardinalityContext):
        max = self.visit(ctx.max_cardinality())
        if ctx.min_cardinality():
            min = self.visit(ctx.min_cardinality())
        elif max == 0:
            min = 1
        else:
            min = max
        if max != 0 and min > max:
            raise ValueError(f"Cardinality with min > max: min = {min}, max = {max}")
        return min, max

    # Visit a parse tree produced by MERLANParser#min_cardinality.
    def visitMin_cardinality(self, ctx: MERLANParser.Min_cardinalityContext):
        return ctx.INT_NONZERO().getText()

    # Visit a parse tree produced by MERLANParser#max_cardinality.
    def visitMax_cardinality(self, ctx: MERLANParser.Max_cardinalityContext):
        value = ctx.getChild(0).getText()
        if value == '*':
            value = 0
        return value

    # Visit a parse tree produced by MERLANParser#scenario_image_property.
    def visitScenario_image_property(self, ctx:MERLANParser.Scenario_image_propertyContext):
        attribute_list = []
        name = None
        image_property = None
        for attribute in ctx.scenario_image_property_attribute():
            if attribute.IMAGE_PROPERTY_NAME():
                image_property = attribute.ID().getText()
            elif attribute.NAME():
                name = attribute.STRING().getText()
            else:
                attribute_list.append(self.visit(attribute))
        if not name:
            raise ValueError(f"Missing 'name' in ScenarioImageProperty")
        if not image_property:
            raise ValueError(f"Missing 'image_proeprty' reference in ScenarioImageProperty")
        attributes = ', '.join(attribute_list)
        expression = f'ScenarioImageProperty(name={name}, image_property={image_property}, {attributes})'
        return expression

    # Visit a parse tree produced by MERLANParser#scenario_image_entity_attribute.
    def visitScenario_image_entity_attribute(self, ctx:MERLANParser.Scenario_image_entity_attributeContext):
        attribute_name = ctx.getChild(1).getText()
        attribute_value = ctx.getChild(3).getText()
        if ctx.IMAGE_ENTITY_NAME() and not self.symbol_table.is_image_entity_defined(attribute_value):
            raise ValueError(f"ImageEntity '{attribute_value}' is not defined")
        return f'{attribute_name}={attribute_value}'

    # Visit a parse tree produced by MERLANParser#scenario_image_property_attribute.
    def visitScenario_image_property_attribute(self, ctx:MERLANParser.Scenario_image_property_attributeContext):
        attribute_name = ctx.getChild(1).getText()
        attribute_value = ctx.getChild(3).getText()
        if ctx.IMAGE_PROPERTY_NAME() and not self.symbol_table.is_image_property_defined(attribute_value):
            raise ValueError(f"ImageProperty '{attribute_value}' is not defined")
        return f'{attribute_name}={attribute_value}'
