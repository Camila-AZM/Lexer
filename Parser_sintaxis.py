import ply.yacc as yacc
from Lexer_sintaxis import tokens

def p_docbook(p):
    '''docbook: TipoDocumento article''' 

def p_article(p):
    '''article: A_Article metadata items sections C_Article
            | A_Article items sections C_Article
            | A_Article items C_Article'''

def p_metadata(p):
    '''metadata: A_Info info C_Info A_Title title C_Title
            | A_Title title C_Title
            | A_Info info C_Info'''

def p_items(p):
    '''items: A_ItemizedList items C_ItemizedList
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

#corregi porque decia 'section', mientras que arriba en article decia sections

def p_sections(p):
    '''section: A_Section contenidosection C_Section
            | A_Section contenidosection C_Section section
            | A_SimpleSection contenidosimpsection C_SimpleSection
            | A_SimpleSection contenidosimpsection C_SimpleSection section'''

def p_contenidosection(p):
    '''contenidosection: metadata items section
                        | metadata items'''

#Agregue esta porque tienen distintos contenidos, simplesect no puede incluir una section dentro

def p_contenidosimpsection(p):
    '''contenidosimpsection: metadata items'''

def p_info(p):
    '''info: A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject info
        | A_Abstract abstract C_Abstract
        | A_Abstract abstract C_Abstract info
        | A_Address address C_Address
        | A_Address address C_Address info
        | A_Author name C_Author
        | A_Author name C_Author info
        | A_Date personalinfo C_Date
        | A_Date personalinfo C_Date info
        | A_Copyright copyright C_Copyright
        | A_Copyright copyright C_Copyright info 
        | A_Title title C_Title
        | A_Title title C_Title info'''
    
def p_title(p):
    '''title: Contenido
        | Contenido title
        | A_Emphasis emphasis C_Emphasis
        | A_Emphasis emphasis C_Emphasis title
        | A_Link link C_Link
        | A_Link link C_Link title
        | A_Email personalinfo C_Email
        | A_Email personalinfo C_Email title'''

def p_important(p):
    '''important: A_Title title C_Title items
        | items'''

def p_paragraph(p):
    '''paragraph: A_Para para C_Para
        | A_Simpara inlinetags C_Simpara
        | A_Para para C_Para paragraph
        | A_Simpara inlinetags C_Simpara paragraph'''

def p_address(p):
    '''address: Contenido 
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
    
def p_mediaobject(p):
    '''mediaobject: info multimedia
                    | multimedia'''

def p_name(p):
    '''name: A_FirstName personalinfo C_FirstName
            | A_FirstName personalinfo C_FirstName name
            | A_SurName personalinfo C_SurName
            | A_SurName personalinfo C_SurName name'''

def p_personalinfo(p):
    '''personalinfo: Contenido 
                    | Contenido personalinfo
                    | A_Link link C_Link
                    | A_Link link C_Link personalinfo
                    | A_Emphasis emphasis C_Emphasis
                    | A_Emphasis emphasis C_Emphasis personalinfo
                    | A_Comment inlinetags C_Comment
                    | A_Comment inlinetags C_Comment personalinfo'''

def p_copyright(p):
    '''copyright: A_Year personalinfo C_Year
                | A_Year personalinfo C_Year A_Holder personalinfo C_Holder
                | A_Year personalinfo C_Year copyright
                | A_Year personalinfo C_Year copyright A_Holder personalinfo C_Holder'''

def p_para(p):
    '''para: Contenido 
            | Contenido para
            | A_Emphasis inlinetags C_Emphasis
            | A_Emphasis inlinetags C_Emphasis para
            | A_Link link C_Link
            | A_Link link C_Link para
            | A_Author name C_Author
            | A_Author name C_Author para
            | A_Comment inlinetags C_Comment
            | A_Comment inlinetags C_Comment para
            | A_ItemizedList items C_ItemizedList
            | A_ItemizedList items C_ItemizedList para
            | A_Important A_Title title C_Title  items C_Important
            | A_Important A_Title title C_Title items C_Important para
            | A_Important items C_Important
            | A_Important items C_Important para 
            | A_Address address C_Address
            | A_Address address C_Address para
            | A_MediaObject mediaobject C_MediaObject
            | A_MediaObject mediaobject C_MediaObject para
            | A_InformalTable table C_InformalTable
            | A_InformalTable table C_InformalTable para'''

def p_inlinetags(p):
    '''inlinetags: Contenido
                | Contenido inlinetags
                | A_Emphasis emphasis C_Emphasis
                | A_Emphasis emphasis C_Emphasis inlinetags
                | A_Link link C_Link
                | A_Link link C_Link inlinetags
                | A_Email personalinfo C_Email
                | A_Email personalinfo C_Email inlinetags
                | A_Author name C_Author
                | A_Author name C_Author inlinetags
                | A_Comment inlinetags C_Comment
                | A_Comment inlinetags C_Comment inlinetags'''

def p_multimedia(p):
    '''multimedia: A_ImageObject imageobj C_ImageObject
                | A_ImageObject imageobj C_ImageObject multimedia
                | A_VideoObject videoobj C_VideoObject
                | A_VideoObject videoobj C_VideoObject multimedia'''

def p_imageobj(p):
    '''imageobj: info ImageData
            | ImageData'''
    
def p_videoobj(p):
    '''videoobj: info VideoData
            | VideoData'''
    
def p_table(p):
    '''table: A_MediaObject mediaobject C_MediaObject A_Tgroup tablecontent C_Tgroup
            | A_Tgroup tablecontent C_Tgroup A_MediaObject mediaobject C_MediaObject
            | A_MediaObject mediaobject C_MediaObject table A_Tgroup tablecontent C_Tgroup
            | A_Tgroup tablecontent C_Tgroup table A_MediaObject mediaobject C_MediaObject'''

def p_tablecontent(p):
    '''tablecontent: A_Tbody conterow C_Tbody
                    | A_Thead conterow C_Thead A_Tbody conterow C_Tbody
                    | A_Tfoot conterow C_Tfoot A_Tbody conterow C_Tbody
                    | A_Thead conterow C_Thead A_Tfoot conterow C_TfootA_Tbody conterow C_Tbody'''

def p_conterow(p):
    '''conterow: A_Row entrance C_Row
                | A_Row entrance C_Row conterow'''

def p_entrance(p):
    '''entrance: A_Entry conteentry C_Entry
                | A_EntryTbl conteetbl C_EntryTbl
                | A_Entry conteentry C_Entry entrance
                | A_EntryTbl conteetbl C_EntryTbl entrance'''

def p_conteentry(p):
    '''conteentry: Contenido 
                | Contenido conteentry 
                | items
                | items conteentry'''

def p_conteetbl(p):
    '''conteetbl: A_Tbody conterow C_Tbody
                | A_Thead conterow C_Thead A_Tbody conterow C_Tbody'''
