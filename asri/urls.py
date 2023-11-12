from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='asri'),
    path('penmu', views.penmu, name='penmu'),
    path('opini', views.opini, name='opini'),
    path('puisi', views.puisi, name='puisi'),
    path('aboutme', views.aboutme, name='aboutme'),
    
]