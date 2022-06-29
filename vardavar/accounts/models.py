from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
# Create your models here.
class User(AbstractUser):
    buyer=1
    seller=2
    super_user=3
    user_choices=[
        (buyer,_("Üye")),
        (seller,_("Restoran Sahibi")),
    ]
    sub= models.PositiveIntegerField(choices=user_choices,default=buyer)
   
