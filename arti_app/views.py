from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import CreateView,UpdateView
from .models import ArtiModel
from django.urls import reverse_lazy


class Arti_view(ListView):
    model = ArtiModel
    template_name = 'home.html'

class Arti_Detail_View(DetailView):
    model = ArtiModel
    template_name = 'Arti_detail.html'

class Arti_Create_View(CreateView):
    model = ArtiModel
    template_name = 'Arti_create.html'
    fields = '__all__'

class Arti_Update_View(UpdateView):
    model = ArtiModel
    template_name = 'Arti_edit.html'
    fields = ['title','body']

class Arti_Delete_view(DeleteView):
    model = ArtiModel
    template_name = 'Arti_delete.html'
    success_url = reverse_lazy('home')