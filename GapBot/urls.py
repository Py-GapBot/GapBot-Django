from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<token>[0-9a-f]{32})/$', views.dispatcher)
]