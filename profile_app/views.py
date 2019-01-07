from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from profile_app.models import Profile
from twitter_app.models import Tweet
from profile_app.forms import SignupForm, LoginForm, UserEditForm, ProfileEditForm


def edit(request, profile_id):
  profile = Profile.objects.get(id=profile_id)

  if request.method == 'POST':
    profile.user.first_name = request.POST.get('first_name')
    profile.user.last_name = request.POST.get('last_name')
    profile.bio = request.POST.get('bio')
    profile.user.save()
    profile.save()

  user_edit_form = UserEditForm(initial={
    'first_name': profile.user.first_name,
    'last_name': profile.user.last_name,
  })

  profile_edit_form = ProfileEditForm(initial={
    'bio': profile.bio
  })

  return render(request, 'profile_edit.html', context={
    'user_edit_form': user_edit_form,
    'profile_edit_form': profile_edit_form,
  })


def profile(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  tweets  = Tweet.objects.filter(profile=profile)
  return render(request, 'profile.html', context={
    'profile': profile,
    'tweets': tweets
  })


def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    User.objects.create_user(username=username, password=password)

    user = authenticate(request, username=username, password=password)
    Profile.objects.get_or_create(user=user, bio='')

    if user is not None:
      login(request, user)
      return redirect('/')

  return render(request, 'signup.html', context={ 'signup_form': SignupForm() })


def login_auth(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('/')

  return render(request, 'login.html', context={ 'login_form': LoginForm() })


def logout_auth(request):
  logout(request)
  return redirect('/')

