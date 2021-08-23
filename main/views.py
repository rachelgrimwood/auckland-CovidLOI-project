from django.shortcuts import render
from django.http import HttpResponse
from .models import LOIModel

def index(request):
    context = {
        'LOITable': LOIModel.objects.order_by('-updated'),
    }
    return render(request, 'main/home.html', context)
