from django.conf.urls import url
from personnel import views


urlpatterns = [
    url(r'^personnel/$', views.person_list),
    url(r'^personnel/(?P<pk>[0-9]+)/$', views.person_detail),
]