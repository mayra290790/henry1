# coding: utf8
# intente algo como
def chevrolet(): return dict(message="")
def correctordecomba():

    if(request.get_vars.buscar):
       correctordecomba= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      correctordecomba

    except:
      correctordecomba = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Corrector de Comba')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(correctordecomba=correctordecomba)
    
def plaquetasdesoportes():

    if(request.get_vars.buscar):
       plaquetas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      plaquetas

    except:
     plaquetas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Plaqueta de Soportes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(plaquetas=plaquetas)
    
def torretas():

    if(request.get_vars.buscar):
       torretas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      torretas

    except:
      torretas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Torretas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(torretas=torretas)
        
def gemelodeelastico():

    if(request.get_vars.buscar):
       gemelodeelastico= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      gemelodeelastico

    except:
      gemelodeelastico = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo== 'Gemelos de Elastico')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict( gemelodeelastico= gemelodeelastico)
    
def abrazaderas():

    if(request.get_vars.buscar):
        mabrazaderas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       mabrazaderas

    except:
       mabrazaderas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Abrazaderas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(mabrazaderas=mabrazaderas)
    
def barras():

    if(request.get_vars.buscar):
        barras= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       barras

    except:
      barras = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Barras')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(barras=barras)
        
def montantes():

    if(request.get_vars.buscar):
        montantes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       montantes

    except:
      montantes = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Montantes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(montantes=montantes)   
    
def almohadillas():
     if(request.get_vars.buscar):
        almohadillas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        almohadillas
     except:
          almohadillas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Almohadillas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
          
     return dict(almohadillas=almohadillas)
     
     
def brazos():
     if(request.get_vars.buscar):
        brazos= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        brazos
     except:
       brazos= db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Brazos')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(brazos=brazos)




def bieletas():

    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
               bieletas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)
    
    
    
def soportes():
    if(request.get_vars.buscar):
        soportes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       soportes

    except:
       soportes = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Soportes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(soportes=soportes)
    
    
def cazoletas():
    if(request.get_vars.buscar):
        cazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cazoletas

    except:
       cazoletas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cazoletas=cazoletas)
    
    
    
def bujes():
    if(request.get_vars.buscar):
        bujes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      bujes

    except:
       bujes = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Bujes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bujes=bujes)
    
      
def mazas():
     if(request.get_vars.buscar):
        mazas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        mazas
     except:
          mazas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Mazas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(mazas=mazas)





def crapodinas():
     if(request.get_vars.buscar):
        crapodinas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
      crapodinas
     except:
       crapodinas = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Crapodinas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(crapodinas=crapodinas)
     
     
     
def fuelles():
        if(request.get_vars.buscar):
         fuelles = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
        try:
            fuelles
        except:
            fuelles = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Fuelles')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

        return dict(fuelles=fuelles)


def tapondeejes():
     if(request.get_vars.buscar):
        tapondeejes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        tapondeejes

     except:
      tapondeejes = db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Tapon de ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(tapondeejes=tapondeejes)
     
     

def manchons():
     if(request.get_vars.buscar):
        manchons = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        manchons

     except:
         manchons= db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Seguro Manchon´s')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(manchons=manchons)
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
       
def puntadeeje():
     if(request.get_vars.buscar):
        puntadeeje = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        puntadeeje

     except:
              puntadeeje= db((db.catalogoxtipo.marca=='Chevrolet')&(db.catalogoxtipo.tipo=='Punta de ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(puntadeeje=puntadeeje)
     
def catalogochevrolet():
    ccatalogo = db((db.catalogoxtipo.marca=='Chevrolet')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(ccatalogo=ccatalogo)
