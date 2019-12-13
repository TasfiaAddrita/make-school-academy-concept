from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
# Create your views here.

class TutorialListView(ListView):
    template_name = 'tutorials/index.html'
    queryset = Tutorial.objects.all()

class TutorialDetailView(ListView):
    template_name = 'tutorials/tutorial.html'
    # queryset = Tutorial.objects.get(id=1)
    model = Tutorial
