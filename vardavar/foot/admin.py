from django.contrib import admin

from foot.models import Catagori,AllFoot

# Register your models here.
admin.site.register(Catagori)

@admin.register(AllFoot)
class AllfootAdmin(admin.ModelAdmin):
    list_display=["whos_foot","name","price"]