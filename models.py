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
    provID = models.CharField(max_length=50, unique=True)
    provName = models.CharField(max_length=100, unique=True)
    # provLogo - binary
    provAddressLine1 = models.CharField(max_length=50)
    provAddressLine2 = models.CharField(max_length=50)
    provAddressLine3 = models.CharField(max_length=50)
    provAddressLine4 = models.CharField(max_length=50)
    provAddressLine5 = models.CharField(max_length=50)
    provPostcode = models.CharField(max_length=10)
    # provLat
    # provLng
    provTel = models.CharField(max_length=50)
    provEmail = models.CharField(max_length=100)
    provWeb = models.CharField(max_length=100)

    content_panels = Page.content_panels + [
        FieldPanel('provID', classname="full"),
        FieldPanel('provName', classname="full"),
        # provLogo
        FieldPanel('provAddressLine1', classname="full"),
        FieldPanel('provAddressLine1', classname="full"),
        FieldPanel('provAddressLine2', classname="full"),
        FieldPanel('provAddressLine3', classname="full"),
        FieldPanel('provAddressLine4', classname="full"),
        FieldPanel('provAddressLine5', classname="full"),
        FieldPanel('provPostcode', classname="full"),
        # provLat
        # provLng
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
        # provLat
        # provLng
        APIField('provTel'),
        APIField('provEmail'),
        APIField('provWeb'),
        ]
