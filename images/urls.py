# Django libraries
from django.conf.urls import *

#Application specific libraries
from images import views


urlpatterns = patterns('',
    url(r'^/new$',views.upload_images),
)

