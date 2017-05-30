from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.api import APIField

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
        ]

class DictionaryPage(Page):
    entryKey = models.CharField(max_length=20, unique=True)
    entryName = models.CharField(max_length=100, unique=True)
    entryDescription = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('entryKey', classname="full"),
        FieldPanel('entryName', classname="full"),
        FieldPanel('entryDescription', classname="full")
        ]

     api_fields = [
        APIField('entryKey'),
        APIField('entryName'),
        APIField('entryDescription'),
        ]

class ProviderPage(Page):
    provID = models.CharField("ID", max_length=50, unique=True)
    provName = models.CharField("Name", max_length=100, unique=True)
    # provLogo - binary
    provAddressLine1 = models.CharField("Address Line 1", max_length=50, null=True, blank=True)
    provAddressLine2 = models.CharField("Address Line 2", max_length=50, null=True, blank=True)
    provAddressLine3 = models.CharField("Address Line 3", max_length=50, null=True, blank=True)
    provAddressLine4 = models.CharField("Address Line 4", max_length=50, null=True, blank=True)
    provAddressLine5 = models.CharField("Address Line 5", max_length=50, null=True, blank=True)
    provPostcode = models.CharField("Postcode", max_length=10, null=True, blank=True)
    provLat = models.FloatField("Latitude", null=True, blank=True)
    provLng = models.FloatField("Longitude", null=True, blank=True)
    provTel = models.CharField("Telephone number", max_length=50, null=True, blank=True)
    provEmail = models.EmailField("Email address", max_length=100, null=True, blank=True)
    provWeb = models.URLField("Website address", max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('provID', classname="full"),
        FieldPanel('provName', classname="full"),
        # provLogo
        FieldPanel('provAddressLine1', classname="full"),
        FieldPanel('provAddressLine2', classname="full"),
        FieldPanel('provAddressLine3', classname="full"),
        FieldPanel('provAddressLine4', classname="full"),
        FieldPanel('provAddressLine5', classname="full"),
        FieldPanel('provPostcode', classname="full"),
        FieldPanel('provLat', classname="full"),
        FieldPanel('provLng', classname="full"),
        FieldPanel('provTel', classname="full"),
        FieldPanel('provEmail', classname="full"),
        FieldPanel('provWeb', classname="full"),
        ]

    api_fields = [
        APIField('provID'),
        APIField('provName'),
        # provLogo
        APIField('provAddressLine1'),
        APIField('provAddressLine2'),
        APIField('provAddressLine3'),
        APIField('provAddressLine4'),
        APIField('provAddressLine5'),
        APIField('provPostcode'),
        APIField('provLat'),
        APIField('provLng'),
        APIField('provTel'),
        APIField('provEmail'),
        APIField('provWeb'),
        ]
