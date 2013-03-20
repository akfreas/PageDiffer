from django.shortcuts import render_to_response
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect

from Differ.models import *
from django.views.decorators.csrf import csrf_exempt
from Differ import forms
from Differ import settings
from Differ import forms

import phonenumbers
import json

from twilio import twiml


def index(request):

    form = forms.RegisterPersonForm()
    return render_to_response("index.html", {'form' : form})

def capture_info(request):

    register_form = forms.RegisterPersonForm(request.POST)

    if register_form.is_valid():
        person = RegisteredPerson(phone_number=request.POST['phone_number'], name=request.POST['name'], email="joe@blow.com")
        person.save()
    else:

        failure_dict = dict({"success" : False, "errors" : register_form.errors})

        error_json = json.dumps(failure_dict)
        return HttpResponse(status=200, content=error_json)



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
