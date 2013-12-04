# coding: utf8

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    session.connect(request, response, db = db) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
else:                                         # else use a normal relational database
    db = DAL('sqlite://store.sqlite')       # if not, use SQLite or other DB
## if no need for session
# session.forget()
from gluon.tools import *
mail = Mail()                                  # mailer
auth = Auth(globals(),db)                      # authentication/authorization
crud = Crud(globals(),db)                      # for CRUD helpers using auth
service = Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()


# definimos nuestra tabla de usuarios:
db.define_table(
    auth.settings.table_user_name,
    Field ('foto', 'upload', label=T('Foto'),),
    Field('first_name',length=128,label=T('Nombres')),
    Field('last_name',length=128,label=T('Apellidos')),
    Field('dni','integer',label=T('DNI')),
    Field('email',length=128,label=T('Email')),
    Field('password','password',default='',readable=False,label=T('Contraseña')),
    Field('address1','string',length=128,label=T('Direccion Particular'),default=''),
    Field('localidad',label=T('Ciudad/Localidad'),default=''),
    Field('provincia',label=T('Provincia'),default=''),
    Field('pais',label=T('Pais'),default=''),
    Field('cp',label=T('Codigo Postal'),default=''),
    Field('telefono',label=T('Numero Telefono')),
    Field('estado','string',default='pendiente',label=T('estado'),writable=False,readable=False),
    Field('created_on','datetime',writable=False,readable=False,default=request.now),
    Field('registration_key', length=64,
          writable=False, readable=False, default='',label=T('Clave de registracion')),
    Field('reset_password_key', length=64,
          writable=False, readable=False, default='',label=T('Clave de contraseña de restablecimiento')),
    Field('registration_id', length=64,
          writable=False, readable=False, default='',label=T('ID de registracion'))
          )
          
usuario = db[auth.settings.table_user_name] # Con esto se abrevia todo en "usuario"

usuario.first_name.requires=IS_NOT_EMPTY(error_message='Falta ingresar nombre')

usuario.last_name.requires=IS_NOT_EMPTY(error_message='Falta ingresar apellido')

usuario.password.requires=IS_NOT_EMPTY(error_message='Falta ingresar contraseña')
usuario.foto.requires=IS_NOT_EMPTY(error_message='Falta ingresar imagen')
usuario.dni.lenght=8
usuario.dni.requires=IS_NOT_IN_DB(db, 'auth_user.dni')  
usuario.dni.requires=IS_INT_IN_RANGE(10000000, 100000001, error_message=('Falta ingresar el DNI o lo ingreso mal'))
usuario.registration_key.insert='pending'
#########################################################################
## Here is sample code if you need for 
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## (more options discussed in gluon/tools.py)
#########################################################################
mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'you@gmail.com'         # your email
mail.settings.login = 'username:password'      # your credentials or None

auth.settings.hmac_key = 'sha512:2a404a87-ac69-4edd-bfce-f84d671bdd42'   # before define_tables()

# usamos nuestra propia tabla para usuarios:
auth.settings.table_user=db.auth_user 
# Solicito verificación de mail:
auth.settings.registration_requires_verification = False
# Solicito aprobación manual 
#  * Ir al admin, buscar el usuario y limpiar registration_key


auth.define_tables()                           # creates all needed tables

auth.settings.mailer = mail                    # for user email verification

auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = False
auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['reset_password'])+'/%(key)s to reset your password'

#########################################################################
## If you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, uncomment and customize following
# from gluon.contrib.login_methods.rpx_account import RPXAccount
# auth.settings.actions_disabled=['register','change_password','request_reset_password']
# auth.settings.login_form = RPXAccount(request, api_key='...',domain='...',
#    url = "http://localhost:8000/%s/default/user/login" % request.application)
## other login methods are in gluon/contrib/login_methods
#########################################################################

crud.settings.auth = None                      # =auth to enforce authorization on crud

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


## after defining tables, uncomment below to enable auditin






db.define_table('catalogoxtipo',
     Field ('marca', 'string', label=T('Marcas'),requires = IS_UPPER()),
    Field ('cod_articulo','string' , label=T('Codigo de articulo'),requires = IS_UPPER()), 
    Field ('foto', 'upload', label=T('Producto')),
    Field ('tipo' , 'string', label=T('Tipo')),
    Field ('descripcion' , 'text' , label=T('Descripcion'),requires = IS_UPPER()),
    Field('ofertar','boolean',label=T('Ofertar')))
db.catalogoxtipo.cod_articulo.requires= IS_NOT_EMPTY(error_message='No se ha ingresado ningun codigo de articulo')
db.catalogoxtipo.foto.requires= IS_NOT_EMPTY(error_message='No se ha cargado ninguna foto')
db.catalogoxtipo.tipo.requires= IS_NOT_EMPTY(error_message='No se ha seleccionado ningun tipo')
db.catalogoxtipo.descripcion.requires= IS_NOT_EMPTY(error_message='No se ha ingresado ninguna descripcion del articulo')
db.catalogoxtipo.marca.requires= IS_IN_SET(('Alfa romeo','BMW','Cherokee','Chevrolet','Chrysler','Citroen','Fiat','Ford','Hyundai','Honda','Lada','Land-Rover','Mazda','Mercedes-Benz','Mitsubishi','Musso','Nissan','Peugeot', 'Renault','Suzuki','Volkswagen','Otros'))
db.catalogoxtipo.tipo.requires= IS_IN_SET(('Abrazaderas','Almohadillas','Arandelas','Acoples','Barras','Bieletas', 'Bujes',' Bridas','Cazoletas', 'Crapodinas','Corrector de Comba','Cubre cazoletas','Distancial de Mazas','Ejes','Fuelles','Gemelos de Elastico','Gomas','Mazas ruedas','Manchon´s','Montantes','Otros','Ojal', 'Punta de ejes','Platos de Apoyo','Platillos de Fijacion','Palanca de Embrague','Ruleman Paliers' ,'Seguro Manchon´s','Soportes','Topes','Tuercas','Tapon de ejes','Torretas','Traba de Rotulas'))
db.catalogoxtipo.cod_articulo.widget = SQLFORM.widgets.autocomplete(request, db.catalogoxtipo.cod_articulo, limitby=(0,10), min_length=2)
db.catalogoxtipo.descripcion.widget = SQLFORM.widgets.autocomplete(request, db.catalogoxtipo.descripcion, limitby=(0,10), min_length=2)



db.define_table('novedad',
    Field('id','id',label=T('Nº producto')),
    Field('novedad','upload',label=T('Producto')),
    Field('detalle','text',label=T('Oferta')),
    Field('fecha_novedad','datetime',default=request.now,label=T('Fecha de oferta')),)
