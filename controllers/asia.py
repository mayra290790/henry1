# coding: utf8
# intente algo como
def asia(): return dict(message="")
def bieletas():

    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
               bieletas = db((db.catalogoxtipo.marca=='Asia')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)
    

def otros():
    if(request.get_vars.buscar):
        otros= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      otros

    except:
       otros = db((db.catalogoxtipo.marca=='Asia')&(db.catalogoxtipo.tipo==' Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(otros=otros)
    
def catalogoasia():
    mcatalogo = db((db.catalogoxtipo.marca=='Asia')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)
