from django.shortcuts import render
from . models import Project
# Create your views here.
from django.views.generic import ListView


class ProjectList(ListView):
    model = Project