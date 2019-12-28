from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^schedule/$', views.schedule_list),
    url(r'^schedule/(?P<id>[0-9]+)$', views.schedule_detail),
]
