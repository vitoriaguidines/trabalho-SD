def sw_view(request):
    frase = "teste"
    return render(request, "sw.html", {'frase': frase})