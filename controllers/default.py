# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
  if len(request.args):
       page=int(request.args[0])
  else:
     page=0
  items_per_page=5
  limitby=(page*items_per_page,(page+1)*items_per_page+1)
  novedades= db((db.catalogoxtipo.ofertar==True)).select(db.catalogoxtipo.foto,db.catalogoxtipo.descripcion,orderby="catalogoxtipo.cod_articulo ASC",limitby=limitby)
  return dict(novedades=novedades,page=page,items_per_page=items_per_page)   

def user():
    auth.messages.access_denied = 'Privilegios insuficientes'
    auth.messages.logged_in = 'Sesión iniciada'
    auth.messages.email_sent = 'Correo electrónico enviado'
    auth.messages.unable_to_send_email = 'Incapaz de envíar correo electrónico'
    auth.messages.email_verified = 'Correo electrónico verificado'
    auth.messages.logged_out = 'Sesión finalizada'
    auth.messages.registration_successful = 'Registración satisfactoria'
    auth.messages.invalid_email = 'Correo electrónico inválido'
    auth.messages.invalid_login = 'Inicio de sesión inválida'
    auth.messages.invalid_user = 'Usuario inválido'
    auth.messages.mismatched_password = "Los campos de contraseña no coinciden"
    auth.messages.verify_email = 'Presione en el enlace http://...verify_email/%(key)s para verificar su correo electrónico'
    auth.messages.verify_email_subject = 'Verificar contraseña'
    auth.messages.username_sent = 'Su nombre de usuario le fue enviado por correo'
    auth.messages.new_password_sent = 'Una nueva contraseña le fue enviada por correo'
    auth.messages.password_changed = 'Contraseña cambiada'
    auth.messages.retrieve_username = 'Su nombre de usuario es: %(username)s'
    auth.messages.retrieve_username_subject = 'Recuperar nombre de usuario'
    auth.messages.retrieve_password = 'Su contraseña es: %(password)s'
    auth.messages.retrieve_password_subject = 'Recuperar contraseña'
    auth.messages.profile_updated = 'Perfil actualizado'
    auth.messages.new_password = 'Nueva contraseña'
    auth.messages.old_password = 'Vieja contraseña'
    
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
