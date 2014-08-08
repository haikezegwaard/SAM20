from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views import generic
from myMonitor.models import Project


# Create your views here.

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project.html'
