import ply.lex as lex
import sys

#Palabras reservadas
resultado_lexema = []

with open('main.txt','r',encoding='utf8') as programa: 
    mein = programa.read()

reserved ={
    'if': 'IF',
    'else':'ELSE',
    'main':'MAIN',
    'let' :'LET',
    'for':'FOR',
    'while':'WHILE',
    'loop':'LOOP',
    'print':'PRINT',
    'read' : 'READ',
    'break':'BREAK',
    'in': 'IN',
    'fun': 'FUN',
    'rows':'ROWS',
    'columns':'COLUMNS'
}

tokens =[
    'PLUS','MINUS','DIVIDE','MULT','MENOR','MAYOR','IGUAL','EQUAL',
    'MENORIGUAL','MAYORIGUAL','CONSTANTE','ID','LPAREN',
    'RPAREN','NOTEQUAL','LCOR','RCOR',
    'AND','OR','STRING','RKEY','LKEY','PUNTO'
]+list(reserved.values())

#DEFINICON DE LOS TOKENS
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUAL = r'='
t_MULT = r'\*'
t_LPAREN =r'\('
t_RPAREN =r'\)'
#t_NOT = r'\!'
t_LCOR = r'\['
t_RCOR = r'\]'
t_ignore  = ' \t'
t_LKEY =r'\{'
t_RKEY =r'\}'
t_PUNTO =r'\.'




def t_EQUAL(t):
    r'=='
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_CONDOUBLE(t):
    r'(\d+|(\-)\d+)(\.)(\d+)'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0.0
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_CONSTANTE(t):
    r'(\d+)|(\-)\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
   #r'\w(\w|\d)*(_(\d|\w)+)*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NOTEQUAL(t):
    r'!='
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MINMIN(t):
    r'\-\-'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#def t_COMMENT(t):
#     r'(/\*(.|\n)*?\*/)|(//.*)'
#     pass


def t_STRING(t):
    r'\"(.)*?\"'
    t.type = reserved.get(t.value,'STRING')
    return t


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    #while True:
        #data = input("ingrese: ")
    #data = programa.read()
    prueba(mein)
    #print(mein)
    for i in range(0, len(resultado_lexema)):
        print(resultado_lexema[i] + "\n")