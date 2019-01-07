from django import forms
from twitter_app.models import Tweet


class TweetForm(forms.ModelForm):
  class Meta:
    model   = Tweet
    fields  = ('text',)
    widgets = {
      'text': forms.Textarea(attrs={
          'id': 'tweet-text',
          'placeholder': 'Tweet here...',
          'required': True,
        }),
    }