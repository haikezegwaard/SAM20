from django.conf.urls import patterns, include, url
from myMonitor import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myMonitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^summary/(?P<pk>\d+)/$', views.ProjectSummaryMail.as_view(), name='summary'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^niki/', include('niki.urls')),
)
