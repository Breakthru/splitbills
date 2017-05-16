from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='splitbill.home'),
    url(r'^account/(?P<account_id>[0-9]+)$', views.account, name='splitbill.account'),
    url(r'^statement/(?P<statement>[0-9]+)$', views.statement, name='splitbill.statement'),
    url(r'^statement_csv/(?P<statement>[0-9]+)$', views.statement_csv, name='splitbill.statement_csv'),
    url(r'^autotag/(?P<statement>[0-9]+)$', views.autotag, name='splitbill.autotag'),
    url(r'^tag/(?P<statement>[0-9]+)/(?P<tag>[0-9]+)$', views.tag, name='splitbill.tag'),
    url(r'^addtag$', views.addtag, name='splitbill.addtag'),
    url(r'^removetag/(?P<transaction>[0-9]+)/(?P<tag>[0-9]+)$', views.removetag, name='splitbill.removetag'),
    url(r'^upload/(?P<account>[0-9]+)$', views.upload, name='splitbill.upload'),
    url(r'^test/$', views.test, name='splitbill.test'),
    ]
