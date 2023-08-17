from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listagem_usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    listagem_usuarios={
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'listagem_usuarios.html', listagem_usuarios)
