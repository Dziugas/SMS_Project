from django.conf.urls import url
from . import views

urlpatterns = [
    # Here we add our Twilio URL
    url(r'^$', views.index, name='index'),
]