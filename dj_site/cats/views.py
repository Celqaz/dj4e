from django.views.generic import ListView, DetailView,DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Breed, Cat


# Cat View
class CatList(LoginRequiredMixin, ListView):
    queryset = Cat.objects.all()
    context_object_name = 'cats'
    template_name = 'cats/cat_list.html'

class CatDetail(LoginRequiredMixin, DetailView):
    model = Cat


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:all')
    template_name_suffix = '_confirm_delete'

# Breed View
class BreedList(LoginRequiredMixin, ListView):
    queryset = Breed.objects.all()
    context_object_name = 'breeds'
    template_name = 'cats/breed_list.html'

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:breed_list')
    template_name_suffix = '_confirm_delete'