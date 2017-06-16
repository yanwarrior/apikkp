from django.conf.urls import url
from . import views


urlpatterns = [
	url('^lampu/$', views.api_lampu_list),
	url('^lampu/add/$', views.api_lampu_add),
	url('^lampu/(?P<pk>[0-9]+)/$', views.api_lampu_detail),
	url('^lampu/(?P<pk>[0-9]+)/edit/$', views.api_lampu_edit),
	url('^lampu/(?P<pk>[0-9]+)/delete/$', views.api_lampu_delete),
	
	url('^jadwal/$', views.api_jadwal_list),
	url('^jadwal/add/$', views.api_jadwal_add),
	url('^jadwal/(?P<pk>[0-9]+)/$', views.api_jadwal_detail),
	url('^jadwal/(?P<pk>[0-9]+)/edit/$', views.api_jadwal_edit),
	url('^jadwal/(?P<pk>[0-9]+)/delete/$', views.api_jadwal_delete),
]

# Token fe33ef36604bb788093463fb932395a3881b1770