# coding: utf8
# intente algo como
def renault(): return dict(message="")
def otros():

    if(request.get_vars.buscar):
        otros= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
         otros

    except:
        otros = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Otros')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(otros=otros)
def renaultseparadores():

    if(request.get_vars.buscar):
       separadores= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
        separadores

    except:
        separadores = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Separadores de Ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(separadores= separadores)
    
def horquillas():

    if(request.get_vars.buscar):
        horquillas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
        horquillas

    except:
        horquillas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Horquillas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(horquillas=horquillas)
def mazas():

    if(request.get_vars.buscar):
        mazas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
        mazas

    except:
        mazas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Mazas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(mazas=mazas)
    
def sacasdeespigas():

    if(request.get_vars.buscar):
        sacasdeespigas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
     sacasdeespigas

    except:
      sacasdeespigas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Sacas de Espigas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(sacasdeespigas=sacasdeespigas)
def abrazaderas():

    if(request.get_vars.buscar):
        mabrazaderas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       mabrazaderas

    except:
       mabrazaderas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Abrazaderas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(mabrazaderas=mabrazaderas)
    
def bieletas():
    if(request.get_vars.buscar):
        bieletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       bieletas

    except:
      bieletas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Bieletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bieletas=bieletas)
def cazoletas():
    if(request.get_vars.buscar):
        cazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cazoletas

    except:
       cazoletas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cazoletas=cazoletas)

def bujes():
    if(request.get_vars.buscar):
        bujes = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
      bujes

    except:
       bujes = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Bujes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(bujes=bujes)

def barras():
     if(request.get_vars.buscar):
        barras= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        barras
     except:
       barras= db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Barras')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(barras=barras)
     
def catalogorenault():
    mcatalogo = db((db.catalogoxtipo.marca=='Renault')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)
    
def puntadeeje():
     if(request.get_vars.buscar):
        puntadeeje = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        puntadeeje

     except:
          puntadeeje= db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Punta de ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")
     return dict(puntadeeje=puntadeeje)
     
def almohadillas():
     if(request.get_vars.buscar):
        almohadillas = db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()
     try:
        almohadillas
     except:
          almohadillas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Almohadillas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(almohadillas=almohadillas)
     
     
def acoples():

    if(request.get_vars.buscar):
        acoples= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       acoples

    except:
       acoples = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Acoples')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(acoples=acoples)
    
def cubrecazoletas():

    if(request.get_vars.buscar):
        cubrecazoletas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       cubrecazoletas

    except:
       cubrecazoletas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Cubre Cazoletas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(cubrecazoletas=cubrecazoletas)
    
def distancialdemazas():

    if(request.get_vars.buscar):
        distancialdemazas= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       distancialdemazas

    except:
       distancialdemazas = db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo=='Distancial de Mazas')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(distancialdemazas=distancialdemazas)
    
def ejes():

    if(request.get_vars.buscar):
        ejes= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select()

    try:
       ejes

    except:
        ejes= db((db.catalogoxtipo.marca=='Renault')&(db.catalogoxtipo.tipo==' Ejes')).select(db.catalogoxtipo.cod_articulo, db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC")

    return dict(ejes=ejes)
    

def catalogorenault():
    mcatalogo = db((db.catalogoxtipo.marca=='Renault')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
    return dict(mcatalogo=mcatalogo)
