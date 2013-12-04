# coding: utf8
# intente algo como
def mercedesbenz(): return dict(message="")

def abrazaderas():

    if(request.get_vars.buscar):
        mabrazaderas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       mabrazaderas

    except:
       mabrazaderas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Abrazaderas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(mabrazaderas=mabrazaderas)
    
    
    
    
def almohadillas():
     if(request.get_vars.buscar):
        almohadillas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        almohadillas
     except:
          almohadillas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Almohadillas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
          
     return dict(almohadillas=almohadillas)
     
     
def barras():
     if(request.get_vars.buscar):
        barras= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        barras
     except:
       barras= db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Barras')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(barras=barras)




def bieletas():

    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
               bieletas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)
    
    
    
def soportes():
    if(request.get_vars.buscar):
        soportes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       soportes

    except:
       soportes = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Soportes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(soportes=soportes)
    
    
def cazoletas():
    if(request.get_vars.buscar):
        cazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cazoletas

    except:
       cazoletas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cazoletas=cazoletas)
    
    
    
def bujes():
    if(request.get_vars.buscar):
        bujes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      bujes

    except:
       bujes = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Bujes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bujes=bujes)
    
      
def mazas():
     if(request.get_vars.buscar):
        mazas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        mazas
     except:
          mazas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Mazas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(mazas=mazas)


def catalogomercedesbenz():
    mcatalogo = db((db.catalogoxtipo.marca=='Mercedes-Benz')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)


def crapodinas():
     if(request.get_vars.buscar):
        crapodinas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
      crapodinas
     except:
       crapodinas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Crapodinas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(crapodinas=crapodinas)
     
     
     
def fuelles():
        if(request.get_vars.buscar):
         fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
        try:
            fuelles
        except:
            fuelles = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

        return dict(fuelles=fuelles)


def gomas():
     if(request.get_vars.buscar):
        gomas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        gomas

     except:
       gomas = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Gomas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(gomas=gomas)
     
     
def platillos():
     if(request.get_vars.buscar):
        platillos = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
         platillos
     except:
       platillos = db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Platillos')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(platillos=platillos)
     
     
def manchons():
     if(request.get_vars.buscar):
        manchons = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        manchons

     except:
         manchons= db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Seguro Manchon´s')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(manchons=manchons)
     
     
def tricetas():
     if(request.get_vars.buscar):
        tricetas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        tricetas

     except:
       tricetas= db((db.catalogoxtipo.marca=='Mercedes-Benz')&(db.catalogoxtipo.tipo=='Tricetas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(tricetas=tricetas)


def rulemans():
     if(request.get_vars.buscar):
        rulemans = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        rulemans

     except:
       rulemans= db((db.catalogoxtipo.marca=='Chevr')&(db.catalogoxtipo.tipo=='Ruleman Paliers')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(rulemans=rulemans)


def arandelas():

    if(request.get_vars.buscar):
        arandelas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       arandelas

    except:
       arandelas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Arandelas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(arandelas=arandelas)
    
    
    
def ejes():
      if(request.get_vars.buscar):
        ejes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
      try:
        ejes

      except:
          ejes= db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
         
      return dict(ejes=ejes)


def topes():
     if(request.get_vars.buscar):
        topes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        topes

     except:
          topes= db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Topes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(topes=topes)
     
def otros():
     if(request.get_vars.buscar):
        otros = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        otros

     except:
          otros= db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(otros=otros)
     
def seguros():
    if(request.get_vars.buscar):
        seguros = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      seguros

    except:
       seguros = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Seguro Manchon´s')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(seguros=seguros)
    
    
def puntadeeje():
     if(request.get_vars.buscar):
        puntadeeje = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        puntadeeje

     except:
              puntadeeje= db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Punta de ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(puntadeeje=puntadeeje)
     
def catalogomercedesbenz():
    mcatalogo = db((db.catalogoxtipo.marca=='Mercedesbenz')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)
