from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from modulo1.views import crea_curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CreaCurso/<nombre>/<camada>', crea_curso),
    path('modulo1', include('modulo1.urls'))
    
]
