from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ColetaForm
from django.contrib import messages
from .models import Coleta  # Importando o modelo Coleta 

def index(request):
    return render(request, 'recicle/index.html')

def cadastro(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            coleta = form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('cadastro')
        else:
            messages.error(request, 'Verifique se todos os campos foram preenchidos corretamente')
    else:
        form = ColetaForm()
    
    return render(request, 'recicle/cadastro.html', {'form': form})

@login_required
def parceiros(request):
    coletas = Coleta.objects.all()  # Busca todos os registros do modelo Coleta
    return render(request, 'recicle/parceiros.html', {'coletas': coletas})  # Renderiza o template 'parceiros.html'
def dicas(request):
    return render(request, 'recicle/dicas.html')


