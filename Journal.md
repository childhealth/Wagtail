# 25/05/2017

Following [Your first Wagatail site](http://docs.wagtail.io/en/v1.10.1/getting_started/tutorial.html)

Edit `~/maternity/home/models.py`
```python
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
```

```
cd ~/maternity
python3 manage.py makemigrations
python3 manage.py migrate

sudo python3 manage.py runserver 0.0.0.0:80
```
Look for a template filename formed from the app and model name, separating capital letters with underscores.

Edit `~/maternity/home/templates/home/home_page.html`

```django
{% extends "base.html" %}

{% load wagtailcore_tags %}

{% block body_class %}template-homepage{% endblock %}

{% block content %}
    {{ page.body|richtext }}
{% endblock %}
```
# 26/05/2017
The project template
```
mysite/
    home/
        migrations/
            __init__.py
            0001_initial.py
            0002_create_homepage.py
        templates/
            home/
                home_page.html
        __init__.py
        models.py
    search/
        templates/
            search/
                search.html
        __init__.py
        views.py
    mysite/
        settings/
            __init__.py
            base.py
            dev.py
            production.py
        static/
            css/
                mysite.css
            js/
                mysite.js
        templates/
            404.html
            500.html
            base.html
        __init__.py
        urls.py
        wsgi.py
    manage.py
    requirements.txt
```
### The “home” app
Location: `/mysite/home/`

This app is here to help get you started quicker by providing a HomePage model with migrations to create one when you first setup your app.

### Default templates and static files
Location: `/mysite/mysite/templates/` and `/mysite/mysite/static/`

The templates directory contains base.html, 404.html and 500.html. These files are very commonly needed on Wagtail sites to they have been added into the template.

The static directory contains an empty JavaScript and CSS file.

### Django settings
Location: `/mysite/mysite/settings/`

The Django settings files are split up into base.py, dev.py, production.py and local.py.

base.py
This file is for global settings that will be used in both development and production. Aim to keep most of your configuration in this file.
dev.py
This file is for settings that will only be used by developers. For example: DEBUG = True
production.py
This file is for settings that will only run on a production server. For example: DEBUG = False
