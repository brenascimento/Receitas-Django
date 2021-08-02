from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

def index(request):
    receitas_db = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas_db
    }

    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita_obj = get_object_or_404(Receita, pk=receita_id)
    receita = {
        'receita': receita_obj
    }
    return render(request, 'receita.html', receita)

def buscar(request):
    listar_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            listar_receitas = Receita.objects.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = { 'receitas' : listar_receitas}

    return render(request, 'buscar.html', dados)

