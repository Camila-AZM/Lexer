import ply.yacc as yacc
import os
import time
import xml.etree.ElementTree as ET
from Lexer_sintaxis import tokens


def p_docbook(p):
    '''docbook : TipoDocumento article'''

def p_article(p):
    '''article : A_Article  metadata items sections C_Article
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
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link title
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
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link para
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
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link inlinetags
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
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link personalinfo
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
    '''videoobject : VideoData
        | info VideoData'''

def p_imageobject(p):
    '''imageobject : ImageData
        | info ImageData'''

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
    '''tgroup : A_Thead row C_Thead A_Tfoot row C_Tfoot A_Tbody row C_Tbody
        | A_Thead row C_Thead A_Tbody row C_Tbody
        | A_Tfoot row C_Tfoot A_Tbody row C_Tbody
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
    '''entry : Contenido entry
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
    print("Error en la linea", p.lineno, "Valor:", p.value)

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

time.sleep(6)

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
    with open("EJEMPLO1.xml", "r") as archivo:
        documento = archivo.read()

    error_flag = False

    # Crea el parser y llama a la función parse con el contenido XML
    parser = yacc.yacc()
    parser.parse(documento)


if error_flag:
    print("Hubieron errores sintacticos")
else:
    print("El analisis sintactico se realizo correctamente")

    tree = ET.parse("EJEMPLO1.xml")
    root = tree.getroot()
    # Crea el tipo de documento que se va a usar
    tipodoc = ET.Element("!DOCTYPE html")
    # Crear el elemento raíz del documento HTML
    html = ET.Element("html")

    # Crear el elemento head
    head = ET.SubElement(html, "head")

    # Crear el elemento title y establecer el título del documento
    title = ET.SubElement(head, "title")
    title.text = "Título del documento"

    # Crear el elemento body
    body = ET.SubElement(html, "body")

    # Función auxiliar para generar el elemento <p> con formato específico
    def create_paragraph(text):
        paragraph = ET.Element("p")
        paragraph.set("style", "background-color: green; color: white; font-size: 8pt;")
        text = ""
        for child in element:
            text += ET.tostring(child, encoding="unicode")

        paragraph.text = text.strip()  # Eliminar espacios en blanco al inicio y final del texto

        return paragraph

    # Función auxiliar para generar el elemento <h2>
    def create_heading2(text):
        heading2 = ET.Element("h2")
        heading2.text = text
        return heading2

    # Recorrer las etiquetas y generar el contenido HTML correspondiente
    for element in root.iter():
        if element.tag == "TipoDocumento":
            # Crear el título del documento
            heading1 = ET.SubElement(body, "h1")
            heading1.text = element.text
        elif element.tag == "info":
            # Crear los párrafos con fondo verde para las etiquetas dentro de info(article, section)
            paragraph = create_paragraph(element.text)
            body.append(paragraph)
        elif element.tag == "important":
            # Crear el contenido de texto dentro de una etiqueta <important> con color de fondo rojo y texto en blanco
            paragraph = create_paragraph(element.text)
            paragraph.set("style", "background-color: red; color: white;")
            body.append(paragraph)
        elif element.tag == "para" or element.tag == "simpara":
            # Traducir las etiquetas <para> y <simpara> como párrafos <p>
            paragraph = ET.Element("p")
            paragraph.text = element.text
            body.append(paragraph)
        elif element.tag == "emphasis":
            # Traducir las etiquetas <emphasis> como texto enfatizado
            emphasis = ET.Element("em")
            emphasis.text = element.text
            body.append(emphasis)
        elif element.tag == "Link":
            # Traducir la etiqueta <Link> como un enlace <a> con el atributo xlink:href como href
            link = ET.Element("a")
            link.text = element.text
            link.set("href", element.attrib.get("xlink:href"))
            body.append(link)
        elif element.tag == "ItemizedList":
            # Traducir las etiquetas <ItemizedList> como una lista <ul>
            ul = ET.Element("ul")
            body.append(ul)
            for child in element:
                if child.tag == "listitem":
                    # Traducir las etiquetas <listitem> como elementos de lista <li>
                    li = ET.Element("li")
                    li.text = child.text
                    ul.append(li)

    # Crear el árbol del documento HTML
    html_tree = ET.ElementTree(html)

    # Guardar el documento HTML en un archivo
    html_tree.write("EJEMPLO1.html", encoding="utf-8", method="html")
input()