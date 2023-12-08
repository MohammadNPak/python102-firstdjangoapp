from django import forms
from django.core.exceptions import ValidationError


def password_len_validator(text):
    if len(text)<8:
        raise ValidationError("password must be at least 8 character")

class UserCreationForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        help_text='username must be a string')
    
    email = forms.EmailField()
    password1 = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(),
        validators=[password_len_validator])
    
    password2 = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={"class":"my-password-class"}),
        validators=[password_len_validator])

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1!= password2:
            raise ValidationError("password1 should be equal to password2!")
        return cleaned_data
    
    # class Meta:
    #     help_texts = {
    #         'username': 'username must be a string',
    #     }