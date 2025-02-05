grammar MERLAN;

// Root rule
script
        : NEWLINE?
          image_entities?
          image_properties?
          scenarios?
          NEWLINE?
          EOF
        ;

// Image entities definition
image_entities
        : IMAGE_ENTITIES NEWLINE image_entity*
        ;

image_entity
        : ID NEWLINE image_entity_attribute*
        ;


image_entity_attribute
        : HYPHEN DESCRIPTION COLON STRING NEWLINE
        | HYPHEN COLOR COLON STRING NEWLINE
        | HYPHEN WEIGHT COLON FLOAT NEWLINE
        ;

// Image properties definition
image_properties
        : IMAGE_PROPERTIES NEWLINE image_property*
        ;

image_property
        : ID NEWLINE image_property_attribute*
        ;

image_property_attribute
        : HYPHEN DESCRIPTION COLON STRING NEWLINE
        | HYPHEN LIGHTING COLON STRING NEWLINE
        | HYPHEN VERSION COLON SIGINT NEWLINE
        ;

// Scenarios definition
scenarios
        : SCENARIOS (NEWLINE scenario)+
        ;

scenario
        : ID NEWLINE expression
        ;

expression
        : boolean_expression
        | scenario_requirement
        ;

boolean_expression
        : (AND | OR) NEWLINE expression_list
        | NOT NEWLINE expression
        ;

expression_list
        : expression (NEWLINE expression)*
        ;

scenario_requirement
        : scenario_image_entity
        | scenario_image_property
        ;

scenario_image_entity
        : IMAGE_ENTITY cardinality? (NEWLINE scenario_image_entity_attribute)+
        ;

cardinality
        : '[' min_cardinality? max_cardinality ']'
        ;

min_cardinality
        : INT_NONZERO '..'
        ;

max_cardinality
        : INT_NONZERO | STAR
        ;

scenario_image_property
        : IMAGE_PROPERTY (NEWLINE scenario_image_property_attribute)+
        ;

scenario_image_entity_attribute
        : HYPHEN IMAGE_ENTITY_NAME COLON ID
        | HYPHEN NAME COLON STRING
        | HYPHEN SCORE COLON FLOAT
        ;

scenario_image_property_attribute
        : HYPHEN IMAGE_PROPERTY_NAME COLON ID
        | HYPHEN NAME COLON STRING
        | HYPHEN SCORE COLON FLOAT
        ;

// Tokens

IMAGE_ENTITY        : 'IMAGE_ENTITY' ;
IMAGE_ENTITIES      : 'IMAGE_ENTITIES' ;
IMAGE_PROPERTY      : 'IMAGE_PROPERTY' ;
IMAGE_PROPERTIES    : 'IMAGE_PROPERTIES' ;
SCENARIOS           : 'SCENARIOS' ;

AND                 : 'AND' ;
OR                  : 'OR' ;
NOT                 : 'NOT' ;

COLOR               : 'color' ;
DESCRIPTION         : 'description' ;
WEIGHT              : 'weight' ;
LIGHTING            : 'lighting' ;
VERSION             : 'version' ;

IMAGE_ENTITY_NAME   : 'image_entity' ;
IMAGE_PROPERTY_NAME : 'image_property' ;
NAME                : 'name' ;
SCORE               : 'score' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING : '"' (~["\\] | '\\' .)* '"' ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT_NONZERO : [1-9] [0-9]* ;
INT : [0-9]+ ;
SIGINT : '-'? INT ;
STAR : '*' ;

// Whitespace and formatting
NEWLINE : ('\r'? '\n')+ ;
WS : [ \t]+ -> skip ;
HYPHEN : '- ' ;
COLON : ': ' ;

// Comments (inline C++-style)
COMMENT   : '//' ~('\n'|'\r')* '\r'? '\n' -> skip ;
