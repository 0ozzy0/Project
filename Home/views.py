from django.shortcuts import render
from .models import Project
from django.views.generic import DetailView
from django.core.paginator import Paginator
import matplotlib.pyplot as plt
import io
import urllib,base64





def project(request):

    Projects = Project.objects.all()

    project_paginator = Paginator(Projects, 20)

    page_num = request.GET.get('page')

    page = project_paginator.get_page(page_num)



    context = {
        "project":Projects,
        "page": page,
        "count": project_paginator.count
    }
    return render(request, 'Home/home.html', context)





class ProjectDetailView(DetailView):
    model = Project




def graph(request):
    failed_list = 0
    succesful_list = 0
    cancel_list = 0
    live_list = 0
    for project in Project.objects.all():
        if project.project_status == "successful" :
            succesful_list += 1
        elif project.project_status == "failed":
            failed_list += 1
        elif project.project_status == "canceled":
            cancel_list += 1
        elif project.project_status == "live":
            live_list += 1

    slices = [failed_list, succesful_list, cancel_list, live_list]
    labels = ['failed', 'succesful', 'canceled', 'live']

    plt.style.use("fivethirtyeight")
    plt.pie(slices, labels = labels, wedgeprops= {'edgecolor': 'black'})
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "Home/graphs.html", {"data": uri})


def about(request):

    return render(request, "Home/about.html")

