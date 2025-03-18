from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import *



class EmployesView(ListView):
    model = Employes
    template_name = 'emp_view.html'
    context_object_name = 'emp_v'


class FormAdd(CreateView):
    model = Employes
    template_name = 'employes_add.html'
    fields = ['last_name', 'first_name', 'midle_name', 'email', 'phone', 'data_fild','fk_departamen', 'fk_region']
    success_url = reverse_lazy('emp')





