from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^set_language/$', 'util.i18n.set_language', name='set_language'),
)
