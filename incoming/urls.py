from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Here we add our Twilio URLs
    url(r'^sms/$', 'incoming.views.sms'),
]