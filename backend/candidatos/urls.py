from django.urls import path
from .views import BuscarCandidatosGitHub

urlpatterns = [
    path('buscar-github/', BuscarCandidatosGitHub.as_view(), name='buscar_github'),
]
