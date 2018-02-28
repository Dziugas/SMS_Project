from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^note/(?P<note_id>[0-9]+)/$', views.detail, name='detail'),

    # delete
    url(r'^note/(?P<note_id>[0-9]+)/delete$', views.delete_note, name='delete')
]