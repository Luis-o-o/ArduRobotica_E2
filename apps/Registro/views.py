from django.shortcuts import render
from .models import Recomendacion
from .forms import RecomendacionesForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q 

# Create your views here.
def listar_recomendaciones(request):
    recomendaciones = Recomendacion.objects.all()
    return render(request, "Registro/listar_recomendaciones.html", {'recomendaciones': recomendaciones})


class RecomendacionCreate(CreateView):
    model = Recomendacion
    form_class = RecomendacionesForm
    template_name = 'Registro/recomendaciones_form.html'
    success_url = reverse_lazy('list_recomendaciones')
    
class RecomendacionList(ListView):
    model = Recomendacion
    template_name = 'Registro/list_recomendaciones.html'
    # paginate_by = 4

class RecomendacionUpdate(UpdateView):
    model = Recomendacion
    form_class = RecomendacionesForm
    template_name = 'Registro/recomendaciones_form.html'
    success_url = reverse_lazy('list_recomendaciones')

        

class RecomendacionDelete(DeleteView):
    model = Recomendacion
    template_name = 'Registro/recomendaciones_delete.html'
    success_url = reverse_lazy('list_recomendaciones')


def mantenedor(request):
    lista= Recomendacion.objects.all()
    nombre_producto= request.GET.get('nombre-producto')
    nombre= request.GET.get('nombre')
 
    if 'btn-nombre-producto' in request.GET:
       if nombre_producto: 
           lista= Recomendacion.objects.filter(producto__icontains=nombre_producto)
    elif 'btn-nombre' in request.GET:
        if nombre:
            lista= Recomendacion.objects.filter(nombre__icontains=nombre)
      
    data = {
        'object_list': lista
    }
    return render(request, 'Registro/list_recomendaciones_filtros.html', data)