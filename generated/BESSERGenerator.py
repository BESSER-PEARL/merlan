# import sys
# sys.path.append("D:\\MARCOS\\Git\\merlan")

from antlr4 import *
from generated.MERLANLexer import MERLANLexer
from generated.MERLANParser import MERLANParser
from generated.MERLANVisitor import MERLANVisitor


class SymbolTable:

    def __init__(self):
        self.image_objects: set = set()
        self.image_properties: set = set()
        self.scenarios: set = set()

    def add_image_object(self, name: str):
        if name in self.image_objects | self.image_properties | self.scenarios:
            raise ValueError(f"'{name}' is already defined")
        self.image_objects.add(name)

    def add_image_property(self, name: str):
        if name in self.image_objects | self.image_properties | self.scenarios:
            raise ValueError(f"'{name}' is already defined")
        self.image_properties.add(name)

    def add_scenario(self, name: str):
        if name in self.image_objects | self.image_properties | self.scenarios:
            raise ValueError(f"'{name}' is already defined")
        self.scenarios.add(name)

    def is_image_object_defined(self, name: str) -> bool:
        return name in self.image_objects

    def is_image_property_defined(self, name: str) -> bool:
        return name in self.image_properties

    def is_scenario_defined(self, name: str) -> bool:
        return name in self.scenarios


class BESSERGenerator(MERLANVisitor):
    def __init__(self):
        super().__init__()
        self.symbol_table: SymbolTable = SymbolTable()
        self.code: list[str] = [
            "from besser.agent.core.image.image_object import ImageObject",
            "from besser.agent.core.image.image_property import ImageProperty",
            "from besser.agent.core.scenario.scenario import Scenario, AND, OR, NOT",
            "from besser.agent.core.scenario.scenario_image_object import ScenarioImageObject",
            "from besser.agent.core.scenario.scenario_image_property import ScenarioImageProperty",
        ]

    # Visit a parse tree produced by MERLANParser#script.
    def visitScript(self, ctx: MERLANParser.ScriptContext):
        self.visit(ctx.image_objects())
        self.visit(ctx.image_properties())
        self.visit(ctx.scenarios())
        return '\n'.join(self.code)

    # Visit a parse tree produced by MERLANParser#image_objects.
    def visitImage_objects(self, ctx: MERLANParser.Image_objectsContext):
        self.code.append('# Image Objects')
        for image_object in ctx.image_object():
            self.visit(image_object)

    # Visit a parse tree produced by MERLANParser#image_object.
    def visitImage_object(self, ctx: MERLANParser.Image_objectContext):
        id = ctx.ID().getText()
        self.symbol_table.add_image_object(id)
        attribute_list = []
        for attribute in ctx.image_object_attribute():
            attribute_list.append(self.visit(attribute))
        attributes = ', '.join(attribute_list)
        self.code.append(f'{id} = ImageObject(name="{id}", attributes={{{attributes}}})')

    # Visit a parse tree produced by MERLANParser#image_object_attribute.
    def visitImage_object_attribute(self, ctx: MERLANParser.Image_object_attributeContext):
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
        if ctx.scenario_entity():
            return self.visit(ctx.scenario_entity())

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

    # Visit a parse tree produced by MERLANParser#scenario_entity.
    def visitScenario_entity(self, ctx:MERLANParser.Scenario_entityContext):
        if ctx.scenario_image_object():
            return self.visit(ctx.scenario_image_object())
        if ctx.scenario_image_property():
            return self.visit(ctx.scenario_image_property())

    # Visit a parse tree produced by MERLANParser#scenario_image_object.
    def visitScenario_image_object(self, ctx:MERLANParser.Scenario_image_objectContext):
        attribute_list = []
        for attribute in ctx.image_object_expression_attribute():
            attribute_list.append(self.visit(attribute))
        attributes = ', '.join(attribute_list)
        expression = f'ScenarioImageObject({attributes})'
        return expression


    # Visit a parse tree produced by MERLANParser#scenario_image_property.
    def visitScenario_image_property(self, ctx:MERLANParser.Scenario_image_propertyContext):
        attribute_list = []
        for attribute in ctx.image_property_expression_attribute():
            attribute_list.append(self.visit(attribute))
        attributes = ', '.join(attribute_list)
        expression = f'ScenarioImageProperty({attributes})'
        return expression

    # Visit a parse tree produced by MERLANParser#image_object_expression_attribute.
    def visitImage_object_expression_attribute(self, ctx:MERLANParser.Image_object_expression_attributeContext):
        attribute_name = ctx.getChild(1).getText()
        attribute_value = ctx.getChild(3).getText()
        if ctx.IMAGE_OBJECT_NAME() and not self.symbol_table.is_image_object_defined(attribute_value):
            raise ValueError(f"ImageObject '{attribute_value}' is not defined")
        return f'{attribute_name}={attribute_value}'

    # Visit a parse tree produced by MERLANParser#image_property_expression_attribute.
    def visitImage_property_expression_attribute(self, ctx:MERLANParser.Image_property_expression_attributeContext):
        attribute_name = ctx.getChild(1).getText()
        attribute_value = ctx.getChild(3).getText()
        if ctx.IMAGE_PROPERTY_NAME() and not self.symbol_table.is_image_property_defined(attribute_value):
            raise ValueError(f"ImageProperty '{attribute_value}' is not defined")
        return f'{attribute_name}={attribute_value}'
