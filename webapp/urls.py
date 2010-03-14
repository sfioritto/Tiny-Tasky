from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = \
    patterns('',
             (r'^lists/', include('webapp.lists.urls')),
             (r'^account/', include('webapp.account.urls')),
             (r'^admin/', include(admin.site.urls)),
             )
