from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def local(request):
    return render(request, 'local.html')
    
def exibiritem(request, id):
    return render(request, 'exibiritem.html', {'id': id})

def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario': usuario})

def dia_da_semana(request, num):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    dia = dias.get(num, "Número inválido! Escolha um número entre 1 e 7.")
    return render(request, 'dia.html', {'dia': dia})
