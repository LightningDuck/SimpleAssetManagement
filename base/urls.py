

from django.conf.urls import url, include
from base import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^locations$', views.list_locations, name="list_locations")

]