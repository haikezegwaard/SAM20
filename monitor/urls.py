from django.conf.urls import patterns, include, url
from monitor import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^summary/', views.ProjectSummaryMail.as_view(), name='summary'),
    url(r'^(?P<projectId>[0-9]+)/summarize/$', views.summarize, name='summarize'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^niki/', include('niki.urls')),
    url(r'^digest/', include('notifier.urls')),
    url(r'^nikiInterest/', include('nikiInterest.urls')),
    url(r'^facebook/', include('facebook.urls')),
    url(r'^cyfe/', include('cyfe.urls')),
    url(r'^mailchimp/', include('mcapi.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$',views.ProfileView.as_view(), name='profile')
)
