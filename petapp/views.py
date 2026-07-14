from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Petshop
from .forms import PetshopForm


class PetshopListView(ListView):
    model = Petshop
    template_name = 'pet_list.html'
    context_object_name = 'pets'

class PetshopCreateView(CreateView):
    model = Petshop
    form_class = PetshopForm
    template_name = 'pet_add.html' 
    success_url = reverse_lazy('pet_list')

class PetshopUpdateView(UpdateView):
    model = Petshop
    form_class = PetshopForm
    template_name='pet_edit.html'
    success_url =reverse_lazy('pet_list')

class PetshopDeleteView(DeleteView):
    model = Petshop
    template_name = 'pet_delete.html'
    success_url = reverse_lazy('pet_list')

