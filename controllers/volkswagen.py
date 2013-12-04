# coding: utf8
# intente algo como
def volkswagen(): return dict(message="")
def otros():
     if(request.get_vars.buscar):
        otros = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        otros

     except:
          otros= db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(otros=otros) 
     
def trabaderotulas():

    if(request.get_vars.buscar):
       trabaderotulas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      trabaderotulas

    except:
       trabaderotulas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Traba de Rotulas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(trabaderotulas=trabaderotulas)    
def cubrecazoletas():

    if(request.get_vars.buscar):
        cubrecazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cubrecazoletas

    except:
       cubrecazoletas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Cubre Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cubrecazoletas=cubrecazoletas)
def platos():

    if(request.get_vars.buscar):
        platos= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
        platos

    except:
       platos = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Platos')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict( platos= platos)
def palancadeejes():

    if(request.get_vars.buscar):
        palancadeejes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      palancadeejes

    except:
       palancadeejes = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Palanca de Ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(palancadeejes=palancadeejes)

def soportes():

    if(request.get_vars.buscar):
        soportes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       soportes

    except:
        soportes = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Soportes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(soportes=soportes)
def manchons():

    if(request.get_vars.buscar):
        manchons= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
        manchons

    except:
        manchons = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Manchon´s')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(manchons=manchons)
    
    
def abrazaderas():

    if(request.get_vars.buscar):
        abrazaderas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       abrazaderas

    except:
       abrazaderas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Abrazaderas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(abrazaderas=abrazaderas)
    
def fuelles():

    if(request.get_vars.buscar):
        fuelles= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
        fuelles

    except:
        fuelles = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(fuelles=fuelles)


def bridas():

    if(request.get_vars.buscar):
        bridas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bridas

    except:
       bridas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Bridas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bridas=bridas)   
    
def bieletas():

    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
       bieletas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)
    
def cazoletas():
    if(request.get_vars.buscar):
        cazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cazoletas

    except:
       cazoletas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cazoletas=cazoletas)
    
def crapodinas():
    if(request.get_vars.buscar):
        crapodinas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       crapodinas

    except:
       crapodinas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Crapodinas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(crapodinas=crapodinas)


def bujes():
    if(request.get_vars.buscar):
        bujes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      bujes

    except:
       bujes = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Bujes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bujes=bujes)

def mazas():
     if(request.get_vars.buscar):
        mazas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        mazas
     except:
          mazas = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Mazas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(mazas=mazas)
     
def chapasdecazoletas():
     if(request.get_vars.buscar):
        chapa= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        chapa
     except:
        chapa= db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='ChapadeCazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(chapa=chapa)
     
     
def fuelles ():
        if(request.get_vars.buscar):
         fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
        try:
            fuelles
        except:
            fuelles = db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

        return dict(fuelles=fuelles)



def topes():
     if(request.get_vars.buscar):
        topes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        topes

     except:
          topes= db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Topes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(topes=topes)

def catalogovolkswagen():
        mcatalogo = db((db.catalogoxtipo.marca=='Volkswagen')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
        return dict(mcatalogo=mcatalogo)
def fuelles():
     if(request.get_vars.buscar):
        fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        fuelles

     except:
          fuelles= db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(fuelles=fuelles)
 

             
def otros():
     if(request.get_vars.buscar):
        otros = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        otros

     except:
          otros= db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(otros=otros)
     
def puntadeeje():
     if(request.get_vars.buscar):
        puntadeeje = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        puntadeeje

     except:
          puntadeeje= db((db.catalogoxtipo.marca=='Volkswagen')&(db.catalogoxtipo.tipo=='Punta de ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(puntadeeje=puntadeeje)
