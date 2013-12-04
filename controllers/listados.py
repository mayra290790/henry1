# coding: utf8
# intente algo como
def listadodenovedades():
    novedades=db().select(db.novedad.novedad,db.novedad.detalle)
    listado=[]
    tablaFinal=DIV(listado)
    return dict(novedades=novedades)
def respondermensaje():
    f= SQLFORM(db.mensajesenviado)
    if f.accepts(request.vars, session):
            response.flash = 'Correo enviado'
             #Send html message to single address:
            mail.send('%s' % request.vars.email, #request.vars.email,
                       'Message subject',
                       '<html>tu formulario ha sido enviado corectamente</html>')

    return locals()


def vercorreo():
    correo=db().select(db.correo.id_correo,db.correo.nombre_apellido,db.correo.email,db.correo.asunto,db.correo.mensaje)
    listado=[]
    tablaFinal=DIV(listado)
    return dict(correo=correo)

def catalogoxtipo():
     if(request.get_vars.buscar2):
        mcatalogo= db((db.catalogoxtipo.descripcion.like('%'+request.get_vars.buscar2+'%'))).select() 
     try:
         mcatalogo2

     except:
        mcatalogo2 = db().select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")
     if(request.get_vars.buscar):
         mcatalogo= db((db.catalogoxtipo.cod_articulo.like('%'+request.get_vars.buscar+'%'))).select() 

     try:
        mcatalogo

     except:
        mcatalogo = db().select(db.catalogoxtipo.ALL,orderby="catalogoxtipo.cod_articulo ASC")

     return dict(mcatalogo=mcatalogo,mcatalogo2=mcatalogo2)


def modificar():
    asp=db(db.catalogoxtipo.id==request.args(0)).select()
    aspi=asp[0]
    db.catalogoxtipo.id.readable=False
    form=SQLFORM(db.catalogoxtipo,aspi,deletable=False,
                    field=['marca','cod_articulo','foto','tipo','descripcion'],
                    labels={'marca':'MARCAS','cod_articulo':'CODIGO DE ARTICULO','foto':'IMAGEN','tipo':'TIPO','descripcion':'DESCRIPCION '},
                    submit_button='Guardar')
    response.flash="ADVENTENCIA:los datos modificados se han guardado en la base de datos"
    if form.accepts(request.vars, session):
        response.flash = 'Los datos se han modificado'
        redirect(URL(r=request,f='catalogoxtipo'))
    return dict(form=form)

def borrar():
    asp=db(db.catalogoxtipo.id==request.args(0)).select()
    aspi=asp[0]
    db.catalogoxtipo.id.readable=False
    form=SQLFORM(db.catalogoxtipo,aspi,deletable=True,
                    field=['marca','cod_articulo','foto','tipo','descripcion'],
                    labels={'marca':'MARCAS','cod_articulo':'CODIGO DE ARTICULO','foto':'IMAGEN','tipo':'TIPO','descripcion':'DESCRIPCION '},
                    submit_button='borrar')
    response.flash="ADVENTENCIA:los datos modificados se han guardado en la base de datos"
    if form.accepts(request.vars, session):
        response.flash = 'Los datos se han modificado'
        redirect(URL(r=request,f='catalogoxtipo'))
    return dict(form=form)


def borrarmensaje():
    asp=db(db.correo.id==request.args(0)).select()
    aspi=asp[0]
    db.correo.id.readable=True
    form=SQLFORM(db.correo,aspi,deletable=True,
                    field=['id_correo','nombre_apellido','email','asunto','mensaje'],
                    labels={'id_correo':'Nº CORREO','nombre_apellido':'NOMBRE Y APELLIDO','email':'EMAIL','asunto':'ASUNTO','mensaje':'MENSAJE'},
                    submit_button='borrar')
    response.flash="ADVENTENCIA:los datos modificados se han guardado en la base de datos"
    if form.accepts(request.vars, session):
        response.flash = 'Los datos se han modificado'
        redirect(URL(r=request,f='vercorreo'))
    return dict(form=form)

def usuarios():
    i=0
    no_aprobados = db(db.auth_user.estado == 'pendiente').select(db.auth_user.id,db.auth_user.foto,db.auth_user.first_name, db.auth_user.last_name,
                                                                    db.auth_user.dni,db.auth_user.email,db.auth_user.password,db.auth_user.address1,
                                                                    db.auth_user.localidad,db.auth_user.provincia,db.auth_user.pais,
                                                                    db.auth_user.cp,db.auth_user.telefono,db.auth_user.created_on)
    for x in no_aprobados:
        i=i+1
    lista=[]
    #se arma una tabla con tres campos: CODIGO, NOMBRE y ACCION
    #El pie de la tabla contiene dos celdas: Total y X Carreras donde X es la cantidad de carreras que muestre la tabla
    lista.append(TABLE(TR(TH('CODIGO',_style='width:20px; color:#000; background: #81C3E6; border: 2px solid #81C3E6'),TH('APELLIDO',_style='width:200px; color:#000; background: #81C3E6; border: 2px solid #81C3E6'),TH('NOMBRE',_style='width:200px; color:#000; background: #81C3E6; border: 2px solid #81C3E6'),TH('OPCION',_style='width:200px; color:#000; background: #81C3E6; border: 2px solid #81C3E6'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #81C3E6; border: 2px solid #81C3E6'),TH(i,' PENDIENTES DE APROBACION',_style='width:200px; color:#000; background: #81C3E6; border: 2px solid #81C3E6'))),
    #se agregan las celdas que vinculan los campos "id" y "nombre" contenidos en rows, referenciado mas abajo en el for
    *[TR(TD(rows.id,_style='width:20px; color:#000; background: #81C3E6; border: 2px solid #cdcdcd'),

    TD(rows.last_name,_style='width:200px; color:#000; background: #81C3E6; border: 2px solid #cdcdcd'),
    TD(rows.first_name,_style='width:200px; color:#000; background: #81C3E6; border: 2px solid #cdcdcd'),
    # SE AGREGA UNA CELDA PARA LOS HIPERVINCULOS Ver Y Modificar que enlazan con
    #los controladores muestraCarrera y modificarCarrera respectivamente:
    TD(A('Administrador',_href=URL(r=request, f='aprobar', args=[rows.id,rows.foto, rows.first_name, rows.last_name,rows.dni,rows.email,rows.password,
                                rows.address1,rows.localidad,rows.provincia,rows.pais,rows.cp,rows.telefono]) )
                        , _style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd' ),
 )


    for rows in no_aprobados]),))
    #se conforma la Tabla resultado:
    tablaFinal = DIV(lista)
    return dict (no=tablaFinal)

def aprobar():
   #se reciben los parametros enviados desde la vista usuario.html que son:
# args[0]---> es el id del elemento seleccionado
# args[1]---> es el apellido del elemento seleccionado
# args[2]---> es el nombre del elemento seleccionado

#usando esos datos hacemos un insert en la tabla clientes:
    cod= db.administrador.insert(id=request.args(0),foto=request.args(1),first_name=request.args(2), last_name=request.args(3),dni=request.args(4),email=request.args(5),
            password=request.args(6),address1=request.args(7),localidad=request.args(8),provincia=request.args(9),pais=request.args(10),cp=request.args(11),telefono=request.args(12))
#Seleccionamos los datos del cliente recien ingresado asi se lo mostramos al usuario:
    nuevo=db(db.administrador.id == cod).select(db.administrador.id,db.administrador.foto,db.administrador.first_name,db.administrador.last_name,db.administrador.email)

#Actualizamos en la tabla auth_user el campo registration_key asi ya queda aprobado
    db(db.auth_user.id == request.args(0)).update(estado='activado')
#retornamos a la vista aprobar.html los datos del nuevo cliente:
    lista_dni= db((db.auth_user.id>0)&(db.auth_user.dni==request.args(4))).select()
    for dni in lista_dni:
        id_usuario=dni.id
        db.auth_membership.insert(
            group_id=6,
            user_id=id_usuario,
            )
        response.flash = 'los datos fueron enviados'
        redirect(URL(r=request,f='administradores'))
    return dict (nuevo=nuevo)
def administradores():
    q = db.auth_user.id >0
    q &=db.auth_membership.group_id==6
    q &=db.auth_membership.user_id==db.auth_user.id
    administrador = db(q).select(db.auth_user.id,db.auth_user.foto, db.auth_user.first_name,db.auth_user.last_name,db.auth_user.first_name,db.auth_user.email,
                            )
    return dict(administrador=administrador)



def modificar_admi():
    admi = db(db.auth_user.id==request.args(0)).select()
    administrador = admi[0]
    form = SQLFORM(db.auth_user,administrador,deletable=False,
                    Field=['id','first_name','last_name','email','password'],
                    labels={'id':'Id de usuario'},
                             submit_button='Grabar')

    response.flash="ADVERTENCIA: todos en la los datos de este usuario seran eliminados de la base de datos.Para eliminar haga click en la casilla de confirmacion y luego presione el boton eliminar"
    if form.accepts(request.vars, session):
        response.flash = 'los datos fueron borrados'
        redirect(URL(r=request,f='administradores'))
    return dict(form=form)


def borrar_admi():
    admi = db(db.auth_user.id==request.args(0)).select()
    administrador = admi[0]
    form = SQLFORM(db.auth_user,administrador,deletable=True,
                    Field=['id','first_name','last_name','email','password'],
                    labels={'id':'Id de usuario'},
                             submit_button='Grabar')

    response.flash="ADVERTENCIA: todos en la los datos de este usuario seran eliminados de la base de datos.Para eliminar haga click en la casilla de confirmacion y luego presione el boton eliminar"
    if form.accepts(request.vars, session):
        response.flash = 'los datos fueron borrados'
        redirect(URL(r=request,f='administradores'))
    return dict(form=form)
