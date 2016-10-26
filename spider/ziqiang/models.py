# coding:utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Newssite(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容', null=True)
    url = models.CharField(u'链接', max_length=256, default='SOME STRING')

    def __unicode__(self):
        return self.title
