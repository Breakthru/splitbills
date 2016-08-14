from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/(?P<account>[0-9]+)$', views.upload, name='upload'),
    ]
