# create this file in general manually

# Do it 

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
    # Till here