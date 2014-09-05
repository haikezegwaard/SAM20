from django.conf.urls import patterns, url
from django.contrib import admin
from views import DigestView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', DigestView.as_view(template_name='digest.html', extra_context={ 'foo': 'bar'}),  name='digest')
)