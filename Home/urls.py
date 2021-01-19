from django.conf.urls import url
from django.urls import path, include
from . import views, admin
from .views import ProjectDetailView

urlpatterns = [
    path('home/', views.project, name="home"),
    path('about/', views.about, name="about"),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name="detail"),
    path('graph/', views.graph, name="graph"),
    path('graph2/', views.graph2, name="graph2"),
    path('graph3/', views.graph3, name="graph3"),
    path('graph4/', views.graph4, name="graph4"),
    path('graph5/', views.graph5, name="graph5"),
    path('graph6/', views.graph6, name="graph6"),
    path('graph7/', views.graph7, name="graph7"),
    path('graph8/', views.graph8, name="graph8"),
    path('graph9/', views.graph9, name="graph9"),
    path('', views.project, name="home")

]
