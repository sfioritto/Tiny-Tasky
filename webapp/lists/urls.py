from django.conf.urls.defaults import *

urlpatterns = patterns(
    'webapp.lists.views',
    (r'^$', 'show_lists'),
    (r'^create/$', 'create'),
    (r'^(?P<key>.+)/$', 'show_list'),
)
