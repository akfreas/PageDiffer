from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class RegisteredPerson(models.Model):
    def __unicode__(self):
        return "%s - %s" % (self.name, self.phone_number)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField()
    confirmed = models.BooleanField()
    paid = models.BooleanField()

class DiffedSite(models.Model):

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    registered_users = models.ManyToManyField("RegisteredPerson")
    message = models.CharField(max_length=155)
