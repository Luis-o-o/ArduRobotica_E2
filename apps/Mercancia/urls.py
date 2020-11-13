from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import MercanciaList, MercanciaCreate, MercanciaUpdate , MercanciaDelete,MercanciaListG

urlpatterns = [
    path('listar/', MercanciaList.as_view(), name="mercancia_list"),
    path('producto/', MercanciaListG.as_view(), name="producto_listG"),

    path('crear/', MercanciaCreate.as_view(), name="mercancia_form"),
    path('editar/<int:pk>', MercanciaUpdate.as_view(), name="mercancias_update"),
    path('borrar/<int:pk>', MercanciaDelete.as_view(), name="mercancias_borrar"),
    
]
