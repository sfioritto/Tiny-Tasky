from django.conf.urls.defaults import *

urlpatterns = patterns(
    'webapp.account.views',
    (r'^create/$', 'create'),
)
