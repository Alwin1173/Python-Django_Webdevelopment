from django import forms
from general.models import FeedbackModel
from general.models import LoginModel
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['name','email','contact','message','place']
class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ['name','password']