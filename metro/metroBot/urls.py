from django.urls import path
from . import views

app_name = 'metroBot'

urlpatterns = [
    path('', views.index, name="index"),
    path('process_input/', views.process_input, name='process_input'),
    
]