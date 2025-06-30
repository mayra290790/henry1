# coding: utf8
# intente algo como

def catalogoxtipo():
    f=SQLFORM(db.catalogoxtipo, submit_button='GUARDAR')
    if f.accepts(request.vars, session):
            response.flash='Se ingreso un nuevo articulo' 
          
    else:
        response.flash='Complete el formulario'
    return dict(f=f)
