from django.forms import ModelForm
from django import forms
from .models import Project
from django.contrib.auth.models import User


# class UserForm(ModelForm):
#     class Meta:
#         model=User
#         fields= ['username','password']

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','images']
        # fields=['title','target_company','description','start_date','end_date','service_type']
        # widgets = {
        #         'images':forms.Textarea(attrs={"rows":5, "cols":50}),
        #         'start_date': forms.DateInput(format=('%Y-%m-%d'), 
        #                 attrs={'class': 'datepicker', 'placeholder':'Select a date','type':'date'}
        #                 ),
        #         'end_date': forms.DateInput(format=('%Y-%m-%d'), 
        #                 attrs={'class': 'datepicker', 'placeholder':'Select a date','type':'date'}
        #                 ),
        # }

#EditProjectForm
class EditProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','images']
        # fields='__all__'
        # widgets = {
        #         'description':forms.Textarea(attrs={"rows":5, "cols":50}),
        #         'start_date': forms.DateInput(format=('%Y-%m-%d'), 
        #                 attrs={'class': 'datepicker', 'placeholder':'Select a date','type':'date'}
        #                 ),
        #         'end_date': forms.DateInput(format=('%Y-%m-%d'), 
        #                 attrs={'class': 'datepicker', 'placeholder':'Select a date','type':'date'}
        #                 ),
        # }