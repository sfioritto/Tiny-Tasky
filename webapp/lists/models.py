from django.db import models
from django.core.urlresolvers import reverse
from webapp.account.models import Account

class List(models.Model):

    created_on = models.DateTimeField(auto_now_add=True, auto_now=True)
    name = models.CharField(max_length=64)
    account = models.ForeignKey(Account)

    def get_absolute_url(self):
        return reverse('webapp.lists.views.show_list', args=[self.name])
    url = property(get_absolute_url)

    def __unicode__(self):
        return self.name

