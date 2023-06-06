#from django.conf.urls import url
from django.urls import path
from  . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  # path('index', views.index, name='index'),
  # path('listadoSQL', views.listadoSQL, name='listadoSQL'),
   path('base', views.base, name='base'),
   path('', views.home, name='home'),
   path('nosotros', views.nosotros, name='nosotros'),
   path('contacto', views.contacto, name='contacto'),
   path('cursos', views.cursos, name='cursos')
   
] 

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
