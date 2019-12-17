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
    model = Tutorial

    def get(self, request):
        """ GET a list of Pages. """
        tutorials = self.get_queryset().all()[::-1]
        return render(request, self.template_name, {
          'tutorials': tutorials
    })

class TutorialDetailView(ListView):
    template_name = 'tutorials/tutorial_2.html'
    model = Tutorial

    def get(self, request, id):
        """ Returns a specific wiki page by slug. """
        tutorial = self.model.objects.get(pk=id)
        modules = Module.objects.get_queryset().get(tutorial=tutorial.id)
        return render(request, self.template_name, {
          'modules': modules
    })

class TutorialCreateView(CreateView):
    template_name = 'new_tutorial.html'
    form_class = TutorialForm
    success_url = '/'
    ModuleFormSet = formset_factory(ModuleForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = self.ModuleFormSet
        return context

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