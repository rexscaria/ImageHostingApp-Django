from django.conf.urls import patterns, include, url
from django.contrib import admin
from imageapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'image_space.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),

    url(r'^$', include('imageapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
