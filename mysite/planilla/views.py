from django.shortcuts import render, redirect, get_object_or_404
from .models import Presupuesto 


# Create your views here.
def mostrar_presupuestos(request):
    servicios= Presupuesto.objects.all()
    return render(
        request,
        'mostrar_presupuestos.html',
        {'servicios':servicios}
    )
def detail_pres(request, id):
    servicio= get_object_or_404(Presupuesto, id= id)
    return render(
        request, 
        'detail_pres',
        {'servicio':servicio}
      ) 
##C R U D
def create_pres(request):
    if request.method =='POST':
        titulo = request.POST.get('titulo')
        materiaPrima = request.POST.get('materiaPrima')
        manoDeObra = request.POST.get('manoDeObra')
        fecha = request.POST.get('fecha')
        precio = request.POST.get('precio')
        Presupuesto.objects.create(
        titulo = titulo,
        materiaPrima = materiaPrima,
        manoDeObra = manoDeObra,
        fecha = fecha,
        precio = precio,
    )
        return redirect('mostrar_presupuestos')
    return render(
            request, 
            'create_pres.html'
        )

def filtrar_presupuesto(request, precio):
    servicioEncontrados = Presupuesto.objects.filter( precio = precio )
    return render(
        request,
        'filtrar_presupuesto.html',
        {'servicio':servicioEncontrados}
    )

def update_presupuesto(request, id, titulo, materiaPrima,manoDeObra, fecha, precio):
    servicio= get_object_or_404(Presupuesto, id = id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        materiaPrima = request.POST.get('materiaPrima')
        manoDeObra = request.POST.get('manoDeObra')
        fecha = request.POST.get('fecha')
        precio = request.POST.get('precio')
        presupuestoActualizado= Presupuesto.objects.get()
        presupuestoActualizado.titulo = titulo,
        presupuestoActualizado.materiaPrima = materiaPrima,
        presupuestoActualizado.manoDeObra = manoDeObra,
        presupuestoActualizado.fecha = fecha,
        presupuestoActualizado.precio = precio,
        presupuestoActualizado.save()
        servicios = Presupuesto.objects.all()
        return redirect('mostrar_presupuestos')
    return render(
        request,
            'create_pres.html',
            {'servicio':servicio}
    )

def delete_presupuesto(request,id):
    presupuestoBorrar= Presupuesto.objects.get(id = id)
    presupuestoBorrar.delete()
    servicios = Presupuesto.objecte.all()
    return render(
        request,
        'mostrar_presupuestos.html',
        {'servicio':presupuestoBorrar}
        )

def delete_planilla(request):
    servicios=Presupuesto.objects.all()
    servicios.delete()
    return render(
        request,
        'mostrar_presupuestos.html',
        {'usuarios':servicios}
    )

