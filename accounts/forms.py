from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth import get_user_model

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Username or Email')
    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            self.user_cache = authenticate(username=username_or_email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
    
