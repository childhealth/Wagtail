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
        FieldPanel('body', classname="full"),
        ]
```

```
cd ~/maternity
python3 manage.py makemigrations
python3 manage.py migrate

sudo python3 manage.py runserver 0.0.0.0:80
```
Look for a template filename formed from the app and model name, separating capital letters with underscores:
```
~/maternity/home/templates/home/home_page.html
```
