from django.shortcuts import render, redirect
from .forms import ProjectForm, EditProjectForm
from .decorators import unauthenticated_user, logout_user_dec
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login, logout
from django.contrib.auth.models import Group
from .user_form import CreateUserForm
from django.contrib import messages
from .models import Project

# Create your views here.

#pages

def home(request):
    logout(request)
    
    return render(request,'index.html')

# def contact(request):
#     return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def features(request):
    return render(request,'features.html')

def projects(request):
    return render(request,'projects.html')

def about(request):
    return render(request,'about.html')

def team(request):
    return render(request,'team.html')

def settings(request):
    return render(request,'settings.html')

def service_detail(request):
     return render(request,'service_detail.html')

def matate_isol_details(request):
    return render(request,'matate_isol_details.html')

def temp_isol_details(request):
    return render(request,'temp_isol_details.html')

def epoxi_isol_details(request):
    return render(request,'epoxi_isol_details.html')

def esmante_isol_details(request):
    return render(request,'esmante_isol_details.html')

def water_isol_details(request):
    return render(request,'water_isol_details.html')

def fom_isol_details(request):
    return render(request,'fom_isol_details.html')

# authentication
def auth(request):
    return render(request,'authentication.html')

#project crud
def get_all_projects(request):
    print('auth ...')
    user=request.user
    # print(user.project.title)
    # projects=Project.objects.filter(created_by=user.id)
    us_projects=Project.objects.all()
    context={'projects':us_projects,"us_projects":us_projects}
    return render(request,"projects.html",context)

@unauthenticated_user
def get_admin_all_projects(request):
    print('called  ...')
    user=request.user
    # print(user.project.title)
    # projects=Project.objects.filter(created_by=user.id)
    us_projects=Project.objects.all()
    context={'projects':us_projects,"us_projects":us_projects}
    return render(request,"dashboard.html",context)

# view_project_detail
def view_project_detail(request,project_id):
    project=Project.objects.get(id=project_id)
    context={'project':project}
    return render(request,"view_project_detail.html",context)
@unauthenticated_user
def add_project(request):
    
    form=ProjectForm()
    if request.method == "POST":
        form=ProjectForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print('error on add  project.............')
    context={'form':form,'title':'إضافة مشروع جديد '}
    return render(request,'add_project.html',context)

@unauthenticated_user
def edit_project(request,project_id):
    project=Project.objects.get(id=project_id)
    form=EditProjectForm(instance=project)
    if request.method == "POST":
        form=EditProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print('erooooooooooooooorr.............')
    context={'form':form,'title':'تعديل المشروع'}
    return render(request,'add_project.html',context)
@unauthenticated_user
def delete_project(request,project_id):
    project=Project.objects.get(id=project_id)
    if request.method=="POST":
        project.delete()
        return redirect('dashboard')
    return render(request,'alert.html')

#users


def signup(request):
        print('********************')
        form=CreateUserForm()
        if request.method=="POST":
            print(request.POST)
            form=CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                print(user)
                group=Group.objects.get(name='users')
                user.groups.add(group)  
                username=request.POST["username"]
                messages.success(request,"Account was created successfully for "+username)
                return redirect('login')
            else:
                print(' not valid...')
        context={'form':form}
        return render(request,'signup.html',context)


def login_user(request):
    print('login now...')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # if hasattr(user, 'emp') or user.username =='admin':
                # group=request.user.groups.all()[0].name
                # print(group)
                login(request,user)
                print('logged successfully ...')
                return redirect('dashboard')
            # else:
            #     messages.info(request,'You must wait until allowed login!')
        else :
            messages.info(request,'Username or password is incorrect')
        
    context={}
    return render(request,'login_user.html',context)

def logout_user(requset):
    logout(requset)
    return redirect('home')

