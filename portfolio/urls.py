from django.urls import path
from . views import ProjectList


app_name = 'portfolio'


urlpatterns = [
    path('',ProjectList.as_view(),name='project_list')
]
