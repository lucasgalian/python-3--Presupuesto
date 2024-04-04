from django.contrib import admin
from .models import Presupuesto
# Register your models here.
   #modeladmin/ORM 
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ['titulo','materiaPrima','manoDeObra','fecha','precio']
    search_fields = ['titulo','materiaPrima','manoDeObra','fecha','precio']


admin.site.register(Presupuesto,PresupuestoAdmin)