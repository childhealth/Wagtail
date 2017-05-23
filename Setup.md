# Setup Instructions
These are the steps to install and configure Wagtail on development server.

The development server is running Ubuntu 16.04 LTS.

### Update OS
Do the normal update of OS:
```
sudo apt-get update
sudo apt-get upgrade
```
### Check Python 3 installed
Python 3 should be installed by default on Ubuntu 16.04:
```
python3 -V
$ Python 3.5.2
```
### Install pip 3
Install the Python 3 package manager:
```
sudo apt-get install python3-pip
```
Check pip installed:
```
pip3 -V
$ pip 8.1.1 from /usr/lib/python3/dist-packages (python3.5)
```
The distribution package may not be the current version of pip, in which case when you use pip it will nag you to upgrade. Therefore do an upgrade now:
```
pip3install --upgrade pip
```
### Install virtual environments for Python
It's best practice to use virtual environments for running Python applications. For this project not going to use them, but install them just in case:
```
sudo apt-get install python3-venv
```
### Install Python pillow
Pillow is the Python imaging library:
```
sudo apt-get install python3-pil
```
### Install Wagtail
Installs the Wagtail Python application:
```
pip3 install wagtail
```
