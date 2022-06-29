from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.

class Catagori(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self) -> str:
        return self.name

class AllFoot(models.Model):
    foot_type= models.ForeignKey("foot.Catagori",on_delete=models.CASCADE,verbose_name="Yemek Tipi")
    whos_foot= models.ForeignKey("accounts.User",on_delete=models.CASCADE,verbose_name="Restoran adı")
    name = models.CharField(max_length=50,verbose_name="Yemek Adı" )
    price= models.PositiveIntegerField(null=False,verbose_name="Fiyatı")
   