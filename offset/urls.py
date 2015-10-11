from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'mtg/(?P<id>[0-9]+)/$', views.mtg, name='offset-mtg'),
    ]