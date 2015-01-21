from django.conf.urls import patterns, include, url
from .views import Registrarse
# from .views import index, Index2
urlpatterns = patterns('',
	# url(r'^$','apps.inicio.views.index'),
	# url(r'^index/$', Index2.as_view()),
	url(r'^$', 'django.contrib.auth.views.login',{'template_name':'inicio/index.html'},name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',name='logout'),
	url(r'^registrarse/$', Registrarse.as_view(), name='registrarse'),
	
)
