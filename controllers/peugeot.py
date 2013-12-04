# coding: utf8
# intente algo como
def peugeot(): return dict(message="")
def ojal():

    if(request.get_vars.buscar):
        ojal= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       ojal

    except:
      ojal = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Ojal')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(ojal=ojal)
def abrazaderas():

    if(request.get_vars.buscar):
        abrazaderas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       abrazaderas

    except:
       abrazaderas = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Abrazaderas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(abrazaderas=abrazaderas)

def brazoderotula():

    if(request.get_vars.buscar):
        rotula= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      rotula

    except:
       rotula = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Brazo de Rotula')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(rotula=rotula)
def bieletas():

    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
       bieletas = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)

def soportes():
    if(request.get_vars.buscar):
        soportes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       soportes

    except:
       soportes = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Soportes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(soportes=soportes)
def cazoletas():
    if(request.get_vars.buscar):
        cazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cazoletas

    except:
       cazoletas = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cazoletas=cazoletas)

def bujes():
    if(request.get_vars.buscar):
        bujes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      bujes

    except:
       bujes = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Bujes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bujes=bujes)

def mazas():
     if(request.get_vars.buscar):
        mazas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        mazas
     except:
          mazas = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Mazas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(mazas=mazas)

def almohadillas():
     if(request.get_vars.buscar):
        almohadillas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        almohadillas
     except:
          almohadillas = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Almohadillas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(almohadillas=almohadillas)

def cubrecazoletas():
     if(request.get_vars.buscar):
        cubre= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        cubre
     except:
           cubre= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Cubre Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(cubre=cubre)

def crapodinas():
     if(request.get_vars.buscar):
        crapodinas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
      crapodinas
     except:
       crapodinas = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Crapodinas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(crapodinas=crapodinas)

def fuelles ():
        if(request.get_vars.buscar):
         fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
        try:
            fuelles
        except:
            fuelles = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

        return dict(fuelles=fuelles)



def topes():
     if(request.get_vars.buscar):
        topes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        topes

     except:
          topes= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Topes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(topes=topes)


def seguros():
    if(request.get_vars.buscar):
        seguros = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      seguros

    except:
       seguros = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Seguro Manchon´s')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(seguros=seguros)

def catalogopeugeot():
        mcatalogo = db((db.catalogoxtipo.marca=='Peugeot')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
        return dict(mcatalogo=mcatalogo)
def fuelles():
     if(request.get_vars.buscar):
        fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        fuelles

     except:
          fuelles= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(fuelles=fuelles)
 

             
def otros():
     if(request.get_vars.buscar):
        otros = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        otros

     except:
          otros= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(otros=otros)
     
def puntadeeje():
     if(request.get_vars.buscar):
        puntadeeje = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        puntadeeje

     except:
          puntadeeje= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Punta de ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(puntadeeje=puntadeeje)
     
     
def tuercas():

    if(request.get_vars.buscar):
        tuercas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       tuercas

    except:
       tuercas = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Tuercas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(tuercas=tuercas)
    
    
def estrellascazoletas():

    if(request.get_vars.buscar):
       estrellascazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       estrellascazoletas

    except:
      estrellascazoletas= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Estrellas cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(estrellascazoletas=estrellascazoletas)
    

def kitderodillos():

    if(request.get_vars.buscar):
        kitderodillos= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       kitderodillos

    except:
       kitderodillos= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Kit de Rodillos')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(kitderodillos=kitderodillos)
    
def tricetas():

    if(request.get_vars.buscar):
        tricetas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       tricetas

    except:
       tricetas= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Tricetas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(tricetas=tricetas)
    
    
def palancadeembrague():

    if(request.get_vars.buscar):
        palancadeembrague= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       palancadeembrague

    except:
       palancadeembrague= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Palanca de Embrague')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(palancadeembragues= palancadeembrague)
    
    
    
def tuercas():

    if(request.get_vars.buscar):
        tuercas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       tuercas

    except:
       tuercas= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Tuercas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(tuercas=tuercas)
    
    
def capuchondeprecap():
        if(request.get_vars.buscar):
         precap = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
        try:
            precap
        except:
            precap = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Capuchon de Precap')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

        return dict(precap=precap)
        
def tricetas():
     if(request.get_vars.buscar):
        tricetas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        tricetas

     except:
       tricetas= db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Tricetas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(tricetas=tricetas)
     
def palancadeembrague():
     if(request.get_vars.buscar):
        palancadeembrague = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
      palancadeembrague

     except:
       palancadeembrague = db((db.catalogoxtipo.marca=='Peugeot')&(db.catalogoxtipo.tipo=='Palanca de Embrague')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(palancadeembrague=palancadeembrague)
