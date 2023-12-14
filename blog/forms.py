from django import forms
from .models import Test

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField()


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__" #["image","description"]
