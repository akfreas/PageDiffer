from django import forms
from Differ import models

from phonenumber_field.formfields import PhoneNumberField

class RegisterPersonForm(forms.ModelForm):

    class Meta:
        model = models.RegisteredPerson
        fields = (
                'name',
                'phone_number'
                )

