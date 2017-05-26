# Create a new Wagtail site for maternity
With Wagtail installed can create a new site for the maternity CMS.
### Create new site
It will be called maternity:
```
cd ~
wagtail start maternity
```
### File structure
The following file structure is created:
```
~/maternity/
~/maternity/db.sqlite3
~/maternity/home/...
~/maternity/manage.py
~/maternity/maternity/
~/maternity/maternity/__init__.py
~/maternity/maternity/__pycache__
~/maternity/maternity/settings/base.py
~/maternity/maternity/settings/dev.py
~/maternity/maternity/settings/__init__.py
~/maternity/maternity/settings/production.py
~/maternity/maternity/settings/__pycache__/...
~/maternity/maternity/static/...
~/maternity/maternity/templates/...
~/maternity/maternity/urls.py
~/maternity/maternity/wsgi.py
~/maternity/requirements.txt
~/maternity/search/...
```
### Django setup
Setup a new Django application for maternity (Wagtail uses Django):
```
cd ~/maternity
pip3 install -r requirements.txt
```
### Synchronize database
This synchronizes the database state with the current set of models and migrations:
```
cd ~/maternity
python3 manage.py migrate
```
### Create super user
The super user for administration of site:
```
cd ~/maternity
python3 manage.py createsuperuser
```
### Set ALLOWED_HOSTS
As the maternity site is going to be directly accessed from the internet, need to put its DNS name in the settings Python module. Edit `~/maternity/maternity/settings/base.py` to add the following line:
```python
ALLOWED_HOSTS = ['www.example.com', 'localhost']
```
### Enable Wagtail API v2
The API allows an external application to query and retrieve content programmatically. Edit `~/maternity/maternity/settings/base.py` to add the following:
```python
INSTALLED_APPS = [
    ...
    "wagtail.api.v2",
    "rest_framework",
    ...
    ]
```
### Configure endpoints for API
Create python file `~/maternity/maternity/api.py`
```python
# api.py

from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.wagtailimages.api.v2.endpoints import ImagesAPIEndpoint
from wagtail.wagtaildocs.api.v2.endpoints import DocumentsAPIEndpoint

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIEndpoint)
api_router.register_endpoint('images', ImagesAPIEndpoint)
api_router.register_endpoint('documents', DocumentsAPIEndpoint)
```
Edit `~/maternity/maternity/urls.py`
```python
from .api import api_router

urlpatterns = [
    ...

    url(r'^api/v2/', api_router.urls),

    ...

    # Ensure that the api_router line appears above the default Wagtail page serving route
    url(r'', include(wagtail_urls)),
]
```
Note: as defined these APIs are open. No API key or client certificate is needed to call them. Not considered an issue for ths experimental project.
### Start the application
Fire up the Quattro :wink:
```
cd ~/maternity
sudo python3 manage.py runserver 0.0.0.0:80
```
Note: this is using HTTP not HTTPS. To use HTTPS requires either a CA issued certificate (£££) or self signed certificate (browser won't trust it). Therefore risk of traffic sniffing for this development project is considered acceptable.
### Test the site
Browse to:
```
http://www.example.com
```
![Image of user screen](https://github.com/childhealth/Wagtail/blob/master/WagtailUserUI.png)

Browse to:
```
http://www.example.com/admin
```
![Image of admin login screen](https://github.com/childhealth/Wagtail/blob/master/WagtailAdminUI.png)
### Test the API
Browse (acting as an external system calling the API for pages) to:
```
http://www.example.com/api/v2/pages/
```
![Image of pages api](https://github.com/childhealth/Wagtail/blob/master/WagtailPagesApi.png)

Browse (acting as an external system calling the API for images) to:
```
http://www.example.com/api/v2/images/
```
![Image of images api](https://github.com/childhealth/Wagtail/blob/master/WagtailImagesApi.png)
Browse (acting as an external system calling the API for documents) to:
```
http://www.example.com/api/v2/documents/
```
![Image of documents api](https://github.com/childhealth/Wagtail/blob/master/WagtailDocumentsApi.png)
