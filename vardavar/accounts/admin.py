from django.contrib import admin
from accounts.models import User, Yemekler


# Register your models here.
admin.site.register(Yemekler)

admin.site.register(User)