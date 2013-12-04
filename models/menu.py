# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################




## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('INICIO'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

if auth.has_membership(role="admin"):
    response.menu+=[
    (T('ADMINISTRACIÒN'), False, URL('default','index'),
     [


             (T('ALTAS DE MARCAS POR TIPO'), False, URL('altas','catalogoxtipo')),
             (T('LISTA DE MARCAS POR TIPO'), False, URL('listados','catalogoxtipo')),
          
        ])
]



if auth.has_membership(role="admin"):
    response.menu+=[
     (T('USUARIOS EXISTENTES'), False, URL('default','index'),
     [


             (T('ADMINISTRATIVOS'), False, URL('listados','administradores')),
             (T('USUARIOS'), False, URL('listados','usuarios')),
           
        ])
]
