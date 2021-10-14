import ply.yacc as yacc
import sys

from lexer import tokens
from lexer import analizador

tabSym =[] #Tabla de simbolos
aux = 0
def p_DUNDLE(p):
    'DUNDLE : FUNCTIONS MEIN'
def p_MEIN(p):
    'MEIN : MAIN LPAREN RPAREN LKEY M RKEY'
def p_FUNCTIONS(p):
    '''
    FUNCTIONS : FUN ID LPAREN RPAREN LKEY M RKEY FUNCTIONS 
              | 
    '''
def p_M(p): 
    '''
    M : AUX1 M             
     |
    '''

def p_AUX1(p):
    '''
    AUX1 : DECLARACION
        | LLAMAFUN
        | IMPRESION
        | CONDICIONALIF
        | CONDICIONALLETIF
        | CICLOWHILE
        | CICLOLOOP
        | CICLOFOR
        | MATASSIG
        | MATOPE
    '''
def p_DECLARACION(p):
    '''
    DECLARACION : LET ID
               | LET ID IGUAL READ LPAREN RPAREN
               | LET ID IGUAL EXPRESION
               | LET ID  DIMENSION
               | ID IGUAL EXPRESION
    '''
    if p[1] == 'let' and p[3] != 'read':
        aux = p[2]
        tabSym.append(aux)
    #elif p[1] == '=':
    #    aux = p[2]



def p_LLAMAFUN(p):
    '''
    LLAMAFUN : ID LPAREN RPAREN
                | ID DIMENSION
    '''
def p_DIMENSION(p):
    '''
    DIMENSION : LCOR CONSTANTE RCOR 
             | LCOR CONSTANTE RCOR LCOR CONSTANTE RCOR
             | LCOR CONSTANTE RCOR LCOR CONSTANTE RCOR LCOR CONSTANTE RCOR
    '''
def p_IMPRESION(p):
    '''
    IMPRESION : PRINT LPAREN ID RPAREN
             | PRINT LPAREN  STRING  RPAREN
    '''
def p_CONDICIONALIF(p):
    '''
    CONDICIONALIF : IF LPAREN C RPAREN LKEY M RKEY
                  | IF LPAREN C RPAREN LKEY M RKEY ELSE LKEY M RKEY
                  | IF LPAREN MATCOMP RPAREN LKEY M RKEY 
                  | IF LPAREN MATCOMP RPAREN LKEY M RKEY ELSE LKEY M RKEY
    '''
def p_MATCOMP(p):
    '''
    MATCOMP : ID PUNTO ROWS EQUAL ID PUNTO ROWS AND ID PUNTO COLUMNS EQUAL ID PUNTO COLUMNS
    '''

def p_CONDICIONALLETLIF(p):
    '''
    CONDICIONALLETIF : LET ID IGUAL IF LPAREN C RPAREN LKEY CONSID RKEY ELSE LKEY CONSID RKEY
    
    '''

def p_CONSID(p):
    '''
    CONSID : CONSTANTE
          | ID
    '''
def p_CICLOWHILE(p):
    '''
    CICLOWHILE : WHILE LPAREN C RPAREN LKEY M RKEY 
    '''
def p_CICLOLOOP(p):
    '''
    CICLOLOOP : LOOP LKEY M RKEY
             | LOOP LKEY M BREAK RKEY

    '''
def p_CICLOFOR(p):
    '''
    CICLOFOR : FOR LPAREN ID IN ID PUNTO CORROWS RPAREN LKEY M RKEY
    '''
def p_CORROWS(p):
    '''
    CORROWS : COLUMNS
            | ROWS
    '''
def p_ANOR(p):
    '''
    ANOR : AND
        | OR
    '''
def p_C(p):
    '''
    C : CONSID SIMBOLS CONSID 
      | CONSID SIMBOLS CONSID ANOR C
    '''
def p_SIMBOLS(p):
    '''
    SIMBOLS : MENOR
           | EQUAL
           | MAYOR
           | NOTEQUAL
           | MENORIGUAL
           | MAYORIGUAL
    '''
def p_EXPRESION(p):
    '''
    EXPRESION : T
             | T PLUS T
             | T MINUS T
    '''
def p_T(p):
    '''
    T : F
     | F MULT
     | F DIVIDE
     |
    '''
def p_F(p):
    '''
    F : ID
     | CONSTANTE
     | LPAREN EXPRESION RPAREN
    '''
def p_MATASSIG(p):
    '''
    MATASSIG : ID LCOR CONSTANTE RCOR LCOR CONSTANTE RCOR IGUAL CONSTANTE 
    '''
def p_MATOPE(p):
    '''
    MATOPE : ID LCOR ID RCOR LCOR ID RCOR IGUAL ID LCOR ID RCOR LCOR ID RCOR OPS ID LCOR ID RCOR LCOR ID RCOR
              '''    
def p_OPS(p):
    '''
        OPS : PLUS
             | MINUS
             | MULT
             | DIVIDE
    '''
def p_error(t):
    if t:
        resultado = "Error sintactico de tipo {} en el valor {} en la linea {} y posicion {}".format(str(t.type), str(t.value),str(t.lineno),str(t.lexpos) )
        print(resultado)
    
parser = yacc.yacc()

if __name__ == '__main__':

    with open('suma.txt','r',encoding='utf8') as programa: 
        mein = programa.read()
    parser.parse(mein)
    print(tabSym)