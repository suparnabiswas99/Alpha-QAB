from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post,name = 'home'),
    url(r'^index/$', views.list_view),
    url(r'^accounts/profile/$', views.profile, name= 'profile'),
    url(r'^index/blog/$', views.blog),
]