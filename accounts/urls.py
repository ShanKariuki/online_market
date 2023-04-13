from django.contrib.auth import views as auth_views
from django.urls import path
from.views import *
app_name='accounts'

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm),name='login'),
    path('logout/', sign_out, name='logout'),
   
]