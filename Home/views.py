from django.shortcuts import render
from .models import Project
from django.views.generic import DetailView
from django.core.paginator import Paginator
import matplotlib.pyplot as plt
import io
import urllib, base64


def project(request):
    Projects = Project.objects.all()

    project_paginator = Paginator(Projects, 20)

    page_num = request.GET.get('page')

    page = project_paginator.get_page(page_num)

    context = {
        "project": Projects,
        "page": page,
        "count": project_paginator.count
    }
    return render(request, 'Home/home.html', context)


class ProjectDetailView(DetailView):
    model = Project


def graph(request):
    context = {
        "header": 'Project Status Distribution',
        'link': '/static/graph1.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph2(request):
    context = {
        "header": 'Category Distribution',
        'link': '/static/graph2.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph3(request):
    context = {
        "header": 'Timey Wimey',
        'link': '/static/graph3.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph4(request):
    context = {
        "header": 'Monthly Success Distribution',
        'link': '/static/graph4.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph5(request):
    context = {
        "header": 'Most Popular Categories',
        'link': '/static/graph5.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph6(request):
    context = {
        "header": 'Categorywise Success Distribution',
        'link': '/static/graph6.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph7(request):
    context = {
        "header": 'Project Country Distribution',
        'link': '/static/graph7.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph8(request):
    context = {
        "header": 'Success Rate Per Year',
        'link': '/static/graph8.png/',
    }
    return render(request, "Home/graphs.html", context)


def graph9(request):
    context = {
        "header": 'Total Money Raised by Category',
        'link': '/static/graph9.png/',
    }
    return render(request, "Home/graphs.html", context)


def about(request):
    return render(request, "Home/about.html")
