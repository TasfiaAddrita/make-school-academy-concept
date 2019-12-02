from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
# from django.views.generic.list import ListView

# Create your views here.

def homepage(request):
    # return HttpResponse('This is an <strong>awesome</strong> homepage!')

    # to reference index.html
    # template_name='tutorials/index.html'

    return render(request=request, template_name='tutorials/index.html', context={'tutorials': Tutorial.objects.all})

def tutorialpage(request):
    return render(request=request, template_name='tutorials/tutorial.html', context={'tutorials': Tutorial.objects.all})
