from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^remove/(?P<id>\d+)/delete$', views.destroy),
    # url(r'^delete$', views.destroy),

]