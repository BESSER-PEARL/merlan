grammar MERLAN;

// Root rule
script
        : NEWLINE?
          image_objects?
          image_properties?
          scenarios?
          NEWLINE?
          EOF
        ;

// Image objects definition
image_objects
        : IMAGE_OBJECTS NEWLINE image_object*
        ;

image_object
        : ID NEWLINE image_object_attribute*
        ;


image_object_attribute
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
        | HYPHEN VERSION COLON INT NEWLINE
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
        | scenario_entity
        ;

boolean_expression
        : (AND | OR) NEWLINE expression_list
        | NOT NEWLINE expression
        ;

expression_list
        : expression (NEWLINE expression)*
        ;

scenario_entity
        : scenario_image_object
        | scenario_image_property
        ;

scenario_image_object
        : IMAGE_OBJECT (NEWLINE image_object_expression_attribute)+
        ;

scenario_image_property
        : IMAGE_PROPERTY (NEWLINE image_property_expression_attribute)+
        ;

image_object_expression_attribute
        : HYPHEN IMAGE_OBJECT_NAME COLON ID
        | HYPHEN NAME COLON STRING
        | HYPHEN MIN COLON INT
        | HYPHEN MAX COLON INT
        | HYPHEN SCORE COLON FLOAT
        ;

image_property_expression_attribute
        : HYPHEN IMAGE_PROPERTY_NAME COLON ID
        | HYPHEN NAME COLON STRING
        | HYPHEN SCORE COLON FLOAT
        ;

// Tokens

IMAGE_OBJECT        : 'IMAGE_OBJECT' ;
IMAGE_OBJECTS       : 'IMAGE_OBJECTS' ;
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

IMAGE_OBJECT_NAME   : 'image_object' ;
IMAGE_PROPERTY_NAME : 'image_property' ;
MAX                 : 'max' ;
MIN                 : 'min' ;
NAME                : 'name' ;
SCORE               : 'score' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING : '"' (~["\\] | '\\' .)* '"' ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT : [0-9]+ ;

// Whitespace and formatting
NEWLINE : ('\r'? '\n')+ ;
WS : [ \t]+ -> skip ;
HYPHEN : '- ' ;
COLON : ': ' ;

// Comments (inline C++-style)
COMMENT   : '//' ~('\n'|'\r')* '\r'? '\n' -> skip ;
