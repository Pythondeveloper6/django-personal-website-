from django.shortcuts import render
from .models import Service , Facts
# Create your views here.
from django.views.generic import ListView



class ServiceList(ListView):
    model = Service

