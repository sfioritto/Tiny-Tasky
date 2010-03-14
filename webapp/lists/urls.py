from django.conf.urls.defaults import *

urlpatterns = patterns(
    'webapp.lists.views',
    (r'^$', 'lists'),
    (r'^(?P<key>.+)/$', 'list'),
)
