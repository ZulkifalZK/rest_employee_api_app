# rest_employee_api_app
Employee Api App using django and django_rest  


1) first create and django project 
   using django-admin startproject [projectName]

2) add corsheaders to your INSTALLED_APPS and MIDDLEWARE in settings.py 
   file for more visit the link https://pypi.org/project/django-cors-headers/
   add rest_framework to the INSTALLED_APPS also

3) start an app using python manage.py startapp [appName]
   after that create some new files inside the app
   serializers.py
   urls.py
   add app name to the INSTALLED_APPS 
  
 4) after you done with the models after creating them 
    run py manage.py makemigrations [appName]
    after that run py manage.py migrate [appName]
