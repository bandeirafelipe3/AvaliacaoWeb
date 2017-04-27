from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.publicaprato),
	url(r'^prato/(?P<pk>[0-9]+)/$', views.receita_detalhe,name="receita_detalhe"),
	url(r'^prato/new/$', views.nova_receita, name='nova_receita'),
	url(r'^prato/(?P<pk>[0-9]+)/edit/$', views.editar_receita, name='editar_receita'),
]