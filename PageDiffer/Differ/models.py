from django.db import models


class RegisteredPerson(models.Model):
    def __unicode__(self):
        return "%s - %s" % (self.name, self.phone_number)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    confirmed = models.BooleanField()

class SiteMembership(models.Model):

    person = models.ForeignKey("RegisteredPerson")
    site = models.ForeignKey("DiffedSite")
    paid = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notified = models.BooleanField()

class SiteHash(models.Model):

    site = models.ForeignKey("DiffedSite")
    md5hash = models.CharField(max_length=100)
    date = models.DateTimeField()

class DiffedSite(models.Model):

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    registered_users = models.ManyToManyField("RegisteredPerson", through="SiteMembership")
    message = models.CharField(max_length=155)
    difference_found = models.BooleanField()
