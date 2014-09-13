from django.shortcuts import render
import mailchimp
from utils import get_mailchimp_api
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader
import logging

# Create your views here.
def index(request):
    m = get_mailchimp_api()
    try:
        m.helper.ping()
        m.lists.growth_history('111177')
        logging.debug("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    except mailchimp.Error:
        messages.error(request,  "Invalid API key")
    return render_to_response('list.html', {}, context_instance=RequestContext(request))