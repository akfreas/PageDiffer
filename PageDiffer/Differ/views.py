from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect

from Differ.models import *
from django.views.decorators.csrf import csrf_exempt

import phonenumbers
from twilio import twiml

@csrf_exempt
def incoming_sms(request):

    user = None

    sms_number = request.POST['From']
    sms_body = request.POST['Body'].upper()
    if sms_body == "CONFIRM":

        phone_matches = phonenumbers.PhoneNumberMatcher(sms_number, "US")
        for match in phone_matches:
            user = RegisteredPerson.objects.get(phone_number=match.number.national_number)
            user.confirmed = True
            user.save()
            response = twiml.Response()
            response.sms("Thanks for confirming, %s!  Keep your phone on for updates!")
            return HttpResponse(content=response.toxml(), mimetype="application/xml")

    return
