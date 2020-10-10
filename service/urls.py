from django.urls import path
from .views import ServiceList

app_name = 'service'



urlpatterns = [
    path('',ServiceList.as_view(),name='service_list')
]
