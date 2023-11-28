from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Actor, Film, Category

def sw_view(request):
    return render(request, 'page.html')


def consultar(request, tabela, entrada):
    tabela = tabela.lower()
    existe = False

    if tabela == 'actor':
        existe = Actor.objects.filter(first_name__icontains=entrada).exists()
    elif tabela == 'film':
        existe = Film.objects.filter(title__icontains=entrada).exists()
    elif tabela == 'category':
        existe = Category.objects.filter(name__icontains=entrada).exists()

    return JsonResponse({'existe': existe})