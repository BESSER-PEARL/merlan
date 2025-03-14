import sys
sys.path.append("D:\\MARCOS\\Git\\merlan")

from antlr4 import *
from generated.MERLANLexer import MERLANLexer
from generated.MERLANParser import MERLANParser
from generated.MERLANVisitor import MERLANVisitor


def get_attribute(attribute_name: str, attributes: list[tuple[str, str]]) -> str:
    attribute_values = [attribute[1] for attribute in attributes if attribute[0] == attribute_name]
    if len(attribute_values) != 1:
        raise ValueError(f"You must define 1 attribute named {attribute_name}")
    return attribute_values[0]


def join_attributes(attributes:  list[tuple[str, str]], exclude: list[str] = None):
    if exclude is None:
        exclude = []
    return ', '.join([f'"{attribute[0]}": {attribute[1]}' for attribute in attributes if attribute[0] not in exclude])

class SymbolTable:

    def __init__(self):
        self.concrete_entities: set = set()
        self.abstract_entities: set = set()
        self.requirements: set = set()

    def add_concrete_entity(self, name: str):
        if name in self.concrete_entities | self.abstract_entities | self.requirements:
            raise ValueError(f"'{name}' is already defined")
        self.concrete_entities.add(name)

    def add_abstract_entity(self, name: str):
        if name in self.concrete_entities | self.abstract_entities | self.requirements:
            raise ValueError(f"'{name}' is already defined")
        self.abstract_entities.add(name)

    def add_requirement(self, name: str):
        if name in self.concrete_entities | self.abstract_entities | self.requirements:
            raise ValueError(f"'{name}' is already defined")
        self.requirements.add(name)

    def is_concrete_entity_defined(self, name: str) -> bool:
        return name in self.concrete_entities

    def is_abstract_entity_defined(self, name: str) -> bool:
        return name in self.abstract_entities

    def is_requirement_defined(self, name: str) -> bool:
        return name in self.requirements


class BESSERGenerator(MERLANVisitor):

    def __init__(self):
        super().__init__()
        self.symbol_table: SymbolTable = SymbolTable()
        self.code: list[str] = [
            "from besser.agent.core.entity.image.abstract_entity import AbstractEntity",
            "from besser.agent.core.entity.image.concrete_entity import ConcreteEntity",
            "from besser.agent.core.requirement.abstract_requirement import AbstractRequirement",
            "from besser.agent.core.requirement.boolean_expression import OR, AND, NOT",
            "from besser.agent.core.requirement.concrete_requirement import ConcreteRequirement",
            "from besser.agent.core.requirement.requirement import Requirement"
        ]

    # Visit a parse tree produced by MERLANParser#script.
    def visitScript(self, ctx:MERLANParser.ScriptContext):
        self.visit(ctx.entities())
        self.visit(ctx.requirements())
        return '\n'.join(self.code)

    # Visit a parse tree produced by MERLANParser#entities.
    def visitEntities(self, ctx:MERLANParser.EntitiesContext):
        self.visit(ctx.concrete_entities())
        self.visit(ctx.abstract_entities())

    # Visit a parse tree produced by MERLANParser#attribute.
    def visitAttribute(self, ctx:MERLANParser.AttributeContext):
        # TODO if value is ID, check it exists (only under requirement, in entity is not allowed)
        attribute_name = ctx.getChild(1).getText()
        attribute_value = ctx.getChild(3).getText()
        if attribute_value == '?':
            attribute_value = '"?"'  # TODO: HANDLE EMPTY VALUES
        return attribute_name, attribute_value

    # Visit a parse tree produced by MERLANParser#concrete_entities.
    def visitConcrete_entities(self, ctx:MERLANParser.Concrete_entitiesContext):
        self.code.append('# Concrete Entities')
        for concrete_entity in ctx.concrete_entity():
            self.visit(concrete_entity)

    # Visit a parse tree produced by MERLANParser#concrete_entity.
    def visitConcrete_entity(self, ctx:MERLANParser.Concrete_entityContext):
        # TODO CHECK ATTRIBUTES ARE NOT REPEATED
        # TODO CHECK MANDATORY ATTRIBUTES
        # TODO ATTRIBUTE VALUE IS VALID TYPE
        id = ctx.ID().getText()
        self.symbol_table.add_concrete_entity(id)
        attribute_list = []
        for attribute in ctx.attribute():
            attribute_list.append(self.visit(attribute))
        attributes = join_attributes(attribute_list)
        # TODO UPDATE PYTHON CODE
        self.code.append(f'{id} = ConcreteEntity(name="{id}", attributes={{{attributes}}})')

    # Visit a parse tree produced by MERLANParser#abstract_entities.
    def visitAbstract_entities(self, ctx:MERLANParser.Abstract_entitiesContext):
        self.code.append('# Abstract Entities')
        for abstract_entity in ctx.abstract_entity():
            self.visit(abstract_entity)

    # Visit a parse tree produced by MERLANParser#abstract_entity.
    def visitAbstract_entity(self, ctx:MERLANParser.Abstract_entityContext):
        # TODO CHECK ATTRIBUTES ARE NOT REPEATED
        # TODO CHECK MANDATORY ATTRIBUTES
        # TODO ATTRIBUTE VALUE IS VALID TYPE
        id = ctx.ID().getText()
        self.symbol_table.add_abstract_entity(id)
        attribute_list = []
        for attribute in ctx.attribute():
            attribute_list.append(self.visit(attribute))
        attributes = join_attributes(attribute_list)
        # TODO UPDATE PYTHON CODE
        self.code.append(f'{id} = AbstractEntity(name="{id}", attributes={{{attributes}}})')

    # Visit a parse tree produced by MERLANParser#requirements.
    def visitRequirements(self, ctx:MERLANParser.RequirementsContext):
        self.code.append('# Requirements')
        for requirement_definition in ctx.requirement_definition():
            self.visit(requirement_definition)

    # Visit a parse tree produced by MERLANParser#requirement_definition.
    def visitRequirement_definition(self, ctx: MERLANParser.Requirement_definitionContext):
        id = ctx.ID().getText()
        self.symbol_table.add_requirement(id)
        # TODO UPDATE PYTHON CODE
        self.code.append(f'{id} = Requirement("{id}")')
        expression = self.visit(ctx.requirement())
        self.code.append(f'{id}.set_expression({expression})')

    # Visit a parse tree produced by MERLANParser#requirement.
    def visitRequirement(self, ctx:MERLANParser.RequirementContext):
        if ctx.simple_requirement():
            return self.visit(ctx.simple_requirement())
        elif ctx.complex_requirement():
            return self.visit(ctx.complex_requirement())

    # Visit a parse tree produced by MERLANParser#complex_requirement.
    def visitComplex_requirement(self, ctx:MERLANParser.Complex_requirementContext):
        operator = ctx.getChild(0).getText()
        requirement_list = []
        for requirement in ctx.requirement():
            requirement_list.append(self.visit(requirement))
        indentation = "    " * (ctx.depth() - 1)
        expressions = indentation + "    " + f',\n{indentation}    '.join(requirement_list) if requirement_list else ''
        boolean_expression = (f'\n{indentation}{operator}([\n'
                              f'{expressions}\n'
                              f'{indentation}])')
        return boolean_expression

    # Visit a parse tree produced by MERLANParser#simple_requirement.
    def visitSimple_requirement(self, ctx:MERLANParser.Simple_requirementContext):
        if ctx.concrete_requirement():
            return self.visit(ctx.concrete_requirement())
        elif ctx.abstract_requirement():
            return self.visit(ctx.abstract_requirement())

    # Visit a parse tree produced by MERLANParser#concrete_requirement.
    def visitConcrete_requirement(self, ctx:MERLANParser.Concrete_requirementContext):
        # TODO CHECK ATTRIBUTES ARE NOT REPEATED
        # TODO CHECK MANDATORY ATTRIBUTES
        # TODO ATTRIBUTE VALUE IS VALID TYPE
        attribute_list = []
        if ctx.cardinality():
            min, max = self.visit(ctx.cardinality())
            attribute_list.append(('min', min))
            attribute_list.append(('max', max))
        for attribute in ctx.attribute():
            attribute_list.append(self.visit(attribute))
        name = get_attribute('name', attribute_list)
        entity = get_attribute('entity', attribute_list)
        attributes = join_attributes(attribute_list, exclude=['name', 'entity'])
        # TODO UPDATE PYTHON CODE
        expression = f'ConcreteRequirement(name={name}, concrete_entity={entity}, attributes={{{attributes}}})'
        return expression

    # Visit a parse tree produced by MERLANParser#abstract_requirement.
    def visitAbstract_requirement(self, ctx:MERLANParser.Abstract_requirementContext):
        # TODO CHECK ATTRIBUTES ARE NOT REPEATED
        # TODO CHECK MANDATORY ATTRIBUTES
        # TODO ATTRIBUTE VALUE IS VALID TYPE
        attribute_list = []
        for attribute in ctx.attribute():
            attribute_list.append(self.visit(attribute))
        name = get_attribute('name', attribute_list)
        entity = get_attribute('entity', attribute_list)
        attributes = join_attributes(attribute_list, exclude=['name', 'entity'])
        # TODO UPDATE PYTHON CODE
        expression = f'AbstractRequirement(name={name}, abstract_entity={entity}, attributes={{{attributes}}})'
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
