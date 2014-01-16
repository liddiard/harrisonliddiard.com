from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.FrontView.as_view(), name='front'),
    url(r'^project/(?P<project>\S+)/$', views.ProjectView.as_view(), name='project'),
    url(r'^skill/(?P<skill>\S+)/$', views.SkillView.as_view(), name='skill'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
