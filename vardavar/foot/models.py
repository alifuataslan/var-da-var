from django.db import models

# Create your models here.

class Foot_catagorie(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self) -> str:
        return self.catagories