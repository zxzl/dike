from django.db import models

from .document import Document


class Sentence(models.Model):
    state = models.IntegerField(default=0)
    content = models.TextField()
    order = models.IntegerField()
    hit = models.IntegerField(default=0)

    document = models.ForeignKey(Document)
    parent = models.ForeignKey('self', null=True)