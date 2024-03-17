# Python-Django_Webdevelopment
 A simple Python-Django web application enabling navigation between three interconnected pages, providing fundamental experience in web development principles. 

# Steps followed during this project
 pip install django 

 -> If in the below commands 'python' does not work use 'py' instead

 1.To start a new project
 python -m django startproject Project_name
              or
 django-admin startproject Project_name 


 2.Change directory to project folder created above
 cd Project_name


 3.For database(sqllite 3)
 python manage.py migrate


 4.To commit changes to database
 python manage.py makemigrations


 5.To run server
 python manage.py runserver 
 python manage.py runserver portnumber -> 8001 is a portnumber
 -> In 8000 portnumber last 2 digits can be changed according to us to make it unique


 6.Module Creation
 python manage.py startapp module_name 


 7.Three folders created inside project file
	  1.templates-html file
	  2.static-css files
	  3.media-background images

   
 8.create file index.html under templates with

 <!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>
 </head>
 <body>
 <h3>Welcome to our world!!! Course BCA BCom BTech MTech</h3>
 </body>
 </html>


 9.settings.py in Restaurant(project)

 import os -> do it in line 12

 DEBUG = True -> in line 26 make it False according to security warning in line 25 at the time said

 ALLOWED_HOSTS = ["*"] -> do it ie  add "*" in line 28

 INSTALLED_APPS = [
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
     'general', -> do it in line 40 i.e add “'general',”
 ]

 -> do it in settings.py from line 121
 STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]

 MEDIA_ROOT=os.path.join(BASE_DIR,'media')

 MEDIA_URL='/media/'
 -> till line 127


 10.urls.py in Restaurant (project)

 from django.urls import path,include ->do it ie add “,include” in line 18

 -> do it from line 19
 from django.conf.urls.static import static
 from django.conf import settings
 -> till line 22

 urlpatterns = [
     path('admin/', admin.site.urls),
     -> do it from line 25
     path('gen/',include('general.urls'))
 ]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

 if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     -> do it till line 32


 11.urls.py in general(app)

 -> create this file in general manually

 -> Do it from line 3

 from django.contrib import admin
 from django.urls import path
 from django.conf.urls.static import static
 from django.conf import settings
 from general.views import HomePageView

 urlpatterns = [
     path('home/', HomePageView.as_view(),name='index_page')
 ]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

 if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     -> Till line 18


 12.views.py in general

 from django.shortcuts import render

 -> Do it from line 3
 from django.views.generic import TemplateView,CreateView

 from general.models import FeedbackModel
 from general.forms import FeedbackForm

 -> Create your views here.

 class CreateFeedbackView(CreateView):
     template_name='create_feedback.html'
     model=FeedbackModel
     form_class=FeedbackForm
     success_url='/gen/home'

 class HomePageView(TemplateView):
     template_name='index.html'
 -> Till line 10

 -> Do it from line 3
 from django.views.generic import TemplateView

 -> Create your views here.

 class HomePageView(TemplateView):
     template_name='index.html'
 -> Till line 10


 13.When running server as in step 5 after the command is typed in terminal and the web is opened to remove display error type in “/gen/home “ along with the existing url
   
   So the URL becomes http://127.0.0.1:8000/gen/home/ 


 14.Html file 'create_feedback.html' in templates folder with following contents

 <html>
     <head>
         <title>Contact us</title>
     </head>
     <body>
         <form method="post">
             {% csrf_token %}
             {{form.as_p}}
             <button>SUBMIT FEEDBACK</button>
         </form>
     </body>
 </html>


 15.in general in admin.py

 from general.models import FeedbackModel -> line  3

 -> Register your models here.

 admin.site.register(FeedbackModel) -> line 7


 16.in general create a forms.py manually with following contents

 from django import forms
 from general.models import FeedbackModel
 class FeedbackForm(forms.ModelForm):
     class Meta:
         model = FeedbackModel
         field = ['name','email','contact','message','place']


 17.in general in models.py

 class FeedbackModel(models.Model): -> line 5
     name = models.CharField(max_length=25)
     email = models.EmailField()
     contact = models.CharField(max_length=30)
     message = models.TextField(max_length=500)
     place = models.CharField(max_length=50,null=True,blank=True)

   def __str__(self) -> str:
        return self.name


 18.modify urls.py in general 

 -> create this file in general manually

 -> Do the following in it 

 from django.contrib import admin
 from django.urls import path
 from django.conf.urls.static import static
 from django.conf import settings

 from general.views import HomePageView,CreateFeedbackView

 urlpatterns = [
     path('home/', HomePageView.as_view(),name='index_page'),
     path('feedback/', CreateFeedbackView.as_view(),name='feedback_page')
 ]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

 if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     -> Till here


 19.in terminal

 PS *:\***\......\****\Python-Django\Restaurant> python manage.py createsuperuser
 Username (leave blank to use '***'): *** 
 Email address: ***@gmail.com
 Password: *******
 Password (again): *******
 Bypass password validation and create user anyway? [y/N]: y
 Superuser created successfully.


 20.create demo.html file in templates with following contents
  -> done to change pages using django as well as to learn difference between changing pages using html

 <!DOCTYPE html>
 <html lang="en">

 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Demo</title>
 </head>

 <body>
     <a href=" *:\***\......\****\****\Python-Django\Restaurant\templates\index.html">Login</a> ->when we need to move through pages using html 
     <a href="{% url 'index_page' %}">Home</a> ->when we need to move through pages using django
 -> the name 'index_page' is found in general in urls.py
     <a href=" *:\***\.....\****\****\Python-Django\Restaurant\templates\index.html">Feedback</a>

 </body>

 </html>

 So it becomes

 <!DOCTYPE html>
 <html lang="en">

 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Demo</title>
 </head>

 <body>
     <a href="{% url 'login_page' %}">Login</a>
     <a href="{% url 'index_page' %}">Home</a>
     <a href="{% url 'feedback_page' %}">Feedback</a>

 </body>

 </html>


 21.modify views.py in general as

 from django.shortcuts import render

 -> Do it from line 3
 from django.views.generic import TemplateView,CreateView

 from general.models import FeedbackModel
 from general.forms import FeedbackForm

 from general.models import LoginModel
 from general.forms import LoginForm
 -> Create your views here.

 class CreateFeedbackView(CreateView):
     template_name='create_feedback.html'
     model=FeedbackModel
     form_class=FeedbackForm
     success_url='/gen/home'

 class CreateLoginView(CreateView):
     template_name='login.html'
     model=LoginModel
     form_class=LoginForm
     success_url='/gen/home'

 class HomePageView(TemplateView):
     template_name='index.html'

 class DemoPageView(TemplateView):
     template_name='demo.html'
 -> Till here line 10


 22.modify urls.py in general as

 -> create this file in general manually

 -> Do it 

 from django.contrib import admin
 from django.urls import path
 from django.conf.urls.static import static
 from django.conf import settings

 from general.views import HomePageView,CreateFeedbackView,CreateLoginView,DemoPageView

 urlpatterns = [
     path('home/', HomePageView.as_view(),name='index_page'),
     path('feedback/', CreateFeedbackView.as_view(),name='feedback_page'),
     path('login/', CreateLoginView.as_view(),name='login_page'),
     path('demo/', DemoPageView.as_view(),name='demo_page')
 ]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

 if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     -> Till here


 23.create css files under static folder with names of the html files created Eg for: demo.html create demo.css and modify demo.css in templates with the lines

 {% load static %}
 <link rel="stylesheet" href="{% static 'myfirst.css' %}">

 Eg:demo.css in static folder

 /* Global styles */
 body {
     font-family: Arial, sans-serif;
     margin: 0;
     padding: 0;
     background-color: ->f0f0f0;
     text-align: center;
     /* Center align all content */
 }

 /* Styles for the heading */
 h3 {
     margin-top: 50px;
     /* Add space from the top */
 }

 /* Styles for links */
 a {
     display: inline-block;
     padding: 10px 20px;
     margin: 10px;
     text-decoration: none;
     color: ->333;
     background-color: ->f9f9f9;
     border: 1px solid ->ccc;
     border-radius: 5px;
     transition: background-color 0.3s, color 0.3s;
 }

 /* Styles for links on hover */
 a:hover {
     background-color: ->e0e0e0;
     color: ->000;
 }

 modify demo.html in templates folder

 <!DOCTYPE html>
 <html lang="en">

 <head>
     {% load static %}
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link rel="stylesheet" href="{% static 'demo.css' %}">
     <title>Demo</title>
 </head>

 <body>
     <h3>Welcome</h3>
     <a href="{% url 'login_page' %}">Login</a>
     <a href="{% url 'index_page' %}">Home</a>
     <a href="{% url 'feedback_page' %}">Feedback</a>

 </body>

 </html>
