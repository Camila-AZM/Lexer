import ply
import ply.lex as lex

tokens=(
    'TipoDocumento',
    'A_Article',
    'C_Article',
    'A_Section',
    'C_Section',
    'A_SimpleSection',
    'C_SimpleSection',
    'A_Info',
    'C_Info',
    'A_Abstract',
    'C_Abstract',
    'A_Address',
    'C_Address',
    'A_Author',
    'C_Author',
    'A_Copyright',
    'C_Copyright',
    'A_Para',
    'C_Para',
    'A_Estructurales',
    'C_Estructurales',
    'A_Important',
    'C_Important',
    'A_InfoAutor',
    'C_InfoAutor',
    'A_MediaObject',
    'C_MediaObject',
    'A_VideoObject',
    'C_VideoObject',
    'A_ImageObject',
    'C_ImageObject',
    'ImageData',
    'VideoData',
    'A_ItemizedList',
    'C_ItemizedList',
    'A_InformalTable',
    'C_InformalTable',
    'A_Tgroup',
    'C_Tgroup',
    'A_Thead',
    'C_Thead',
    'A_Tfoot',
    'C_Tfoot',
    'A_Tbody',
    'C_Tbody',
    'A_Row',
    'C_Row',
    'A_EntryTbl',
    'C_EntryTbl',
    'A_Entry',
    'C_Entry',
    'Protocolo',
    'Dominio',
    'Puerto',
    'Ruta',
    'Contenido',
    'nuevalinea',
    'espacios'
)


def t_TipoDocumento(t):
    r'<!DOCTYPE article>'
    return t

def t_A_Article(t):    
    r'<article>'
    return t

def t_C_Article(t): 
    r'</article>'
    return t

def t_A_Section(t): 
    r'<section>'
    return t

def t_C_Section(t): 
    r'</section>'
    return t

def t_A_SimpleSection(t): 
    r'<simplesect>'
    return t

def t_C_SimpleSection(t):
    r'</simplesect>'
    return t

def t_A_Info(t):
    r'<info>'
    return t

def t_C_Info(t) :   
    r'</info>'
    return t

def t_A_Abstract(t):   
    r'<abstract>'
    return t

def t_C_Abstract(t): 
    r'</abstract>'
    return t

def t_A_Address(t): 
    r'<address>'
    return t

def t_C_Address(t): 
    r'</address>'
    return t

def t_A_Author(t):
    r'<author>'
    return t

def t_C_Author(t):
    r'</author>'
    return t

def t_A_Copyright(t):
    r'<copyright>'
    return t

def t_C_Copyright(t):
    r'</copyright>'
    return t

def t_A_Para(t):
    r'<para>'
    return t

def t_C_Para(t):
    r'</para>'
    return t

def t_A_Important(t):
    r'<important>'
    return t

def t_C_Important(t):
    r'</important>'
    return t

def t_A_MediaObject(t):
    r'<mediaobject>'
    return t

def t_C_MediaObject(t):
    r'</mediaobject>'
    return t

def t_A_VideoObject(t):
    r'<videoobject>'
    return t

def t_C_VideoObject(t):
    r'</videoobject>'
    return t

def t_A_ImageObject(t):
    r'<imageobject>'
    return t

def t_C_ImageObject(t):
    r'</imageobject>'
    return t

def t_ImageData(t): 
    r'<imagedata/>'
    return t

def t_VideoData(t): 
    r'<videodata/>'
    return t

def t_A_ItemizedList(t):
    r'<itemizedlist>'
    return t

def t_C_ItemizedList(t):
    r'</itemizedlist>'
    return t

def t_A_InformalTable(t):
    r'<informaltable>'
    return t

def t_C_InformalTable(t):
    r'</informaltable>'
    return t

def t_A_Tgroup(t):
    r'<tgroup>'
    return t

def t_C_Tgroup(t):
    r'</tgroup>'
    return t

def t_A_Thead(t): 
    r'<thead>'
    return t

def t_C_Thead(t): 
    r'</thead>'
    return t

def t_A_Tfoot(t): 
    r'<tfoot>'
    return t

def t_C_Tfoot(t):
    r'</tfoot>'
    return t

def t_A_Tbody(t): 
    r'<tbody>'
    return t

def t_C_Tbody(t): 
    r'</tbody>'
    return t

def t_A_Row(t): 
    r'<row>'
    return t

def t_C_Row(t):
    r'</row>'
    return t

def t_A_EntryTbl(t):
    r'<entrytbl>'
    return t

def t_C_EntryTbl(t):
    r'</entrytbl>'
    return t

def t_A_Entry(t): 
    r'<entry>'
    return t

def t_C_Entry(t): 
    r'</entry>'
    return t

def t_Protocolo(t):
    r'http|https|ftp|ftps'
    return t

def t_Dominio(t):
    r'[a-zA-Z]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*'
    return t

def t_Contenido(t): 
    r'[^<>]+'
    return t

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_espacios(t):
    r'\s+'
    pass

def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

documento = input("Ingrese el documento a analizar: ")

lexer.input(documento)

while True:
    token = lexer.token()
    if not token:
        break
    print(token.type, token.value)