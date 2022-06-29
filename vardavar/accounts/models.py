from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
# Create your models here.
class User(AbstractUser):
    üye=1
    r_sahibi=2
    super_user=3
    user_choices=[
        (üye,"Üye"),
        (r_sahibi,"Restoran Sahibi"),
    ]
    sub= models.PositiveIntegerField(choices=user_choices,default=1)
   
