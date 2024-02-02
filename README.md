# UpTradeTZ
---

### Description
Django application that implements a tree menu editable in the Django admin using template tags. The menu can be rendered on any page of the application by using the following tags:
```
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```

### Technologies
* Python
* Django

### Running the Project
For Windows:

```shell
git clone git@github.com:TessPlag/UpTradeTZ.git
cd UpTradeTZ
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```
For Linux:

```shell
git clone git@github.com:TessPlag/UpTradeTZ.git
cd UpTradeTZ
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

To ensure the proper functioning of the application, perform the following steps:
* Create a superuser
```shell
python manage.py createsuperuser
```
* Create the menu and its items through the administrative panel.

Start the development server
```shell
python manage.py runserver
```
