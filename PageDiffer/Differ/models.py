from django.db import models


class RegisteredPerson(models.Model):
    def __unicode__(self):
        return "%s - %s" % (self.name, self.phone_number)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    paid = models.BooleanField()

class DiffedSite(models.Model):

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    registered_users = models.ManyToManyField("RegisteredPerson")
