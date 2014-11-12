ImageHostingApp-Django
======================

Image hosting and editing app in Django.

Live demo at http://frozen-brushlands-1546.herokuapp.com/login

All the images used are free and unded creative commons license.
Code is licenced under GPL


Setting Up Instructions
-----------------------
Make sure you have installed python 2.7, postgresql and pip

1. Create virtual environment and activate it. Then run `pip install -r requirements.txt`
2. In command line run `export DATABASE_URL='postgresql://127.0.0.1:5432/database_name'` replacing database name with corresponding value. (Change port and host if necessary)
3. Run migrations. `python manage.py migrate`
4. Run django server. `python manage.py runserver`
5. Your application will be available at http://127.0.0.1:8000

To Run Tests
------------

1. Run `python manage.py test imageapp`


To get Test Coverage
--------------------

1. Run test with `python manage.py test imageapp`
2. Run `coverage report`
