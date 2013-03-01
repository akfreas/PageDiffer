from django.contrib import admin
from Differ.models import *


class RegisteredPersonAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "phone_number", "paid")
    list_filter = ("paid",)

admin.site.register(RegisteredPerson, RegisteredPersonAdmin)

class DiffedSiteAdmin(admin.ModelAdmin):

    list_display = ("name", "url")

admin.site.register(DiffedSite, DiffedSiteAdmin)
