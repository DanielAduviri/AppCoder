from django.urls import path
from modulo1 import views

#Creamos urls.py en nuestra app(modulo1) para evitar que poner 400 urls de la misma app en el backend que seria "proyectoCoder"
#de esta manera si nuestra app tiene  49999 urls no copiamos una por una en urls.py del backend sino que con una sola linea ya tenemos
#todas
urlpatterns = [
    path('CrearCurso/<nombre>/<camada>', views.crea_curso),
    path('Curso', views.curso),
    path('', views.inicio),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables)
]
#ver CrudDjango y agregar o quitar en urls la "/"
