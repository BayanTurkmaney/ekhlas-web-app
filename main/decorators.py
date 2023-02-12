from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import  logout
def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated == False:     
            return redirect('authentication')
        else:
          return view_func(request,*args, **kwargs)
    return wrapper_func

def logout_user_dec(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated: 
            logout(request)   
            return redirect('authentication')
        else:
          return view_func(request,*args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                # print(group)
            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are  not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request,*args, **kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='users':
            return redirect('home')
        if group=='admin':
            return view_func(request,*args, **kwargs)
    return wrapper_func
                