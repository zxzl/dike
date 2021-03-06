from django.db import models

from .document import Document


class Sentence(models.Model):
    state = models.IntegerField(default=0)
    content = models.TextField()
    order = models.IntegerField()
    hit = models.IntegerField(default=0)

    document = models.ForeignKey(Document)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return "{} {:>4} {}".format(self.document.id, self.id, self.content[:10])

    def add_hit(self):
        self.hit += 1
        self.save()

