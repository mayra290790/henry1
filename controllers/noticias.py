# coding: utf8
# intente algo como
def index(): return dict(message="hello from noticias.py")
def noticias():
    f=SQLFORM(db.novedad, submit_button='Guardar')
    if f.accepts(request.vars, session):
        response.flash = 'Se ingreso una nueva noticia'
    else:
        response.flash='Complete el formulario'
    return dict(f=f)
