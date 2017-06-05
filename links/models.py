from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    submitted_by = models.ForeignKey(User)
    upvotes = models.ManyToManyField(User, related_name='votes')
    submitted_on = models.DateTimeField(auto_now_add=True, editable=False)
