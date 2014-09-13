from django.shortcuts import render
import mailchimp
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader
import logging

class MailchimpManager:
    """
    Converter class to interface with Mailchimp API and
    retrieve project specific reporting data
    """

    def __init__(self, apikey):
        self.api = mailchimp.Mailchimp(apikey)

    def get_list_growth_data(self, listid):
