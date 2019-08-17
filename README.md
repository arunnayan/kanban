# kanban

#Settings
python3 -m venv venv
source venv/bin/activate

#Dependencies
pip install django
pip install DjangorestFramework

#Creating the project
django-admin startproject kanban

#Creating the App
python3 manage.py startapp kanbanApi

#Starting server
python3 manage.py runserver

#django provide some database for authentication which can be initialize as below :
python3 manage.py migrate

#creating superuser
python3 manage.py createsuperuser
admin:admin

#Change in model
python3 manage.py makemigrations


#Update in db
python3 manage.py migrate --run-syncdb
