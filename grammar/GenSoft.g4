grammar GenSoft;

// =========================================
// REGLAS DEL PARSER (minúsculas)
// =========================================

programa
    : sentencia+ EOF
    ;

sentencia
    : declaracionProyecto
    | comandoGenerar
    ;

declaracionProyecto
    : PROYECTO ID TIPO tipoProyecto LLAVE_ABRE modulo* LLAVE_CIERRA
    ;

tipoProyecto
    : WEB | CONSOLA | API
    ;

modulo
    : MODULO ID LLAVE_ABRE campo* LLAVE_CIERRA
    ;

campo
    : CAMPO ID DOS_PUNTOS tipoDato PUNTO_COMA
    ;

tipoDato
    : STRING | ENTERO | DECIMAL | BOOLEANO
    ;

comandoGenerar
    : GENERAR ID PUNTO_COMA
    ;

// =========================================
// PALABRAS RESERVADAS
// =========================================

PROYECTO : 'proyecto' ;
MODULO   : 'modulo'   ;
CAMPO    : 'campo'    ;
TIPO     : 'tipo'     ;
GENERAR  : 'generar'  ;

WEB      : 'web'      ;
CONSOLA  : 'consola'  ;
API      : 'api'      ;

STRING   : 'string'   ;
ENTERO   : 'entero'   ;
DECIMAL  : 'decimal'  ;
BOOLEANO : 'booleano' ;

// =========================================
// SÍMBOLOS
// =========================================

LLAVE_ABRE   : '{' ;
LLAVE_CIERRA : '}' ;
DOS_PUNTOS   : ':' ;
PUNTO_COMA   : ';' ;

// =========================================
// IDENTIFICADORES Y ESPACIOS
// =========================================

ID : [a-zA-Z_] [a-zA-Z_0-9]* ;

WS                : [ \t\r\n]+ -> skip ;
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip ;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip ;