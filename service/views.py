from django.shortcuts import render
from .models import Service , Facts
# Create your views here.
from django.views.generic import ListView



class ServiceList(ListView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["facts"] = Facts.objects.last() 
        return context
    
