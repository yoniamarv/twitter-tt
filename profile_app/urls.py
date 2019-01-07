from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
  path('<int:profile_id>/', views.profile, name='profile'),
  path('<int:profile_id>/edit/', views.edit, name='edit'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_auth, name='login'),
  path('logout/', views.logout_auth, name='logout'),
]