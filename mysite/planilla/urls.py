from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.mostrar_presupuestos, name="mostrar_presupuestos"),
    path('detail_pres/<int:id>', views.detail_pres, name="detail_pres"),
    path('create_pres/', views.create_pres, name="create_pres"),
    path('filtrar_presupuesto/', views.filtrar_presupuesto, name="filtrar_presupuesto"),
    path('update_presupuesto/<int:id>/<str:titulo>/<str:materiaPrima>/<str:manoDeObra>/<int:fecha>/<int:precio>/', views.update_presupuesto, name="update_presupuesto"),
    path('delete/<int:id>', views.delete_presupuesto, name="delete_presupuesto"),
    path('delete', views.delete_planilla)
]
