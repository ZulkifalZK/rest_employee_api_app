# rest_employee_api_app
Employee Api App using django and django_rest  

1) run pip install -r requirements.txt

2) first create and django project 
   using django-admin startproject [projectName]

3) add corsheaders to your INSTALLED_APPS and MIDDLEWARE in settings.py 
   file for more visit the link https://pypi.org/project/django-cors-headers/
   add rest_framework to the INSTALLED_APPS also

4) start an app using python manage.py startapp [appName]
   after that create some new files inside the app
   serializers.py
   urls.py
   add app name to the INSTALLED_APPS 
  
 5) after you done with the models after creating them 
    run py manage.py makemigrations [appName]
    after that run py manage.py migrate [appName]

6) copy the data of models, views, serializers and urls into your files respective files and then 
   run python manage.py runserver
   
7) for testing the api's you can use postman or myfavourite (thunder client)
