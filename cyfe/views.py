from django.shortcuts import render
from django.views import generic
# Create your views here.
#create a new summary, store it and render result
class CyfeAPI(generic.ListView):
    #model = Summary
    template_name = 'summaryList.html'