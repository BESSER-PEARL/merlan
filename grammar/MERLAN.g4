grammar MERLAN;

// Root rule
script
        : NEWLINE?
          entities?
          requirements?
          NEWLINE?
          EOF
        ;

entities
        : ENTITIES NEWLINE
          concrete_entities?
          abstract_entities?
        ;


attribute
        : HYPHEN ID COLON (ID | STRING | FLOAT | INT | UNK) NEWLINE
        ;

// Concrete entities definition
concrete_entities
        : CONCRETE NEWLINE concrete_entity*
        ;

concrete_entity
        : ID NEWLINE attribute*
        ;

// Abstract entities definition
abstract_entities
        : ABSTRACT NEWLINE abstract_entity*
        ;

abstract_entity
        : ID NEWLINE attribute*
        ;

// Requirements definition
requirements
        : REQUIREMENTS NEWLINE requirement_definition+
        ;

requirement_definition
        : ID NEWLINE requirement
        ;

requirement
        : complex_requirement
        | simple_requirement
        ;

complex_requirement
        : (AND | OR) NEWLINE requirement+
        | NOT NEWLINE requirement
        ;

simple_requirement
        : abstract_requirement
        | concrete_requirement
        ;

concrete_requirement
        : CONCRETE modality cardinality? NEWLINE attribute*
        ;

abstract_requirement
        : ABSTRACT modality NEWLINE attribute*
        ;

modality
        : IMAGE | AUDIO | TEXT | VIDEO | GESTURE | SENSOR
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

// Tokens

ENTITIES            : 'ENTITIES' ;
CONCRETE            : 'CONCRETE' ;
ABSTRACT            : 'ABSTRACT' ;
REQUIREMENTS        : 'REQUIREMENTS' ;

AND                 : 'AND' ;
OR                  : 'OR' ;
NOT                 : 'NOT' ;

IMAGE               : 'IMAGE' ;
AUDIO               : 'AUDIO' ;
TEXT                : 'TEXT' ;
VIDEO               : 'VIDEO' ;
GESTURE             : 'GESTURE' ;
SENSOR              : 'SENSOR' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING : '"' (~["\\] | '\\' .)* '"' ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT_NONZERO : [1-9] [0-9]* ;
INT : [0-9]+ ;
UNK : '?' ;
SIGINT : '-'? INT ;
STAR : '*' ;

// Whitespace and formatting
NEWLINE : ('\r'? '\n')+ ;
WS : [ \t]+ -> skip ;
HYPHEN : '- ' ;
COLON : ': ' ;

// Comments (inline C++-style)
COMMENT   : '//' ~('\n'|'\r')* '\r'? '\n' -> skip ;
