from django.db import models


class Event(models.Model):
    date = models.DateField()
    text = models.CharField(max_length=250)

    def __unicode__(self):
        return unicode(self.date)

