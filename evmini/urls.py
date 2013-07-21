from django.conf.urls import patterns, url

from evmini import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/elections$', views.elections, name='elections')
)
