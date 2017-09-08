

from django.conf.urls import url, include
from base import views
from base.views import LocationListView

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^locations$', LocationListView.as_view(), name="list_locations")

]