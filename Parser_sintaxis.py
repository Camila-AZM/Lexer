import ply.lex as lex
import ply.yacc as yacc
import os
import time

sec = False
encabezado = 0
head = False

tokens=(
    'TipoDocumento',
    'A_Article',
    'C_Article',
    'A_Section',
    'C_Section',
    'A_Title',
    'C_Title',
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
    'A_Simpara',
    'C_Simpara',
    'A_Emphasis',
    'C_Emphasis',
    'A_Comment',
    'C_Comment',
    'A_Link',
    'C_Link',
    'XLink',
    'A_Important',
    'C_Important',
    'A_FirstName',
    'C_FirstName',
    'A_SurName',
    'C_SurName',
    'A_Street',
    'C_Street',
    'A_City',
    'C_City',
    'A_State',
    'C_State',
    'A_Phone',
    'C_Phone',
    'A_Email',
    'C_Email',
    'A_Date',
    'C_Date',
    'A_Year',
    'C_Year',
    'A_Holder',
    'C_Holder',
    'A_MediaObject',
    'C_MediaObject',
    'A_VideoObject',
    'C_VideoObject',
    'A_ImageObject',
    'C_ImageObject',
    'ImageData',
    'VideoData',
    'Fileref',
    'A_ItemizedList',
    'C_ItemizedList',
    'A_ListItem',
    'C_ListItem',
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
    'URL',
    'nuevalinea',
    'espacios',
    'tabulacion',
    'GT',
    'SLASH_GT',
    'Contenido',
)


archivo = open("EJEMPLO1.html", "w")

def t_TipoDocumento(t):
    r'<!DOCTYPE\sarticle\s*>'
    archivo.write("<!DOCTYPE html>")
    return t

def t_A_Article(t):    
    r'<article>'
    archivo.write("<html lang='es'> <head> </head> <body>")
    return t

def t_C_Article(t): 
    r'</article>'
    return t

def t_A_Section(t): 
    r'<section>'
    global sec
    sec = True
    return t

def t_C_Section(t): 
    r'</section>'
    global sec
    sec = False
    return t

def t_A_Title(t):
    r'<title>'
    global sec
    if sec:
        archivo.write("<H2>")
    else:
        archivo.write("<H1>")
    return t

def t_C_Title(t):
    r'</title>'
    global sec
    if sec:
        archivo.write("</H2>")
    else:
        archivo.write("</H1>")
    return t

def t_A_SimpleSection(t): 
    r'<simplesect>'
    global sec
    sec = True
    return t

def t_C_SimpleSection(t):
    r'</simplesect>'
    global sec
    sec = False
    return t

def t_A_Info(t):
    r'<info>'
    archivo.write('<div style="background-color: green; color: white; font-size: 8pt;">')
    return t

def t_C_Info(t):
    r'</info>'
    archivo.write('</div>')
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
    archivo.write("<p>")
    return t

def t_C_Para(t):
    r'</para>'
    archivo.write("</p>")
    return t

def t_A_SimPara(t):
    r'<simpara>'
    archivo.write("<p>")
    return t

def t_C_SimPara(t):
    r'</simpara>'
    archivo.write("</p>")
    return t

def t_A_Emphasis(t):
    r'<emphasis>'
    return t

def t_C_Emphasis(t):
    r'</emphasis>'
    return t

def t_A_Comment(t):
    r'<comment>'
    return t

def t_C_Comment(t):
    r'</comment>'
    return t

def t_A_Important(t):
    r'<important>'
    archivo.write('<div style="background-color: red; color: white;">')
    return t

def t_C_Important(t):
    r'</important>'
    archivo.write('</div>')
    return t

def t_A_FirstName(t):
    r'<firstname>'
    return t

def t_C_FirstName(t):
    r'</firstname>'
    return t

def t_A_SurName(t):
    r'<surname>'
    return t

def t_C_SurName(t):
    r'</surname>'
    return t

def t_A_Street(t):
    r'<street>'
    return t

def t_C_Street(t):
    r'</street>'
    return t

def t_A_City(t):
    r'<city>'
    return t

def t_C_City(t):
    r'</city>'
    return t

def t_A_State(t):
    r'<state>'
    return t

def t_C_State(t):
    r'</state>'
    return t

def t_A_Phone(t):
    r'<phone>'
    return t

def t_C_Phone(t):
    r'</phone>'
    return t

def t_A_Email(t):
    r'<email>'
    return t

def t_C_Email(t):
    r'</email>'
    return t

def t_A_Date(t):
    r'<date>'
    return t

def t_C_Date(t):
    r'</date>'
    return t

def t_A_Year(t):
    r'<year>'
    return t

def t_C_Year(t):
    r'</year>'
    return t

def t_A_Holder(t):
    r'<holder>'
    return t

def t_C_Holder(t):
    r'</holder>'
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

def t_A_ItemizedList(t):
    r'<itemizedlist>'
    archivo.write("<ul>")
    return t

def t_C_ItemizedList(t):
    r'</itemizedlist>'
    archivo.write("</ul>")
    return t

def t_A_ListItem(t):
    r'<listitem>'
    archivo.write("<li>")
    return t

def t_C_ListItem(t):
    r'</listitem>'
    archivo.write("</li>")
    return t

def t_A_InformalTable(t):
    r'<informaltable>'
    archivo.write("<table>")
    return t

def t_C_InformalTable(t):
    r'</informaltable>'
    archivo.write("</table>")
    return t

def t_A_Tgroup(t):
    r'<tgroup>'
    return t

def t_C_Tgroup(t):
    r'</tgroup>'
    return t

def t_A_Thead(t): 
    r'<thead>'
    global head
    head = True
    archivo.write("<thead>")
    return t

def t_C_Thead(t): 
    r'</thead>'
    global head
    head = False
    archivo.write("</thead>")
    return t

def t_A_Tfoot(t): 
    r'<tfoot>'
    archivo.write("<tfoot>")
    return t

def t_C_Tfoot(t):
    r'</tfoot>'
    archivo.write("</tfoot>")
    return t

def t_A_Tbody(t): 
    r'<tbody>'
    archivo.write("<tbody>")
    return t

def t_C_Tbody(t): 
    r'</tbody>'
    archivo.write("</tbody>")
    return t

def t_A_Row(t): 
    r'<row>'
    archivo.write("<tr>")
    return t

def t_C_Row(t):
    r'</row>'
    archivo.write("</tr>")
    return t

def t_A_EntryTbl(t):
    r'<entrytbl>'
    archivo.write("<table>")
    return t

def t_C_EntryTbl(t):
    r'</entrytbl>'
    archivo.write("</table>")
    return t

def t_A_Entry(t): 
    r'<entry>'
    global head
    if head:
        archivo.write("<th>")
    else:
        archivo.write("<td>")
    return t

def t_C_Entry(t): 
    r'</entry>'
    global head
    if head:
        archivo.write("</th>")
    else:
        archivo.write("</td>")
    return t

def t_A_Link(t):
    r'<link '
    global link
    link = False
    archivo.write("<a ")
    return t

def t_XLink(t):
    r'xlink:href\s*=\s*'
    archivo.write("href =")
    return t

def t_C_Link(t):
    r'</link>'
    global link
    link = False
    archivo.write("</a>")
    return t

def t_ImageData(t): 
    r'<imagedata\s+'
    global link
    link = True
    archivo.write("a ")
    return t

def t_VideoData(t): 
    r'<videodata\s+'
    global link
    link = True
    archivo.write("<a ")
    return t

def t_Fileref(t):
    r'fileref\s*=\s*'
    archivo.write("fileref =")
    return t

def t_URL(t):
    r'(http|https|ftp|ftps)://[a-zA-Z][\w.-]+(:\d*)?(/[a-zA-Z0-9-.-]+)*(\#\w+)?'
    if link:
        archivo.write(t.value + "></a>")
    else:
        archivo.write(t.value + ">")
    return t

# Token para el cierre de etiqueta '>'
def t_GT(t):
    r'>'
    return t

# Token para el cierre automático '/>'
def t_SLASH_GT(t):
    r'/>'
    return t

def t_nuevalinea(t):
    '\\n'
    t.lexer.lineno += len(t.value)
    archivo.write("\n")
    pass

def t_espacios(t):
    '\s+'
    pass

def t_tabulacion(t):
    r'\\t'
    archivo.write("\t\t")
    pass

def t_Contenido(t): 
    r'[^<>\n]+'
    archivo.write(t.value)
    return t

def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.type = 'ERROR_LEXICO'
    t.value = t.value
    t.lineno = t.lineno
    return t

lexer = lex.lex()

lexer.lineno = 1

def p_docbook(p):
    '''docbook : TipoDocumento article'''

def p_article(p):
    '''article : A_Article A_Info info C_Info A_Title title C_Title items sections C_Article
              | A_Article A_Title title C_Title items sections C_Article
              | A_Article A_Info info C_Info items sections C_Article  
              | A_Article items sections C_Article
              | A_Article tabulacion items C_Article'''

def p_metadata(p):
    '''metadata : A_Info info C_Info A_Title title C_Title
        | A_Title title C_Title
        | A_Info info C_Info'''

def p_items(p):
    '''items : A_ItemizedList items C_ItemizedList
        | A_ItemizedList items C_ItemizedList items 
        | A_Important important C_Important
        | A_Important important C_Important items
        | paragraph
        | paragraph items
        | A_Address address C_Address
        | A_Address address C_Address items
        | A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject items
        | A_InformalTable table C_InformalTable
        | A_InformalTable table C_InformalTable items
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment items
        | A_Abstract title paragraph C_Abstract
        | A_Abstract title paragraph C_Abstract items
        | A_Abstract paragraph C_Abstract
        | A_Abstract paragraph C_Abstract items'''



def p_sections(p):
    '''sections : A_Section contenidosection C_Section
        | A_Section contenidosection C_Section sections
        | A_SimpleSection contenidosimpsection C_SimpleSection
        | A_SimpleSection contenidosimpsection C_SimpleSection sections'''
    

def p_contenidosection(p):
    '''contenidosection : metadata items sections
        | metadata items
        | metadata sections
        | metadata'''
    
def p_contenidosimpsection(p):
    '''contenidosimpsection : metadata items
        | metadata'''

def p_info(p):
    '''info : A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject info
        | A_Abstract abstract C_Abstract
        | A_Abstract abstract C_Abstract info
        | A_Address address C_Address
        | A_Address address C_Address info
        | A_Author author C_Author
        | A_Author author C_Author info
        | A_Date personalinfo C_Date
        | A_Date personalinfo C_Date info
        | A_Copyright copyright C_Copyright
        | A_Copyright copyright C_Copyright info 
        | A_Title title C_Title
        | A_Title title C_Title info'''
    
def p_title(p):
    '''title : Contenido
        | Contenido title
        | A_Emphasis inlinetags C_Emphasis
        | A_Emphasis inlinetags C_Emphasis title
        | A_Link XLink URL GT inlinetags C_Link
        | A_Link XLink URL GT inlinetags C_Link title
        | A_Email personalinfo C_Email
        | A_Email personalinfo C_Email title'''

def p_important(p):
    '''important : A_Title title C_Title items
        | items'''

def p_paragraph(p):
    '''paragraph : A_Para para C_Para
        | A_Simpara inlinetags C_Simpara
        | A_Para para C_Para paragraph
        | A_Simpara inlinetags C_Simpara paragraph'''
    
def p_mediaobject(p):
    '''mediaobject : info multimedia
        | multimedia'''

def p_para(p):
    '''para : Contenido 
        | Contenido para
        | A_Emphasis inlinetags C_Emphasis
        | A_Emphasis inlinetags C_Emphasis para
        | A_Link XLink URL GT inlinetags C_Link
        | A_Link XLink URL GT inlinetags C_Link para
        | A_Author author C_Author
        | A_Author author C_Author para
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment para
        | A_ItemizedList items C_ItemizedList
        | A_ItemizedList items C_ItemizedList para
        | A_Important  items C_Important
        | A_Important items C_Important para
        | A_Address address C_Address
        | A_Address address C_Address para
        | A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject para
        | A_InformalTable table C_InformalTable
        | A_InformalTable table C_InformalTable para'''

def p_inlinetags(p):
    '''inlinetags : Contenido
        | Contenido inlinetags
        | A_Emphasis inlinetags C_Emphasis
        | A_Emphasis inlinetags C_Emphasis inlinetags
        | A_Link XLink URL GT inlinetags C_Link
        | A_Link XLink URL GT inlinetags C_Link inlinetags
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment inlinetags
        | A_Email personalinfo C_Email
        | A_Email personalinfo C_Email inlinetags
        | A_Author author C_Author
        | A_Author author C_Author inlinetags'''

def p_abstract(p):
    '''abstract : A_Title title C_Title paragraph
        | paragraph'''
    
def p_address(p):
    '''address : Contenido 
        | Contenido address 
        | A_Street personalinfo C_Street 
        | A_Street personalinfo C_Street address
        | A_City personalinfo C_City
        | A_City personalinfo C_City address
        | A_State personalinfo C_State
        | A_State personalinfo C_State address
        | A_Phone personalinfo C_Phone 
        | A_Phone personalinfo C_Phone address 
        | A_Email personalinfo C_Email
        | A_Email personalinfo C_Email address'''

def p_author(p):
    '''author : A_FirstName personalinfo C_FirstName
        | A_FirstName personalinfo C_FirstName author
        | A_SurName personalinfo C_SurName
        | A_SurName personalinfo C_SurName author'''

def p_copyright(p):
    '''copyright : A_Year personalinfo C_Year
        | A_Year personalinfo C_Year A_Holder personalinfo C_Holder
        | A_Year personalinfo C_Year copyright
        | A_Year personalinfo C_Year copyright A_Holder personalinfo C_Holder'''
    
def p_personalinfo(p):
    '''personalinfo : Contenido
        | Contenido personalinfo
        | A_Link XLink URL GT inlinetags C_Link
        | A_Link XLink URL GT inlinetags C_Link personalinfo
        | A_Emphasis inlinetags C_Emphasis
        | A_Emphasis inlinetags C_Emphasis personalinfo
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment personalinfo'''

def p_multimedia(p):
    '''multimedia : A_ImageObject imageobject C_ImageObject
        | A_ImageObject imageobject C_ImageObject multimedia
        | A_VideoObject videoobject C_VideoObject
        | A_VideoObject videoobject C_VideoObject multimedia'''

def p_videoobject(p):
    '''videoobject : VideoData Fileref SLASH_GT
        | info VideoData Fileref SLASH_GT'''

def p_imageobject(p):
    '''imageobject : ImageData Fileref SLASH_GT
        | info ImageData Fileref SLASH_GT'''

def p_itemizedlist(p):
    '''itemizedlist : A_ListItem listitem C_ListItem'''

def p_listitem(p):
    '''listitem : items'''

def p_table(p):
    '''table : A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject table
        | A_Tgroup tgroup C_Tgroup
        | A_Tgroup tgroup C_Tgroup table'''

def p_tgroup(p):
    '''tgroup : A_Thead row C_Thead A_Tbody row C_Tbody A_Tfoot row C_Tfoot
        | A_Thead row C_Thead A_Tbody row C_Tbody
        | A_Tbody row C_Tbody A_Tfoot row C_Tfoot
        | A_Tbody row C_Tbody'''

def p_row(p):
    '''row : A_Row entries C_Row
    | A_Row entries C_Row row'''

def p_entries(p):
    '''entries : A_Entry entry C_Entry
        | A_Entry entry C_Entry entries
        | A_EntryTbl entrytbl C_EntryTbl
        | A_EntryTbl entrytbl C_EntryTbl entries'''

def p_entry(p):
    '''entry : Contenido
        | Contenido entry
        | A_ItemizedList itemizedlist C_ItemizedList
        | A_ItemizedList itemizedlist C_ItemizedList entry 
        | A_Important important C_Important
        | A_Important important C_Important entry
        | paragraph
        | paragraph entry
        | A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject entry
        | A_InformalTable table C_InformalTable
        | A_InformalTable table C_InformalTable entry
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment entry
        | A_Abstract title paragraph C_Abstract
        | A_Abstract title paragraph C_Abstract entry
        | A_Abstract paragraph C_Abstract
        | A_Abstract paragraph C_Abstract entry'''

def p_entrytbl(p):
    '''entrytbl : A_Thead row C_Thead A_Tbody row C_Tbody
        | A_Tbody row C_Tbody'''
    
def p_error(p):
    global error_flag
    error_flag = True
    print("Error en la linea", p.lineno, "\nValor: "+str(p.value)+"\n")

# Una ventana de presentacion jeje
pantalla = [
    "=================================================================================================",
    "",
    "                                  Trabajo Practico Integrador",
    "                           Diseño e Implementacion de Lexer y Parser",
    "",
    "=================================================================================================",
    "",
    "                                           GRUPO 18",
    "                                         Integrantes:",
    "                                 - Rodriguez Scornik, Matias",
    "                                 - Zeniquel Martinelli, Camila Aylen",
    "",
    "=================================================================================================",
    "",
    "                               Sintaxis y Semantica de los Lenguajes",
    "                                         Comision ISI A",
    "                                            Año 2023"
]

for linea in pantalla:
        print(linea)

time.sleep(2)

os.system('cls')

def menu():
    cosas_de_menu = [
        "=================================================================================================",
        "",
        "                        ANALIZADOR LEXICO/SINTACTICO DE DOCBOOK",
        "Seleccione una de las opciones:",
        "1_ Utilizar el Ejemplo 1",
        "2_ Utilizar el Ejemplo 2",
        "3_ Utilizar el Ejemplo 3",
        "4_ Utilizar un archivo propio",
        "5_ Escribir el documento por pantalla",
        "6_ Salir",
        ""
    ]
    for linea in cosas_de_menu:
        print(linea)

menu()
opcion = int(input("Opcion: "))

if opcion == 1:
    # Lee el contenido del archivo XML
    with open("EJEMPLO1.xml", "r") as arch_xml:
        documento = arch_xml.read()

    error_flag = False

    # Crea el parser y llama a la función parse con el contenido XML
    parser = yacc.yacc()
    parser.parse(documento)


if error_flag:
    print("Hubieron errores sintacticos")
else:
    print("El analisis sintactico se realizo correctamente")
    archivo.write("</body>")

    