from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post,name = 'home'),
    url(r'^index/$', views.list_view, name='index'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^index/(?P<id>\d+)/$', views.blog, name='detail'),
    url(r'^index/create/$', views.post_create,name = 'createpost'),
    url(r'^index/(?P<id>\d+)/update/$', views.post_update,name='updatepost'),
    url(r'^index/(?P<id>\d+)/delete/$', views.post_delete),
    url(r'^post_form/$', views.Profile_Update, name = 'createprofile'),
]
