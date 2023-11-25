from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sw_view(request):
    return render(request, 'page.html')

# Create your views here.