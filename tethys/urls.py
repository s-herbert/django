from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.container_list, name='container_list'),
	url(r'^refresh_container/$',views.refresh_container, name='refresh_container'),
	url(r'^.+/refresh_container/$',views.refresh_container, name='refresh_container'),
	url(r'^(?P<name>\w+)/$', views.container_detail, name='container_detail'),
	url(r'(?P<collection>\w+)/load_document/(?P<doc_name>.+)/$',views.load_document,name='load_document'),
]