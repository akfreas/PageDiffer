from django.contrib import admin
from Differ.models import *

class SiteMembershipInline(admin.TabularInline):
    model = SiteMembership
    extra = 1

class RegisteredPersonAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "phone_number")

admin.site.register(RegisteredPerson, RegisteredPersonAdmin)

class DiffedSiteAdmin(admin.ModelAdmin):

    list_display = ("name", "url")
    inlines = (SiteMembershipInline,)

admin.site.register(DiffedSite, DiffedSiteAdmin)

