# coding: utf8
# intente algo como
def ford(): return dict(message="")

def montantes():

    if(request.get_vars.buscar):
        montantes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      montantes

    except:
        montantes = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Montantes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(montantes=montantes)
def bridas():

    if(request.get_vars.buscar):
        bridas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      bridas

    except:
     bridas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Bridas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bridas=bridas)

def abrazaderas():

    if(request.get_vars.buscar):
        mabrazaderas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       mabrazaderas

    except:
       mabrazaderas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Abrazaderas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(mabrazaderas=mabrazaderas)


def arandelas():

    if(request.get_vars.buscar):
        arandelas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       arandelas

    except:
       arandelas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Arandelas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(arandelas=arandelas)

def bieletas():

    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
       bieletas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)

def soportes():
    if(request.get_vars.buscar):
        soportes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       soportes

    except:
       soportes = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Soportes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(soportes=soportes)
def cazoletas():
    if(request.get_vars.buscar):
        cazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cazoletas

    except:
       cazoletas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cazoletas=cazoletas)
    
    
def cubrecazoletas():
    if(request.get_vars.buscar):
        cubrecazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cubrecazoletas

    except:
       cubrecazoletas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Cubrecazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cubrecazoletas=cubrecazoletas)


def bujes():
    if(request.get_vars.buscar):
        bujes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      bujes

    except:
       bujes = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Bujes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bujes=bujes)

def mazas():
     if(request.get_vars.buscar):
        mazas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        mazas
     except:
          mazas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Mazas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(mazas=mazas)

def almohadillas():
     if(request.get_vars.buscar):
        almohadillas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        almohadillas
     except:
          almohadillas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Almohadillas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(almohadillas=almohadillas)

def acoples():
     if(request.get_vars.buscar):
        acoples= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        acoples
     except:
       acoples= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Acoples')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(acoples=acoples)

def crapodinas():
     if(request.get_vars.buscar):
        crapodinas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
      crapodinas
     except:
       crapodinas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Crapodinas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(crapodinas=crapodinas)

def fuelles ():
        if(request.get_vars.buscar):
         fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
        try:
            fuelles
        except:
            fuelles = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

        return dict(fuelles=fuelles)



def portas():
     if(request.get_vars.buscar):
        portas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        portas
     except:
       portas = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Porta Maza')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(portas=portas)

def platos():
     if(request.get_vars.buscar):
        platos = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
         platos
     except:
       platos = db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Platos de Apoyo')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(platos=platos)

def manchons():
     if(request.get_vars.buscar):
        manchons = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        manchons

     except:
         manchons= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Manchon´s')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(manchons=manchons)

def tricetas():
     if(request.get_vars.buscar):
        tricetas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        tricetas

     except:
       tricetas= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Tricetas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(tricetas=tricetas)
def correctordecomba():

    if(request.get_vars.buscar):
        corrector= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       corrector

    except:
       corrector= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Corrector de Comba')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(corrector=corrector)

def torretas():
     if(request.get_vars.buscar):
        torretas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        torretas
     except:
       torretas= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Torretas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(torretas=torretas)

def topes():
     if(request.get_vars.buscar):
        topes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        topes

     except:
          topes= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Topes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(topes=topes)

def catalogoford():
    mcatalogo = db((db.catalogoxtipo.marca=='Ford')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)
def fuelles():
     if(request.get_vars.buscar):
        fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        fuelles

     except:
          fuelles= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(fuelles=fuelles)
 
def ejes():
      if(request.get_vars.buscar):
        ejes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
      try:
        ejes

      except:
          ejes= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
      return dict(ejes=ejes)                            
def otros():
     if(request.get_vars.buscar):
        otros = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        otros

     except:
          otros= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(otros=otros)     
def puntadeeje():
     if(request.get_vars.buscar):
        puntadeeje = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        puntadeeje

     except:
          puntadeeje= db((db.catalogoxtipo.marca=='Ford')&(db.catalogoxtipo.tipo=='Punta de ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(puntadeeje=puntadeeje)
