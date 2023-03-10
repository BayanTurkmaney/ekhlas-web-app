from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name='home'),
     path('login/',views.login_user,name='login'),
     path('signup/',views.signup,name='signup'),
     path('logout/',views.logout_user,name='logout'),
     # path('contact/',views.contact,name='contact'),
     path('services/',views.services,name='services'),
     path('add_admin/',views.add_admin_view,name='add_admin'),
     path('authentication/',views.auth,name='authentication'),
     path('features/',views.features,name='features'),
     path('about/',views.about,name='about'),
     path('team/',views.team,name='team'),
     # path('settings/',views.settings,name='settings'),
     path('projects/',views.get_all_projects,name='projects'),
     path('dashboard/',views.get_admin_all_projects,name='dashboard'),
     path('add_project/',views.add_project,name='add_project'),
     path('view_project_detail/<int:project_id>',views.view_project_detail,name='view_project_detail'),
     path('edit_project/<int:project_id>',views.edit_project,name='edit_project'),
     path('delete_project/<int:project_id>',views.delete_project,name='delete_project'),
     path('service_detail/',views.service_detail,name='service_detail'),
     path('matate_isol_details/',views.matate_isol_details,name='matate_isol_details'),
     path('fom_isol_details/',views.fom_isol_details,name='fom_isol_details'),
     path('esmante_isol_details/',views.esmante_isol_details,name='esmante_isol_details'),
     path('temp_isol_details/',views.temp_isol_details,name='temp_isol_details'),
     path('epoxi_isol_details/',views.epoxi_isol_details,name='epoxi_isol_details'),
     path('water_isol_details/',views.water_isol_details,name='water_isol_details'),
     ]