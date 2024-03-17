from django.shortcuts import render

# Do it #3
from django.views.generic import TemplateView,CreateView

from general.models import FeedbackModel
from general.forms import FeedbackForm

from general.models import LoginModel
from general.forms import LoginForm
# Create your views here.

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
# Till here #10
