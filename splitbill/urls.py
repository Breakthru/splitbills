from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='splitbill.home'),
    url(r'^upload/(?P<account>[0-9]+)$', views.upload, name='splitbill.upload'),
    url(r'^test/$', views.test, name='splitbill.test'),
    ]
