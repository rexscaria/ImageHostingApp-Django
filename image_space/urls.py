from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from imageapp import views

admin.site.site_header = settings.ADMIN_TITLE
admin.site.site_title = settings.SITE_TITLE

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'image_space.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^home', views.home, name='home'),
    url(r'^upload', views.upload, name='upload'),
    url(r'^settings', views.settings, name='settings'),
    url(r'^logout', views.logout, name='logout'),


    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)