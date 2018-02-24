from django.conf.urls import url
from . import views

app_name = 'incoming'

urlpatterns = [
    # Here we add our Twilio URL
    url(r'^$', views.index, name='index'),
]