from django.contrib import admin
from .models import Espece


class EspeceAdmin(admin.ModelAdmin):
    model = Espece
    ordering = ['slug']
    list_display = ['pk', 'nom', 'slug']
    


admin.site.register(Espece, EspeceAdmin)
