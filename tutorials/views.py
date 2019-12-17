from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Tutorial, Module
from .forms import TutorialForm, ModuleForm

# Create your views here.

class TutorialListView(ListView):
    template_name = 'tutorials/index.html'
    queryset = Tutorial.objects.all()[::-1]

class TutorialDetailView(ListView):
    template_name = 'tutorials/tutorial_2.html'
    # queryset = Tutorial.objects.get(id=1)
    model = Tutorial

class TutorialCreateView(CreateView):
    template_name = 'new_tutorial.html'
    form_class = TutorialForm
    success_url = '/'
    ModuleFormSet = formset_factory(ModuleForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = self.ModuleFormSet
        return context
    
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class

    def post(self, request, *args, **kwargs):
        form = TutorialForm(request.POST)
        formset = self.ModuleFormSet(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            tutorial = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    module = inline_form.save(commit=False)
                    module.tutorial = tutorial
                    module.save()
        return HttpResponseRedirect(self.success_url)