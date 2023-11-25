def friends_view(request):
    frase = "teste"
    return render(request, "sw.html", {'frase': frase})