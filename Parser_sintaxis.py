import ply.yacc as yacc
from Lexer_sintaxis.py import tokens

def p_sigma(p):
    '''sigma: TipoDocumento article''' 

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
            | A_Abstract abstract C_Abstract
            | A_Abstract abstract C_Abstract items'''
