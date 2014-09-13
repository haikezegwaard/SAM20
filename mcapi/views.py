from django.shortcuts import render
import mailchimp
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader
import logging
from mailchimp_manager import MailchimpManager

# Create your views here.
def index(request):
    m = MailchimpManager('8e7536a78b89a35edfa0122d2e417186-us1')

    list_growth = m.get_list_growth_data('23c3cfb062')

    return render_to_response('list.html', {'list_growth' : list_growth}, context_instance=RequestContext(request))