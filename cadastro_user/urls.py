
from django.urls import path
from app_usuario import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.listagem_usuarios, name='listagem_usuarios')
]
