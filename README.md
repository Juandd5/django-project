# Django Project 
This is a CRUD developed with Python and the Django framework.
You can Filter, Create and Update fixed assets of a company.  
You can also Create, Update and Delete persons to whom you assign fixed assets.

## Installing the project in Ubuntu

In your command line:
- git clone git@github.com:Juandd5/django-project.git
- cd django-project
- python3 -m venv venv
- source ./venv/bin/activate

Install all dependencies that are required for the project by running:
- pip install -r requirements.txt

## Some settings

- Open the file: */django_project/settings.py* 
- Look for *DATABASES* variable and configure the following:

![image](https://user-images.githubusercontent.com/95102863/160952571-5f6bc368-0921-4e08-b49f-0fd5597a7df5.png)


## Running the app
- python manage.py makemigrations
- python manage.py migrate  
- python manage.py runserver

Visit: 127.0.0.1:8000/ to see the web app.

