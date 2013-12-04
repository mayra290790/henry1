# coding: utf8
# intente algo como
@auth.requires_membership(role='admin')
def index():
    if auth.user_id:
        if auth.has_membership (group_id=1):
            redirect(URL(r=request, c="default" , f="index"))
      
    return dict()

@auth.requires_membership(role='admin')    
def user():
    return dict(form=auth())
