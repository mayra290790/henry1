# coding: utf8
# intente algo como
def marcas(): return dict(message="")
def listarpeugeot():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1)
        peugeot= db((db.catalogoxtipo.marca=='Peugeot')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(peugeot=peugeot,page=page,items_per_page=items_per_page)
def listarfiat():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1)    
        fiat= db((db.catalogoxtipo.marca=='Fiat')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(fiat=fiat,page=page,items_per_page=items_per_page)
def listarford():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1)    
        ford= db((db.catalogoxtipo.marca=='Ford')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(ford=ford,page=page,items_per_page=items_per_page)
def listarchevrolet():
       if len(request.args):
            page=int(request.args[0])
       else:
           page=0
       items_per_page=15
       limitby=(page*items_per_page,(page+1)*items_per_page+1)    
       chevrolet= db((db.catalogoxtipo.marca=='Chevrolet')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
       return dict(chevrolet=chevrolet,page=page,items_per_page=items_per_page)
def listarcitroen():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1)    
        citroen= db((db.catalogoxtipo.marca=='Citroen')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(citroen=citroen,page=page,items_per_page=items_per_page)
def listarchrysler():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1)  
        chrysler= db((db.catalogoxtipo.marca=='Chrysler')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(chrysler=chrysler,page=page,items_per_page=items_per_page)
def listaralfaromeo():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1)  
        alfaromeo= db((db.catalogoxtipo.marca=='Alfa romeo')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(alfaromeo=alfaromeo,page=page,items_per_page=items_per_page)
def listarlada():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1)  
        lada= db((db.catalogoxtipo.marca=='Lada')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(lada=lada,page=page,items_per_page=items_per_page)

def listarlandrover():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1) 
        landrover= db((db.catalogoxtipo.marca=='Land-Rover')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(landrover=landrover,page=page,items_per_page=items_per_page)

def listarnissan():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1) 
        nissan= db((db.catalogoxtipo.marca=='Nissan')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(nissan=nissan,page=page,items_per_page=items_per_page)
def listarhonda():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1) 
        honda= db((db.catalogoxtipo.marca=='Honda')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(honda=honda,page=page,items_per_page=items_per_page)

def listarmitsubishi():
        if len(request.args):
            page=int(request.args[0])
        else:
           page=0
        items_per_page=15
        limitby=(page*items_per_page,(page+1)*items_per_page+1) 
        mitsubishi= db((db.catalogoxtipo.marca=='Mitsubishi')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
        return dict(mitsubishi=mitsubishi,page=page,items_per_page=items_per_page)
def listarmercedesbenz():
       if len(request.args):
            page=int(request.args[0])
       else:
           page=0
       items_per_page=15
       limitby=(page*items_per_page,(page+1)*items_per_page+1) 
       mercedesbenz= db((db.catalogoxtipo.marca=='Mercedes-Benz')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
       return dict(mercedesbenz=mercedesbenz,page=page,items_per_page=items_per_page)
def listarrenault():
       if len(request.args):
            page=int(request.args[0])
       else:
           page=0
       items_per_page=15
       limitby=(page*items_per_page,(page+1)*items_per_page+1) 
       renault= db((db.catalogoxtipo.marca=='Renault')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
       return dict(renault=renault,page=page,items_per_page=items_per_page)

def listarvolkswagen():
       if len(request.args):
           page=int(request.args[0])
       else:
           page=0
       items_per_page=15
       limitby=(page*items_per_page,(page+1)*items_per_page+1) 
       volkswagen= db((db.catalogoxtipo.marca=='Volkswagen')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
       return dict(volkswagen=volkswagen,page=page,items_per_page=items_per_page)


def listarsusuki():
       if len(request.args):
           page=int(request.args[0])
       else:
           page=0
       items_per_page=15
       limitby=(page*items_per_page,(page+1)*items_per_page+1) 
       suzuki= db((db.catalogoxtipo.marca=='Suzuki')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
       return dict(suzuki=suzuki,page=page,items_per_page=items_per_page)
def listarvolvo():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      volvo= db((db.catalogoxtipo.marca=='Volvo')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(volvo=volvo,page=page,items_per_page=items_per_page)
def listarmusso():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      musso= db((db.catalogoxtipo.marca=='Musso')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(musso=musso,page=page,items_per_page=items_per_page)

def listarhyundai():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      hyundai= db((db.catalogoxtipo.marca=='Hyundai')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(hyundai=hyundai,page=page,items_per_page=items_per_page)

def listarasia():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      asia= db((db.catalogoxtipo.marca=='Asia')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(asia=asia,page=page,items_per_page=items_per_page)

def listartoyota():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      toyota= db((db.catalogoxtipo.marca=='Toyota')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(toyota=toyota,page=page,items_per_page=items_per_page)
def listarcherokee():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      cherokee= db((db.catalogoxtipo.marca=='Cherokee')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(cherokee=cherokee,page=page,items_per_page=items_per_page)
def listarmazda():
      if len(request.args):
          page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      mazda= db((db.catalogoxtipo.marca=='Mazda')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(mazda=mazda,page=page,items_per_page=items_per_page)

def listarbmw():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=30
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      bmw= db((db.catalogoxtipo.marca=='BMW')).select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(bmw=bmw,page=page,items_per_page=items_per_page)
def completo():
      if len(request.args):
           page=int(request.args[0])
      else:
           page=0
      items_per_page=15
      limitby=(page*items_per_page,(page+1)*items_per_page+1) 
      catalogo= db().select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
      return dict(catalogo=catalogo,page=page,items_per_page=items_per_page)
