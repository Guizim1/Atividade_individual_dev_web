from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogador
from .models import MestreDeJogo
from django.contrib import messages
# Home
def home(request):
    return render(request, 'home.html')

# Lista de Mestres
def lista_mestres(request):
    mestres = MestreDeJogo.objects.all()
    return render(request, 'lista_mestres.html', {'mestres': mestres})

def criar_mestre(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')  # Usando .get() para evitar erro
        experiencia = request.POST.get('experiencia', '')  # Valor padrão vazio, caso não exista
        if nome and experiencia:
            MestreDeJogo.objects.create(nome=nome, experiencia=experiencia)
            messages.success(request, 'O Mestre de Jogo foi adicionado com sucesso!')
            return redirect('lista_mestres')  # Redireciona para a lista de mestres
        else:
            messages.error(request, 'Por favor, preencha todos os campos!')
    return render(request, 'form_mestre.html')

def atualizar_mestre(request, pk):
    mestre = get_object_or_404(MestreDeJogo, pk=pk)
    if request.method == 'POST':
        mestre.nome = request.POST['nome']
        mestre.experiencia = request.POST['experiencia']
        mestre.save()
        return redirect('lista_mestres')
    return render(request, 'form_mestre.html', {'mestre': mestre})

def deletar_mestre(request, pk):
    mestre = get_object_or_404(MestreDeJogo, pk=pk)
    if request.method == 'POST':
        mestre.delete()
        return redirect('lista_mestres')
    return render(request, 'confirmar_deletar_mestre.html', {'mestre': mestre})

# Lista de Jogadores
def lista_jogadores(request):
    jogadores = Jogador.objects.all()  # Pega todos os jogadores do banco de dados
    return render(request, 'lista_jogadores.html', {'jogadores': jogadores})

def criar_jogador(request):
    mestres = MestreDeJogo.objects.all()

    if request.method == 'POST':
        nome = request.POST['nome']
        classe = request.POST['classe']
        nivel = request.POST['nivel']
        mestre_id = request.POST['mestre_de_jogo']
        mestre = get_object_or_404(MestreDeJogo, pk=mestre_id)
        Jogador.objects.create(nome=nome, classe=classe, nivel=nivel, mestre_de_jogo=mestre)
        return redirect('lista_jogadores')
    
    return render(request, 'form_jogador.html', {'mestres': mestres})

def atualizar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    mestres = MestreDeJogo.objects.all()
    if request.method == 'POST':
        jogador.nome = request.POST['nome']
        jogador.classe = request.POST['classe']
        jogador.nivel = request.POST['nivel']
        jogador.mestre_de_jogo_id = request.POST['mestre_de_jogo']
        jogador.save()
        return redirect('lista_jogadores')
    return render(request, 'form_jogador.html', {'jogador': jogador, 'mestres': mestres})

def deletar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores')
    return render(request, 'confirmar_deletar_jogador.html', {'jogador': jogador})
