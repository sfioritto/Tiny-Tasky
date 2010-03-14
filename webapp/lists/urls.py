from django.conf.urls.defaults import *

urlpatterns = patterns(
    'webapp.lists.views',
    (r'^$', 'show_lists'),
    (r'^create/$', 'create'),
    (r'^(?P<name>.+)/$', 'show_list'),
)
