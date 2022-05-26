from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page),
    path('<slug:slug>', views.index, name="index_page")
]