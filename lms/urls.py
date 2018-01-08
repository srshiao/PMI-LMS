from django.conf.urls import url
from .models import *
from . import views
from .views import *

#app_name = lms

urlpatterns = [
    url(r'^$', views.adminhome, name= 'index'),
    url(r'^logout/$', views.logout_page, name = 'logout'),

]
