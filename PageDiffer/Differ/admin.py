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


class SiteHashAdmin(admin.ModelAdmin):

    list_display = ("site", "md5hash", "date")
    list_filter = ("site__name",)

admin.site.register(SiteHash, SiteHashAdmin)
