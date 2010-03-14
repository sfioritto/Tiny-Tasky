from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = \
    patterns('',
             (r'^lists/', include('webapp.lists.urls')),
             (r'^account/', include('webapp.account.urls')),
             (r'^admin/', include(admin.site.urls)),
             (r'^login/$', 'django.contrib.auth.views.login', {
            'template_name': 'account/login.html'
            }),
             (r'logout/$', 'django.contrib.auth.views.logout_then_login'),
             )
