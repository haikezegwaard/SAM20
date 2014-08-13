from django.conf.urls import patterns, include, url
from monitor import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^summary/(?P<pk>\d+)/$', views.ProjectSummaryMail.as_view(), name='summary'),
    url(r'^summary/', views.ProjectSummaryMail.as_view(), name='summary'),
    url(r'^(?P<projectId>[0-9]+)/summarize/$', views.summarize, name='summarize'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^niki/', include('niki.urls')),
    url(r'^nikiInterest/', include('nikiInterest.urls')),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
