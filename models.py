from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

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





















                                   [ Read 25 lines ]
^G Get Help   ^O Write Out  ^W Where Is   ^K Cut Text   ^J Justify    ^C Cur Pos
^X Exit       ^R Read File  ^\ Replace    ^U Uncut Text ^T To Linter  ^_ Go To Line
