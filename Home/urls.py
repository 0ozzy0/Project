

from django.urls import path
from . import views
from .views import ProjectDetailView


urlpatterns = [
path('home/', views.project, name = "home"),
path('about/', views.about, name = "about"),
path('detail/<int:pk>/', ProjectDetailView.as_view(), name = "detail"),
path('graphs/', views.graph, name = "graph")


  ]