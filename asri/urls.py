from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='asri'),
    path('penmu', views.penmu, name='penmu'),
]