from django.contrib import admin

from general.models import FeedbackModel
from general.models import LoginModel

# Register your models here.

admin.site.register(FeedbackModel)
admin.site.register(LoginModel)