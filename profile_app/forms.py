from django import forms
from django.contrib.auth.models import User
from profile_app.models import Profile


class SignupForm(forms.ModelForm):
  class Meta:
    model      = User
    fields     = ('username', 'password')
    help_texts = {
      'username': None
    }

    widgets = {
      'username': forms.TextInput(attrs={
          'id': 'signup-username',
          'placeholder': 'Username',
          'required': True,
        }),
      'password': forms.PasswordInput(attrs={
          'id': 'signup-password',
          'placeholder': 'Password',
          'required': True,
        }),
    }


class LoginForm(forms.ModelForm):
  class Meta:
    model      = User
    fields     = ('username', 'password')
    help_texts = {
      'username': None
    }

    widgets = {
      'username': forms.TextInput(attrs={
          'id': 'login-username',
          'placeholder': 'Username',
          'required': True,
        }),
      'password': forms.PasswordInput(attrs={
          'id': 'login-password',
          'placeholder': 'Password',
          'required': True,
        }),
    }


class UserEditForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ('first_name', 'last_name')
    widgets = {
      'first_name': forms.TextInput(attrs={
          'id': 'edit-first-name',
          'placeholder': 'First Name',
          'required': False,
        }),
      'last_name': forms.TextInput(attrs={
          'id': 'edit-last-name',
          'placeholder': 'Last Name',
          'required': False,
        }),
    }


class ProfileEditForm(forms.ModelForm):
  class Meta:
    model   = Profile
    fields  = ('bio',)
    widgets = {
      'bio': forms.Textarea(attrs={
          'id': 'edit-bio',
          'placeholder': 'Bio...',
          'required': False,
        }),
    }