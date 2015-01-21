from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BibliotecaVirtual.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    # inicio
    url(r'^', include('apps.inicio.urls')),
    
    #autores
    url(r'^autor/', include('apps.autores.urls')),

    #libros
    url(r'^libros/', include('apps.libros.urls')),
)
