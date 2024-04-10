from django.contrib import admin
from django.urls import path
from AcademTrilho.views import consultar_cursos_semestres

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Consultar/', consultar_cursos_semestres, name='consultar'),
]

