from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [

    #main
    url(r'^$', views.index, name='index'),

    #main/22/
    url(r'^(?P<sms_id>[0-9]+)/$', views.detail, name='detail'),
]