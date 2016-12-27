from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='splitbill.home'),
    url(r'^account/(?P<account_id>[0-9]+)$', views.account, name='splitbill.account'),
    url(r'^statement/(?P<statement>[0-9]+)$', views.statement, name='splitbill.statement'),
    url(r'^autotag/(?P<statement>[0-9]+)$', views.autotag, name='splitbill.autotag'),
    url(r'^upload/(?P<account>[0-9]+)$', views.upload, name='splitbill.upload'),
    url(r'^test/$', views.test, name='splitbill.test'),
    ]
