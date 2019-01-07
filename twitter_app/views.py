from django.shortcuts import render, redirect
from datetime import datetime
from twitter_app.models import Tweet
from twitter_app.forms import TweetForm


def index(request):
  tweets = Tweet.objects.all().order_by('-date')

  if request.method == 'POST':
    Tweet.objects.get_or_create(
      text=request.POST.get('text'),
      date=datetime.now(),
      profile=request.user.profile
    )

  return render(request, 'index.html', context={
    'tweets': tweets,
    'tweet_form': TweetForm(),
  })
