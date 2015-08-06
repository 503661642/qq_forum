from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qq_forum.core.views.home', name='home'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^signup/$', 'qq_forum.auth.views.signup', name='signup'),
    url(r'^settings/$', 'qq_forum.core.views.settings', name='settings'),
    url(r'^settings/picture/$', 'qq_forum.core.views.picture', name='picture'),
    url(r'^settings/upload_picture/$', 'qq_forum.core.views.upload_picture', name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', 'qq_forum.core.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'^settings/password/$', 'qq_forum.core.views.password', name='password'),
    url(r'^network/$', 'qq_forum.core.views.network', name='network'),
    url(r'^feeds/', include('qq_forum.feeds.urls')),
    url(r'^questions/', include('qq_forum.questions.urls')),
    url(r'^articles/', include('qq_forum.articles.urls')),
    url(r'^messages/', include('qq_forum.messages.urls')),
    url(r'^notifications/$', 'qq_forum.activities.views.notifications', name='notifications'),
    url(r'^notifications/last/$', 'qq_forum.activities.views.last_notifications', name='last_notifications'),
    url(r'^notifications/check/$', 'qq_forum.activities.views.check_notifications', name='check_notifications'),
    url(r'^search/$', 'qq_forum.search.views.search', name='search'),
    url(r'^(?P<username>[^/]+)/$', 'qq_forum.core.views.profile', name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
