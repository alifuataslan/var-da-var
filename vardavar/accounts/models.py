from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    üye=1
    r_sahibi=2
    super_user=3
    sub_type=models.PositiveBigIntegerField(choices=[(üye,"Üye"),(r_sahibi,"RestoranSahibi"),(super_user,"SuperUser")],default=1)

class Yemekler(models.Model):
    catagories=models.CharField(max_length=70)
    def __str__(self) -> str:
        return self.catagories