from django.urls import path
from .views import *

app_name="dashboard"

urlpatterns=[
    path('dash/',index, name='index'),
]