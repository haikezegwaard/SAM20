from django.conf.urls import patterns, include, url
from notifier import views
from django.contrib import admin
from views import DirectTemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', DirectTemplateView.as_view(template_name='digest.html', extra_context={ 'foo': 'bar'}),  name='digest')
)