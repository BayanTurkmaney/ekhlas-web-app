from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models

class Project(models.Model):
    title           =  models.CharField(max_length=50)
    created_at      =  models.DateTimeField(auto_now_add=True)
    created_by      =  models.ForeignKey(User,related_name='project',on_delete=models.SET_DEFAULT,default=1)
    updated_at      =  models.DateTimeField(auto_now=True)
    updated_by      =  models.ForeignKey(User,related_name='+',on_delete=models.SET_DEFAULT,default=1)
    images          =  models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.title


