# Create a new Wagtail site for maternity
With Wagtail installed can create a new site for the maternity CMS.
### Create new site
It will be called maternity:
```
wagtail start maternity
```
### File structure
The following file structure is created:
```
~/maternity/
~/maternity/db.sqlite3
~/maternity/home/
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
cd ~/maternity/maternity
pip3 install -r requirements.txt
```
### Synchronize database
This Synchronizes the database state with the current set of models and migrations:
```
python3 manage.py migrate
```
### Create super user
The super user for administration of site:
```
python3 manage.py createsuperuser
```
### Set ALLOWED_HOSTS
As the maternity site is going to be directly accssed from the intenet, need to put its DNS name in the settings Python module:
```
cd ~/maternity/maternity/settings
```
Edit `base.py` to add the following line:
```
ALLOWED_HOSTS = ['www.example.com']
```
### Start the application
Fire up the Quattro :wink:
```
sudo python3 manage.py runserver 0.0.0.0:80
```
