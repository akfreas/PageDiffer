from django.conf import settings
from django.core.management.base import NoArgsCommand, CommandError
from Differ.models import RegisteredPerson, DiffedSite
from Differ import differs
from sendsms import api

class Command(NoArgsCommand):

    help = "Checks to see if there are changes in each site listed, then sends email and SMS to registered users."

    def handle_noargs(self, **options):

        sites = DiffedSite.objects.all()

        for site in sites:
            is_different = differs.diff_site(site.url, site.name)

            if is_different == True:
                users = site.registered_users.all()

                message = "The site %s has changes. Check them out at %s!!" % (site.name, site.url)
                user_phones = [user.phone_number for user in users]
                print "Sending messages to %s users" % len(user_phones)
                api.send_sms(body=message, from_phone=settings.DEFAULT_PHONE, to_phone=user_phones)





