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


    # Enter a parse tree produced by MERLANParser#entities.
    def enterEntities(self, ctx:MERLANParser.EntitiesContext):
        pass

    # Exit a parse tree produced by MERLANParser#entities.
    def exitEntities(self, ctx:MERLANParser.EntitiesContext):
        pass


    # Enter a parse tree produced by MERLANParser#attribute.
    def enterAttribute(self, ctx:MERLANParser.AttributeContext):
        pass

    # Exit a parse tree produced by MERLANParser#attribute.
    def exitAttribute(self, ctx:MERLANParser.AttributeContext):
        pass


    # Enter a parse tree produced by MERLANParser#concrete_entities.
    def enterConcrete_entities(self, ctx:MERLANParser.Concrete_entitiesContext):
        pass

    # Exit a parse tree produced by MERLANParser#concrete_entities.
    def exitConcrete_entities(self, ctx:MERLANParser.Concrete_entitiesContext):
        pass


    # Enter a parse tree produced by MERLANParser#concrete_entity.
    def enterConcrete_entity(self, ctx:MERLANParser.Concrete_entityContext):
        pass

    # Exit a parse tree produced by MERLANParser#concrete_entity.
    def exitConcrete_entity(self, ctx:MERLANParser.Concrete_entityContext):
        pass


    # Enter a parse tree produced by MERLANParser#abstract_entities.
    def enterAbstract_entities(self, ctx:MERLANParser.Abstract_entitiesContext):
        pass

    # Exit a parse tree produced by MERLANParser#abstract_entities.
    def exitAbstract_entities(self, ctx:MERLANParser.Abstract_entitiesContext):
        pass


    # Enter a parse tree produced by MERLANParser#abstract_entity.
    def enterAbstract_entity(self, ctx:MERLANParser.Abstract_entityContext):
        pass

    # Exit a parse tree produced by MERLANParser#abstract_entity.
    def exitAbstract_entity(self, ctx:MERLANParser.Abstract_entityContext):
        pass


    # Enter a parse tree produced by MERLANParser#requirements.
    def enterRequirements(self, ctx:MERLANParser.RequirementsContext):
        pass

    # Exit a parse tree produced by MERLANParser#requirements.
    def exitRequirements(self, ctx:MERLANParser.RequirementsContext):
        pass


    # Enter a parse tree produced by MERLANParser#requirement_definition.
    def enterRequirement_definition(self, ctx:MERLANParser.Requirement_definitionContext):
        pass

    # Exit a parse tree produced by MERLANParser#requirement_definition.
    def exitRequirement_definition(self, ctx:MERLANParser.Requirement_definitionContext):
        pass


    # Enter a parse tree produced by MERLANParser#requirement.
    def enterRequirement(self, ctx:MERLANParser.RequirementContext):
        pass

    # Exit a parse tree produced by MERLANParser#requirement.
    def exitRequirement(self, ctx:MERLANParser.RequirementContext):
        pass


    # Enter a parse tree produced by MERLANParser#complex_requirement.
    def enterComplex_requirement(self, ctx:MERLANParser.Complex_requirementContext):
        pass

    # Exit a parse tree produced by MERLANParser#complex_requirement.
    def exitComplex_requirement(self, ctx:MERLANParser.Complex_requirementContext):
        pass


    # Enter a parse tree produced by MERLANParser#simple_requirement.
    def enterSimple_requirement(self, ctx:MERLANParser.Simple_requirementContext):
        pass

    # Exit a parse tree produced by MERLANParser#simple_requirement.
    def exitSimple_requirement(self, ctx:MERLANParser.Simple_requirementContext):
        pass


    # Enter a parse tree produced by MERLANParser#concrete_requirement.
    def enterConcrete_requirement(self, ctx:MERLANParser.Concrete_requirementContext):
        pass

    # Exit a parse tree produced by MERLANParser#concrete_requirement.
    def exitConcrete_requirement(self, ctx:MERLANParser.Concrete_requirementContext):
        pass


    # Enter a parse tree produced by MERLANParser#abstract_requirement.
    def enterAbstract_requirement(self, ctx:MERLANParser.Abstract_requirementContext):
        pass

    # Exit a parse tree produced by MERLANParser#abstract_requirement.
    def exitAbstract_requirement(self, ctx:MERLANParser.Abstract_requirementContext):
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



del MERLANParser