from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='hth/home_page.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
#    url(r'^news/', include(bandcms.urls.post_patterns)),
#    url(r'^calendar/', include(bandcms.urls.gig_patterns)),
#    url(r'^music/songs/', include(bandcms.urls.song_patterns)),
#    url(r'^music/', include(bandcms.urls.release_patterns)),
#    url(r'^videos/', include(bandcms.urls.video_patterns)),
)

