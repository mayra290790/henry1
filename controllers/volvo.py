# coding: utf8
# intente algo como
def volvo(): return dict(message="")


def bieletas():

    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
       bieletas = db((db.catalogoxtipo.marca=='Volvo')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)

def catalogovolvo():
    mcatalogo = db((db.catalogoxtipo.marca=='Volvo')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)

def otros():

    if(request.get_vars.buscar):
        otros= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       otros

    except:
               otros = db((db.catalogoxtipo.marca=='Volvo')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(otros=otros)
