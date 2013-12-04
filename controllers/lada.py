# coding: utf8
# intente algo como
def lada(): return dict(message="")

def abrazaderas():

    if(request.get_vars.buscar):
        abrazaderas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       abrazaderas

    except:
       abrazaderas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Abrazaderas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(abrazaderas=abrazaderas)
    
    
def otros():

    if(request.get_vars.buscar):
       otros= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       otros

    except:
        otros = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(otros=otros)
    
    
def catalogolada():
    mcatalogo = db((db.catalogoxtipo.marca=='Lada')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)
