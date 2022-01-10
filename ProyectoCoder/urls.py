from django.contrib import admin
from django.urls import path

from modulo1.views import crea_curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CreaCurso/<nombre>/<camada>', crea_curso)
]
