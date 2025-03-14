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


    # Visit a parse tree produced by MERLANParser#entities.
    def visitEntities(self, ctx:MERLANParser.EntitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#attribute.
    def visitAttribute(self, ctx:MERLANParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#concrete_entities.
    def visitConcrete_entities(self, ctx:MERLANParser.Concrete_entitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#concrete_entity.
    def visitConcrete_entity(self, ctx:MERLANParser.Concrete_entityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#abstract_entities.
    def visitAbstract_entities(self, ctx:MERLANParser.Abstract_entitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#abstract_entity.
    def visitAbstract_entity(self, ctx:MERLANParser.Abstract_entityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#requirements.
    def visitRequirements(self, ctx:MERLANParser.RequirementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#requirement_definition.
    def visitRequirement_definition(self, ctx:MERLANParser.Requirement_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#requirement.
    def visitRequirement(self, ctx:MERLANParser.RequirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#complex_requirement.
    def visitComplex_requirement(self, ctx:MERLANParser.Complex_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#simple_requirement.
    def visitSimple_requirement(self, ctx:MERLANParser.Simple_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#concrete_requirement.
    def visitConcrete_requirement(self, ctx:MERLANParser.Concrete_requirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MERLANParser#abstract_requirement.
    def visitAbstract_requirement(self, ctx:MERLANParser.Abstract_requirementContext):
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



del MERLANParser