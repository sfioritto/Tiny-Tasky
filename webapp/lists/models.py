from django.db import models
from webapp.account.models import Account

class List(models.Model):

    created_on = models.DateTimeField(auto_now_add=True, auto_now=True)
    name = models.CharField(max_length=64)
    account = models.ForeignKey(Account)

    def __unicode__(self):
        return self.name

