from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),

]